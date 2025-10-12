import requests
import json

class OllamaService: 

    def __init__(self):
        self.modelName = "mxbai-embed-large:latest"

    def get_embedding(self, text_to_embed):

        url = "http://localhost:11434/api/embeddings"
        
        payload = {
            "model": self.modelName,
            "prompt": text_to_embed,
        }
        
        try:
            response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
            response.raise_for_status()
            
            result = response.json()
            embedding = result.get("embedding")
            
            return embedding

        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi gọi API Ollama: {e}")
            return None
        
    # --------------------------------------------------------------

    def ollama_get_embedding(self, query):

        vector = self.get_embedding(query.lower())

        if vector:
            print(f"Chuỗi văn bản: '{query}'")
            print(f"Kích thước vector (Dimensions): {len(vector)}")
        else:
            print("Không thể trích xuất embedding.")
        
        return vector
    
    # --------------------------------------------------------------