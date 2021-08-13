import requests, subprocess

a = requests.get('https://archlinux.org/mirrorlist/?country=all&protocol=http&protocol=https&ip_version=4')
print(a.text)
a = a.text

username = str(subprocess.check_output('whoami'))
username = username.replace("b'",'').replace("\\n'",'')
dir = f'/home/{username}/mirrorlist'

a = a.replace('#S', 'S')

filew = open(dir, 'w')
filew.write(a)
filew.close()

filer = open(dir, 'r')
print(filer.read())
subprocess.call(['sudo','mv',dir,'/etc/pacman.d/'])
subprocess.call(['rm','dir'])
