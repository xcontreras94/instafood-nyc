from db.insta_food_db import Insta_Food_DB
from selenium import webdriver
from time import sleep

class Account_Agent:
    def __init__(self, db, webdriver):
        self.webdriver = webdriver
        self.db = db

    def login(self):
        print("Retrieving credentials")
        db = self.db
        db.create_connection()
        creds = db.retrieve_credentials()
        print("Attempting to sign in...")
        webdriver = self.webdriver
        webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(3)
        username = webdriver.find_element_by_name('username')
        username.send_keys(creds['username'])
        password = webdriver.find_element_by_name('password')
        password.send_keys(creds['password'])
        #Get the login button
        button_login = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section[1]/main[1]/div[1]/article[1]/div[1]/div[1]/div[1]/form[1]/div[4]/button[1]/div[1]')
        #sleep again
        sleep(2)
        #click login
        button_login.click()
        sleep(3)
        #In case you get a popup after logging in, press not now.
        #If not, then just return
        print("Successfully logged in")
        try:
            notnow = webdriver.find_element_by_css_selector(
                'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
            notnow.click()
        except:
            return

