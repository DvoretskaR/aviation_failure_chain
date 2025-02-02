from pathlib import Path
from rich.console import Console
from rich.progress import Progress, TextColumn, BarColumn, TimeRemainingColumn

from src.text_extractor import TextExtractor
from src.text_analyzer import TextAnalyzer
from src.report_generator import ReportGenerator
from src.config import Config

# Rich Initialisierung
console = Console()
progress_columns = [
    TextColumn("[bold blue]{task.description}"), 
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    TimeRemainingColumn()
]

def main():
    Config.OUTPUT_DIR.mkdir(exist_ok=True)
    
    with Progress(*progress_columns, console=console) as progress:
        pdf_files = list(Config.INPUT_DIR.glob("*.pdf"))
        main_task = progress.add_task("[bold]Verarbeite Berichte[/bold]", total=len(pdf_files))
        
        for pdf_path in pdf_files:
            try:
                # Text extrahieren
                text = TextExtractor.extract_text_from_pdf(pdf_path)
                if not text.strip():
                    raise ValueError("Leere PDF-Datei")
                
                # Analyse durchführen
                analyzer = TextAnalyzer(Config.CODING_KEYWORDS)
                analysis = analyzer.analyze_text(text)
                
                # Report erstellen
                report_content = ReportGenerator.generate_report(pdf_path.stem, analysis)
                
                # Datei speichern
                output_path = Config.OUTPUT_DIR / f"{pdf_path.stem}_analysis.txt"
                ReportGenerator.save_report(output_path, report_content)
                progress.console.print(f"✅ [bold green]Bericht gespeichert:[/bold green] {output_path}")
                
            except Exception as e:
                progress.console.print(f"❌ [bold red]Fehler bei {pdf_path.name}:[/bold red] {str(e)}")
            
            progress.update(main_task, advance=1)

if __name__ == "__main__":
    main()