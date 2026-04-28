import requests
from requests import exceptions as request_exceptions

from modules.pyMotion.core.account import Account

baseUrl = "https://killbill.accmov.com"
kb_port = "8443"
other_port = "9090"


class APIResponse:
    def __init__(self, status_code, payload=None, error_message=""):
        self.status_code = status_code
        self._payload = payload if payload is not None else {}
        self.error_message = error_message

    def json(self):
        return self._payload


def _request_get(url, **kwargs):
    try:
        response = requests.get(url=url, **kwargs)
        payload = {}
        try:
            payload = response.json()
        except ValueError:
            payload = {}
        return APIResponse(response.status_code, payload=payload)
    except request_exceptions.ConnectTimeout:
        return APIResponse(408, error_message="Connection to server timed out")
    except request_exceptions.ReadTimeout:
        return APIResponse(408, error_message="Server response timed out")
    except request_exceptions.SSLError:
        return APIResponse(495, error_message="Secure connection to server failed")
    except request_exceptions.ConnectionError:
        return APIResponse(503, error_message="Unable to connect to server")
    except request_exceptions.RequestException as e:
        return APIResponse(500, error_message=str(e))

def get_tenant(username: str, password: str):
    return _request_get(
        url=f"{baseUrl}:{kb_port}/1.0/kb/tenants",
        params={"apiKey": username + "_apikey"},
        headers={"accept": "application/json"},
        verify=True,
        timeout=10,
        auth=requests.auth.HTTPBasicAuth(username, password),
    )

def login(username: str, password: str):
    return _request_get(
        url=f"{baseUrl}:{other_port}/login",
        headers={"accept": "application/json"},
        verify=True,
        timeout=10,
        auth=requests.auth.HTTPBasicAuth(username, password),
    )

def logout(username: str, password: str):
    return _request_get(
        url=f"{baseUrl}:{other_port}/logout",
        headers={"accept": "application/json"},
        verify=True,
        timeout=10,
        auth=requests.auth.HTTPBasicAuth(username, password),
    )

def heartBeat(username: str, password: str):
    return _request_get(
        url=f"{baseUrl}:{other_port}/status",
        params={},
        headers={"accept": "application/json"},
        verify=True,
        timeout=10,
        auth=requests.auth.HTTPBasicAuth(username, password),
    )
