# Initialization Process Automation v1.0 [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)


## Setup?
> Current version works only on Ubuntu
* Download the repository
* Download [Chrome webDriver](http://chromedriver.chromium.org/downloads)
* [Auto Config](#auto-config)
* [Manual Config](#manual-config)

### Auto Config
* Run setup.py 
```terminal
sudo python3 setup.py
```
### Manual Config

* install requirements.tx 
```terminal 
pip install -r requirements.txt
```
* In config.ini add 
```ini
[AUTH]
USERNAME = <github username>
PASSWORD = <github password>

[PATH]
PROJECT_PATH = <path to your projects directory >
```
* In commands.sh add 
```sh
function create() {
    cd
    python3 <path to create.py file> $1 
}

```
### install the commands.sh
* open  .bashsrc 
> .bashrc file is located in your user directory
```terminal 
$ vim ~/.bashrc
```
* at end of the file add
```sh
source <path to commands.sh> 
Ex: source /home/cyber/cyber-Tech/commands.sh
```
# Terminal command
```terminal 
create <your project name>
Ex : create myproject
```

