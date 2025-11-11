import math

class RecommendService:

    def distance(self, x1, y1, x2, y2):
        distance = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
        return distance*10

    def recommendJob(self, reference, jobs):
        location = reference['location']
        clientLat = location['lat']
        clientLon = location['lon']
        experiences = reference['experiences']

        experiencesScore = {
            'CLEANING': 2,
            'HEALTHCARE': 2,
            'MAINTENANCE': 2
        }

        check = {
            'CH': False,
            'CM': False,
            'HM': False
        }

        if experiences['CLEANING'] > experiences['HEALTHCARE']: check['CH'] = True
        if experiences['CLEANING'] > experiences['MAINTENANCE']: check['CM'] = True
        if experiences['HEALTHCARE'] > experiences['MAINTENANCE']: check['HM'] = True

        if check['CH'] and check['CM']:
            experiencesScore['CLEANING'] = 0
            if check['HM']: experiencesScore['HEALTHCARE'] = 1
            else: experiencesScore['MAINTENANCE'] = 1
        elif not check['CH'] and check['HM']:
            experiencesScore['HEALTHCARE'] = 0
            if check['CM']: experiencesScore['CLEANING'] = 1
            else: experiencesScore['MAINTENANCE'] = 1
        elif not check['CM'] and not check['HM']:
            experiencesScore['MAINTENANCE'] = 0
            if check['CH']: experiencesScore['CLEANING'] = 1
            else: experiencesScore['HEALTHCARE'] = 1


        indexScore = 0
        scoreMin = None
        print("==============================================================")
        print(f"Địa chỉ: {location['name']}\n")
        for i in range(len(jobs)):
            jobLat = jobs[i]['lat']
            jobLon = jobs[i]['lon']
            score = 0
            score += self.distance(clientLat, clientLon, jobLat, jobLon)
            score += experiencesScore[jobs[i]['serviceType']]

            print(f"Score: {str(score)}. {jobs[i]['location']}")

            if scoreMin==None or scoreMin>score:
                scoreMin = score
                indexScore = i

        return jobs[indexScore]