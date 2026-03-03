def test_root_redirects_to_index(client):
    # Arrange
    # client is configured with follow_redirects=False so we can inspect the redirect

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code in (301, 302, 307, 308)
    assert response.headers["location"].endswith("/static/index.html")
