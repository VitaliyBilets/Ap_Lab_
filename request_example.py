
import requests

url = "https://www.ssh.com"

response = requests.get(url)

print(response.text)
