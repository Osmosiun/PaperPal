# Improvement
# Remove unwanted stuff
# Use Semantic Splitter

from DocumentLoader import load_and_read_pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_cohere.embeddings import CohereEmbeddings

def combine_text(pages):
    '''
    This function will take list of pages generate by the PyPdf loader and then cobine text from each page
    '''
    final_text = ""

    n = len(pages)

    for i in range(n):
        final_text += pages[i].page_content
    
    return final_text

def recursive_chunking(text):

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000,
                                              chunk_overlap=200,
                                              length_function=len,
                                              is_separator_regex=True)
    
    chunks_obj = text_splitter.create_documents([text])

    chunks_text = [cur_obj.page_content for cur_obj in chunks_obj]
    
    return chunks_text

def calculate_num_splits(cur_text_len, max_chunk_size):
    
    num_splits = 2

    while(cur_text_len/num_splits > max_chunk_size):
        num_splits += 1
    
    return num_splits 

def recursive_split_big_chunks(cur_text, cur_text_len, max_chunk_size):
    num_splits = calculate_num_splits(cur_text_len, max_chunk_size)

    chunk_size_of_recursive_splitter = cur_text_len/num_splits

    recursive_text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size_of_recursive_splitter,
                                                                chunk_overlap=int(0.1*cur_text_len),
                                                                length_function=len,
                                                                is_separator_regex=True)
    
    chunks_obj = recursive_text_splitter.create_documents([cur_text])

    chunks_text = [cur_obj.page_content for cur_obj in chunks_obj]

    return chunks_text

def post_process_chunks_of_text(chunks_of_text, min_chunk_size, max_chunk_size):

        final_chunks = []
        forward_text = ""

        for cur_text in chunks_of_text:

            cur_text += forward_text
            
            cur_text_len = len(cur_text)

            if cur_text_len > max_chunk_size:
                final_chunks += recursive_split_big_chunks(cur_text, cur_text_len, max_chunk_size)
            
            elif cur_text_len < min_chunk_size:
                 
                if final_chunks:
                    final_chunks[-1] += cur_text
                else:
                    forward_text = cur_text 
            
            else:
                final_chunks.append(cur_text)
        
        return final_chunks
            
def semantic_chunking(combined_text, min_chunk_size, max_chunk_size):

    cohere_api_key = "NgN2P0LvOckIGwvcj0xcUfYluIzTEaVZ9Y9zxpo8" # This will be save in environment

    cohere_embeddings = CohereEmbeddings(cohere_api_key=cohere_api_key, model="embed-english-light-v3.0")

    text_splitter = SemanticChunker(cohere_embeddings,breakpoint_threshold_type = 'gradient')
    
    chunks_obj = text_splitter.create_documents([combined_text])

    chunks_of_text = [cur_obj.page_content for cur_obj in chunks_obj]

    return post_process_chunks_of_text(chunks_of_text, min_chunk_size, max_chunk_size)


def chunking(text, splitter = "recursive"):
    '''
    This function will take list of pages generate by the PyPdf loader and then perform chunking operation
    '''

    if splitter=="recursive":
        return recursive_chunking(text)

    elif splitter == "semantic":
        return semantic_chunking(text, min_chunk_size=400, max_chunk_size=2000)
    
    else:
        raise ValueError("Wrong splitter option choosen")

if __name__ == "__main__":
    pages = load_and_read_pdf(file_path = "VisionTransformers.pdf")
    print(chunking(combine_text(pages)))