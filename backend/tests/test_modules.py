import sys
sys.path.append('../')
from controller import app
import pytest

def test_get_all_modules():
    with app.test_client() as c:
        rv = c.get('/modules')
        assert rv.status_code == 200
        res = rv.get_json()
        assert 'modules' in res
        assert len(res['modules']) > 0
        res_mod = res['modules']
        assert 'id' in res_mod[0]
        assert type(res_mod[0]['id']) == int
        assert 'name' in res_mod[0]
        assert type(res_mod[0]['name']) == str
        assert 'module' in res_mod[0]
        assert type(res_mod[0]['module']) == str
        assert 'semester' in res_mod[0]
        assert type(res_mod[0]['semester']) == int

def test_create_module():
    with app.test_client() as c:
        rv = c.post('/modules', json={'name': 'Einführung in die Programmierung', 'module': 'IT-1234', 'semester': 1})
        assert rv.status_code == 201
        res = rv.get_json()
        assert type(res) is dict
        assert 'id' in res
        assert type(res['id']) == int
        assert res['id'] != 0
        assert 'name' in res
        assert type(res['name']) == str
        assert 'module' in res
        assert type(res['module']) == str
        assert 'semester' in res
        assert type(res['semester']) == int

def test_update_module():
    with app.test_client() as c:
        rv = c.put('/modules/1', json={'name': 'Einführung in die Programmierung II', 'module': 'IT-9876', 'semester': 2})
        assert rv.status_code == 200
        res = rv.get_json()
        assert type(res) is dict
        assert 'id' in res
        assert type(res['id']) == int
        assert res['id'] == 1
        assert 'name' in res
        assert type(res['name']) == str
        assert res['name'] == "Einführung in die Programmierung II"
        assert 'module' in res
        assert type(res['module']) == str
        assert res['module'] == 'IT-9876'
        assert 'semester' in res
        assert type(res['semester']) == int
        assert res['semester'] == 2
        
def test_get_module_by_id():
    with app.test_client() as c:
        rv = c.get('/modules/1')
        assert rv.status_code == 200
        res = rv.get_json()
        assert type(res) is dict
        assert 'id' in res
        assert type(res['id']) == int
        assert res['id'] == 1
        assert 'name' in res
        assert type(res['name']) == str
        assert 'module' in res
        assert type(res['module']) == str
        assert 'semester' in res
        assert type(res['semester']) == int