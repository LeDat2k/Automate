DetectHiddenWindows, On
SetTitleMatchMode, 2 
; Run D:\d.Skill\AutoHotkey\ikonemi.ahk
IfWinNotExist, ikonemi.ahk
	; Run, D:\d.Skill\AutoHotkey\ikonemi.exe
	Run, ikonemi.ahk ; run if this file vs ikonemi.ahk file are in the same folder
Return

#x::ExitApp  ; Win+X : exit this script