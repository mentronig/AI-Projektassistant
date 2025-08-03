"""
BaseContextRepository definiert ein Interface für kontextbezogene Speichersysteme.
Dies ermöglicht eine flexible Implementierung mit TinyDB, MongoDB oder anderen Backends.
"""

from abc import ABC, abstractmethod

class BaseContextRepository(ABC):
    @abstractmethod
    def save_context(self, session_id: str, context: dict):
        """Speichert den Kontext einer Session."""
        pass

    @abstractmethod
    def load_context(self, session_id: str) -> dict:
        """Lädt den gespeicherten Kontext einer Session."""
        pass

    @abstractmethod
    def delete_context(self, session_id: str):
        """Löscht den Kontext einer Session."""
        pass
