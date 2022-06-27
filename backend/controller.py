from flask import Flask, jsonify, request
import json
import random

app = Flask(__name__)

elements = {"elements": [
    { "id": 1, "name": "My first", "position": 2, "difficulty": "Easy", "progress": 2, "date": "2022-06-13T16:05:54.908Z", "topic": "Informatik I", "semester": 2, "style": "visual", "proLIST": "Lorem Ipsum", "contraLIST": "Lorem Ipsum", "duration": 1.5 },
    { "id": 2, "name": "My second element", "position": 3, "difficulty": "Easy", "progress": 2, "date": "2022-06-13T16:05:54.908Z", "topic": "Informatik I", "semester": 2, "style": "visual", "proLIST": "Lorem Ipsum", "contraLIST": "Lorem Ipsum", "duration": 1.5 },
    { "id": 3, "name": "My last element", "position": 4, "difficulty": "Easy", "progress": 2, "date": "2022-06-13T16:05:54.908Z", "topic": "Informatik I", "semester": 2, "style": "visual", "proLIST": "Lorem Ipsum", "contraLIST": "Lorem Ipsum", "duration": 1.5 }
    ]}

learning_path = {"elements": []}

modul =  '{ "id": 1, "name": "Einführung in die Programmierung", "modul": "IT-1234", "semester": 1,"level": "beginner"}'

students = {"students": [{"id": 1, "name": "Max Musterfrau", "semester": 2, "style": "Active, Verbal, Intuitive, Global", "courseOfStudy": "Angewandte Informatik", "modules": [{"id": 1, "name": "Einführung in die Programmierung", "modul": "IT-1234", "semester": 1, "level": "beginner"}]}]}

@app.route('/elements')
def get_elements():
    return jsonify(elements)

@app.route('/elements', methods=['POST'])
def upload_element():
    uploaded_element = request.get_json()
    new_element = {
        'id': len(elements['elements'])+1,
        'name': uploaded_element['name'].strip(),
        'position': None,
        'difficulty': 'Easy',
        'progress': 0,
        'date': uploaded_element['date'].strip(),
        'topic': uploaded_element['topic'].strip(),
        'semester': uploaded_element['semester'],
        'style': uploaded_element['style'].strip(),
        'proLIST': '',
        'contraList': '',
        'duration': 0
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
    name, semester, courseOfStudy = created_student['name'].strip(),created_student['semester'].strip(),created_student['courseOfStudy'].strip()
    new_student = {
        'id': len(students['students'])+1,
        'name': name,
        'semester': semester,
        'style': '',
        'courseOfStudy': courseOfStudy,
        'modules': [
            {}
        ]
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

@app.route('/learningPath/<int:studentId>')
def get_learning_path_for_student(studentId):
    return jsonify(learning_path)

@app.route('/learningPath', methods=['POST'])
def create_learning_Path():
    created_learning_path = request.get_json()
    for i in range(len(created_learning_path['elements'])):
        new_learning_path = {
            'id': len(learning_path['elements'])+1,
            'name': created_learning_path['elements'][i]['name'].strip(),
            'position': created_learning_path['elements'][i]['position'],
            'difficulty': created_learning_path['elements'][i]['difficulty'].strip(),
            'progress': created_learning_path['elements'][i]['progress'],
            'date': created_learning_path['elements'][i]['date'].strip(),
            'topic': created_learning_path['elements'][i]['topic'].strip(),
            'semester': created_learning_path['elements'][i]['semester'],
            'style': created_learning_path['elements'][i]['style'].strip(),
            'proLIST': created_learning_path['elements'][i]['proLIST'].strip(),
            'contraList': created_learning_path['elements'][i]['contraLIST'].strip(),
            'duration': created_learning_path['elements'][i]['duration']
        }
        learning_path['elements'].append(new_learning_path)
    return jsonify(learning_path), 201

@app.route('/learningPath/<int:studentId>', methods=['PUT'])
def update_learning_path(studentId):
    print(learning_path)
    print(len(learning_path['elements']))
    for i in range(len(learning_path['elements'])):
        del learning_path['elements'][0]
    print(learning_path)
    created_learning_path = request.get_json()
    for i in range(len(created_learning_path['elements'])):
        new_learning_path = {
            'id': created_learning_path['elements'][i]['id'],
            'name': created_learning_path['elements'][i]['name'].strip(),
            'position': created_learning_path['elements'][i]['position'],
            'difficulty': created_learning_path['elements'][i]['difficulty'].strip(),
            'progress': created_learning_path['elements'][i]['progress'],
            'date': created_learning_path['elements'][i]['date'].strip(),
            'topic': created_learning_path['elements'][i]['topic'].strip(),
            'semester': created_learning_path['elements'][i]['semester'],
            'style': created_learning_path['elements'][i]['style'].strip(),
            'proLIST': created_learning_path['elements'][i]['proLIST'].strip(),
            'contraList': created_learning_path['elements'][i]['contraLIST'].strip(),
            'duration': created_learning_path['elements'][i]['duration']
        }
        learning_path['elements'].append(new_learning_path)
    return jsonify(learning_path)

if __name__ == '__main__':
    app.run(debug=True)