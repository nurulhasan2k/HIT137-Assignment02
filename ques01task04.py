#Running NER using Spacy
import spacy

from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

nlp_sci_sm = spacy.load('en_core_sci_sm')
nlp_ner_bc5cdr = spacy.load('en_ner_bc5cdr_md')

with open('q1Output_combinedText.txt', 'r') as file:
    text = file.read()

text = text[:100]
#limited the data to check if we getting appropriate output.

def chunk_text(text, chunk_size=100000):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

text_chunks = chunk_text(text)    

for i, chunk in enumerate(text_chunks):
    print(f"Processing chunk {i + 1}/{len(text_chunks)} with en_core_sci_sm")
    doc_sci_sm = nlp_sci_sm(chunk)
    for ent in doc_sci_sm.ents:
        print(ent.text, ent.label_)

    print(f"\nProcessing chunk {i + 1}/{len(text_chunks)} with en_ner_bc5cdr_md")
    doc_ner_bc5cdr = nlp_ner_bc5cdr(chunk)
    for ent in doc_ner_bc5cdr.ents:
        print(ent.text, ent.label_)
        

#Running NER using BioBERT

tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")

ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)

for i, chunk in enumerate(text_chunks):
    tokenized_chunk = tokenizer(chunk, truncation=True, max_length=512, return_tensors="pt")
    
    ner_results = ner_pipeline(chunk[:512])
    
    print(f"Processing chunk {i + 1}/{len(text_chunks)} with BioBERT")
    for result in ner_results:
        print(f"Entity: {result['word']}, Label: {result['entity']}")
        
        
#compare the results from both Spact and BioBERT
#collect entities from SciSpaCy and BioBERT
sci_sm_entities = set([ent.text for chunk in text_chunks for ent in nlp_sci_sm(chunk).ents])
bc5cdr_entities = set([ent.text for chunk in text_chunks for ent in nlp_ner_bc5cdr(chunk).ents])
biobert_entities = set([result['word'] for chunk in text_chunks for result in ner_pipeline(chunk)])
  
#compare entities
common_entities = sci_sm_entities.intersection(biobert_entities)
unique_sci_sm = sci_sm_entities.difference(biobert_entities)
unique_biobert = biobert_entities.difference(sci_sm_entities)

print("Common Entities Detected by Both Models:", common_entities)
print("Entities Unique to en_core_sci_sm:", unique_sci_sm)
print("Entities Unique to BioBERT:", unique_biobert)  