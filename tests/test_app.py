from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_endpoint():
    email = "unregister-test@mergington.edu"

    signup_response = client.post(f"/activities/Chess Club/signup?email={email}")
    assert signup_response.status_code == 200

    delete_response = client.delete(f"/activities/Chess Club/unregister?email={email}")
    assert delete_response.status_code == 200

    payload = delete_response.json()
    assert payload["message"] == f"Unregistered {email} from Chess Club"

    activities = client.get("/activities").json()
    assert email not in activities["Chess Club"]["participants"]
