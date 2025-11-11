from src.accuracy.data.CreateData import getDatas
from src.arag.AragController import AragController
from src.info.InfoController import InfoController
from src.job.JobController import JobController

def checkJob(details, response):
    data = response['data']
    print(f"Response: {data}")

    serviceType = details['serviceType']
    price = details['price']
    time = details['time']
    location = details['location']

    print(details)
    if serviceType['check'] and serviceType['checkName']!=data['serviceType']: 
        print("Error: ServiceType")
        return False

    if price['check']:
        [title, salary] = price['checkName'].split(" ")

        if title == "Above" and data['price']<=int(salary): 
            print("Error: Price")
            return False
        elif title == "Equal" and data['price']!=int(salary): 
            print("Error: Price")
            return False
        elif title == "Below" and data['price']>=int(salary): 
            print("Error: Price")
            return False

    if time['check']:
        timeRef = time['checkName'].split(" hoặc ")

        checkTime = False
        for i in timeRef:
            if i == data['startTime']: checkTime = True

        if not checkTime: 
            print("Error: Time")
            return False

    if location['check']:
        locationRef = location['checkName'].split(", ")

        checkLocation = False
        for i in locationRef[::-1]:
            if i in data['location']:
                checkLocation = True
                break

        if not checkLocation: 
            print("Error: Location")
            return False

    return True

def checkInfo(details, response):
    data = response['data'].strip()
    array = []

    if details['name'] == 'Other': array = details['others']
    elif details['name'] == 'Cleaning': array = details['tasks']
    elif details['name'] == 'Healthcare': 
        if details['duties']!=None: array.extend(details['duties'])
        if details['excludedTasks']!=None: array.extend(details['excludedTasks'])

    for i in array:
        if i.lower() not in data.lower(): return False

    return True

if __name__ == "__main__":
    datas = getDatas()

    cntCorrect = 0
    cntIncorrect = 0

    aragController = AragController(InfoController(), JobController())
    for data in datas:
        response = aragController.agent_search(data['query'], data['reference'])

        answer = data['answer']
        successCheck = answer['success']
        typeCheck = answer['type']
        details = answer['details']

        check = False 
        if response['success']==successCheck and response['type']==typeCheck:
            if typeCheck=='Job' and checkJob(details=details, response=response): check = True
            elif typeCheck=='Info' and checkInfo(details=details, response=response): check = True

        if check: cntCorrect += 1
        else: cntIncorrect += 1

        print(f"Result: {check}")
        print("=====================================================")        

    print('\n================Result================')
    print(f"Correct: {cntCorrect}")
    print(f"Incorrect: {cntIncorrect}")