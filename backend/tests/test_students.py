import sys
sys.path.append('../')
from controller import app
import pytest

def test_get_all_students():
    with app.test_client() as c:
        rv = c.get('/student')
        assert rv.status_code == 200
        res = rv.get_json()['students']
        assert len(res) > 0
        assert type(res[0]) is dict
        assert 'id' in res[0]
        assert type(res[0]['id']) == int
        assert 'name' in res[0]
        assert type(res[0]['name']) == str
        assert 'semester' in res[0]
        assert type(res[0]['semester']) == int
        assert 'style' in res[0]
        assert type(res[0]['style']) == str
        assert 'courseOfStudy' in res[0]
        assert type(res[0]['courseOfStudy']) == str
        assert 'modules' in res[0]
        assert 'id' in res[0]['modules'][0]
        assert type(res[0]['modules'][0]['id']) == int
        assert 'name' in res[0]['modules'][0]
        assert type(res[0]['modules'][0]['name']) == str
        assert 'module' in res[0]['modules'][0]
        assert type(res[0]['modules'][0]['module']) == str
        assert 'semester' in res[0]['modules'][0]
        assert type(res[0]['modules'][0]['semester']) == int

def test_create_student():
    with app.test_client() as c:
        rv = c.post('/student', json={"name": "Eva Mustermann", "semester": 1, "courseOfStudy": "Mechatronik"})
        assert rv.status_code == 201
        res = rv.get_json()
        assert type(res) is dict
        assert 'id' in res
        assert type(res['id']) == int
        assert res['id'] != 0
        assert 'name' in res
        assert type(res['name']) == str
        assert 'semester' in res
        assert type(res['semester']) == int
        assert 'style' in res
        assert type(res['style']) == str
        assert 'courseOfStudy' in res
        assert type(res['courseOfStudy']) == str
        assert 'modules' in res
        assert len(res['modules']) == 0

def test_update_student():
    with app.test_client() as c:
        rv = c.put('/student/1', json={"name": "Maria Mustermann", "semester": 3, "courseOfStudy": "Game Engineering", "style": "Active, Verbal, Intuitive, Global", "modules": [{"id": 1, "modul": "IT-1234", "name": "Visualisierungstechniken", "semester": 3}]})
        assert rv.status_code == 200
        res = rv.get_json()
        assert type(res) is dict
        assert 'id' in res
        assert type(res['id']) == int
        assert res['id'] == 1
        assert 'name' in res
        assert type(res['name']) == str
        assert res['name'] == 'Maria Mustermann'
        assert 'semester' in res
        assert type(res['semester']) == int
        assert res['semester'] == 3
        assert 'style' in res
        assert type(res['style']) == str
        assert res['style'] = "Active, Verbal, Intuitive, Global"
        assert 'courseOfStudy' in res
        assert type(res['courseOfStudy']) == str
        assert 'modules' in res
        assert 'id' in res['modules'][0]
        assert type(res['modules'][0]['id']) == int
        assert res['modules'][0]['id'] == 1
        assert 'name' in res['modules'][0]
        assert type(res['modules'][0]['name']) == str
        assert res['modules'][0]['name'] == "Visualisierungstechniken"
        assert 'module' in res['modules'][0]
        assert type(res['modules'][0]['module']) == str
        assert res['modules'][0]['module'] == "IT-1234"
        assert 'semester' in res['modules'][0]
        assert type(res['modules'][0]['semester']) == int
        assert res['modules'][0]['semester'] == 3

def test_get_student_by_id():
    with app.test_client() as c:
        rv = c.get('/student/1')
        assert rv.status_code == 200
        res = rv.get_json()
        assert type(res) is dict
        assert 'id' in res
        assert type(res['id']) == int
        assert res['id'] == 1
        assert 'name' in res
        assert type(res['name']) == str
        assert 'semester' in res
        assert type(res['semester']) == int
        assert 'style' in res
        assert type(res['style']) == str
        assert 'courseOfStudy' in res
        assert type(res['courseOfStudy']) == str
        assert 'modules' in res
        assert 'id' in res['modules'][0]
        assert type(res['modules'][0]['id']) == int
        assert 'name' in res['modules'][0]
        assert type(res['modules'][0]['name']) == str
        assert 'module' in res['modules'][0]
        assert type(res['modules'][0]['module']) == str
        assert 'semester' in res['modules'][0]
        assert type(res['modules'][0]['semester']) == int