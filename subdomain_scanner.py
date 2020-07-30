import requests
import os
os.system("clear")
print('''\033[1;36;40m
          _        _                _                                      
  ____  _| |__  __| |___ _ __  __ _(_)_ _    ___ __ __ _ _ _  _ _  ___ _ _ 
 (_-< || | '_ \/ _` / _ \ '  \/ _` | | ' \  (_-</ _/ _` | ' \| ' \/ -_) '_|
 /__/\_,_|_.__/\__,_\___/_|_|_\__,_|_|_||_| /__/\__\__,_|_||_|_||_\___|_|  \033[0m
				\033[1;34;40mcreated by \033[0m \033[1;33;40mTechnical Dangwal\033[0m
''')
a=input("\033[1;33;40mEnter website name : \033[0m \033[1;32;40m")
b=input("\033[1;33;40mEnter wordlist name : \033[0m \033[1;32;40m")
with open(b,"r") as file:
	for line in file.readlines():
		line=line.strip()
		url=f"https://{line}.{a}.com"
		try:
			r=requests.get(url)
			if r.status_code==200:
				print(f"\033[1;32;40mSubdomain Found : {url}\033[0m")
			else:
				pass
		except:
			print(f"\033[1;31;40mNot Found : {url}\033[0m")
