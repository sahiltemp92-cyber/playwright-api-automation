import os
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_get_games_list(api_context):
    response = api_context.get(
        "/api/games",
        params={
            "key": os.getenv("RAWG_API_KEY")
        }
    )

    assert response.status == 200

    body = response.json()

    assert "results" in body
    assert isinstance(body["results"], list)
    assert len(body["results"]) > 0

    game = body["results"][0]

    assert "id" in game
    assert "name" in game