import os
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_get_platforms_list(api_context):
    response = api_context.get(
        "/api/platforms",
        params={
            "key": os.getenv("RAWG_API_KEY")
        }
    )

    assert response.status == 200

    body = response.json()

    assert "results" in body
    assert isinstance(body["results"], list)

    platform = body["results"][0]

    assert "id" in platform
    assert "name" in platform
    assert "slug" in platform