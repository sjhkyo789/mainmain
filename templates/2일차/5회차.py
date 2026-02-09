from flask import Flask, request, jsonify

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

todos = {
      1: "공부하기",
      2: "자기"
 }


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

# READ: 특정 항목 조회
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    task = todos.get(todo_id)
    if not task:


# CREATE: 새로운 항목 조회
@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    new_id = max(todos.keys()) + 1 if todos else 1
    todos[new_id] = data.get("task")
    return jsonify({new_id: todos[new_id]}), 201

# UPDATE: 특정 항목 수정
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.get_json()
    New_id = max(todos.keys()) + 1 if todos else 1
    todos[New_id] = data.get("task")
    return jsonify({New_id: todos[New_id]}), 201

# DELETE: 특정 항목 삭제
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    if todo_id not in todos:
        return jsonify({"error": "해당 할 일이 없습니다"}), 404
    deleted = todos.pop(todo_id)
    return jsonify({"deleted": deleted})



        return jsonify({"error": "해당 할 일이 없습니다"}), 404
    return jsonify({todo_id: task})