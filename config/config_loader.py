"""
Konfigurations-Loader für das Projekt.
Lädt Umgebungsvariablen aus einer .env-Datei und erzeugt bei Bedarf automatisch eine env.template.
Stellt zentrale Konfigurationswerte bereit.

Lädt Konfiguration aus .env und erzeugt bei Bedarf automatisch eine env.template.

Aktuell unterstützt:
- Auswahl des Speicher-Backends (TinyDB, MongoDB etc.)

Autor: Dein Projektassistent
"""

import os
from dotenv import load_dotenv
import logging
from pathlib import Path

# -----------------------------
# Pfade definieren
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
TEMPLATE_PATH = BASE_DIR / "env.template"

# -----------------------------
# Automatisch env.template erzeugen
# -----------------------------
def generate_env_template():
    if TEMPLATE_PATH.exists():
        return
    TEMPLATE_CONTENT = """\
# ==========================================
# Konfigurationsdatei für AI-Projektassistant
# ==========================================

# Speicher-Backend: tinydb (Standard) oder mongodb
STORAGE_BACKEND=tinydb

# API-Schlüssel für OpenAI
OPENAI_API_KEY=sk-...

# Lokaler Entwicklungsmodus aktivieren
USE_LOCAL_MODE=false

# Theme-Einstellung: light oder dark
DEFAULT_THEME=light
"""
    TEMPLATE_PATH.write_text(TEMPLATE_CONTENT, encoding="utf-8")
    logging.info("📄 env.template automatisch erstellt.")


# -----------------------------
# .env laden oder Fehlermeldung
# -----------------------------
def load_config():
    generate_env_template()

    if not ENV_PATH.exists():
        raise FileNotFoundError(
            f"\n❌ .env-Datei nicht gefunden im Projekt-Root: {ENV_PATH}\n"
            f"➡️  Bitte kopiere 'env.template' nach '.env' und trage deine Werte ein."
        )
    load_dotenv(ENV_PATH)
    logging.debug(f"✅ .env geladen von: {ENV_PATH}")

# ------------------------------------------
# Funktionen zur Konfig-Abfrage
# ------------------------------------------

def get_storage_backend() -> str:
    """
    Gibt das konfigurierte Speicher-Backend zurück.

    Returns:
        str: z. B. "tinydb", "mongodb"
    """
    backend = os.getenv("STORAGE_BACKEND", "tinydb").lower()
    logging.debug(f"Konfiguriertes STORAGE_BACKEND: {backend}")
    return backend
