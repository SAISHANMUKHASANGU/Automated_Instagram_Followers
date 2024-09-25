import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

SIMILAR_USER="SPECIFED ACCOUNT"
EMAIL="YOUR DETAILS"
PASSWORD="YOUR PASSWORD"

class InstaFollower():
    def __init__(self):
        self.driver=webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/?hl=en")
        email=self.driver.find_element(By.NAME,value='username')
        email.send_keys(EMAIL)
        password=self.driver.find_element(By.NAME,value='password')
        password.send_keys(PASSWORD)
        login_button=self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[3]')
        login_button.click()
        time.sleep(5)
        not_now_button=self.driver.find_element(By.XPATH,value="//div[contains(text(), 'Not now')]")
        not_now_button.click()
        time.sleep(5)
        not_now_button2 = self.driver.find_element(By.XPATH, value="// button[contains(text(), 'Not Now')]")
        not_now_button2.click()
        time.sleep(5)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_USER}/")
        time.sleep(20)
        following=self.driver.find_element(By.XPATH,value="//a[contains(@href, '/pickbysurya_/following/')]")
        following.click()
        time.sleep(6)
        model_xpath="/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]"
        model=self.driver.find_element(By.XPATH,value=model_xpath)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", model)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot=InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
