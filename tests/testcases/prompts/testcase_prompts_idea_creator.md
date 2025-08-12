# 🧪 Rollenprompt-Testfall

## 🎭 Rolle:
`idea_creator`

## 📝 Ziel des Tests:
Validierung, ob die Rollenbeschreibung ohne vorherigen Kontext verständlich, hilfreich und zielführend ist. Der Test simuliert ein echtes Nutzungsszenario durch einen unbekannten Anwender.

## 🔄 Testvorgehen:
1. Leeren Chat ohne Kontext starten.
2. Prompt der Rolle in den Chat kopieren.
3. Folgende Testeingaben ausprobieren:
   - „Ich suche eine Softwareidee, aber weiß nicht genau, was.“
   - „Ich möchte ein Tool zur Projektverwaltung bauen. Was sollte es können?“
   - „Ich will etwas mit KI machen, hast du eine Idee?“
4. Beobachten, wie die Rolle reagiert:
   - Werden gezielte Rückfragen gestellt?
   - Gibt es konkrete, kreative Vorschläge?
   - Bleibt die Rolle innerhalb ihrer Aufgabe?
   - Funktioniert der Prompt komplett ohne Vorkenntnisse?

## ✅ Bewertungsbogen:

| Kriterium                   | Bewertung (1–5) | Notizen zur Verbesserung               |
|----------------------------|------------------|----------------------------------------|
| Klarheit der Rollenbeschreibung | 5            | Sehr gut verständlich, klare Aufgabenbeschreibung |
| Qualität der Rückfragen    | 4                | Gute, aber noch ausbaufähige Rückfragen |
| Hilfreiche Interaktionen   | 5                | Liefert direkt umsetzbare Ideen        |
| Selbstständigkeit der Rolle| 5                | Führt strukturiert durch den Ideenprozess |
| Kontextunabhängigkeit      | 5                | Funktioniert komplett ohne Vorwissen   |

## 🎯 Erwartetes Ergebnis:
- Die Rolle stellt mindestens **eine gezielte Rückfrage**.
- Die Rolle liefert **mindestens zwei kreative, zur Anfrage passende Vorschläge**.
- Es erfolgt **eine strukturierte, unterstützende Kommunikation**.
- Die Rolle **bleibt im definierten Aufgabenrahmen** (z. B. keine Ausführung fremder Rollenanteile).
- Der Prompt funktioniert **vollständig ohne gespeicherten Kontext**.

---

📅 Testdatum: 2025-08-06
🧪 Tester: Mentronig AI-Projektassistent
