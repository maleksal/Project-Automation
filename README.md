# Project Initialization Automation
## How it works?

* Download the repository
* install requirements.tx 
```terminal 
pip install -r requirements.txt
```
* Download [Chrome webDriver](http://chromedriver.chromium.org/downloads)
* In create.py add your Github username and password
```python
username = ''
password = ''
```
* Edit the commands.sh
```sh
function create() {
    cd
    cd <your projects path> Ex: /home/cyber/Desktop/Dev-Projects/
    python3 <path to create.py file> $1 Ex: /home/cyber/cyber-Tech/create.py
}

```
### install the commands.sh
* open .bashsrc 
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
![Alt text](https://user-images.githubusercontent.com/25385625/58741936-582d7880-8417-11e9-8b37-b35931ae9f74.png)
