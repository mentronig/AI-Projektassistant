# logic/agent_controller.py

import os
import logging
from textwrap import dedent
from typing import Optional

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None  # Falls openai nicht installiert

class AgentResponseGenerator:
    def __init__(self, mode="dummy", model="gpt-4", temperature=0.7):
        self.mode = mode.lower()
        self.model = model
        self.temperature = temperature
        self.client = None

        if self.mode == "openai":
            self._initialize_openai()

        logging.info(f"AgentResponseGenerator gestartet im Modus: {self.mode}")

    def _initialize_openai(self):
        if not OpenAI:
            raise ImportError("OpenAI SDK nicht installiert.")
        
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise EnvironmentError("OPENAI_API_KEY ist nicht gesetzt.")
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, system_prompt: str, user_input: str) -> str:
        try:
            if self.mode == "dummy":
                return self._dummy_response(system_prompt, user_input)
            elif self.mode == "openai":
                return self._openai_response(system_prompt, user_input)
            else:
                raise ValueError(f"Unbekannter Modus: {self.mode}")
        except Exception as e:
            logging.error(f"Fehler bei Antwortgenerierung: {e}")
            return "⚠️ Fehler bei der Agentenantwort."

    def _dummy_response(self, system_prompt: str, user_input: str) -> str:
        return dedent(f"""
        🤖 *(Simulierte Dummy-Antwort)*

        Rolle: {system_prompt[:60]}...
        Frage: {user_input}

        → In einer späteren Version antwortet hier GPT.
        """)

    def _openai_response(self, system_prompt: str, user_input: str) -> str:
        if not self.client:
            raise RuntimeError("OpenAI-Client nicht initialisiert.")

        chat_response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=self.temperature
        )
        reply = chat_response.choices[0].message.content.strip()
        logging.info("Antwort vom GPT-Modell erfolgreich empfangen.")
        return reply