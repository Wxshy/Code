import base64, requests
import datetime
from urllib.parse import urlencode
from urllib.request import urlopen

endpoint = 'https://api.clashofclans.com/v1/players/%23'
tag = input('Player Tag: ').upper()
lookupURL = f"{endpoint}{tag}"

token  = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjZlMzVmZGUyLTZmZjctNDZlNi04Y2FjLTVkZTI1MGQ3OWNkMyIsImlhdCI6MTU5MDA5NTc1Mywic3ViIjoiZGV2ZWxvcGVyLzlkZWI3YWE2LWRhNjctMjg2OC05MmIwLTQxYzY4MWMyN2VkNCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjg2LjE2Ny4xMTQuNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.ZFh6H1SimqNGhKD0yaSwVh99fgRGd5JWCe5zmn-Yr0eSl-OIaIOESEsvmb4y8qh3GXlHyWdPgl6ZRB_ulGYN9Q"

header ={
    "Authorization": f"Bearer {token}"
}

r = requests.get(lookupURL, headers=header)
data = r.json()

print(data)