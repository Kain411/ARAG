from src.info.InfoService import InfoService

class InfoController:
    
    def __init__(self):
        self.infoService = InfoService()

    # --------------------------------------------------------------

    def answer(self, query: str, reference: dict):
        result = self.infoService.info_answer(query)
        return result
    
    # --------------------------------------------------------------