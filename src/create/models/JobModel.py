class JobModel:

    def __init__(self, data):
        self.uid = data['uid']
        self.userID = data['userID']
        self.price = data['price']
        self.startTime = data['startTime']
        self.listDays = data['listDays']
        self.status = data['status']
        self.serviceType = data['serviceType']
        self.location = data['location']
        self.createdAt = data['createdAt']
        
class CleaningJobModel(JobModel):

    def __init__(self, data):
        super(self, data)
        self.durationID = data['durationID']