# AI-Projektassistant
in AI-gestützter Projektassistent für rollenbasiertes Arbeiten und schnelle Entwicklung
=======
# 🤖 AI-Projektassistant

Ein modular aufgebautes Python-Toolkit zur Unterstützung von AI-basierten Softwareprojekten – mit Fokus auf rollenbasiertes Prompt-Management, Kontextsicherung, Logging und Wiederverwendbarkeit.

---

## 🌟 Funktionen

- 🧠 Rollenbasiertes Prompt-System (Idea Creator, PO, Dev, Architekt, Tester, Admin)
- 💾 Kontextverwaltung via TinyDB (Backend-Wechsel auf MongoDB möglich)
- 📂 Strukturierte Prompt-Verwaltung als Markdown
- 🧪 Test-Suite mit `unittest` & Rich-Ausgabe (`run_tests.py`)
- 📝 Logging mit sinnvoller Formatierung
- 🧰 `.env`- und `.env.template`-Handling (inkl. automatischem Check)
- 📑 Benutzerfreundliche CLI-Tools (z. B. für .env-Erzeugung)
- 📦 Streamlit-UI optional integrierbar (in Arbeit)

---

## 📁 Projektstruktur

```text
AI-Projektassistant/
│
├── main.py                        # Startpunkt für Kontextsicherung & Testausführung
├── .env                           # Konfigurationswerte (nicht im Git!)
├── .env.template                  # Vorlage für .env-Datei
├── .gitignore                     # Ignorierte Dateien/Ordner
├── requirements.txt              # Abhängigkeiten
├── run_tests.py                  # Farbig formatierter Testrunner
│
├── data/
│   └── context_db.json           # Kontextdatenbank (TinyDB)
│
├── prompts/
│   └── roles/                    # Markdown-Dateien der Rollen (Idea Creator, PO, etc.)
│
├── repositories/                 # Datenzugriffsschicht (TinyDB, MongoDB optional)
│   ├── base_repository.py
│   └── tinydb_repository.py
│
├── services/
│   └── context_service.py        # Kontext-Service mit Backend-Switch
│
├── tests/                        # Testfälle mit Cleanup-Strategien
│   └── test_context_service.py
│
├── tools/
│   └── env_helper.py             # CLI-Tool zur .env-Erzeugung
│
└── ui/
    └── project_ui.py             # Streamlit-UI (Work in Progress)
