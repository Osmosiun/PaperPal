import cohere
import numpy as np
from Chunking import chunking, combine_text
from DocumentLoader import load_and_read_pdf



cohere_key = "NgN2P0LvOckIGwvcj0xcUfYluIzTEaVZ9Y9zxpo8" 

def generate_embeddings(chunks_of_text):

    co = cohere.Client(cohere_key)

    doc_emb = co.embed(texts=chunks_of_text, input_type="search_document", model="embed-english-v3.0").embeddings
    doc_emb = np.asarray(doc_emb)

    return doc_emb

if __name__ == "__main__":

    pages = load_and_read_pdf(file_path = "VisionTransformers.pdf")

    final_text = combine_text(pages)

    chunks_of_text = chunking(final_text)

    embeddings = generate_embeddings(chunks_of_text)

    print(embeddings.shape)