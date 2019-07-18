import os 
import sys
import git

import configparser

from selenium import webdriver



def config():
    """
    get data from config.ini
    """
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'))
    return config



def create_repo():
    
    # Login to Github.com
    python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
    python_button.send_keys(username) 
    python_button = browser.find_elements_by_xpath("//input[@name='password']")[0] 
    python_button.send_keys(password)
    python_button = browser.find_elements_by_xpath("//input[@name='commit']")[0]
    python_button.click()
    print("[+] Logged into Github.com")

    # Create repository
    browser.get(config()["URLS"]["NEW_REPO"]) 
    python_button = browser.find_elements_by_xpath("//input[@name='repository[name]']")[0] 
    python_button.send_keys(repo_name)
    
    # init a readme file
    browser.find_elements_by_xpath('//*[@id="repository_auto_init"]')[0].click()
   
    python_button = browser.find_element_by_css_selector('button.first-in-line')
    python_button.submit()
    print(f"[+] Created repository: {repo_name}")

    # Clone repository
    git.Git(path).clone(browser.current_url)
    print(f"[+] Repository cloned to {path} ")

    browser.quit()

if __name__ == "__main__":
    
    try:
        repo_name = str(sys.argv[1])
    except:
        print("Usage: create <project_name>")
        sys.exit()
    

    # get current dir and project name

    path = config()["PATH"]["PROJECT_PATH"]

    browser = webdriver.Chrome()
    browser.get(config()["URLS"]["LOGIN_LINK"])

    username = config()["AUTH"]["USERNAME"]
    password = config()["AUTH"]["PASSWORD"]

    create_repo()
