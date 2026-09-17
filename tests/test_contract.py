# tests/test_contract.py
import pytest
from jsonschema import validate
from framework.schemas import user_data_schema



@pytest.mark.api
def test_datosuser_cumple_el_contrato(logged_in_client):
    r = logged_in_client.datos_user()
    assert r.status_code == 200, f"{r.status_code} — {r.text}"
    validate(instance=r.json(), schema=user_data_schema.USER_DATA_SCHEMA)