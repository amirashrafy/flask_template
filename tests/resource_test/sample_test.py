import pytest
from tests.required_functions import *


# region Sample Test
@pytest.mark.parametrize(
    ('status'),
    [
        (200),  # 0
    ])
def test_sample(app, client, status,):
    reset_db(app)
    res = client.get("/api/v1/sample", json={})
    assert res.status_code == status
# endregion
