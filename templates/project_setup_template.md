
# 📦 Projektstart-Vorlage: AI-gestütztes Softwareprojekt

Diese Vorlage dient als Ausgangspunkt für neue AI-basierte Projekte (z. B. Agenten, Tools, Webapps).

---

## 🧠 Projektidee

**Kurzbeschreibung**  
<Was soll das Projekt leisten? Für wen? Mit welchem Mehrwert?>

---

## 🧾 Zieldefinition

- [ ] Reales Problem oder Bedürfnis erkannt
- [ ] Use Case beschrieben
- [ ] Zielgruppe definiert
- [ ] Innovationspotenzial hervorgehoben

---

## 🧰 Technisches Setup

- **Plattform**: Web / Desktop / CLI / Mobil / Hybrid
- **Zielsystem**: Windows / Linux / Cloud / Docker / Hugging Face
- **Programmiersprache**: Python / JavaScript / …
- **Frameworks/Libs**: <z. B. Streamlit, FastAPI, LangChain>
- **Konfig-Dateien**: `.gitignore`, `README.md`, `.env`, `CHANGELOG.md`, `requirements.txt`
- **Modellwahl**: GPT-4o / GPT-4-turbo (4.5) / Lokales Modell (ggf. spezifizieren)

---

## 🔑 Rollen & Workflows

| Rolle              | Beschreibung                               |
|--------------------|--------------------------------------------|
| Idea Creator       | Generiert und konkretisiert die Idee       |
| Product Owner      | Entwickelt Produktvision und MVP-Roadmap   |
| Architekt/Designer | Entwirft Projektstruktur und Komponenten   |
| Developer          | Implementiert Code und Tests               |
| Admin/DevOps       | Sorgt für CI/CD, Setup, Sicherheit          |
| Tester             | Sichert Qualität mit Tests & Reports       |

---

## 📂 Projektstruktur (empfohlen)

```
📦 project_root/
├── main.py
├── ui/
│   └── project_ui.py
├── logic/
│   └── agent_controller.py
├── repositories/
│   ├── tinydb_repository.py
│   └── base_repository.py
├── services/
│   └── context_service.py
├── prompts/
│   └── roles/
│       ├── idea_creator.md
│       ├── product_owner.md
│       └── ...
├── tests/
│   ├── test_project_ui.py
│   └── ...
├── data/
│   └── context_db.json
├── config/
│   └── config_loader.py
├── templates/
│   └── project_setup_template.md
├── README.md
├── requirements.txt
├── .gitignore
└── .env.template
```

---

## 🔄 Versionierung & Release

- Semantische Versionierung: `vX.Y.Z`
- GitHub-Tags für Releases
- `CHANGELOG.md` gepflegt
- Automatisierte Releases optional

---

## ✅ Nächste Schritte

1. [ ] Diese Datei duplizieren und anpassen
2. [ ] Projektstruktur lokal oder im GitHub-Repo anlegen
3. [ ] Erste Rolle aktivieren: „Idea Creator“
4. [ ] MVP schrittweise umsetzen
