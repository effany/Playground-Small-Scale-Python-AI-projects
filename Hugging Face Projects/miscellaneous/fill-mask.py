from transformers import pipeline

unmasker = pipeline('fill-mask', model='bert-base-uncased', top_k=5)
result1 = unmasker('This man works as a [MASK].')
result2 = unmasker('This woman works as a [MASK].')

print("Man:", [r["token_str"] for r in result1])
print("Woman:", [r["token_str"] for r in result2])