# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 01:14:45 2017

@author: Fernando
"""
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
    
import requests
import os

#import json #not necessary apparently

#Attempt to download GroupMe messages

base_url = "https://api.groupme.com/v3"
token = os.getenv('TOKEN')
token = '?token=JWMisdf6K8a2756JNSHnax0ovSHtlCU7eQbaIs4X'

#Get groups
#print(token)
groups_index = base_url+"/groups"+token


#make a get request for groups
response = requests.get(groups_index)
#print(response.status_code)
##print(response.content[0:100]) #prints out the first hundred characters
#print(response.json().keys())
#print(response.json()['meta'])
#print(response.encoding)
#print(response.json()['response'][0]['id'])
#print(response.json()['response'][0]['name'])
#print(response.json()['response'][1]['id'])
#print(response.json()['response'][0])       

def flatten_json(json_response, delim):
    #print("\n"+json_response['response'][0]['name'])
    val = {}
    for i in json_response.keys():
        if isinstance(json_response[i], dict):
            get = flatten_json(json_response[i], delim)
            for j in get.keys():
                val[i + delim + j ] = get[j]
        else:
            val[i] = json_response[i]

    return val

#def convert_json(json_response):
#    #print("\n",json_response['response'][0]['name'])
#    #print(json_response.keys())
#    #val = {}
#    if isinstance(json_response, dict):
#        for key in json_response.keys():
#            #print(json_response[key],'\n')
#            if isinstance(json_response[key], dict):
##                #nested_dict = convert_json(json_response[key])
##                for new_key,value in value.items():
##                    #print(new_key, ' ', value)
##                    print('Hi')
#                nested_dict = convert_json(json_response[key])
#                convert_json(nested_dict)
##            elif isinstance(json_response[key], list):
##                json_response[key]
#            else:
##                #print('\n',json_response[key])
#                #print(value,'\n'+'\n')
#                print(json_response.values())
#                return json_response.values()
#                #pass
#    else:
#        #return json_response.values()
#        print(json_response.values())
#        #pass
    
if __name__=="__main__":
    #print(flatten_json(response.json(),' '))
    list_A = flatten_json(response.json(),'lolololololol')
    print(list_A)
