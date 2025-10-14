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
# Test: Find Job
@app.route("/api/job/search", methods=['POST'])
def search_job():
    data = request.get_json()

    jobController = JobController()
    result = jobController.search(data['query'])

    return result

# --------------------------------------------------------------
# Test: Find info of application
@app.route("/api/info/answer", methods=['POST'])
def answer_info():
    data = request.get_json()

    infoController = InfoController()
    result = infoController.answer(data['query'])

    return result

# --------------------------------------------------------------

@app.route("/api/chatbox", methods=['POST'])
def chat_box():
    data = request.get_json()

    aragController = AragController()
    result = aragController.agent_search(data['query'])

    return result

# --------------------------------------------------------------

@app.route("/api/job/<jobID>", methods=['DELETE'])
def delete_embed(jobID):
    
    createController = CreateController()
    result = createController.delete_job_embed(jobID)
    
    return result

# --------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=8000)

# --------------------------------------------------------------