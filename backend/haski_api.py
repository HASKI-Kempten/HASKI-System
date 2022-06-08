import time
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/getLearningPath', methods = ['GET'])
def get_learning_path():
    if(request.method == 'GET'):
        learningPath = {
            "student": 1,
            "name": "John",
            "learnTyp": "Active, Verbal, Intuitive, Global",
            "elements": [
                {"name": "Metriken zu Lines of Codes", "position": 1, "type": "PDF"},
                {"name": "Metriken zu Lines of Codes", "position": 2, "type": "Video"},
                {"name": "Metriken zu Lines of Codes", "position": 3, "type": "Übung"},
            ]
        }

        return jsonify(learningPath)