from src.utils.OllamaService import OllamaService
from src.utils.PineconeService import PineconeService
from src.utils.RecommendService import RecommendService

class JobController:

    def __init__(self):
        self.ollamaService = OllamaService()
        self.pineconeService = PineconeService()
        self.recommendService = RecommendService()

    # --------------------------------------------------------------

    def search(self, query: str, reference: dict):
        
        query_vector = f"{query}"

        embed = self.ollamaService.ollama_get_embedding(query_vector)

        if not embed:  return { "success": False }   

        result = self.pineconeService.pinecone_search_data(embed, query)

        if result['success']: 
            jobRecommend = self.recommendService.recommendJob(reference=reference, jobs=result['data'])
            print(jobRecommend)

        return {
            "jobRecom": jobRecommend,
            "jobs": result['data']
        }
    
    # --------------------------------------------------------------