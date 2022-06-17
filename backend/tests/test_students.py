import sys
sys.path.append('../')
from controller import app
import pytest

def test_get_all_students():
    with app.test_client() as c:
        rv = c.get('/student')
        res = rv.get_json()['students']
        assert type(res[0]) is dict
        assert res[0]['name'] == 'Max Musterfrau'
        assert rv.status_code == 200

def test_create_students():
    with app.test_client() as c:
        rv = c.post('/student', json={"name": "Eva Mustermann", "semester": "1", "courseOfStudy": "Mechatronik"})
        res = rv.get_json()
        assert type(res) is dict
        assert res['name'] == 'Eva Mustermann'
        assert res['id'] == 2
        assert res['modules'] == [{}]
        assert rv.status_code == 201

def test_update_student():
    with app.test_client() as c:
        rv = c.put('/student/2', json={"name": "Maria Mustermann", "modules": [{"id": 1, "level": "beginner", "modul": "IT-1234", "name": "Einführung in die Programmierung", "semester": 1}]})
        res = rv.get_json()
        assert type(res) is dict
        assert res['name'] == 'Maria Mustermann'
        assert res['modules'] != []
        assert rv.status_code == 200

def test_get_student_by_id():
    with app.test_client() as c:
        rv = c.get('/student/2')
        res = rv.get_json()
        assert type(res) is dict
        assert res['name'] == 'Maria Mustermann'
        assert rv.status_code == 200