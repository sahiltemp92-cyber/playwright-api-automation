import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def api_context():
    """
    Shared Playwright API context for all tests.
    """
    with sync_playwright() as p:
        context = p.request.new_context(
            base_url="https://api.rawg.io/api",
            extra_http_headers={
                "Accept": "application/json"
            }
        )
        yield context
        context.dispose()