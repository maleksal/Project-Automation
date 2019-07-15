# Auto Configure Files

from __utilities__.utilities import config_file
from __utilities__.utilities import command_sh
from __utilities__.utilities import write_bashrc


# Inputs for config.ini 
get_username = input("[*] Github Username/Email:  ")
get_password = input("[*] Github Password: ")
get_dir_path = input("[*] Path to Your Projects DIR: ")


print("\n\n")

print("[+] Edit config.ini")
config_file(get_username, get_password, get_dir_path)
print("[+] Edit commands.sh")
command_sh()
print("[+] writing into bashrc")
write_bashrc()
print("[====== DONE ======]")