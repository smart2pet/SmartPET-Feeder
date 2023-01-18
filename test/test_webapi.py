import pytest
import requests
class TestWebApi():
    def test_all(self):
        ip = input("Enter the IP address of the raspberry pi:")
        request_add_plan = requests.post(f'http://{ip}:8000/plan', json='{"time_h": 25, "time_m": 90, "weight": 200}"')
        assert x.text == '{"result":1,"reason":"Data invalid."}'

