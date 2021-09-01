import os, subprocess, sys, pyautogui, time

dark_mode = 'New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name SystemUsesLightTheme -Value 0 -Type Dword -Force; New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme -Value 0 -Type Dword -Force'
light_mode = 'New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name SystemUsesLightTheme -Value 1 -Type Dword -Force; New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme -Value 1 -Type Dword -Force'
# os.system('echo $SHELL') #-> just run with cmd
# print() 
# ------------------------------------------------------------
# subprocess.call('notepad.exe')

# code = subprocess.call(['ping', 'www.google.com']) -> run OK
# code = subprocess.call('dir') -> can't run?????
# x = subprocess.run('ls') #->can't run??

# print(code)

# program = 'powershell.exe'
# process = subprocess.call(program)
# time.sleep(2)
# pyautogui.write('dir') #-> can't run
# code = process.wait()
# print(code)

# subprocess.Popen(['notepad.exe', 'D:\\1.IT\\Python\\Automate\\Shortcut_script\\.dark.ps1']) # -> run OK
# subprocess.Popen(['powershell.exe', 'D:\\1.IT\\Python\\Automate\\Shortcut_script\\.dark.ps1'], shell=True) # -> can't run
# subprocess.Popen(['powershell.exe', 'D:\\1.IT\\Python\\Automate\\Shortcut_script\\.dark.ps1']) # can't run

# ------------------------------------------------------------

# program = "notepad.exe"
# process = subprocess.Popen(program)
# code = process.wait()
# print(code)
# >>> 0

# ------------------------------------------------------------ 

# process = subprocess.Popen(['powershell.exe', dark_mode])
# code = process.wait()

process = subprocess.Popen(['powershell.exe', light_mode])
process.communicate()

# j------------------------------------------------------------
# open file as default program

subprocess.Popen(['start', filePath], shell=True)


# 2 way to execute cmd or powershell command
p = subprocess.Popen(['explorer', filePath], shell=True)
p.communicate()

p = subprocess.Popen(['powershell.exe', command])
p.communicate()