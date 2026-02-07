from transformers import MarianMTModel, MarianTokenizer

class EnglishToCzechTranslator:
    def __init__(self):
        self.tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-cs")
        self.translation_model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-cs")

    def translate(self, script):
        translated = self.translation_model.generate(**self.tokenizer(script, return_tensors="pt", padding=True))
        czech_text = self.tokenizer.decode(translated[0], skip_special_tokens=True)
        return czech_text

        
       