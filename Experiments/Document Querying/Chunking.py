# Improvement
# Remove unwanted stuff
# Use Semantic Splitter

from DocumentLoader import load_and_read_pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter

def combine_text(pages):
    '''
    This function will take list of pages generate by the PyPdf loader and then cobine text from each page
    '''
    final_text = ""

    n = len(pages)

    for i in range(n):
        final_text += pages[i].page_content
    
    return final_text


def chunking(text):
    '''
    This function will take list of pages generate by the PyPdf loader and then perform chunking operation
    '''

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
                                              chunk_overlap=100,
                                              length_function=len,
                                              is_separator_regex=True)
    
    chunks_obj = text_splitter.create_documents([text])

    chunks_text = [cur_obj.page_content for cur_obj in chunks_obj]
    
    return chunks_text

if __name__ == "__main__":
    pages = load_and_read_pdf(file_path = "VisionTransformers.pdf")
    print(chunking(combine_text(pages)))