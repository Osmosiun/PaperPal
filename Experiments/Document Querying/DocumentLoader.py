# Improvements
# Use Amazon Texttract


from langchain_community.document_loaders import PyPDFLoader



def load_and_read_pdf(file_path):

    loader = PyPDFLoader(file_path, extract_images = False)
    pages = []

    for page in loader.lazy_load():
        pages.append(page)
    
    return pages

if __name__ == "__main__":
    pages = load_and_read_pdf(file_path = "VisionTransformers.pdf")

    # print(f"{pages[0].metadata}\n")
    # print(pages[0].page_content)
