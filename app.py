from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/todo', methods=['POST'])
def add_todo():
    data = request.json
    content = data['content']
    new_todo = Todo(content=content)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({"id": new_todo.id}), 201

@app.route('/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Todo deleted!"}), 200

@app.route('/todo', methods=['GET'])
def list_todos():
    todos = Todo.query.all()
    return jsonify([{"id": t.id, "content": t.content, "completed": t.completed} for t in todos])

@app.route('/todo/<int:todo_id>/complete', methods=['PUT'])
def mark_complete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.completed = True
    db.session.commit()
    return jsonify({"message": "Todo marked as complete!"}), 200

if __name__ == "__main__":
    with app.app_context():  # this ensures the code runs within the app context
        db.create_all()
    app.run(debug=True)
            return jsonify({'message': 'TODO item marked as completed'})
    return jsonify({'error': 'TODO item not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
