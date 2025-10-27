from flask import Flask, request, jsonify
from flask_cors import CORS
from src.create.CreateController import CreateController
from src.job.JobController import JobController
from src.info.InfoController import InfoController
from src.arag.AragController import AragController

app = Flask(__name__)

CORS(app, origins="*", supports_credentials=True)

# --------------------------------------------------------------

@app.route("/api/job-embedding", methods=['POST'])
def job_embed():
    job = request.get_json()
    if not job:
        return jsonify({
            "success": False,
            "error": "Phải là JSON."
        })
    
    createController = CreateController()
    result = createController.job_embed_controller(job)

    if result:
        return jsonify({
            "success": True,
            "message": "Thành công"
        })
    else:
        return jsonify({
            "success": False,
            "error": "Không thành công"
        })
    
# --------------------------------------------------------------

@app.route("/api/update-metadata/status", methods=['PUT'])
def update_status():
    data = request.get_json()
    jobID = data['uid']
    status = data['status']

    createController = CreateController()
    result = createController.update_status_controller(jobID, status)

    if result:
        return jsonify({
            "success": True,
            "message": "Thành công"
        })
    else:
        return jsonify({
            "success": False,
            "error": "Không thành công"
        })

# --------------------------------------------------------------

@app.route("/api/update-metadata/location", methods=['PUT'])
def update_location():
    data = request.get_json()
    jobID = data['uid']
    location = data['location']

    createController = CreateController()
    result = createController.update_location_controller(jobID, location)

    if result:
        return jsonify({
            "success": True,
            "message": "Thành công"
        })
    else:
        return jsonify({
            "success": False,
            "error": "Không thành công"
        })

# --------------------------------------------------------------
    
@app.route("/api/job/<jobID>", methods=['DELETE'])
def delete_embed(jobID):
    
    createController = CreateController()
    result = createController.delete_job_embed(jobID)
    
    return result

# --------------------------------------------------------------
# Test: Find Job
@app.route("/api/job/search", methods=['POST'])
def search_job():
    data = request.get_json()

    jobController = JobController()
    result = jobController.search(data['query'], data['reference'])

    return result

# --------------------------------------------------------------
# Test: Find info of application
@app.route("/api/info/answer", methods=['POST'])
def answer_info():
    data = request.get_json()

    infoController = InfoController()
    result = infoController.answer(data['query'], data['reference'])

    return result

# --------------------------------------------------------------

@app.route("/api/chatbot", methods=['POST'])
def chat_box():
    data = request.get_json(force=True)

    print(data['query'])

    aragController = AragController()
    result = aragController.agent_search(data['query'], data['reference'])

    return result

# --------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=8000)

# --------------------------------------------------------------