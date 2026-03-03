REQUIRED_KEYS = {"description", "schedule", "max_participants", "participants"}


def test_get_activities_returns_200(client):
    # Arrange
    # No additional setup needed; activities are pre-loaded

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_non_empty_dict(client):
    # Arrange
    # No additional setup needed

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert isinstance(data, dict)
    assert len(data) > 0


def test_each_activity_has_required_keys(client):
    # Arrange
    # No additional setup needed

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    for name, details in data.items():
        assert REQUIRED_KEYS.issubset(details.keys()), (
            f"Activity '{name}' is missing keys: {REQUIRED_KEYS - details.keys()}"
        )


def test_activity_field_types(client):
    # Arrange
    # No additional setup needed

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    for name, details in data.items():
        assert isinstance(details["description"], str), f"'{name}' description should be a str"
        assert isinstance(details["schedule"], str), f"'{name}' schedule should be a str"
        assert isinstance(details["max_participants"], int), f"'{name}' max_participants should be an int"
        assert isinstance(details["participants"], list), f"'{name}' participants should be a list"
