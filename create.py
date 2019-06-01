import os 
import sys
import git

from selenium import webdriver

# get current dir and project name
path = os.getcwd()
try:
    repo_name = str(sys.argv[1])
except:
    print("Usage: create <project_name>")
    sys.exit()

browser = webdriver.Chrome()
browser.get('http://github.com/login')

username = ''
password = ''

def create_repo():
    
    # Login to Github.com
    python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
    python_button.send_keys(username) 
    python_button = browser.find_elements_by_xpath("//input[@name='password']")[0] 
    python_button.send_keys(password)
    python_button = browser.find_elements_by_xpath("//input[@name='commit']")[0]
    python_button.click()
    print("[+] Logged in to Github.com")

    # Create repository
    browser.get('https://github.com/new') 
    python_button = browser.find_elements_by_xpath("//input[@name='repository[name]']")[0] 
    python_button.send_keys(repo_name)
    init_readme = browser.find_elements_by_xpath('//*[@id="repository_auto_init"]')[0].click()
    python_button = browser.find_element_by_css_selector('button.first-in-line')
    python_button.submit()
    print(f"[+] Created repository: {repo_name}")

    # Clone repository
    git.Git(path).clone(browser.current_url)
    print(f"[+] Repository cloned to {path} ")

    browser.quit()

if __name__ == "__main__":
        create_repo()
