from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activity data before and after each test."""
    baseline = deepcopy(app_module.activities)

    yield

    app_module.activities.clear()
    app_module.activities.update(deepcopy(baseline))


@pytest.fixture
def client():
    return TestClient(app_module.app)
