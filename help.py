from pathlib import Path

def analyze_unknown_problems():
    report_dir = Path("reports/")
    total_files = 0
    unknown_count = 0

    # Durchsuche alle TXT-Reports
    for report_path in report_dir.glob("*.txt"):
        total_files += 1
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                content = f.read()
                
                # Suche nach dem Kategoriewert
                if "Kategorie: UNKNOWN" in content:
                    unknown_count += 1
                    
        except Exception as e:
            print(f"Fehler beim Lesen von {report_path.name}: {str(e)}")

    # Berechne Statistiken
    if total_files > 0:
        unknown_percent = (unknown_count / total_files) * 100
        return {
            "total_reports": total_files,
            "unknown_count": unknown_count,
            "unknown_percent": round(unknown_percent, 2)
        }
    return {"error": "Keine Reports gefunden"}

# Beispielaufruf
if __name__ == "__main__":
    stats = analyze_unknown_problems()
    if "error" in stats:
        print(stats["error"])
    else:
        print(f"Analyseergebnisse:")
        print(f"Gesamtberichte: {stats['total_reports']}")
        print(f"Unbekannte Primärprobleme: {stats['unknown_count']}")
        print(f"Prozentualer Anteil: {stats['unknown_percent']}%")