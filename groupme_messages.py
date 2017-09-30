# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 01:14:45 2017

@author: Fernando
"""

import requests
#import json #not necessary apparently

#Attempt to download GroupMe messages

base_url = "https://api.groupme.com/v3"
token = "?token=JWMisdf6K8a2756JNSHnax0ovSHtlCU7eQbaIs4X"

#Get groups
groups_index = base_url+"/groups"+token


#make a get request for groups
response = requests.get(groups_index)
print(response.status_code)
#print(response.content[0:100]) #prints out the first hundred characters
print(response.json().keys())
print(response.json()['meta'])
print(response.encoding)
print(response.json()['response'][0]['id'])
print(response.json()['response'][0]['name'])
print(response.json()['response'][1]['id'])
print(response.json()['response'][0])

def clean_json(json_response):
    print("\n"+json_response['response'][0]['name'])
    
if __name__=="__main__":
    clean_json(response.json())

#Fascinating... I will have to continue messing around with this, but let's use this to establish some of
#the things I want this app to be able to do:
    #1 - Pull all data from response/json but only from the first group and clean
    #2 - Make specific data request functions
    #2.1 - Specify which group to pull data from in function, otherwise just default to the latest group
    #3 - From data pulled, there are default limits to how much data we receive, adjust as necessary
    #4 - Store data in PostgreSQL server by calling a function
    #5 - Create environment variables that we can use to access GM and PostgreSQL so we don't store sensitive info in the app
    #6 - Find a way to not have to overwrite all the data each time new messages are introduced from groupchats
    #7 - Store different messages from different groupchats in different files (text or csv? probably csv)
    #8 - download_messages(gc_name, nmbr_prev_msgs), upload_messages_server(msg_file(text/csv)), clean_messages(msg_file(text/csv)) 
    #8.1 - the above are the minimum that should be considered