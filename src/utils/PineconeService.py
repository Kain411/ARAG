import os
import requests
import json
from pinecone import Pinecone
from dotenv import load_dotenv

load_dotenv()

class PineconeService:
    
    def __init__(self):

        self.PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
        self.PINECONE_HOST = os.getenv("PINECONE_HOST")

        self.pc = Pinecone(api_key=self.PINECONE_API_KEY)
        self.index = self.pc.Index(name="demo-pinecone", host=self.PINECONE_HOST)

        self.namespace = "jobs-area"

    # --------------------------------------------------------------

    def pinecone_upsert_all_datas(self, datas):
        self.index.upsert_records(
            self.namespace,
            datas
        ) 

    # --------------------------------------------------------------

    def pinecone_upsert_one_data(self, job, embed):

        self.index.upsert(
            namespace=self.namespace,
            vectors=[
                {
                    "id": job['uid'],
                    "values": embed,
                    "metadata": {
                        "jobID": job['uid'],
                        "userID": job['user']['uid'],
                        "price": job['price'],
                        "startTime": job['startTime'],
                        "listDays": job['listDays'],
                        "serviceType": job['serviceType'],
                        "location": job['location'],
                        "createdAt": job['createdAt']
                    }
                }
            ]
        )
        return True

    # --------------------------------------------------------------

    def pinecone_update_metadata_status(self, jobID, status):
        
        try:
            url = f"{self.PINECONE_HOST}/vectors/update"

            headers = {
                "Api-Key": self.PINECONE_API_KEY,
                "Content-Type": "application/json",
                "X-Pinecone-API-Version": "unstable"
            }

            data = {
                "dry_run": False,
                "namespace": self.namespace,
                "filter": {
                    "jobID": {"$eq": f"{jobID}"}
                },
                "setMetadata": {
                    "status": f"{status}"
                }
            }

            response = requests.post(url, headers=headers, data=json.dumps(data))
            print(response.json())
            return True
        
        except requests.exceptions.RequestException as e:
            print(f"Lỗi cập nhật metadata Pinecone: {e}")
            return False

    # --------------------------------------------------------------

    def pinecone_search_data(self, embed):
        
        try:
            result = self.index.query(
                namespace = self.namespace,
                vector=embed,
                top_k=2,
                include_metadata=True,
                include_values=False
            )

            print(result)

            data = []
            for match in result['matches']:
                data.append(match['metadata'])
            return {
                "success": True,
                "message": "Thành công",
                "type": "Job",
                "data": data
            }
        except Exception as e:
            print(f"Lỗi tìm kiếm: {e}")
            return {
                "success": False,
                "error": "Không tìm thấy thông tin"
            }

    # --------------------------------------------------------------

    def pinecone_delete(self, jobID):
        try: 
            self.index.delete(ids=[jobID], namespace=self.namespace)

            return {
                "success": True,
                "message": "Thành công"
            }
        except Exception as e:
            print(e)
            return {
                "success": False,
                "error": "Xoá embed không thành công"
            }

    # --------------------------------------------------------------