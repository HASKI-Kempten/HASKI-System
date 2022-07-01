from flask import Flask, jsonify, request
import json
import random
from data.elements import elements as E

app = Flask(__name__)

elements = { "elements": E}

# elements = {"elements": [
#     { "id": 1, "name": "My first", "position": 2, "difficulty": "Easy", "progress": 2, "date": "2022-06-13T16:05:54.908Z", "topic": "Informatik I", "semester": 2, "style": "visual", "proLIST": "Lorem Ipsum", "contraLIST": "Lorem Ipsum", "duration": 1.5 },
#     { "id": 2, "name": "My second element", "position": 3, "difficulty": "Easy", "progress": 2, "date": "2022-06-13T16:05:54.908Z", "topic": "Informatik I", "semester": 2, "style": "visual", "proLIST": "Lorem Ipsum", "contraLIST": "Lorem Ipsum", "duration": 1.5 },
#     { "id": 3, "name": "My last element", "position": 4, "difficulty": "Easy", "progress": 2, "date": "2022-06-13T16:05:54.908Z", "topic": "Informatik I", "semester": 2, "style": "visual", "proLIST": "Lorem Ipsum", "contraLIST": "Lorem Ipsum", "duration": 1.5 }
#     ]}

learning_path = {"1-987": [{"id": 1, "moduleId": 987, "module": "Informatik I", "elements": [
        {"elementId": 12, "position": "1.1"},
        {"elementId": 2, "position": "1.2"},
        {"elementId": 3, "position": "2.1"}
    ]}] }

learning_way ={}

module =  {"modules": [{"id": 1, "name": "Einführung in die Informatik", "module": "IT-1234", "semester": 1},{"id": 2, "name": "Einführung in die Informatik II", "module": "IT-9876", "semester": 2}]}

students = {"students": [{"id": 1, "name": "Max Musterfrau", "semester": 2, "style": "Active, Verbal, Intuitive, Global", "courseOfStudy": "Angewandte Informatik", "modules": [{"id": 1, "name": "Einführung in die Programmierung", "module": "IT-1234", "semester": 1}]}]}

@app.route('/elements')
def get_elements():
    return jsonify(elements)

@app.route('/elements', methods=['POST'])
def upload_element():
    uploaded_element = request.get_json()
    new_element = {
        'id': len(elements['elements'])+1,
        'name': uploaded_element['name'].strip(),
        'difficulty': '1',
        'creationDate': uploaded_element['creationDate'].strip(),
        'modul': uploaded_element['modul'].strip(),
        'semester': uploaded_element['semester'],
        'style': uploaded_element['style'].strip(),
        'proLIST': '',
        'contraLIST': '',
        'averageDuration': 0
    }
    elements['elements'].append(new_element)
    return jsonify(elements['elements'][new_element['id']-1]), 201

@app.route('/elements/<int:id>')
def get_element_by_id(id):
    for element in elements['elements']:
        if element['id'] == id:
            return jsonify(element)
    return {'code': 404, 'message': "Element not found!"}

@app.route('/elements/<int:id>', methods=['PUT'])
def update_element(id):
    updated_element = request.get_json(force=True)
    if 'name' in updated_element:
        name = updated_element['name']
        for element in elements['elements']:
            if element['id'] == id:
                element.update({'name': name})
    if 'position' in updated_element:
        position = updated_element['position']
        for element in elements['elements']:
            if element['id'] == id:
                element.update({'position': position})
    if 'difficulty' in updated_element:
        difficulty = updated_element['difficulty']
        for element in elements['elements']:
            if element['id'] == id:
                element.update({'difficulty': difficulty})
    if 'progress' in updated_element:
        progress = updated_element['progress']
        for element in elements['elements']:
            if element['id'] == id:
                element.update({'progress': progress})
    if 'date' in updated_element:
        date = updated_element['date']
        for element in elements['elements']:
            if element['id'] == id:
                element.update({'date': date})
    if 'topic' in updated_element:
        topic = updated_element['topic']
        for element in elements['elements']:
            if element['id'] == id:
                element.update({'topic': topic})
    if 'semester' in updated_element:
        semester = updated_element['semester']
        for element in elements['elements']:
            if element['id'] == id:
                element.update({'semester': semester})
    if 'style' in updated_element:
        style = updated_element['style']
        for element in elements['elements']:
            if element['id'] == id:
                element.update({'style': style})
    if 'proLIST' in updated_element:
        proLIST = updated_element['proLIST']
        for element in elements['elements']:
            if element['id'] == id:
                element.update({'proLIST': proLIST})
    if 'contraLIST' in updated_element:
        contraLIST = updated_element['contraLIST']
        for element in elements['elements']:
            if element['id'] == id:
                element.update({'contraLIST': contraLIST})
    if 'duration' in updated_element:
        duration = updated_element['duration']
        for element in elements['elements']:
            if element['id'] == id:
                element.update({'duration': duration})
    return jsonify(elements['elements'][id-1])

@app.route('/student')
def get_students():
    return jsonify(students)

@app.route('/student', methods=['POST'])
def create_student():
    created_student = request.get_json()
    name, semester, courseOfStudy = created_student['name'].strip(),created_student['semester'],created_student['courseOfStudy'].strip()
    new_student = {
        'id': len(students['students'])+1,
        'name': name,
        'semester': semester,
        'style': '',
        'courseOfStudy': courseOfStudy,
        'modules': []
    }
    students['students'].append(new_student)
    return jsonify(students['students'][new_student['id']-1]), 201

@app.route('/student/<int:studentId>')
def get_student_by_id(studentId):
    for student in students['students']:
        if student['id'] == studentId:
            return jsonify(student)
    return {'code': 404, 'message': "Student not found!"}

@app.route('/student/<int:studentId>', methods=['PUT'])
def update_student(studentId):
    updated_student = request.get_json(force=True)
    if 'name' in updated_student:
        for student in students['students']:
            if student['id'] == studentId:
                student.update({'name': updated_student['name']})
    if 'semester' in updated_student:
        for student in students['students']:
            if student['id'] == studentId:
                student.update({'semester': updated_student['semester']})
    if 'style' in updated_student:
        for student in students['students']:
            if student['id'] == studentId:
                student.update({'style': updated_student['style']})
    if 'courseOfStudy' in updated_student:
        for student in students['students']:
            if student['id'] == studentId:
                student.update({'courseOfStudy': updated_student['courseOfStudy']})
    if 'modules' in updated_student:
        for student in students['students']:
            if student['id'] == studentId:
                student.update({'modules': updated_student['modules']})
    return jsonify(students['students'][studentId-1])

@app.route('/learningPath/<int:pathId>/<int:moduleId>')
def get_learning_path_for_student(pathId,moduleId):
    id = str(pathId) + "-" + str(moduleId)
    return jsonify(learning_path[id][0]),200

@app.route('/learningPath', methods=['POST'])
def create_learning_Path():
    created_learning_path = request.get_json()
    id = str(len(learning_path)+1) + "-" + str(created_learning_path['moduleId'])
    new_elements = []
    for element in created_learning_path['elements']:
        new_elements.append({
            'elementId': element['elementId'],
            'position': element['position'].strip()
        })
    new_learning_path = [{
        'id': id,
        'moduleId': created_learning_path['moduleId'],
        'module': created_learning_path['module'],
        'elements': new_elements        
    }]
    learning_path[id] = new_learning_path
    return jsonify(learning_path[id][0]), 201

@app.route('/learningPath/<int:pathId>/<int:moduleId>', methods=['PUT'])
def update_learning_path(pathId,moduleId):
    created_learning_path = request.get_json()
    id = str(pathId) + "-" + str(moduleId)
    new_elements = []
    for element in created_learning_path['elements']:
        new_elements.append({
            'elementId': element['elementId'],
            'position': element['position'].strip()
        })
    new_learning_path = [{
        'id': pathId,
        'moduleId': created_learning_path['moduleId'],
        'module': created_learning_path['module'],
        'elements': new_elements        
    }]
    learning_path[id] = new_learning_path
    return jsonify(learning_path[id][0]), 200

@app.route('/learningWay/<int:studentId>/<int:moduleId>', methods=['POST'])
def create_learning_way(studentId, moduleId):
    created_learning_way = request.get_json()
    id = str(studentId) + "-" + str(len(learning_way)+1)
    way_id = len(learning_way)+1
    new_learning_way = {}
    new_learning_way['id'] = way_id
    new_learning_way['moduleId'] = moduleId
    new_learning_way['studentId'] = studentId
    new_learning_way['recommendedElement'] = None
    for key in learning_path:
        if str("-"+str(moduleId)) in key:
            new_learning_way['elements'] = learning_path[key][0]['elements']
            for element in new_learning_way['elements']:
                element['done'] = False
                element['doneAt'] = None
                element['evaluation'] = None
            new_learning_way['module'] = learning_path[key][0]['module'] 
    if "module" not in new_learning_way:
        new_learning_way['elements'] = None
        new_learning_way['module'] = None
    learning_way[id] = new_learning_way
    print(id)
    return jsonify(new_learning_way), 201

@app.route('/learningWay/<int:studentId>/<int:moduleId>/<int:learningWayId>', methods=['PUT'])
def update_learning_way(studentId,moduleId,learningWayId):
    updated_learning_way = request.get_json()
    id = str(studentId) + "-" + str(learningWayId)
    new_learning_way = learning_way[id]
    new_learning_way['module'] = updated_learning_way['module']
    new_learning_way['moduleId'] = updated_learning_way['moduleId']
    new_learning_way['elements'] = updated_learning_way['elements']
    new_learning_way['recommendedElement'] = updated_learning_way['recommendedElement']
    return jsonify(new_learning_way),200

@app.route('/learningWay/<int:studentId>/<int:moduleId>/<int:learningWayId>')
def get_learning_way_for_student(studentId,moduleId,learningWayId):
    id = str(studentId) + "-" + str(learningWayId)
    return jsonify(learning_way[id])

@app.route('/modules')
def get_all_modules():
    return jsonify(module), 200

@app.route('/modules', methods=['POST'])
def create_module():
    params = request.get_json()
    new_module = {}
    new_module['id'] = len(module['modules'])+1
    new_module['name'] = params['name']
    new_module['module'] = params['module']
    new_module['semester'] = params['semester']
    module['modules'].append(new_module)
    return jsonify(new_module), 201

@app.route('/modules/<int:moduleId>')
def get_module_by_id(moduleId):
    for element in module['modules']:
        if element['id'] == moduleId:
            return jsonify(element), 200

@app.route('/modules/<int:moduleId>', methods=['PUT'])
def update_module(moduleId):
    params = request.get_json()
    for element in module['modules']:
        if element['id'] == moduleId:
            element['name'] = params['name']
            element['module'] = params['module']
            element['semester'] = params['semester']
            return jsonify(element), 200

if __name__ == '__main__':
    app.run(debug=True)