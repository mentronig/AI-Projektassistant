import logging
from config.config_loader import load_config
from ui.project_ui import ProjectAssistantUI

# -----------------------------
# Logging einrichten
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# -----------------------------
# Anwendung starten
# -----------------------------
try:
    load_config()  # .env prüfen und laden
    app = ProjectAssistantUI()
    app.run()
except Exception as e:
    logging.error(f"❌ Fehler beim Starten der Anwendung: {e}")
