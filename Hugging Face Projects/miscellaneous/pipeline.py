from transformers import pipeline

# classifer = pipeline('sentiment-analysis')
# result = classifer('I feel very happy today!')


# unmasker = pipeline('fill-mask')
# result = unmasker('I will tell you all about <mask>', top_k=2)

# print(result)

# ner = pipeline('ner', aggregation_strategy="simple")
# result = ner("I'm Bla, working in bla and in bla")

# print(result)

from transformers import BartForConditionalGeneration, BartTokenizer

# For summarization without the pipeline task
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

text = """
Guide intro: ( while we stand in the middle of the stage, heads down prepare for the sing)
(0:00 - 0:03) Welcome to Taiwan. A small, vibrant island sitting in the Pacific Ocean, home to
23 million people.
(0:03 - 0:10) It's an island forged by a complex history of foreign rule—from Dutch trade to
Japanese occupation—giving it a truly unique identity. Yet, it thrives as a center for cutting-edge
innovation.
(0:10 - 0:16) But beyond the hardware is the heritage: a delicious fusion of Chinese, Japanese,
and indigenous influences. We're the birthplace of Boba Milk Tea and a center for exquisite tea
culture and artisanal crafts.
(0:16 - 0:20) A vibrant democracy and cultural powerhouse, shaped by its own past. This is a
place you need to experience. This is Taiwan.
"""

inputs = tokenizer(text, return_tensors='pt', max_length=1024, truncation=True)
summary_ids = model.generate(inputs['input_ids'], max_length=60, min_length=50, length_penalty=2.0, num_beams=4)
result = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print(result)