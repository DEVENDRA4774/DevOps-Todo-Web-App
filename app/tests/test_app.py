import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Todo List' in rv.data

def test_add_todo(client):
    rv = client.post('/add', data=dict(todo='Test Task'), follow_redirects=True)
    assert rv.status_code == 200
    assert b'Test Task' in rv.data

def test_delete_todo(client):
    client.post('/add', data=dict(todo='Task to Delete'), follow_redirects=True)
    rv = client.get('/delete/0', follow_redirects=True)
    assert rv.status_code == 200
    assert b'Task to Delete' not in rv.data
