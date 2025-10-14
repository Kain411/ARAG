from langchain_ollama import ChatOllama
from langchain.agents import Tool, initialize_agent
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
            func=self.infoController.answer,
            description=(
                "Dùng để trả lời về các thông tin của ứng dụng như danh mục, dịch vụ, công việc, giá tiền, ca làm việc, thời lượng làm việc, ..."
            ),
            return_direct=True
        )

        self.jobTool = Tool(
            name="Find Job Retriever",
            func=self.jobController.search,
            description=(
                "Không dùng tool này nếu role là user. Dùng để tìm kiếm công việc theo nhu cầu như ngày làm, giờ làm, loại công việc, giá tiền, địa chỉ hoặc số giờ làm."
            ),
            return_direct=True
        )

        self.agent = initialize_agent(
            tools=[self.jobTool, self.infoTool],
            llm=self.llm,
            agent_type="zero-shot-react-description",
            verbose=True
        )

    def agent_search(self, query):
        response = self.agent.run(query)
        return response