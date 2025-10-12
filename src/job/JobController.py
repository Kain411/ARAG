from src.utils.OllamaService import OllamaService
from src.utils.PineconeService import PineconeService

class JobController:

    def __init__(self):
        self.ollamaService = OllamaService()
        self.pineconeService = PineconeService()

    # --------------------------------------------------------------

    def search(self, query):
        embed = self.ollamaService.ollama_get_embedding(query)

        if not embed:  return { "success": False }   

        result = self.pineconeService.pinecone_search_data(embed)
        return result
    
    # --------------------------------------------------------------