from transformers import pipeline

class SentimentManager:
    def __init__(self):
        self.sentiment = "Neutral"
        self.classifer = pipeline('sentiment-analysis', model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

    def analyze(self, input):
        self.result = self.classifer(input)
        return self.result