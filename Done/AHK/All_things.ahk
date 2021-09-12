; # window ; ^ Ctrl ; ! Alt ; + Shift
#SingleInstance, force

!+m::run https://mail.google.com/mail/u/0/h/1p1nogfydjb1p/?zy=e&f=1
:::archive::-in:Sent -in:Draft -in:Inbox

!+Del::FileRecycleEmpty
F1::Send, {LWinDown}1{LWinUp}

^!t::Run, wsl.exe 

F5::Run, C:\Users\ASUS\Desktop\Hibernate.lnk

:*:hsd::hsddung92.lpdat@gmail.com
:*:alone1::alone147896321@gmail.com
:*:ledat.fake::ledat.fake@gmail.com
:*:ledat.code::ledat.code@gmail.com
:*:py3::python3
:*:taskkill::taskkill /IM pythonw.exe /F
:*:312::3120219024
:*::phone::0869570027
; ------------------------------------------------------------
; computer win 10 Directory PATHs
:*:\class::D:\Class\
:*:\code::D:\Code\
:*:\eng::D:\English
:*:\skill::D:\Skill\

:*:\down::C:\Users\ASUS\Downloads
:*:\desk::C:\Users\ASUS\Desktop
:*:\doc::C:\Users\ASUS\Documents
:*:\mu::D:\Music

:*:j-::-----------------------------------------------------------
; vim user
Capslock::Esc

!z::Send, {AltDown}{Left}{AltUp}
	
; change volume 
>!j::Send, {Volume_Down}
>!k::Send, {Volume_Up}
>!m::Send, {Volume_Mute}}
; -------------------------------------------------------------
; ;time vs ;date vs ;now
; without ending character: có thêm * ở giữa :*:
:R*?::time::
	FormatTime, CurrentDateTime,, HH:mm
	SendInput %CurrentDateTime%
return

:R*?::date::
	FormatTime, date,, MM/dd/yyyy
	Send, %date%
return

:R*?::now::
	FormatTime, CurrentDateTime, HH:mm MM-dd-yyyy
	SendInput %CurrentDateTime%
return

	; now() có bật việt key là không được
	; :now có bật việt key thì được
		;-> nếu từ tiếng việt hiện dấu vào cuối ký tự thì chấp nhận được
; ------------------------------------------------------------
; Dark vs Light color change in time
!+d::
 	; Run, ..\changeTheme.pyw
 	Run, D:\code\Python\Automate\Done\changeTheme.pyw
return
; ------------------------------------------------------------
^g:: ; GoogleSearch or Show Link with CTRL+G
  prevClipboard := ClipboardAll ; make copy of previous Clipboard
  Send, {ctrl down}c{ctrl up} ; copy selected text
  ClipWait ; delay
  if !(ErrorLevel)  { 
    Clipboard := RegExReplace(RegExReplace(Clipboard, "\r?\n"," "), "(^\s+|\s+$)")
    If (SubStr(ClipBoard,1,7)="http://" || SubStr(ClipBoard,1,8)="https://")
      Run, % Clipboard
    else 
      Run, http://www.google.com/search?q=%Clipboard%
  } 
  ; Clipboard := prevClipboard ; return to previous clipboard
return

; ------------------------------------------------------------
; cheat chủ nghĩa xã hội khoa học
; can't use the code in the file ?? need to open in another file ??
; -----------------------------------------------------------
; only exercute in chrome app 
; #IfWinActive, ahk_exe Chrome.exe ;; start of IfWinActive condition, for me it didn't work with ahk_class so i changed it to ahk_exe
; {
; 	#If, A_Cursor != "IBeam" 
; 	{
; 		j::Down
; 		h::Left
; 		k::Up
; 		l::Right
; 	}
; }
; #IfWinActive ;; end of condition IfWinActive
; Return
 
^F2::Edit


