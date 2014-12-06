#! /usr/bin/python
#
# DESCRIPTION:	
# AUTHOR: 	Mohamed Osama (mohamed.osama.aboelkheir@gmail.com)
# CREATED: 	Thu 27-Nov-2014
# LAST REVISED:	Thu 27-Nov-2014
#
##############
# DISCLAIMER #
##############
# Anyone is free to copy, modify, use, or distribute this script for any purpose, and by any means. However, Please take care THIS IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND AND YOU SHOULD USE IT AT YOUR OWN RISK.

import os.path
import ConfigParser
import re


# Function to set value in conf file
def set_value(config,section,option):
	if config.has_option(section,option):
	    value=config.get(section,option)
	else:
	    value=""
	
	if value != "":
	    decision=raw_input("The current value of \""+option+"\" is \""+value+"\" ... do you wish to change it? (y/n): ")
	    if decision == "y" or decision == "Y":
			value=raw_input("Please enter the new value for \""+option+"\" : ")
			config.set(section,option,value)
	else:
		value=raw_input("Please enter value for \""+option+"\" : ")
		config.set(section,option,value)


dir_name=os.path.dirname(os.path.realpath(__file__))
#config_file=os.path.join(dir_name,"settings_inital.conf")
config_file=os.path.join(dir_name,"settings.conf")

config=ConfigParser.ConfigParser()
config.read(config_file)

#Gcal

print "\n#####################"
print "# Gcal settings     #"
print "#####################"

if not config.has_section("Gcal"):
	config.add_section("Gcal")

# Calendar address
set_value(config,"Gcal","calendar_address")

# Client ID
#set_value(config,"Gcal","client_id")

# Client secret
#set_value(config,"Gcal","client_secret")

print "\n#####################"
print "# Toggl settings    #"
print "#####################"

if not config.has_section("Toggl"):
	config.add_section("Toggl")

# toggl api token
set_value(config,"Toggl","toggl_api_token")

# workspace id
set_value(config,"Toggl","workspace_id")

# Color mapping
print "\n#####################"
print "# Project Color map #"
print "#####################"
print "NOTE: Possible values for colorId (1-11)"
print "1 ->  blue , 2 ->  cyan , 3 ->  purple , 4 ->  red\n5 ->  yellow , 6 ->  orange , 7 ->  turquoise , 8 ->  grey\n9 ->  bold blue , 10 -> bold green , 11 -> bold red\n"

if not config.has_section("Color_mapping"):
	config.add_section("Color_mapping")

options=config.options("Color_mapping")
if options:
	print "Current Config:"
	for option in options:
		set_value(config,"Color_mapping",option)

cont=True
while cont:
	answer=raw_input("Do you wish to add color mappings for a Toggl Project? (y/n): ")
	if answer == "y" or answer == "Y":
		project_name=raw_input("Please enter project name: ")
		color=raw_input("Please enter colorId (1-11): ")
		config.set("Color_mapping",project_name,color)
	else:
		cont=False


with open(config_file, 'wb') as configfile:
	config.write(configfile)

with open(config_file, 'rb') as configfile:
	print configfile.read()
	
