import api.authApi as authApi
import requests
from credentials import Creds

creds = Creds()

accessToken = authApi.createAccessToken(
    creds.username, creds.password, creds.subscriptionKey)

authHeaders = authApi.getAuthHeaders(
    accessToken=accessToken, subscriptionKey=creds.subscriptionKey)

SERVER = "https://testapi.dnvgl.com/TVX_classification_test/"

query = "NM_007294.3:c.981A>G"
endpoint = f"{SERVER}/classification/search/GRCh37?query={query}"

classificationsByHgvs = requests.get(endpoint, headers=authHeaders)

print(classificationsByHgvs.json())
