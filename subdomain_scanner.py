import requests
import os
os.system("clear")
a=input("\033[1;33;40mEnter website name : \033[0m\033[1;32;40m")
b=input("\033[1;33;40mEnter wordlist path : \033[0m \033[1;32;40m")
with open(b,"r") as file:
	for pas in file.readlines():
		password=pas.strip()
		url=f"https://{password}.{a}.com"
		try:
			r=requests.get(url)
			if r.status_code==200:
				print(f"\033[1;32;40mSubdomain Found : {url}\033[0m")
			else:
				pass
		except:
			print(f"\033[1;31;40mNot Found : {url}\033[0m")

