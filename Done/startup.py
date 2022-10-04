import subprocess

PATH = r'C:\Users\ASUS\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

p = subprocess.Popen(['explorer', PATH])
p.communicate()