#SingleInstance, force
; keyboard: ikonemi simpli 10 
; bàn phím bấm rất nhẹ lúc mới mua về.

; check if have 2 keyboard connected to laptop

; check if device drive of ikonemi is connected
AppsKey::LAlt 	; Menu button 
Ins::RCtrl
LAlt::LWin

; ctrl + ESC: turn on / off
^Esc::
	Suspend On
	; MsgBox, Script has been paused/suspended
	Pause On
return

#If (A_IsPaused)

	^Esc::
		Suspend Off
		Pause Off
		; MsgBox, Script has been unpaused/unsuspended
	return

#If