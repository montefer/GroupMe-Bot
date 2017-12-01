"""
Created on Thu Nov 30 21:03:48 2017

@author: Fernando
"""

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
    #5.1 - Apparently I can't use environment variables??? Just use the API to get my sensitive vars (also makes it better if I
    #      plan on making this open source)
    #6 - Find a way to not have to overwrite all the data each time new messages are introduced from groupchats
    #7 - Store different messages from different groupchats in different files (text or csv? probably csv)
    #8 - download_messages(gc_name, nmbr_prev_msgs), upload_messages_server(msg_file(text/csv)), clean_messages(msg_file(text/csv)) 
    #8.1 - the above are the minimum that should be considered
    
import requests
import json


#Establish the base of the url that will vary depending on what we need to do
base_url = "https://api.groupme.com/v3"

#Pull token info from text file that will NOT be uploaded to GitHub to preserve my security
token = open("groupme_token.txt", 'r').read()

#Get groups
groups_index = base_url+"/groups"+token


#make a get request for groups
response = requests.get(groups_index)

group_list = response.json()['response']#[0]#['name']#[:]['id']

def clean_json(json_response):
    i=0
    #group = 'ML Fun With Bots' #input('What group do you want to pull data from?\n')
    group = '[Insert Group Chat Name Here]'
    for group_iteration in group_list:
        if group==group_list[i]['name']:
            #print('Members: ', group_list[i]['members']) ##Gets entire dict within dict
            print('Members: \n')
            for member in group_list[i]['members']:
                print(member['nickname'])  
                print(member,'\n') #will print out each individual dict for each member
            i+=1
        else:
            i+=1
            

def flatten_json(json_response):
    i=0
    group = 'ML Fun With Bots' #input('What group do you want to pull data from?\n')
    #group = '[Insert Group Chat Name Here]'
    for group_iteration in group_list:
        if group==group_list[i]['name']:
            #print('Members: ', group_list[i]['members']) ##Gets entire dict within dict
            print(group_list[i])
            print('Members: \n')
            for member in group_list[i]['members']:
                print(member['nickname'])  
                print(member,'\n') #will print out each individual dict for each member
            i+=1
        else:
            i+=1        
    
    
def get_group_id(group_info):
    i=0
    group = 'ML Fun With Bots' #input('What group do you want to pull data from?\n')
    for group_iteration in group_list:
        if group==group_list[i]['name']:
            print(group_list[i]['group_id'])
            i+=1
        else:
            i+=1

def get_group_name(group_info):
    i=0
    group = 'ML Fun With Bots' #input('What group do you want to pull data from?\n')
    for group_iteration in group_list:
        if group==group_list[i]['name']:
            print(group_list[i]['name'])
            i+=1
        else:
            i+=1
    
def get_group_phone_number(group_info):
    i=0
    group = 'ML Fun With Bots' #input('What group do you want to pull data from?\n')
    for group_iteration in group_list:
        if group==group_list[i]['name']:
            print(group_list[i]['phone_number'])
            i+=1
        else:
            i+=1
    
    
if __name__=="__main__":
    other_url = 'https://api.groupme.com/v3/groups'+token
    getting = requests.get(other_url)

    groupInfo = flatten_json(response.json())

    
    get_group_id(groupInfo)
    get_group_name(groupInfo)
    