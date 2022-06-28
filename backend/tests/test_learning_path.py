import sys
sys.path.append('../')
from controller import app
import pytest

def test_create_learning_path():
    with app.test_client() as c:
        rv = c.post('/learningPath', json={ "moduleId": 987, "module": "Informatik I", "elements": [{ "elementId": 1, "position": "1.1"},{"elementId": 2, "position": "1.2"}]})
        assert rv.status_code == 201
        res = rv.get_json()
        assert type(res) is dict
        assert 'id' in res
        assert type(res['id']) == str
        assert res['id'] != "0-0"
        assert 'moduleId' in res
        assert type(res['moduleId']) == int
        assert 'module' in res
        assert type(res['module']) == str
        assert 'elements' in res
        assert type(res['elements'][0]) is dict
        assert len(res['elements']) > 0
        assert 'elementId' in res['elements'][0]
        assert type(res['elements'][0]['elementId']) == int
        assert 'position' in res['elements'][0] 
        assert type(res['elements'][0]['position']) == str

def test_update_learning_path():
    with app.test_client() as c:
        rv = c.put('/learningPath/1/1', json={"moduleId": 1, "module": "Informatik I", "elements": [
            {"elementId": 1234, "position": "1.1"},
            {"elementId": 2, "position": "1.2"}
        ]})
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
        assert 'elements' in res
        assert type(res['elements'][0]) is dict
        assert len(res['elements']) > 0
        assert 'elementId' in res['elements'][0]
        assert type(res['elements'][0]['elementId']) == int
        assert res['elements'][0]['elementId'] == 1234
        assert 'position' in res['elements'][0] 
        assert type(res['elements'][0]['position']) == str
        res['elements'][0]['position'] == '1.1'
        
def test_get_learning_path_by_id():
    with app.test_client() as c:
        rv = c.get('/learningPath/1/1')
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
        assert 'elements' in res
        assert type(res['elements'][0]) is dict
        assert len(res['elements']) > 0
        assert 'elementId' in res['elements'][0]
        assert type(res['elements'][0]['elementId']) == int
        assert 'position' in res['elements'][0] 
        assert type(res['elements'][0]['position']) == str