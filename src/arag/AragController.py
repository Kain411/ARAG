from langchain_ollama import ChatOllama
from langchain.agents import Tool, initialize_agent
import json

from src.job.JobController import JobController
from src.info.InfoController import InfoController


class AragController:
    
    def __init__(self):

        self.llmModel = "llama3"
        self.llm = ChatOllama(model=self.llmModel, temperature=0)

        self.infoController = InfoController()
        self.jobController = JobController()

        self.infoTool = Tool(
            name="Search Info Application",
            func=lambda x: self.infoController.answer(**json.loads(x)),
            description=(
                "Dùng để trả lời về các thông tin của ứng dụng bao gồm các thông tin như: danh mục, dịch vụ, thời lượng, mức tiền, thông tin người sáng tạo."
            ),
            return_direct=True
        )

        self.jobTool = Tool(
            name="Find Job Retriever",
            func=lambda x: self.jobController.search(**json.loads(x)),
            description=(
                "Dùng để tìm kiếm công việc theo nhu cầu của người dùng như ngày làm, loại công việc, giá tiền, địa chỉ hoặc số giờ làm."
            ),
            return_direct=True
        )

        self.agent = initialize_agent(
            tools=[self.jobTool, self.infoTool],
            llm=self.llm,
            agent_type="zero-shot-react-description",
            verbose=True
        )

    def agent_search(self, query, reference):
        input_data = json.dumps({
            "query": query,
            "reference": reference
        })

        response = self.agent.invoke({"input": input_data})
        return response
