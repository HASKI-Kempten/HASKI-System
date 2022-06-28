import sys
sys.path.append('../')
from controller import app
import pytest

def test_get_all_elements():
    with app.test_client() as c:
        rv = c.get('/elements')
        res = rv.get_json()['elements']
        assert rv.status_code == 200
        assert type(res[0]) is dict
        assert 'id' in res[0]
        assert type(res[0]['id']) is int
        assert 'name' in res[0]
        assert type(res[0]['name']) is str
        assert 'difficulty' in res[0]
        assert type(res[0]['difficulty']) is str
        assert 'creationDate' in res[0]
        assert type(res[0]['creationDate']) is int
        assert 'module' in res[0]
        assert type(res[0]['module']) is str
        assert 'averageDuration' in res[0]
        assert type(res[0]['averageDuration']) is int
        assert 'semester' in res[0]
        assert type(res[0]['semester']) is int
        assert 'style' in res[0]
        assert type(res[0]['style']) is str
        assert 'proLIST' in res[0]
        assert type(res[0]['proLIST']) is str
        assert 'contraLIST' in res[0]
        assert type(res[0]['contraLIST']) is str

def test_create_element():
    with app.test_client() as c:
        rv = c.post('/elements', json={"name": "My test Element 2","date": 1656330943,"topic": "Informatik I","semester": 1,"style": "visual"})
        res = rv.get_json()
        assert type(res) is dict
        assert rv.status_code == 201
        assert 'id' in res
        assert type(res['id']) is int
        assert res['id'] != 0
        assert 'name' in res
        assert type(res['name']) is str
        assert 'difficulty' in res
        assert type(res['difficulty']) is str
        assert 'creationDate' in res
        assert type(res['creationDate']) is int
        assert 'module' in res
        assert type(res['module']) is str
        assert 'averageDuration' in res
        assert type(res['averageDuration']) is int
        assert 'semester' in res
        assert type(res['semester']) is int
        assert 'style' in res
        assert type(res['style']) is str
        assert 'proLIST' in res
        assert type(res['proLIST']) is str
        assert 'contraLIST' in res
        assert type(res['contraLIST']) is str

def test_update_element():
    with app.test_client() as c:
        rv = c.put('/elements/1', json={'difficulty': "Medium"})
        res = rv.get_json()
        assert type(res) is dict
        assert rv.status_code == 200
        assert type(res) is dict
        assert 'id' in res
        assert type(res['id']) is int
        assert res['id'] == 1
        assert 'name' in res
        assert type(res['name']) is str
        assert 'difficulty' in res
        assert type(res['difficulty']) is str
        assert res['difficulty'] == 'Medium'
        assert 'creationDate' in res
        assert type(res['creationDate']) is int
        assert 'module' in res
        assert type(res['module']) is str
        assert 'averageDuration' in res
        assert type(res['averageDuration']) is int
        assert 'semester' in res
        assert type(res['semester']) is int
        assert 'style' in res
        assert type(res['style']) is str
        assert 'proLIST' in res
        assert type(res['proLIST']) is str
        assert 'contraLIST' in res
        assert type(res['contraLIST']) is str

def test_get_element_by_id():
    with app.test_client() as c:
        rv = c.get('/elements/1')
        res = rv.get_json()
        assert type(res) is dict
        assert rv.status_code == 200
        assert type(res) is dict
        assert 'id' in res
        assert type(res['id']) is int
        assert res['id'] == 1
        assert 'name' in res
        assert type(res['name']) is str
        assert 'difficulty' in res
        assert type(res['difficulty']) is str
        assert 'creationDate' in res
        assert type(res['creationDate']) is int
        assert 'module' in res
        assert type(res['module']) is str
        assert 'averageDuration' in res
        assert type(res['averageDuration']) is int
        assert 'semester' in res
        assert type(res['semester']) is int
        assert 'style' in res
        assert type(res['style']) is str
        assert 'proLIST' in res
        assert type(res['proLIST']) is str
        assert 'contraLIST' in res
        assert type(res['contraLIST']) is str
