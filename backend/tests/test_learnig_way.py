import sys
sys.path.append('../')
from controller import app
import pytest

def test_create_learning_way():
    with app.test_client() as c:
        rv = c.post('/learningWay/1', json={"module": "Informatik I", "moduleId": 234, "studentId": 1, "elements": [{ "elementId": 1, "done": True, "doneAt": 1656331243, "evaluation": "2.0", "position": "1.1"},{ "elementId": 2, "done": False, "doneAt": None, "evaluation": None, "position": "1.2"}]})
        assert rv.status_code == 201
        res = rv.get_json()
        assert type(res) is dict
        assert 'id' in res
        assert type(res['id']) == int
        assert res['id'] != 0
        assert 'moduleId' in res
        assert type(res['moduleId']) == int
        assert 'module' in res
        assert type(res['module']) == str
        assert 'studentId' in res
        assert type(res['studentId']) == int
        assert res['studentId'] == 1
        assert 'recommendedElement' in res
        assert type(res['recommendedElement']) == int
        assert 'elements' in res
        assert type(res['elements'][0]) is dict
        assert len(res['elements']) > 0
        assert 'elementId' in res['elements'][0]
        assert type(res['elements'][0]['elementId']) == int
        assert 'done' in res['elements'][0]
        assert type(res['elements'][0]['done']) == bool
        assert 'doneAt' in res['elements'][0]
        assert type(res['elements'][0]['doneAt']) == int
        assert 'evaluation' in res['elements'][0]
        assert type(res['elements'][0]['evaluation']) == str
        assert 'position' in res['elements'][0] 
        assert type(res['elements'][0]['position']) == str

def test_update_learning_way():
    with app.test_client() as c:
        rv = c.put('/learningWay/1/1', json={"module": "Informatik I", "moduleId": 234, "studentId": 1, "elements": [{ "elementId": 1, "done": True, "doneAt": 1656331243, "evaluation": "2.0", "position": "1.1"},{ "elementId": 2, "done": True, "doneAt": 1656332482, "evaluation": "1.7", "position": "1.2"}]})
        assert rv.status_code == 200
        res = rv.get_json()
        assert type(res) is dict
        assert 'id' in res
        assert type(res['id']) == int
        assert res['id'] == 1
        assert 'moduleId' in res
        assert type(res['moduleId']) == int
        assert 'module' in res
        assert type(res['module']) == str
        assert 'studentId' in res
        assert type(res['studentId']) == int
        assert res['studentId'] == 1
        assert 'recommendedElement' in res
        assert type(res['recommendedElement']) == int
        assert 'elements' in res
        assert type(res['elements'][1]) is dict
        assert len(res['elements']) > 1
        assert 'elementId' in res['elements'][1]
        assert type(res['elements'][1]['elementId']) == int
        assert 'done' in res['elements'][0]
        assert type(res['elements'][1]['done']) == bool
        assert res['elements'][1]['done'] == True
        assert 'doneAt' in res['elements'][0]
        assert type(res['elements'][1]['doneAt']) == int
        assert res['elements'][1]['doneAt'] == 1656332482
        assert 'evaluation' in res['elements'][0]
        assert type(res['elements'][1]['evaluation']) == str
        assert res['elements'][1]['evaluation'] == "1.7"
        assert 'position' in res['elements'][0] 
        assert type(res['elements'][1]['position']) == str
        

def test_get_learning_way_by_id():
    with app.test_client() as c:
        rv = c.get('/learningWay/1/1')
        assert rv.status_code == 200
        res = rv.get_json()
        assert type(res) is dict
        assert 'id' in res
        assert type(res['id']) == int
        assert res['id'] == 1
        assert 'moduleId' in res
        assert type(res['moduleId']) == int
        assert 'module' in res
        assert type(res['module']) == str
        assert 'studentId' in res
        assert type(res['studentId']) == int
        assert res['studentId'] == 1
        assert 'recommendedElement' in res
        assert type(res['recommendedElement']) == int
        assert 'elements' in res
        assert type(res['elements'][0]) is dict
        assert len(res['elements']) > 0
        assert 'elementId' in res['elements'][0]
        assert type(res['elements'][0]['elementId']) == int
        assert 'done' in res['elements'][0]
        assert type(res['elements'][0]['done']) == bool
        assert 'doneAt' in res['elements'][0]
        assert type(res['elements'][0]['doneAt']) == int
        assert 'evaluation' in res['elements'][0]
        assert type(res['elements'][0]['evaluation']) == str
        assert 'position' in res['elements'][0] 
        assert type(res['elements'][0]['position']) == str