from transformers import WhisperProcessor, WhisperForConditionalGeneration
from transformers import MarianMTModel, MarianTokenizer
import librosa 
from TTS.api import TTS

## this is a test file. Testing all the needed functions

processor = WhisperProcessor.from_pretrained('openai/whisper-small')
model = WhisperForConditionalGeneration.from_pretrained('openai/whisper-small')
forced_decoder_ids = processor.get_decoder_prompt_ids(language='chinese', task='translate')

audio_array, sample_rate = librosa.load('./assets/whisper-translate.m4a', sr=16000)

input_features = processor(audio_array, sampling_rate=sample_rate, return_tensors="pt").input_features 

predicted_ids = model.generate(input_features, forced_decoder_ids=forced_decoder_ids)

transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

# Translate English to Czech using MarianMT directly
tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-cs")
translation_model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-cs")

translated = translation_model.generate(**tokenizer(transcription[0], return_tensors="pt", padding=True))
czech_text = tokenizer.decode(translated[0], skip_special_tokens=True)

tts = TTS('tts_models/multilingual/multi-dataset/xtts_v2')
tts_to_file(text=czech_text, file_path='./assets/output.wav')

print("English:", transcription[0])
print("Czech:", czech_text)