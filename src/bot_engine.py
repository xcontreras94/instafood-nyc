from account_agent import Account_Agent

class Bot_Engine:
    def __init__(self, db, webdriver):
        self.db = db
        self.webdriver = webdriver
        self.agent = Account_Agent(db, webdriver)
    
    def init(self):
        self.agent.login()
        return

    def update(self):
        return