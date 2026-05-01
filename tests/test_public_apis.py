import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_jsonplaceholder_posts(api_context):
    response = api_context.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    assert response.status == 200

    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0


@pytest.mark.smoke
@pytest.mark.regression
def test_reqres_users(api_context):
    response = api_context.get(
        "https://reqres.in/api/users?page=2"
    )

    # ReqRes may return 200 or 401 depending on throttling
    assert response.status in [200, 401]