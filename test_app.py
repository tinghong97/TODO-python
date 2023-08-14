import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_todo_item(client):
    response = client.post('/add', json={'task': 'Add TODO'})
    assert response.status_code == 201

def test_list_todo_items(client):
    response = client.get('/list')
    assert response.status_code == 200
    assert 'todo_list' in response.json

# Add more test cases for other API endpoints

if __name__ == '__main__':
    pytest.main()
