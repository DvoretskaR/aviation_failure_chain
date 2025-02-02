import re
from transformers import (
    BertTokenizer,
    BertForSequenceClassification,
    pipeline
)
import torch

class TextAnalyzer:
    def __init__(self, coding_keywords):
        self.coding_keywords = coding_keywords

    def analyze_text(self, text):
        """Führt die Textanalyse durch"""
        results = {}
        
        # Schlüsselwortanalyse
        coding_results = {}
        for category, patterns in self.coding_keywords.items():
            matches = []
            for pattern in patterns:
                matches.extend(re.findall(pattern, text, re.IGNORECASE))
            coding_results[category] = list(set(matches))
        
        # Primärproblem Identifikation
        primary_problem = self.identify_primary_problem(coding_results)
        
        # Ursachenanalyse mit BERT
        cause = self.classify_accident_cause(text)
        
        # Fehlerkettenanalyse
        failure_chain = self.generate_failure_chain(primary_problem, cause)
        
        results.update({
            "codings": coding_results,
            "primary_problem": primary_problem,
            "cause": cause,
            "failure_chain": failure_chain
        })
        
        return results

    def identify_primary_problem(self, coding_results):
        """Identifiziert das primäre Problem"""
        problem_priority = [
            "PRIMARY_PROBLEM",
            "MECHANICAL",
            "HUMAN_FACTOR",
            "PROCEDURAL"
        ]
        
        for category in problem_priority:
            if coding_results.get(category):
                return {
                    "category": category,
                    "evidence": coding_results[category][:3]
                }
        return {"category": "UNKNOWN", "evidence": []}

    def classify_accident_cause(self, text):
        """Klassifiziert die Unfallursache mit BERT"""
        tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

        model = BertForSequenceClassification.from_pretrained(
            "textattack/bert-base-uncased-yelp-polarity", 
            num_labels=3
        )
        
        inputs = tokenizer(
            text[:512],
            return_tensors="pt",
            truncation=True,
            padding="max_length"
        )
        
        outputs = model(**inputs)
        labels = ["Mechanical Failure", "Human Error", "Procedural Violation"]
        return labels[torch.argmax(outputs.logits).item()]

    def generate_failure_chain(self, primary_problem, cause):
        """Generiert Fehlerkette mit kausaler Verknüpfung"""
        generator = pipeline(
            "text-generation",
            model="gpt2-medium",
            device=0 if torch.cuda.is_available() else -1
        )
        
        prompt = (
            f"Primary problem: {primary_problem['category']}\n"
            f"Main cause: {cause}\n"
            "Explain the failure chain leading to the accident:"
        )
        
        response = generator(
            prompt,
            max_length=200,
            temperature=0.7,
            top_p=0.9
        )
        
        return response[0]["generated_text"]