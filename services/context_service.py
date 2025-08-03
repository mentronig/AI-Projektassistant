"""
ContextService – zentrale Logik zum Speichern, Laden und Löschen von Kontextsitzungen.
Ermöglicht das einfache Austauschen des Repository-Backends (z. B. TinyDB, MongoDB).

Autor: Dein Projektassistent
"""

import logging
from typing import Any, Dict, Optional

from repositories.base_repository import BaseContextRepository
from repositories.tinydb_repository import TinyDBContextRepository
from config.config_loader import get_storage_backend

# ----------------------------------------------------
# Factory-Funktion zur Auswahl des Speicher-Backends
# ----------------------------------------------------
def create_repository() -> BaseContextRepository:
    """
    Erstellt das Repository-Objekt je nach eingestelltem Backend.
    Zurzeit wird nur TinyDB unterstützt, lässt sich aber leicht erweitern.

    Returns:
        BaseContextRepository: Eine Instanz des entsprechenden Repositories.
    """
    backend = get_storage_backend()

    if backend == "tinydb":
        return TinyDBContextRepository("data/context_db.json")
    else:
        raise ValueError(f"Unbekannter STORAGE_BACKEND: {backend}")

# ----------------------------------------------------
# Kontext-Service für die Anwendungslogik
# ----------------------------------------------------
class ContextService:
    def __init__(self, repository: Optional[BaseContextRepository] = None):
        """
        Konstruktor für den ContextService.

        Args:
            repository (Optional[BaseContextRepository]): Optionales Repository-Objekt, z. B. für Tests.
                                                     Wenn nicht angegeben, wird das Standard-Backend verwendet.
        """
        self.repo = repository or create_repository()
        logging.debug("✅ ContextService initialisiert.")

    def save(self, session_id: str, context: Dict[str, Any]) -> None:
        """
        Speichert den Kontext für eine gegebene Session-ID.

        Args:
            session_id (str): Eindeutige Kennung der Sitzung.
            context (dict): Kontextdaten als Wörterbuch.
        """
        logging.info(f"💾 Speichern von Kontext für Session-ID '{session_id}'")
        self.repo.save_context(session_id, context)

    def load(self, session_id: str) -> Dict[str, Any]:
        """
        Lädt den gespeicherten Kontext einer Session.

        Args:
            session_id (str): Session-ID

        Returns:
            dict: Kontextdaten oder leeres Dict, wenn nicht gefunden
        """
        logging.info(f"📥 Laden von Kontext für Session-ID '{session_id}'")
        return self.repo.load_context(session_id)

    def delete(self, session_id: str) -> None:
        """
        Löscht den Kontext zu einer Session-ID.

        Args:
            session_id (str): Session-ID
        """
        logging.warning(f"🗑️ Löschen von Kontext für Session-ID '{session_id}'")
        self.repo.delete_context(session_id)
