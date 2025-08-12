# Testfall: `architekt_designer.md`

## Ziel des Prompts
Der Prompt soll dem Benutzer helfen, basierend auf einer gegebenen Produktidee eine solide technische Architektur zu entwerfen. Dabei werden technische Optionen verglichen, sinnvolle Komponenten vorgeschlagen und die Machbarkeit eingeschätzt.

---

## Eingabe:
Die vom `idea_creator` generierte Produktidee (z. B. ein MVP mit dem Ziel „Automatisierung von GitHub-Operationen via ChatGPT“).

---

## Erwartetes Verhalten:
- Der Prompt erkennt die Hauptanforderungen der Idee.
- Es werden sinnvolle technische Optionen vorgeschlagen.
- Vor- und Nachteile der Ansätze werden benannt.
- Es wird ein Architekturvorschlag erstellt (ggf. mit Komponenten wie UI, Backend, Datenhaltung etc.).
- Die technische Machbarkeit wird nicht nur bejaht, sondern nachvollziehbar begründet.
- Falls Unsicherheiten bestehen, stellt die Rolle Rückfragen.
- Es wird automatisch auf die nächste Rolle (z. B. `developer`) übergeleitet – sofern vom Nutzer gewünscht.

---

## Erwartetes Ergebnis:
- Ein klarer, strukturierter Architekturvorschlag
- Technologische Empfehlungen mit begründeter Entscheidung
- Hinweise zu kritischen Aspekten und möglichen Stolpersteinen
- Optional: Visualisierungsvorschläge oder Verweise auf Standards
