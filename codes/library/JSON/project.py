import requests

url="https://api.nationalize.io"
parms={"name":"Prince Raj Kiran"}
resp=requests.get(url, params=parms)

print(resp.json())