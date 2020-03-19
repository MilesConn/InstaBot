from time import sleep
from selenium import webdriver
import secrets 

class InstaBot:
    def __init__(self, username, pw):
        self.username = username
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
#        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
#                .click
#Instagram page goes to login page automatically so the above line is not essenetial
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
                .send_keys(username)
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                .send_keys(pw)
        sleep(1)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
                .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                .click()
        print("done init")

    def get_account(self):
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
                .click()


    ##Goes to saved page and scrolls down to the bottom 
    def go_to_saved(self):
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format("saved")).click()

    def scroll_down(self):
        sleep(2)
        self.links=[]
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        saved_box = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(3)
            images=saved_box.find_elements_by_xpath("//img")
            for i in images:
                self.links.append(i.get_attribute('src'))
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.links =  list(set(self.links)) #gets ride of non unique links

    def save_links(self):
        with open("links.txt", "w") as x:
            for i in self.links:
                x.write("%s\n" % i)




if __name__ == "__main__":
    x = InstaBot(secrets.username, secrets.pw)
    x.get_account()
    x.go_to_saved()
    x.scroll_down()
    x.save_links()
    print("done")
