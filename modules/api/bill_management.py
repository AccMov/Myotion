import requests

from modules.pyMotion.core.account import Account

baseUrl = "https://killbill.accmov.com"
port = "8443"


def get_tenant(username: str, password: str):
    return requests.get(
        url=f"{baseUrl}:{port}/1.0/kb/tenants",
        params={"apiKey": username + "_apikey"},
        headers={"accept": "application/json"},
        verify=False,
        auth=requests.auth.HTTPBasicAuth(username, password),
    )
