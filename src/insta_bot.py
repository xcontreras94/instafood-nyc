import configparser
from bot_engine import Bot_Engine
from db.insta_food_db import Insta_Food_DB
from selenium import webdriver
from time import sleep


def main():
    config = configparser.ConfigParser()
    config.read("src/config.ini")
    
    wd = webdriver.Firefox(executable_path=config["DEFAULT"]["firefox_path"])
    db = Insta_Food_DB(config["DEFAULT"]["db_path"])

    bot = Bot_Engine(db, wd)
    bot.init()
    bot.update()

    wd.close()



if __name__ == '__main__':
    main()