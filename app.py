from flask import Flask, request, jsonify,render_template,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(1000), nullable=False)
    complete = db.Column(db.Boolean) 
    user_id = db.Column(db.Integer)
    
# Routes
@app.route('/')
def index():

    todoList = Todo.query.all()
    return render_template('base.html', todo_list=todoList)

# add a task
@app.route('/add', methods=["POST"])
def add():
    


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
