import configparser
import pwd
import os



def install_requirements():
    try: 
        os.system("sudo pip3 install -r requirements.txt")
        os.system("clear")
    except:
        os.system("sudo pip install -r requirements.txt")
        os.system("clear")


def config():
    """
    get data from config.ini
    """

    config = configparser.ConfigParser()
    config.read(os.path.join(os.getcwd(), 'config.ini'))
    return config


def config_file(username, password, path):
    """
    write data into config.ini
    """
    code = f"""
        [AUTH]
        USERNAME = {username}
        PASSWORD = {password}

        [URLS]
        LOGIN_LINK = https://github.com/login
        NEW_REPO = https://github.com/new

        [PATH]
        PROJECT_PATH = {path}
    """
    file = open("config.ini", "w")
    file.write(code)
    file.close


def command_sh():
    code = (
    " #!/bin/bash\n\nfunction create() {\n" 
    + f"python3 {os.getcwd()}/create.py $1\n"
    +"}")



    file = open("commands.sh","w")
    file.write(code)
    file.close()


def write_bashrc():
    system_username =  pwd.getpwuid(os.getuid())[ 0 ]
    code = f"source {os.getcwd()}/commands.sh"
    
    with open(f'/home/{system_username}/.bashrc', 'a') as content:
        content.write(code)
    
