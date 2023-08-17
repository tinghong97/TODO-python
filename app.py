from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Initialize an empty list to store TODO items
todo_list = []

# Routes
@app.route('/add', methods=['POST'])
def add_todo():
    data = request.get_json()
    task = data.get('task')
    if task:
        todo_item = {
            'id': len(todo_list) + 1,
            'task': task,
            'completed': False
        }
        todo_list.append(todo_item)
        return jsonify({'message': 'TODO item added successfully'}), 201
    return jsonify({'error': 'Task is required'}), 400

@app.route('/delete/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todo_list
    todo_list = [item for item in todo_list if item['id'] != todo_id]
    return jsonify({'message': 'TODO item deleted successfully'})

@app.route('/list', methods=['GET'])
def list_todo():
    return jsonify({'todo_list': todo_list})

@app.route('/complete/<int:todo_id>', methods=['PUT'])
def complete_todo(todo_id):
    for item in todo_list:
        if item['id'] == todo_id:
            item['completed'] = True
            return jsonify({'message': 'TODO item marked as completed'})
    return jsonify({'error': 'TODO item not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
