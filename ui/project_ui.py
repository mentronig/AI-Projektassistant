# ui/project_ui.py

import streamlit as st
from pathlib import Path
from textwrap import dedent
from logic.agent_controller import AgentResponseGenerator
from utils.streamlit_helpers import is_streamlit
import subprocess

import logging

# Logging konfigurieren
logging.basicConfig(
    filename="project_assistant.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class ProjectAssistantUI:
    """
    Klasse zur Darstellung der Streamlit-Oberfläche für die rollenbasierte AI-gestützte Projektbegleitung.
    """

    def __init__(self):
        self.prompt_dir = Path("prompts/roles")
        self.selected_role = None
        self.agent_mode = st.session_state.get("agent_mode", "dummy")
        self.agent = AgentResponseGenerator(mode=self.agent_mode)

    def run(self):
        st.set_page_config(page_title="AI-Projektassistent", layout="wide")
        st.title("🧠 AI-Projektassistent")
        st.markdown("Begleitet dich durch alle Projektrollen – von der Idee bis zum Release.")

        roles = self._load_roles()
        if not roles:
            st.error("Keine Rollenprompts gefunden.")
            return

        self.selected_role = st.selectbox("🎭 Rolle auswählen", roles, key="role_selector")
        prompt_content = self._load_prompt_content(self.selected_role)

        st.markdown("### 📄 Rollenbeschreibung")
        with st.expander(f"Prompt für **{self.selected_role}** anzeigen", expanded=False):
            st.code(prompt_content, language="markdown")

        st.markdown("### 🗨️ Eingabe an den Assistenten")
        user_input = st.text_area(
            "Was möchtest du besprechen oder starten?",
            height=150,
            key="user_input_area"
        )

        if st.button("Absenden", key="submit_button") and user_input.strip():
            with st.spinner("Die Rolle denkt nach..."):
                ai_answer = self._generate_ai_response(prompt_content, user_input)
                st.success("✅ KI-Antwort erhalten")
                st.markdown("### 🤖 Antwort des Assistenten")
                st.markdown(ai_answer)

        st.markdown("---")
        self._show_settings()

        st.markdown("---")
        self._show_test_section()

    def _show_settings(self):
        st.subheader("⚙️ Einstellungen")

        mode = st.radio(
            "Agenten-Modus wählen:",
            ["dummy", "openai"],
            index=0 if self.agent_mode == "dummy" else 1,
            key="agent_mode_selector",
            help="Wechsle zwischen Dummy- und OpenAI-Modus"
        )

        if mode != self.agent_mode:
            st.session_state["agent_mode"] = mode
            st.success(f"Modus gewechselt auf: {mode}. Anwendung wird neu gestartet.")
            try:
                logging.info(f"Mode gewechselt. Mode = {mode}")
                st.rerun()
                logging.info("Anwendung neu gestartet")
            except AttributeError:
                st.experimental_rerun()  # Fallback für ältere Streamlit-Version

    def _load_roles(self):
        try:
            roles = sorted([f.stem for f in self.prompt_dir.glob("*.md")])
            logging.info(f"{len(roles)} Rollen geladen.")
            return roles
        except Exception as e:
            logging.error(f"Fehler beim Laden der Rollen: {e}")
            return []

    def _load_prompt_content(self, role_name):
        try:
            path = self.prompt_dir / f"{role_name}.md"
            if not path.exists():
                raise FileNotFoundError(f"{path} existiert nicht.")
            return path.read_text(encoding="utf-8")
        except Exception as e:
            logging.error(f"Fehler beim Laden des Prompt-Inhalts für {role_name}: {e}")
            return "⚠️ Fehler beim Laden des Rollenprompts."

    def _generate_ai_response(self, role_prompt: str, user_input: str) -> str:
        try:
            combined = dedent(f"""
            {role_prompt}

            --- Benutzeranfrage ---
            {user_input}
            """)
            logging.info("Dummy-Antwort generiert.")
            return (
                "🤖 *(Beispielantwort des Agenten)*\n\n"
                "In einer späteren Version wird hier GPT oder ein lokales Modell antworten."
            )
        except Exception as e:
            logging.error(f"Fehler bei der Agentenantwort: {e}")
            return "⚠️ Fehler bei der Agentenantwort."

    def _show_test_section(self):
        with st.expander("🧪 Projekt testen", expanded=False):
            if st.button("Tests ausführen", key="run_tests_button"):
                self._run_internal_tests()

    def _run_internal_tests(self):
        try:
            st.info("📋 Tests werden ausgeführt...")
            result = subprocess.run(
                ["python", "-m", "unittest", "tests/test_project_ui.py"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                st.success("✅ Alle Tests erfolgreich bestanden.")
                st.code(result.stdout, language="text")
            else:
                st.error("❌ Einige Tests sind fehlgeschlagen.")
                st.code(result.stdout + result.stderr, language="text")
        except Exception as e:
            logging.error(f"Testausführung fehlgeschlagen: {e}")
            st.error(f"⚠️ Fehler beim Teststart: {e}")

    def _generate_ai_response(self, role_prompt: str, user_input: str) -> str:
        return self.agent.generate_response(role_prompt, user_input)