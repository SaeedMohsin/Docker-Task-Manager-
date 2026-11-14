from flask import Flask, request, jsonify
from psycopg.rows import dict_row

from app.database import get_connection, init_db

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Docker Task Manager API",
        "status": "running",
        "database": "PostgreSQL"
    })


@app.route("/health")
def health():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")

        return jsonify({
            "status": "healthy",
            "database": "connected"
        })

    except Exception:
        return jsonify({
            "status": "unhealthy",
            "database": "disconnected"
        }), 503


@app.route("/api/tasks", methods=["GET", "POST"])
def manage_tasks():

    if request.method == "GET":
        with get_connection() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute(
                    "SELECT id, title, completed FROM tasks ORDER BY id"
                )
                tasks = cur.fetchall()

        return jsonify(tasks)

    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"error": "Task title is required"}), 400

    with get_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                """
                INSERT INTO tasks (title)
                VALUES (%s)
                RETURNING id, title, completed
                """,
                (data["title"],)
            )
            task = cur.fetchone()

    return jsonify(task), 201


@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid request"}), 400

    with get_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                "SELECT id, title, completed FROM tasks WHERE id = %s",
                (task_id,)
            )

            task = cur.fetchone()

            if task is None:
                return jsonify({"error": "Task not found"}), 404

            new_title = data.get("title", task["title"])
            new_completed = data.get("completed", task["completed"])

            cur.execute(
                """
                UPDATE tasks
                SET title = %s, completed = %s
                WHERE id = %s
                RETURNING id, title, completed
                """,
                (new_title, new_completed, task_id)
            )

            updated_task = cur.fetchone()

    return jsonify(updated_task)


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM tasks WHERE id = %s",
                (task_id,)
            )

            if cur.rowcount == 0:
                return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task deleted successfully"})


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
