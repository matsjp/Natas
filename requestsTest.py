import requests
username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
url = 'http://natas17.natas.labs.overthewire.org/index.php?&debug&username=natas16'

response = requests.get(url, verify = False, auth = (username, password))
print(response.text)