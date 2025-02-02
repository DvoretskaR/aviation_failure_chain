# aviation_failure_chain
# Aviation Failure Chain Analysis

Dieses Projekt analysiert Flugunfallberichte (PDF-Dateien) und identifiziert primäre Probleme, Ursachen und Fehlerketten. Es verwendet NLP-Techniken (BERT, GPT-2) und regelbasierte Schlüsselwortanalyse.

## Voraussetzungen

- Python 3.8 oder höher
- `venv` (virtuelle Umgebung)

## Einrichtung

1. **Klonen des Repositorys**:
   ```bash
   git clone https://github.com/DvoretskaR/aviation_failure_chain.git
   cd aviation_failure_chain

2. **Virtuelle Umgebung erstellen und aktivieren**:

- Windows:
    ```cmd 
    python -m venv venv
    venv\Scripts\activate

- Linux/macOS:
    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. **Abhängigkeiten installieren**:
    ```bash
    pip install -r requirements.txt

4. **Projektstruktur**:

- data/: Enthält die PDF-Dateien der - Flugunfallberichte.

- reports/: Enthält die generierten Analyseberichte.

- src/: Enthält den Quellcode des Projekts.
 
- .gitignore: Ignoriert bestimmte Dateien (z. B. .- env).

- README.md: Diese Datei.
 
- requirements.txt: Liste der Python-Abhängigkeiten.

5. **PDF-Dateien vorbereiten**:

- Legen Sie die zu analysierenden PDF-Dateien im Verzeichnis data/ ab

6. **Ausführung**:
    ```bash
    python main.py
