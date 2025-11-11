from langchain_ollama import ChatOllama
from langchain.agents import Tool, initialize_agent
import json

from src.info.InfoController import InfoController
from src.job.JobController import JobController

class AragController:
    
    def __init__(self, infoController, jobController):

        self.llmModel = "llama3"
        self.llm = ChatOllama(model=self.llmModel, temperature=0)

        # self.infoController = infoController
        # self.jobController = jobController
        self.infoController = InfoController()
        self.jobController = JobController()

        self.infoTool = Tool(
            name="Search Info Application",
            func=lambda x: self.infoController.answer(**json.loads(x)),
            description=(
                "Trả lời CÁC CÂU HỎI VỀ THÔNG TIN ỨNG DỤNG (App): "
                "Ví dụ: ứng dụng có danh mục, dịch vụ gì, ai tạo ra ứng dụng, giá tiền, thời lượng."
                "Chỉ dùng cho câu hỏi về THÔNG TIN ỨNG DỤNG, KHÔNG phải tìm việc."
            ),
            return_direct=True
        )

        self.jobTool = Tool(
            name="Find Job Retriever",
            func=lambda x: self.jobController.search(**json.loads(x)),
            description=(
                "TÌM CÔNG VIỆC (Job): "
                "Dùng khi người dùng hỏi về việc làm, loại công việc, ngày làm, giá tiền, địa chỉ, thời gian làm việc."
                "KHÔNG dùng cho câu hỏi về ứng dụng."
            ),
            return_direct=True
        )

        self.agent = initialize_agent(
            tools=[self.jobTool, self.infoTool],
            llm=self.llm,
            agent_type="zero-shot-react-description",
            verbose=True,
            agent_kwargs={
                "prefix": (
                    "Bạn là một trợ lý AI hiểu tiếng Việt. "
                    "Luôn giữ nguyên văn bản đầu vào (không cắt, không dịch, không rút gọn). "
                    "Không dựa vào nội dung trong 'reference' để chọn công cụ. "
                    "Chỉ dựa vào câu hỏi ('query') để quyết định."
                ),
                "system_message": (
                    "Nếu người dùng hỏi về ứng dụng, dịch vụ, tính năng hoặc thông tin app -> dùng Search Info Application.\n"
                    "Nếu người dùng hỏi về việc làm, tìm kiếm công việc -> dùng Find Job Retriever.\n"
                    "Không chọn Find Job Retriever chỉ vì 'reference' chứa location."
                )
            }
        )

    def agent_search(self, query, reference):

        jobKeywords = ["tuyển", "tìm công việc", "cần người làm"]
        infoKeywords = ["ứng dụng", "app", "dịch vụ", "chức năng", "giá", "nhà sáng tạo", "thời lượng"]

        queryLower = query.lower()
        if any(k in queryLower for k in jobKeywords):
            response = self.jobController.search(query, reference) 
            # print(f"Job: {response}")
            return response
        elif any(k in queryLower for k in infoKeywords):
            response = self.infoController.answer(query, reference)
            # print(f"Info: {response}")
            return response
        else:
            input_data = json.dumps({
                "query": query,
                "reference": reference
            })

            response = self.agent.invoke({"input": input_data})
            return response.output
