# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 01:14:45 2017

@author: Fernando
"""

    
import requests
import json
import groupme_get_group_info as gmi


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
    

    
    
    
if __name__=="__main__":
    ###############Add New Members Example###########################
#    flatten_json(response.json())
#    new_member = json.dumps({
#     "members": [
#                 {
#                    "nickname": "Jackson Chen",
#                    "user_id": "+1 7202344186",
#                    "guid": "GUID-1"
#                 }
#                ]
#        })
#    url  = 'https://api.groupme.com/v3/groups/33317180/members/add?token=JWMisdf6K8a2756JNSHnax0ovSHtlCU7eQbaIs4X'
#    posting = requests.post(url, data=new_member)
#    print(posting)
    other_url = 'https://api.groupme.com/v3/groups'+token
    getting = requests.get(other_url)
#    print(getting)     #Prints html response code

    groupInfo = flatten_json(response.json())

    
    #print(groupInfo)
    
    gmi.get_group_id(groupInfo)
    gmi.get_group_name(groupInfo)
    gmi.get_group_phone_number(groupInfo)
    
    
    
#    list_A = flatten_json(response.json())
#    list_A = response.json()
#    print(list_A)
#    print(group_list[0])
#    print(list_A['response'][0])
