import requests

SERVER = "https://testapi.dnvgl.com/TVX_oauth_test"
ENDPOINT = f"{SERVER}/token"


def createAccessToken(username: str, password: str, subscriptionKey: str) -> str:
    tokenResponse = createToken(
        username=username, password=password, subscriptionKey=subscriptionKey
    )

    return tokenResponse.json()["access_token"]


def createToken(username: str, password: str, subscriptionKey: str):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Ocp-Apim-Subscription-Key": subscriptionKey,
    }

    data = {"grant_type": "password", "username": username, "password": password}

    return requests.post(ENDPOINT, data=data, headers=headers)


def getAuthHeaders(accessToken: str, subscriptionKey: str):
    return {"Authorization": f"Bearer {accessToken}", "Ocp-Apim-Subscription-Key": subscriptionKey}
