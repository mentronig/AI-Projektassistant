"""
run_tests.py – Benutzerdefinierter TestRunner für AI-Projektassistant

Führt alle Unittests im Projekt aus und gibt für jede Testmethode den Status (OK, Fehler, Übersprungen) aus.
Verwendet das `rich`-Modul für farbige und strukturierte Ausgabe.
"""

import unittest
import logging
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Logging konfigurieren
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
console = Console()


def run_all_tests():
    """
    Lädt und führt alle Tests aus dem Verzeichnis 'tests' aus.
    Gibt für jede Testmethode den Status aus und erstellt eine zusammenfassende Übersicht.
    """
    console.rule("[bold cyan]🧪 Starte Testsuite für AI-Projektassistant", style="cyan")

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests")

    # Testausgabe unterdrücken – wir übernehmen das Logging manuell
    runner = unittest.TextTestRunner(stream=open(os.devnull, "w"))
    result = runner.run(suite)

    summary_table = Table(title="Testergebnisse", show_lines=True)
    summary_table.add_column("Status", justify="center", style="bold")
    summary_table.add_column("Testmethode", style="dim")

    all_tests = []
    for test_group in suite:
        for test_case in test_group:
            all_tests.append(str(test_case))

    # Fehlerlisten vorbereiten
    failed = [str(f[0]) for f in result.failures]
    errors = [str(e[0]) for e in result.errors]
    skipped = [str(s[0]) for s in result.skipped]

    for test in all_tests:
        if test in failed:
            summary_table.add_row("[red]❌ Fehler", test)
            logging.error(f"Fehlerhafter Test: {test}")
        elif test in errors:
            summary_table.add_row("[red]💥 Crash", test)
            logging.error(f"Crash im Test: {test}")
        elif test in skipped:
            summary_table.add_row("[yellow]⚠️ Überspr.", test)
            logging.warning(f"Übersprungener Test: {test}")
        else:
            summary_table.add_row("[green]✅ OK", test)
            logging.info(f"Erfolgreich: {test}")

    console.print(summary_table)

    # Zusammenfassung
    summary = f"""
    ✅ Erfolgreich: {result.testsRun - len(failed) - len(errors)}
    ❌ Fehler: {len(failed)}
    💥 Crashes: {len(errors)}
    ⚠️ Übersprungen: {len(skipped)}
    📊 Gesamt: {result.testsRun}
    """
    border_color = "green" if result.wasSuccessful() else "red"
    console.print(Panel.fit(summary.strip(), title="📋 Zusammenfassung", border_style=border_color))


if __name__ == "__main__":
    try:
        run_all_tests()
    except Exception as e:
        logging.error(f"❌ Fehler beim Ausführen der Testsuite: {e}")
