from app.app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_health_route_exists():
    assert "/health" in [
        rule.rule for rule in app.url_map.iter_rules()
    ]


def test_empty_task_title():
    client = app.test_client()

    response = client.post(
        "/api/tasks",
        json={}
    )

    assert response.status_code == 400
    assert response.json["error"] == "Task title is required"

