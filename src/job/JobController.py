from src.utils.OllamaService import OllamaService
from src.utils.PineconeService import PineconeService

class JobController:

    def __init__(self):
        self.ollamaService = OllamaService()
        self.pineconeService = PineconeService()

    # --------------------------------------------------------------

    def search(self, query: str, reference: dict):
        location = reference['location']

        print(query)
        print(location)

        query_vector = f"{query}. Tôi ở địa chỉ {location}"
        embed = self.ollamaService.ollama_get_embedding(query_vector)

        if not embed:  return { "success": False }   

        result = self.pineconeService.pinecone_search_data(embed)
        return result
    
    # --------------------------------------------------------------