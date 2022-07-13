import re
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from pytest import param
from database.db_connector import DbConnector
from models.data.element import Element
from models.data.learning_way import LearningWay
from models.data.learning_way_element import LearningWayElement
from models.data.module import Module
from models.data.learing_path import LearningPath
from models.data.element_meta import ElementMeta
from models.data.student import Student
from models.data.student_module import StudentModule

app = Flask(__name__)
CORS(app, supports_credentials=True)

#Elements
@app.route('/elements')
@cross_origin(supports_credentials=True)
def get_elements():
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    elements = {}
    elements_new = []
    for result in cursor.execute('SELECT * FROM element').fetchall():
        element = Element(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9], result[10], result[11])
        elements_new.append(element.__dict__)
    cursor.close()
    elements['elements'] = elements_new
    response = jsonify(elements)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/elements', methods=['POST'])
@cross_origin(supports_credentials=True)
def create_element():
    params = request.get_json()
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    cursor.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (params['name'].strip(), '0', params['date'], params['topic'].strip(), 0, params['semester'], params['style'].strip(), params['type'].strip(), 'Lorem Ipsum', 'Lorem Ipsum','content')
            )
    cursor.commit()
    id = cursor.execute("SELECT MAX(id) FROM element").fetchone()[0]
    result = cursor.execute('SELECT * FROM element WHERE ID=%d' %id).fetchall()
    element = Element(result[0][0],result[0][1],result[0][2],result[0][3],result[0][4],result[0][5],result[0][6],result[0][7],result[0][8],result[0][9], result[0][10], result[0][11])
    cursor.close()
    return jsonify(element.__dict__), 201

@app.route('/elements/<int:id>')
@cross_origin(supports_credentials=True)
def get_element_by_id(id):
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    result = cursor.execute('SELECT * FROM element WHERE ID=%d' %id).fetchall()
    element = Element(result[0][0],result[0][1],result[0][2],result[0][3],result[0][4],result[0][5],result[0][6],result[0][7],result[0][8],result[0][9], result[0][10], result[0][11])
    cursor.close()
    return jsonify(element.__dict__)

@app.route('/elements/<int:id>', methods=['PUT'])
@cross_origin(supports_credentials=True)
def update_element(id):
    params = request.get_json()
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    cursor.execute("UPDATE element SET name=? WHERE id=?",(params['name'], params['id']))
    cursor.commit()
    result = cursor.execute('SELECT * FROM element WHERE ID=%d' %id).fetchall()
    element = Element(result[0][0],result[0][1],result[0][2],result[0][3],result[0][4],result[0][5],result[0][6],result[0][7],result[0][8],result[0][9], result[0][10], result[0][11])
    cursor.close()
    return jsonify(element.__dict__)

#Students
@app.route('/student')
@cross_origin(supports_credentials=True)
def get_students():
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    students = {}
    students_new = []
    for result in cursor.execute('SELECT * FROM student').fetchall():
        modules_new = []
        for result_module in cursor.execute('SELECT * FROM studentModule WHERE studentId=?', (str(result[0]))).fetchall():
            module = StudentModule(result_module[0],result_module[1],result_module[2])
            modules_new.append(module.__dict__)
        student = Student(result[0],result[1],result[2],result[3],result[4], modules_new)
        students_new.append(student.__dict__)
    cursor.close()
    students['students'] = students_new
    return jsonify(students)

@app.route('/student', methods=['POST'])
@cross_origin(supports_credentials=True)
def create_student():
    params = request.get_json()
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    cursor.execute("INSERT INTO student (name, semester, style, courseOfStudy) VALUES (?, ?, ?, ?)",
            (params['name'].strip(), params['semester'], "", params['courseOfStudy'].strip())
            )
    cursor.commit()
    id = cursor.execute("SELECT MAX(id) FROM student").fetchone()[0]
    result = cursor.execute('SELECT * FROM student WHERE ID=%d' %id).fetchall()
    student = Student(result[0][0],result[0][1],result[0][2],result[0][3],result[0][4],[])
    cursor.close()
    return jsonify(student.__dict__), 201

@app.route('/student/<int:studentId>')
@cross_origin(supports_credentials=True)
def get_student_by_id(studentId):
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    result = cursor.execute('SELECT * FROM student WHERE id=?', str(studentId)).fetchall()
    modules_new = []
    for result_module in cursor.execute('SELECT * FROM studentModule WHERE studentId=?', (str(studentId))).fetchall():
        module = StudentModule(result_module[0],result_module[1],result_module[2])
        modules_new.append(module.__dict__)
    cursor.close()
    student = Student(result[0][0],result[0][1],result[0][2],result[0][3],result[0][4], modules_new)
    return jsonify(student.__dict__)

@app.route('/student/<int:studentId>', methods=['PUT'])
@cross_origin(supports_credentials=True)
def update_student(studentId):
    params = request.get_json()
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    cursor.execute("UPDATE student SET name=?, semester=?, courseOfStudy=?, style=? WHERE id=?",(params['name'], params['semester'], params['courseOfStudy'], params['style'], str(studentId)))
    cursor.execute("DELETE FROM studentModule WHERE studentId=?", (str(studentId)))
    for module in params['modules']:
        cursor.execute("INSERT INTO studentModule (studentId, moduleId) VALUES (?, ?)", (str(studentId), module['id']))
    result = cursor.execute('SELECT * FROM student WHERE id=?', str(studentId)).fetchall()
    modules_new = []
    for result_module in cursor.execute('SELECT * FROM studentModule WHERE studentId=?', (str(studentId))).fetchall():
        module = StudentModule(result_module[0],result_module[1],result_module[2])
        modules_new.append(module.__dict__)
    student = Student(result[0][0],result[0][1],result[0][2],result[0][3],result[0][4], modules_new)
    cursor.commit()
    cursor.close()
    return jsonify(student.__dict__)

#Learning Paths
@app.route('/learningPath/<int:pathId>/<int:moduleId>')
@cross_origin(supports_credentials=True)
def get_learning_path_for_student(pathId,moduleId):
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    result = cursor.execute('SELECT * FROM learningPath WHERE id=%d AND moduleId=%d' %(pathId, moduleId)).fetchall()
    elements_new = []
    for result_element in cursor.execute('SELECT * FROM elementMetaPath WHERE learningPath=%d' %(pathId)):
        element = ElementMeta(result_element[0],result_element[1],result_element[2],result_element[3])
        elements_new.append(element.__dict__)
    if not result:
        return jsonify({'message': 'Id not found', 'code': 404}), 404
    learning_path = LearningPath(result[0][0],result[0][1],result[0][2], elements_new)
    cursor.close()
    return jsonify(learning_path.__dict__)

@app.route('/learningPath', methods=['POST'])
@cross_origin(supports_credentials=True)
def create_learning_Path():
    params = request.get_json()
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    cursor.execute("INSERT INTO learningPath (moduleId, module) VALUES (?, ?)",
            (params['moduleId'], params['module'].strip())
            )
    cursor.commit()
    id = cursor.execute("SELECT MAX(id) FROM learningPath").fetchone()[0]
    for element in params['elements']:
        cursor.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)", (element['elementId'],id, element['position']))
    cursor.commit()
    result = cursor.execute("SELECT * FROM learningPath WHERE id=%d" %id).fetchall()
    elements_new = []
    for result_element in cursor.execute("SELECT * FROM elementMetaPath WHERE learningPath=%d" %id):
        element = ElementMeta(result_element[0],result_element[1],result_element[2],result_element[3])
        elements_new.append(element.__dict__)
    if not result:
        return jsonify({'message': 'Id not found', 'code': 404}), 404
    learning_path = LearningPath(result[0][0],result[0][1],result[0][2], elements_new)
    cursor.close()
    return jsonify(learning_path.__dict__),201

@app.route('/learningPath/<int:pathId>/<int:moduleId>', methods=['PUT'])
@cross_origin(supports_credentials=True)
def update_learning_path(pathId,moduleId):
    params = request.get_json()
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    cursor.execute("UPDATE learningPath SET moduleId=?, module=? WHERE id=?", (params['moduleId'],params['module'],pathId))
    cursor.execute("DELETE FROM elementMetaPath WHERE learningPath=?", (str(pathId)))
    for element in params['elements']:
        cursor.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)", (element['elementId'], pathId, element['position']))
    cursor.commit()
    result = cursor.execute("SELECT * FROM learningPath WHERE id=?", str(pathId)).fetchall()
    elements_new = []
    for result_element in cursor.execute("SELECT * FROM elementMetaPath WHERE learningPath=?", str(pathId)):
        element = ElementMeta(result_element[0],result_element[1],result_element[2],result_element[3])
        elements_new.append(element.__dict__)
    if not result:
        return jsonify({'message': 'Id not found', 'code': 404}), 404
    learning_path = LearningPath(result[0][0],result[0][1],result[0][2], elements_new)
    cursor.close()
    return jsonify(learning_path.__dict__),200

#Learning Ways
@app.route('/learningWay/<int:studentId>/<int:moduleId>', methods=['POST'])
@cross_origin(supports_credentials=True)
def create_learning_way(studentId, moduleId):
    params = request.get_json()
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    cursor.execute("INSERT INTO learningWay (module, moduleId, studentId) VALUES (?, ?, ?)",
            (params['module'].strip(), moduleId, studentId)
            )
    cursor.commit()
    id = cursor.execute("SELECT MAX(id) FROM learningWay").fetchone()[0]
    for element in params['elements']:
        cursor.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)", (element['elementId'],element['done'], element['doneAt'] if "doneAt" in element else None, element['evaluation'] if "evaluation" in element else None, element['position'], id))
    cursor.commit()
    result = cursor.execute("SELECT * FROM learningWay WHERE id=?", str(id)).fetchall()
    elements_new = []
    for result_element in cursor.execute("SELECT * FROM learningWayElement WHERE learningWayId=?", str(id)):
        element = LearningWayElement(result_element[0],result_element[1],result_element[2],result_element[3],result_element[4], result_element[5],result_element[5])
        elements_new.append(element.__dict__)
    learning_way = LearningWay(result[0][0],result[0][1],result[0][2],result[0][3],result[0][4], elements_new)
    cursor.close()
    return jsonify(learning_way.__dict__),201

@app.route('/learningWay/<int:studentId>/<int:moduleId>/<int:learningWayId>', methods=['PUT'])
@cross_origin(supports_credentials=True)
def update_learning_way(studentId,moduleId,learningWayId):
    params = request.get_json()
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    cursor.execute("UPDATE learningWay SET moduleId=?, module=?, studentId=?, recommendedElement=? WHERE id=?", (moduleId, params['module'], studentId, params['recommendedElement'] if "recommendedElement" in params else None, learningWayId))
    cursor.execute("DELETE FROM learningWayElement WHERE learningWayId=?", (str(learningWayId)))
    for element in params['elements']:
        cursor.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)", (element['elementId'],element['done'], element['doneAt'] if "doneAt" in element else None, element['evaluation'] if "evaluation" in element else None, element['position'], learningWayId))
    cursor.commit()
    result = cursor.execute("SELECT * FROM learningWay WHERE id=?", str(learningWayId)).fetchall()
    elements_new = []
    for result_element in cursor.execute("SELECT * FROM learningWayElement WHERE learningWayId=?", str(learningWayId)):
        element = LearningWayElement(result_element[0],result_element[1],result_element[2],result_element[3],result_element[4], result_element[5],result_element[5])
        elements_new.append(element.__dict__)
    learning_way = LearningWay(result[0][0],result[0][1],result[0][2],result[0][3],result[0][4], elements_new)
    cursor.close()
    return jsonify(learning_way.__dict__),200

@app.route('/learningWay/<int:studentId>/<int:moduleId>/<int:learningWayId>')
@cross_origin(supports_credentials=True)
def get_learning_way_for_student(studentId,moduleId,learningWayId):
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    result = cursor.execute('SELECT * FROM learningWay WHERE studentId=? AND moduleId=? AND id=?', (str(studentId), str(moduleId), str(learningWayId))).fetchall()
    if not result:
        return jsonify({'message': 'Id not found', 'code': 404}), 404
    elements_new = []
    for result_element in cursor.execute('SELECT * FROM learningWayElement WHERE learningWayId=?', str(learningWayId)):
        element = LearningWayElement(result_element[0],result_element[1],result_element[2],result_element[3],result_element[4],result_element[5], result_element[6])
        elements_new.append(element.__dict__)
    learning_way = LearningWay(result[0][0],result[0][1],result[0][2],result[0][3],result[0][4], elements_new)
    cursor.close()
    return jsonify(learning_way.__dict__)

#Modules
@app.route('/modules')
@cross_origin(supports_credentials=True)
def get_all_modules():
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    modules = {}
    module_new = []
    for result in cursor.execute('SELECT * FROM module').fetchall():
        module = Module(result[0],result[1],result[2],result[3])
        module_new.append(module.__dict__)
    cursor.close()
    modules['modules'] = module_new
    return jsonify(modules)

@app.route('/modules', methods=['POST'])
@cross_origin(supports_credentials=True)
def create_module():
    params = request.get_json()
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    cursor.execute("INSERT INTO module (name, module, semester) VALUES (?, ?, ?)",
            (params['name'].strip(), params['module'], params['semester'])
            )
    cursor.commit()
    id = cursor.execute("SELECT MAX(id) FROM module").fetchone()[0]
    result = cursor.execute('SELECT * FROM module WHERE id=%d' %id).fetchall()
    module = Module(result[0][0],result[0][1],result[0][2],result[0][3])
    cursor.close()
    return jsonify(module.__dict__), 201

@app.route('/modules/<int:moduleId>')
@cross_origin(supports_credentials=True)
def get_module_by_id(moduleId):
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    result = cursor.execute('SELECT * FROM module WHERE ID=%d' %moduleId).fetchall()
    if not result:
        return jsonify({'message': 'Id not found', 'code': 404}), 404
    module = Module(result[0][0],result[0][1],result[0][2],result[0][3])
    cursor.close()
    return jsonify(module.__dict__)

@app.route('/modules/<int:moduleId>', methods=['PUT'])
@cross_origin(supports_credentials=True)
def update_module(moduleId):
    params = request.get_json()
    conn = DbConnector('database/database.db')
    cursor = conn.get_db_connection()
    cursor.execute("UPDATE module SET name=?, module=?, semester=? WHERE id=?",(params['name'], params['module'], params['semester'], moduleId))
    cursor.commit()
    result = cursor.execute('SELECT * FROM module WHERE ID=%d' %moduleId).fetchall()
    module = Module(result[0][0],result[0][1],result[0][2],result[0][3])
    cursor.close()
    return jsonify(module.__dict__)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')