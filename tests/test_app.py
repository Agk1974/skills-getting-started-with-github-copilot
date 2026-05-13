from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

client = TestClient(app)
BASE_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    yield
    activities.clear()
    activities.update(deepcopy(BASE_ACTIVITIES))


def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200

    data = response.json()
    assert "Chess Club" in data
    assert data["Chess Club"]["description"] == "Learn strategies and compete in chess tournaments"


def test_signup_for_activity():
    response = client.post("/activities/Chess Club/signup?email=test@mergington.edu")
    assert response.status_code == 200
    assert response.json()["message"] == "Signed up test@mergington.edu for Chess Club"
    assert "test@mergington.edu" in activities["Chess Club"]["participants"]


def test_signup_duplicate_returns_400():
    response = client.post("/activities/Chess Club/signup?email=michael@mergington.edu")
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up"


def test_remove_participant():
    response = client.delete("/activities/Chess Club/participants?email=michael@mergington.edu")
    assert response.status_code == 200
    assert response.json()["message"] == "Removed michael@mergington.edu from Chess Club"
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]


def test_remove_missing_participant_returns_404():
    response = client.delete("/activities/Chess Club/participants?email=missing@mergington.edu")
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
