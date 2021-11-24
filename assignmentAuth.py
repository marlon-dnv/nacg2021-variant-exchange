import api.authApi as authApi
from credentials import Creds

creds = Creds()

token = authApi.createToken(creds.username, creds.password, creds.subscriptionKey)

print("Token:", token.json())
