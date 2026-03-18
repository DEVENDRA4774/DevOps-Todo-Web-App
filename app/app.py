from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Simple in-memory todo list
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append(todo)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for('index'))

@app.route('/metrics')
def metrics():
    # Placeholder for Prometheus metrics
    return "todo_app_count " + str(len(todos))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
