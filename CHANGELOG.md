# 📋 CHANGELOG

Alle relevanten Änderungen dieses Projekts werden hier dokumentiert.

Das Format folgt dem Prinzip der [Keep a Changelog](https://keepachangelog.com/de/1.0.0/)-Initiative  
und nutzt [semantische Versionierung](https://semver.org/lang/de/).

---

## [v0.1.0] – 2025-08-02
### Hinzugefügt
- Erste Projektstruktur angelegt
- Rollen-Prompts für Idea Creator, Product Owner, Developer, Admin/DevOps, Architect/Designer, Tester
- Basisarchitektur mit `main.py`, `config`, `services`, `repositories`, `ui` etc.
- Streamlit-Oberfläche mit Projektstart
- Test-Setup (`run_tests.py`, `tests/`-Verzeichnis)
- .gitignore, README.md, requirements.txt

### Geändert
- Konsolidierte Rollen-Prompts inklusive strukturierter Zusammenfassungen

### Sicherheit
- `.env.template` eingeführt und `.env` aus `.gitignore` geschützt

---

## [Unveröffentlicht]
### Geplant
- Erste Funktion zur Auswahl und Initialisierung eines Projekts
- Konfigurierbare Kontextdatenbank
