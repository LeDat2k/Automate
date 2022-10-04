#!/usr/bin/env sh
#!/system/bin/sh

shell="adb shell"
tap="${shell} input touchscreen tap"
swipe="${shell} input touchscreen swipe"
text="${shell} input text"
key="${shell} input keyevent"

unlock() {
    $text 1472 && $key KEYCODE_ENTER
}

cleanCurrent() {
    $key KEYCODE_APP_SWITCH
    $swipe 360 700 360 100 150
    $key KEYCODE_HOME
}

# clean all background running app by GUI
cleanAll() {
    $key KEYCODE_APP_SWITCH
    $swipe 1 640 719 640 150
    $tap 135 490
}

shopeeCoin() {
    $shell am start -a android.intent.action.VIEW -d https://shopee.vn/universal-link/shopee-coins/?__classic__=1&deep_and_web=1&smtt=0.0.9
    sleep 8

    # daily coin
    $tap 360 290
    sleep 2

    # Xo so
    $swipe 360 1279 360 0 2000
    $tap 360 268
    $tap 360 600
    sleep 0.5
    $tap 470 567
    sleep 0.5

    # Mo qua
    $tap 360 1120
    
    $swipe 360 200 360 1279 500

    # nong trai
    $tap 80 915
    sleep 16
    $tap 615 1165
    sleep 1
}

momo() {
    cleanAll
    sleep 0.25
    $shell am start -n com.mservice.momotransfer/vn.momo.platform.MainActivity
    sleep 9

    # click Heo đất
    $tap 360 700
    sleep 4

    # click Close Announcement 
    $tap 360 915
    sleep 1

    # click Cho heo ăn
    $tap 360 915
    sleep 1
    
    # click "Quyen gop" ??? Wait too long
    $tap 455 1025
    sleep 7

    # click to chuc tu thien dau tien
    $tap 455 1025
    sleep 5

    # click Quyen gop
    $tap 455 1225
    sleep 4

    # click choose "Quyên góp ẩn danh"
    $tap 665 990
    sleep 0.2

    # # trừ bớt số heo
    for i in $(seq 1 9); do
        $tap 265 810
        sleep 0.5
    done

    # click Quyên góp
    $tap 455 1225
    sleep 1
}

unlock
sleep 1
cleanAll