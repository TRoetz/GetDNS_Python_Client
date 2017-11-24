#!/usr/bin/env python
import sys
import requests
import json

# Update the following
username = "test@example.com" 	# Your registered username with GetDNS.Co
password = "testpassword"		# Your registered password with GetDNS.Co

yourhost = "tesa" 				# Your host you created on GetDNS.Co that you want to update.
getdnsDomain = "web.direct"		# The Domain picked when you created your host

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

def updateARecord() :
	print("Updating DNS...")
	url = "https://getdns.co/api/dns/ARecord"
	payload = '{"IPAddress":"%s","Hostname":"%s", "Domain":"%s"}' % (ipAddress, yourhost, getdnsDomain)
	headers = {
	    'content-type': "application/json",
		'authorization': bearer_token,
		'cache-control': "no-cache"
		}
	response = requests.request("PUT", url, data=payload, headers=headers)
	if response.status_code == 200 :
		print("IP Address: %s updated for %s.%s" % (ipAddress, yourhost, getdnsDomain))
		return True
	else :
		print (response.status_code)
	return False
		
def main():
	if getLoginToken(username,password):
		getDNSIP()
		print(ipAddress)
		updateARecord()

if __name__ == "__main__":
    main()
