from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
tasks = [

     
]

class Task:
    def __init__(self, task_id, name, description, date, time, status):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.date = date
        self.time = time
        self.status = status

sample_task_1 = Task(1, "Buy groceries", "Buy milk and eggs", "2023-08-20", "10:00 AM", "Incomplete")
tasks.append(sample_task_1)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify([task.__dict__ for task in tasks])

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task.task_id == task_id), None)
    if task:
        return jsonify(task.__dict__)
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task_id = len(tasks) + 1
    task = Task(task_id, data['name'], data['description'], data['date'], data['time'], data['status'])
    tasks.append(task)
    return jsonify({'message': 'Task created successfully', 'task_id': task_id}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task.task_id == task_id), None)
    if task:
        data = request.json
        task.name = data['name']
        task.description = data['description']
        task.date = data['date']
        task.time = data['time']
        task.status = data['status']
        return jsonify({'message': 'Task updated successfully'})
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.task_id != task_id]
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
