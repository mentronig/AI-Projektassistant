# tests/test_context_service.py

import os
import unittest
import logging
from repositories.tinydb_repository import TinyDBContextRepository
from services.context_service import ContextService

TEST_DB_PATH = "data/test_context_db.json"

class TestContextService(unittest.TestCase):
    """
    Unittests für den ContextService mit TinyDB-Repository.
    """

    def setUp(self):
        self.test_db_path = TEST_DB_PATH
        self.repo = TinyDBContextRepository(self.test_db_path)
        self.service = ContextService(repository=self.repo)
        self.session_id = "test-session"
        self.test_context = {
            "role": "Tester",
            "project": "Demo",
            "last_action": "save"
        }

    def test_save_and_load_context(self):
        """
        Speichert einen Kontext und lädt ihn anschließend – beide Objekte sollten identisch sein.
        """
        self.service.save(self.session_id, self.test_context)
        result = self.service.load(self.session_id)
        self.assertEqual(result, self.test_context)

    def test_delete_context(self):
        """
        Löscht den Kontext und überprüft, ob er nicht mehr vorhanden ist.
        """
        self.service.save(self.session_id, self.test_context)
        self.service.delete(self.session_id)
        result = self.service.load(self.session_id)
        self.assertEqual(result, {})

    def tearDown(self):
        """
        Testdatenbank schließen und löschen. Fehler werden geloggt.
        """
        try:
            self.repo.db.close()
        except Exception as e:
            logging.warning(f"Fehler beim Schließen der DB: {e}")

        if os.path.exists(self.test_db_path):
            try:
                os.remove(self.test_db_path)
            except Exception as e:
                logging.warning(f"Datei konnte nicht gelöscht werden → {e}")

if __name__ == "__main__":
    unittest.main()
