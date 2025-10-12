from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain.prompts import PromptTemplate

class InfoService:

    def __init__(self):
        self.modelName = "mxbai-embed-large:latest"
        self.persistDir = "chroma_db"
        self.llmModel = "llama3"

        self.llm = ChatOllama(model=self.llmModel)
        self.embeddings = OllamaEmbeddings(model=self.modelName)
        self.vs = Chroma(
            persist_directory=self.persistDir,
            embedding_function=self.embeddings
        )


        self.promptTemplate = """
            Bạn là một trợ lý AI thông minh.
            Luôn luôn trả lời bằng TIẾNG VIỆT rõ ràng, tự nhiên, kể cả khi câu hỏi bằng ngôn ngữ khác.
            Chỉ trả lời thông tin chính của câu hỏi không thêm chi tiết và nguồn tài liệu.
            Nếu không biết hãy trả lời: "Không có thông tin", không bịa ra thông tin hoặc lấy từ bên ngoài.

            Ngữ cảnh từ tài liệu:
            {context}

            Câu hỏi: {question}

            Trả lời bằng Tiếng Việt:
        """

        self.customPrompt = PromptTemplate(
            input_variables=["context", "question"],
            template=self.promptTemplate
        )
    
    # --------------------------------------------------------------

    def searchVectorDB(self, query):
        queryVector = self.embeddings.embed_query(query)
        docs = self.vs.similarity_search_by_vector(queryVector, k=4)
        context = "".join([d.page_content for d in docs])
        return context
    
    # --------------------------------------------------------------

    def sendToLLM(self, context, question):
        prompt = self.customPrompt.format(context=context, question=question)
        response = self.llm.invoke(prompt)
        return response
    
    # --------------------------------------------------------------
    
    def info_answer(self, query):
        try:
            print(f"Câu hỏi: {query}")
            context = self.searchVectorDB(query=query)
            answer = self.sendToLLM(context=context, question=query)
            print(f"\nTrả lời:\n\t{answer.content}")
            print("\n=================================================================\n")
            return {
                "success": True,
                "message": "Thành công",
                "type": "Info",
                "data": answer.content
            }
        except Exception as e:
            return {
                "success": False,
                "error": "Không tìm thấy thông tin"
            }
    
    # --------------------------------------------------------------