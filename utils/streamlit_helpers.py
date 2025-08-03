"""
Hilfsfunktionen für den sicheren Einsatz von Streamlit-Komponenten
"""

def is_streamlit():
    """
    Überprüft, ob das Skript im Kontext von 'streamlit run' ausgeführt wird.

    Returns:
        bool: True, wenn im Streamlit-Kontext, sonst False
    """
    try:
        from streamlit.runtime.scriptrunner import get_script_run_ctx
        return get_script_run_ctx() is not None
    except Exception:
        return False




