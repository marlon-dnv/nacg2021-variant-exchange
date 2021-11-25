import json
import api.authApi as authApi
from credentials import Creds

creds = Creds()

token = authApi.createToken(creds.username, creds.password, creds.subscriptionKey)

print("Token:", json.dumps(token.json(), indent=2))
