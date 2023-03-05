from appium import webdriver

def driver():

    capabilities = {
        "platformName": "Android",
        "deviceName": "AndroidTestDevice",
        "platformVersion": "8.0",
        "automationName": "Appium",
        "appPackage": "org.wikipedia",
        "appActivity": ".main.MainActivity",
        "app": "C:\Python\Wikipedia.apk"
    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
    yield driver
    print("First test run")
    driver.quit()