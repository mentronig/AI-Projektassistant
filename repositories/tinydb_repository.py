"""
TinyDBContextRepository implementiert das BaseContextRepository für die Verwendung mit TinyDB.
Ideal für lokale, leichtgewichtige Kontexte mit geringer Einstiegshürde.
"""

import logging
from tinydb import TinyDB, Query
from repositories.base_repository import BaseContextRepository

class TinyDBContextRepository(BaseContextRepository):
    def __init__(self, db_path="data/context_db.json"):
        self.db = TinyDB(db_path)
        self.table = self.db.table("contexts")
        logging.info(f"TinyDB initialisiert mit Pfad: {db_path}")

    def __del__(self):
        self.db.close()

    def save_context(self, session_id: str, context: dict):
        self.table.upsert({ "session_id": session_id, "context": context }, Query().session_id == session_id)
        logging.info(f"Kontext gespeichert für Session: {session_id}")

    def load_context(self, session_id: str) -> dict:
        result = self.table.get(Query().session_id == session_id)
        logging.info(f"Kontext geladen für Session: {session_id}")
        return result["context"] if result else {}

    def delete_context(self, session_id: str):
        self.table.remove(Query().session_id == session_id)
        logging.info(f"Kontext gelöscht für Session: {session_id}")
