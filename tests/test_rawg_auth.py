import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_missing_api_key_returns_401(api_context):
    response = api_context.get("/api/games")

    # RAWG hides endpoints without API key
    assert response.status == 401
