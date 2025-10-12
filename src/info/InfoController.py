from src.info.InfoService import InfoService

class InfoController:
    
    def __init__(self):
        self.infoService = InfoService()

    # --------------------------------------------------------------

    def answer(self, query):
        result = self.infoService.info_answer(query)
        return result
    
    # --------------------------------------------------------------