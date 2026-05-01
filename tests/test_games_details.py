import os
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_get_game_details(api_context):
    game_id = 3498  # GTA V (stable ID)

    response = api_context.get(
        f"/api/games/{game_id}",
        params={
            "key": os.getenv("RAWG_API_KEY")
        }
    )

    assert response.status == 200

    body = response.json()

    assert body["id"] == game_id
    assert body["name"]
    assert "description_raw" in body
    assert "rating" in body


@pytest.mark.regression
def test_get_game_details_not_found(api_context):
    response = api_context.get(
        f"/api/games/999999999",
        params={
            "key": os.getenv("RAWG_API_KEY")
        }
    )

    assert response.status == 404
