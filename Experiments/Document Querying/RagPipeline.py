from groq import Groq
from langchain.prompts import PromptTemplate


class RAGPipeline:
    def __init__(self, groq_api_key, Docdb_VS):
        """
        Initializes the RAG Pipeline with a Groq LLM API key and DocumentDB client.

        :param groq_api_key: API key for Groq LLM.
        :param docdb_client: Client for DocumentDB connection.
        """
        self.llm = Groq(api_key=groq_api_key)
        self.Docdb_VS = Docdb_VS  # DocumentDB Vector Search
        
        # Define the prompt template to be used in the RAG pipeline
        self.prompt_template = PromptTemplate(
            input_variables=["question", "documents"],
            template="""You are a helpful assistant. Based on the documents below, answer the following question: {question}

            Documents:
            {documents}
            """
        )

    def vector_search(self, prompt, num_results=5):
        """
        Performs a vector search on the DocumentDB instance based on the prompt.
        
        :param prompt: The query or prompt to search for in the database.
        :param num_results: Number of documents to retrieve.
        :return: List of documents retrieved from DocumentDB.
        """
        return self.Docdb_VS.vector_search(prompt, num_results)
    
    def generate_answer(self, question, num_results=5):
        """
        Generates an answer based on the provided question by fetching relevant documents
        from DocumentDB and passing them to the Groq LLM for generation.

        :param question: The question to answer.
        :param num_results: Number of documents to retrieve.
        :return: The generated answer.
        """
        # Step 1: Retrieve documents using vector search
        documents = self.vector_search(question, num_results)
        
        # Convert documents to a string format for input into the prompt
        docs_text = "\n".join([doc['text'] for doc in documents])  # Assuming 'text' contains the document content
        
        # Step 2: Format the prompt with the question and retrieved documents
        formatted_prompt = self.prompt_template.format(question=question, documents=docs_text)
        
        # Step 3: Generate the answer using the Groq LLM
        answer = self.llm.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": formatted_prompt,
                }
                ],
                model="llama-3.3-70b-versatile")
        
        return answer.choices[0].message.content

    def run(self, question, num_results=5):
        """
        Run the RAG pipeline: Retrieve documents and generate an answer.

        :param question: The question to be answered.
        :param num_results: Number of documents to retrieve.
        :return: The generated answer from the RAG pipeline.
        """
        return self.generate_answer(question, num_results)


# Example usage:
if __name__ == "__main__":
    # Initialize the pipeline with the Groq API key and DocumentDB client
    docdb_client = None  # Replace with your actual DocumentDB client instance
    groq_api_key = "your_groq_api_key_here"  # Replace with your actual Groq API key

    rag_pipeline = RAGPipeline(groq_api_key, docdb_client)

    # Query the pipeline
    question = "What are the latest trends in AI?"
    answer = rag_pipeline.run(question, num_results=5)
    
    print("Answer:", answer)
