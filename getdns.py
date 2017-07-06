#!/usr/bin/env python
import sys
import requests
import json

username = "test@example.com" # Your registered username with GetDNS.Co
password = "testpass"			# Your registered password with GetDNS.Co

yourhost = "electricfence.web.direct" # Your host you created on GetDNS.Co that you want to update.

bearer_token = ""
ipAddress = ""

def getLoginToken(username, password) :
	url = "https://getdns.co/api/"
	payload = "username="+username+"&password="+password
	headers = {
		'content-type': "application/x-www-form-urlencoded",
		'cache-control': "no-cache"
		}
	response = requests.request("POST", url+"token", data=payload, headers=headers)
	if response.status_code == 200 :
		global bearer_token 
		data = response.json()
		bearer_token = "bearer " + data['access_token']
		return True
	return False

	
def getDNSIP() :
	url = "https://getdns.co/api/DNS/YourIP/"
	headers = {
		'authorization': bearer_token,
		'cache-control': "no-cache"
		}
	response = requests.request("GET", url, headers=headers)
	if response.status_code == 200 :
		global ipAddress 
		data = response.json()
		ipAddress = data['ipAddress']

def updateARecord() : # TODO
	print("Updating DNS...")
		
def main():
	if getLoginToken(username,password):
		getDNSIP()
		print(ipAddress)
		updateARecord()

if __name__ == "__main__":
    main()