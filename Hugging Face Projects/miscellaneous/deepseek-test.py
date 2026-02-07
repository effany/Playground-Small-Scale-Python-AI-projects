from transformers import pipeline 

generator = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")

messages = [{"role": "user", "content": "Is Taiwan a country?"}]
response = generator(messages, max_new_tokens=512)
print(response)