import requests

baseUrl = "https://killbill.accmov.com"
port = "8443"

res = requests.get(
    url=baseUrl + ":" + port + "/1.0/kb/tenants",
    params={"apiKey": "api_key"},
    headers={
        "accept": "application/json",
    },
    verify=False,
    auth=requests.auth.HTTPBasicAuth("admin", "i-0f96c0c2f6cdd1289"),
)


def get_tenants(apiKey: str, userAuth):
    requests.get(
        url=baseUrl + ":" + port + "/1.0/kb/tenants",
        params={"apiKey": apiKey},
        headers={"accept": "application/json"},
        verify=False,
        auth=requests.auth.HTTPBasicAuth("admin", "i-0f96c0c2f6cdd1289"),
    )


def login(username: str, password: str):
    return requests.get(
        url=baseUrl + ":" + port + "/1.0/kb/tenants",
        params={"apiKey": "api_key"},
        headers={"accept": "application/json"},
        verify=False,
        auth=requests.auth.HTTPBasicAuth(username, password),
    )
