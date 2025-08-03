"""
main.py – Startpunkt für das Kontextsicherungssystem
Ermöglicht Speichern, Laden und Löschen von Sessions via Console.
"""

import logging
from services.context_service import ContextService

# Logging konfigurieren
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def main():
    service = ContextService()
    session_id = "session-001"

    # Kontext simulieren
    context = {
        "role": "Product Owner",
        "project": "AI-Projektassistant",
        "last_action": "Create context storage module"
    }

    # Speichern
    service.save(session_id, context)

    # Laden
    loaded = service.load(session_id)
    print(f"\n🔁 Geladener Kontext:\n{loaded}")

    # Löschen
    service.delete(session_id)
    print(f"\n🗑️  Kontext gelöscht für: {session_id}")

if __name__ == "__main__":
    main()
