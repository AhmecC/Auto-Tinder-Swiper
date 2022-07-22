from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from random import randint

# -------------------- CONSTANTS -------------------- #
path = r"CHROMEDRIVER LOCATION"
LOGIN = "YOUR FB LOGIN"
PASS = "YOUR FB PASS"

# -------------------- CONNECT TO TINDER -------------------- #
driver = webdriver.Chrome(executable_path=path)
driver.get("https://tinder.com/")
sleep(0.5)


# -------------------- DIRECT TO FACEBOOK LOGIN -------------------- #
driver.find_element(By.XPATH, f'//*[@id="{id1}"]/div/div[2]/div/div/div[1]/div[1]/button').click()
# Accepts Tinder Cookies

driver.find_element(By.XPATH, f'//*[@id="{id1}"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
sleep(0.5)  # Finds the Login Button on Main Page

driver.find_element(By.XPATH, f'//*[@id="{id2}"]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click()
sleep(1.5)  # Chooses Facebook as Login Option


# -------------------- LOGIN VIA FACEBOOK-------------------- #
base_window, fb_window = driver.window_handles[0], driver.window_handles[1]
driver.switch_to.window(fb_window)  # Switch Window Handle to Facebook-Popup Login

driver.find_elements(By.XPATH, "//button[contains(string(), 'Allow essential and optional cookies')]")[0].click()
sleep(1)  # Accepts Cookies on Facebook Popup

driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(LOGIN)
# Enters your facebook email/number

driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(PASS)
# Enters your facebook password

driver.find_element(By.XPATH, '//*[@id="loginbutton"]').click()
sleep(5)  # Confirms Login


# -------------------- ACCEPT PREFERENCES TINDER -------------------- #
driver.switch_to.window(base_window)  # Switch Window Handle to Tinder

driver.find_element(By.XPATH, f'//*[@id="{id2}"]/div/div/div/div/div[3]/button[1]').click()
sleep(0.5)  # Allows Location

driver.find_element(By.XPATH, f'//*[@id="{id2}"]/div/div/div/div/div[3]/button[2]').click()
sleep(7)  # Disables Notifications


# -------------------- START MATCHING -------------------- #
for i in range(0, 150):  # Stops code running forever (should allow for 100 ssuccesful swipes)
        sleep(randint(1, 3))  # How often it will attempt Swipe
    try:
        match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
        match_popup.click()
        # Checks if match was made, and if true it clicks button to remove from screen (and allows swiping to continue)
    except:
        print("Swiping")
        like = driver.find_element(By.XPATH, '//body')
        like.send_keys(Keys.ARROW_RIGHT)  # Sends Right Key to swipe

        driver.execute_script('el = document.elementFromPoint(47, 457); el.click();')
        # Clicks to Alleviate Out of Click Popup and Add to Home Screen
