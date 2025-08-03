# tests/test_project_ui.py

import unittest
from ui.project_ui import ProjectAssistantUI

class TestProjectAssistantUI(unittest.TestCase):
    def setUp(self):
        self.ui = ProjectAssistantUI()

    def test_generate_ai_response(self):
        role_prompt = "Du bist ein kreativer AI-Ideen-Scout."
        user_input = "Ich suche nach einer Idee für ein Tool für Juristen."
        response = self.ui._generate_ai_response(role_prompt, user_input)
        self.assertIn("Beispielantwort", response)
        self.assertIn("simulierte Antwort", response)

    def test_prompt_directory_exists(self):
        self.assertTrue(self.ui.prompt_dir.exists())

    def test_roles_loaded(self):
        roles = self.ui._load_roles()
        self.assertIsInstance(roles, list)
        self.assertGreater(len(roles), 0)