# tests/test_contract.py
import pytest
from jsonschema import validate
from framework.schemas import user_data_schema



@pytest.mark.api
def test_datosuser_contract_is_valid(logged_in_client):
    res = logged_in_client.datos_user()
    assert res.status_code == 200, f"{res.status_code} — {res.text}"
    validate(instance=res.json(), schema=user_data_schema.USER_DATA_SCHEMA)