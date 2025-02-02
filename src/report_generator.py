class ReportGenerator:
    @staticmethod
    def format_codings(codings):
        """Formatiert die Kodierungsergebnisse"""
        output = []
        for category, matches in codings.items():
            if matches:
                output.append(f"- {category.replace('_', ' ').title()}:")
                output.extend([f"  • {match}" for match in matches[:3]])
        return "\n".join(output)

    @staticmethod
    def generate_report(pdf_stem, analysis):
        """Generiert den Bericht"""
        return f"""\
        FLUGUNFALLANALYSEBERICHT: {pdf_stem}
        
        1. Kodierte Probleme:
        {ReportGenerator.format_codings(analysis['codings'])}
        
        2. Primärproblem:
        Kategorie: {analysis['primary_problem']['category']}
        Beweise: {", ".join(analysis['primary_problem']['evidence'])}
        
        3. Hauptursache:
        {analysis['cause']}
        
        4. Fehlerkette:
        {analysis['failure_chain']}
        """

    @staticmethod
    def save_report(output_path, content):
        """Speichert den Report als TXT-Datei"""
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)