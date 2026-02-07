from transformers import WhisperProcessor, WhisperForConditionalGeneration
from datasets import load_dataset
import librosa 

class Transcribtor():
    def __init__(self):
        self.processor = WhisperProcessor.from_pretrained("openai/whisper-small")
        self.model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")

        self.model.config.forced_decoder_ids = None

    def transcribe(self, audio):
        audio_array, sample_rate = librosa.load(audio, sr=16000)
        input_features = self.processor(audio_array, sampling_rate=sample_rate, return_tensors="pt").input_features 
        predicted_ids = self.model.generate(input_features, language='en')
        transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=False)

        return transcription


## translation

