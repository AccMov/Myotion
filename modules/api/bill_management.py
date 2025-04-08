import requests

from modules.pyMotion.core.account import Account

baseUrl = "https://killbill.accmov.com"
kb_port = "8443"
other_port = "9090"

def get_tenant(username: str, password: str):
    return requests.get(
        url=f"{baseUrl}:{kb_port}/1.0/kb/tenants",
        params={"apiKey": username + "_apikey"},
        headers={"accept": "application/json"},
        verify=True,
        auth=requests.auth.HTTPBasicAuth(username, password),
    )

def heartBeat(username: str, password: str):
    return requests.get(
        url=f"{baseUrl}:{other_port}/status",
        params={},
        headers={"accept": "application/json"},
        verify=True,
        auth=requests.auth.HTTPBasicAuth(username, password),
    )
