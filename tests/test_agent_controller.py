# tests/test_agent_controller.py

import unittest
from logic.agent_controller import AgentResponseGenerator

class TestAgentResponseGenerator(unittest.TestCase):
    def test_dummy_response(self):
        agent = AgentResponseGenerator(mode="dummy")
        result = agent.generate_response("Du bist ein Testagent", "Hallo Agent")
        self.assertIn("Simulierte Dummy-Antwort", result)

    def test_invalid_mode(self):
        with self.assertRaises(ValueError):
            AgentResponseGenerator(mode="unbekannt").generate_response("X", "Y")


