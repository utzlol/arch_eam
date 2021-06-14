import requests

a = requests.get('https://archlinux.org/mirrorlist/?country=all&protocol=http&protocol=https&ip_version=4')
print(a.text)
a = a.text

a = a.replace('#S', 'S')

filew = open('mirrorlist', 'w')
filew.write(a)
filew.close()

filer = open('mirrorlist', 'r')
print(filer.read())
