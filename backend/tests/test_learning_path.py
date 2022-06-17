import sys
sys.path.append('../')
from controller import app
import pytest

def test_create_learning_path():
    with app.test_client() as c:
        rv = c.post('/learningPath', json={"elements": [{ "id": 1, "name": "My test Element", "position": 1, "difficulty": "Easy", "progress": 0, "date": "2022-06-13T16:05:54.908Z", "topic": "Informatik I", "semester": 2, "style": "visual", "proLIST": "Lorem Ipsum", "contraLIST": "Lorem Ipsum", "duration": 1.5 },{ "id": 2, "name": "My test element 2", "position": 2, "difficulty": "Medium", "progress": 0, "date": "2022-06-13T16:05:54.908Z", "topic": "Informatik I", "semester": 2, "style": "verbal", "proLIST": "Lorem Ipsum", "contraLIST": "Lorem Ipsum", "duration": 3 }]})
        res = rv.get_json()['elements']
        assert type(res[0]) is dict
        assert len(res) > 0
        assert res[0]['name'] == 'My test Element'
        assert res[0]['id'] != 0
        assert res[0]['difficulty'] == 'Easy'
        assert rv.status_code == 201

def test_update_learning_path():
    with app.test_client() as c:
        rv = c.put('/learningPath/1', json={"elements": [{"id": 1234,"name": "My test element","position": 2,"difficulty": "Easy","progress": 2,"date": "2022-06-17T12:34:21.063Z","topic": "Informatik I","semester": 2,"style": "visual","proLIST": "Lorem Ipsum","contraLIST": "Lorem Ipsum","duration": 1.5},{"contraLIST": "Something bad","date": "2022-06-13T16:05:54.908Z","difficulty": "Medium","duration": 3,"id": 3,"name": "My test element 3","position": 2,"proLIST": "Someting good","progress": 0,"semester": 2,"style": "text","topic": "Informatik I"}]})
        res = rv.get_json()['elements']
        assert type(res[0]) is dict
        assert len(res) > 1
        assert res[1]['name'] == 'My test element 3'
        assert res[1]['id'] == 3
        assert res[1]['difficulty'] == 'Medium'
        assert rv.status_code == 200

def test_get_element_by_id():
    with app.test_client() as c:
        rv = c.get('/learningPath/2')
        res = rv.get_json()['elements']
        assert type(res[0]) is dict
        assert len(res) > 1
        assert res[1]['name'] == 'My test element 3'
        assert res[1]['id'] == 3
        assert res[1]['difficulty'] == 'Medium'
        assert rv.status_code == 200