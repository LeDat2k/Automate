#!/usr/bin/env python3

# Android environment
import os
import time
from appium import webdriver
# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import selenium



options = UiAutomator2Options()
options.platformVersion = '10'
options.udid = 'f4df68177d44'

# Appium1 points to http://127.0.0.1:4723/wd/hub by default 
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)

# cmd = 'adb shell am start -a android.intent.action.VIEW -d "https://shopee.vn/digital-product/m/\\?dp_from_source\\=1"'
# os.system(cmd)

driver.start_activity('com.shopee.vn', '')
# time.sleep(15)


# driver.implicitly_wait(30)
start=time.time()

driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View').click()
driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.ListView[1]/android.view.View[1]/android.view.View/android.view.View').click()
# driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[8]/android.view.View/android.widget.Button').click()

print(time.time()-start)

# mo bang inspect thi no xoa het du lieu luon
# Khong duoc mo bang options.appActivity='' neu khong thi se xoa het du lieu trong app

# resourceID
# 'com.shopee.vn:id/webView'




