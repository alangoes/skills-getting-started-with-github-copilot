def test_unregister_happy_path(client):
    # Arrange
    activity = "Chess Club"
    # michael@mergington.edu is already registered in the seed data
    email = "michael@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    body = response.json()
    assert email in body["message"]
    participants = client.get("/activities").json()[activity]["participants"]
    assert email not in participants


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    activity = "Underwater Basket Weaving"
    email = "anyone@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404


def test_unregister_not_registered_returns_400(client):
    # Arrange
    activity = "Chess Club"
    email = "notregistered@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert "not signed up" in response.json()["detail"].lower()
