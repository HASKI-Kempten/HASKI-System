import sys
sys.path.append('../')
from controller import app
import pytest

def test_get_all_elements():
    with app.test_client() as c:
        rv = c.get('/elements')
        res = rv.get_json()['elements']
        assert type(res[0]) is dict
        assert res[0]['name'] == 'My test element'
        assert rv.status_code == 200

def test_create_element():
    with app.test_client() as c:
        rv = c.post('/elements', json={"name": "My test Element 2","date": "2022-06-17T12:16:41.226Z","topic": "Informatik I","semester": 1,"style": "visual"})
        res = rv.get_json()
        assert type(res) is dict
        assert res['name'] == 'My test Element 2'
        assert res['id'] != 0
        assert res['difficulty'] == 'Easy'
        assert rv.status_code == 201

def test_update_element():
    with app.test_client() as c:
        rv = c.put('/elements/2', json={'difficulty': "Medium"})
        res = rv.get_json()
        assert res['name'] == 'My test Element 2'
        assert res['id'] == 2
        assert res['difficulty'] == 'Medium'
        assert rv.status_code == 200

def test_get_element_by_id():
    with app.test_client() as c:
        rv = c.get('/elements/2')
        res = rv.get_json()
        assert type(res) is dict
        assert res['name'] == 'My test Element 2'
        assert rv.status_code == 200