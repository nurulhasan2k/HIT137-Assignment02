from transformers import AutoTokenizer
from collections import Counter

tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

with open('q1Output_combinedText.txt', 'r') as file:
    text = file.read()

#function to count unique tokens in the text file using chunks    
def chunk_text(text, chunk_size=512):
    tokens = tokenizer.tokenize(text)
    return [tokens[i:i + chunk_size] for i in range(0, len(tokens), chunk_size)]

# text = text[:200]
#limited the data to check if we getting appropriate output.
token_chunks = chunk_text(text)

all_tokens = [token for chunk in token_chunks for token in chunk]

token_counts = Counter(all_tokens)

top_30_tokens = token_counts.most_common(30)

for token, count in top_30_tokens:
    print(f"Token: {token}, Count: {count}")