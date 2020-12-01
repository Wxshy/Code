import base64, requests
import datetime
from urllib.parse import urlencode

client_id = "6b37fd1a38284371b224837b77ad56a2"
client_secret = "96929e780b1f4483a4dc71d8cb9bbcaf"


class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"
    


    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def getClientCreds(self):
        '''Returns b64 encoded string'''
        client_id = self.client_id
        client_secret = self.client_secret

        if client_id == None or client_secret == None:
            raise Exception('Must set a client id and secret')

        client_creds  = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def getTokenHeader(self):
        client_creds_b64 = self.getClientCreds()
        return {
            'Authorization':f"Basic {client_creds_b64}"
        }

    def getTokenData(self):
        return {
            "grant_type":"client_credentials"
        }

    def perform_auth(self):
        token_url = self.token_url
        token_data = self.getTokenData()
        token_header = self.getTokenHeader()

        r = requests.post(token_url, data=token_data, headers=token_header)

        if r.status_code  not in range(200,299):
            return False

        now = datetime.datetime.now()
        token_response_data = r.json()
        access_token = token_response_data['access_token']
        expires_in = token_response_data['expires_in']
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
             
         
        return True

        


spotify = SpotifyAPI(client_id, client_secret)
print(spotify.perform_auth())
token = spotify.access_token
header = {
    "Authorization": f"Bearer {token}", 
}
endpoint = "https://api.spotify.com/v1/search"
data = urlencode({"q": "Money Longer", "type": "track"})
lookupURL = f"{endpoint}?{data}"

r = requests.get(lookupURL, headers=header)
print(r.json())
