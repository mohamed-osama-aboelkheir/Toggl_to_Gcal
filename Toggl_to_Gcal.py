#! /usr/bin/python
#
# DESCRIPTION:	
# AUTHOR: 	Mohamed Osama (mohamed.osama.aboelkheir@gmail.com)
# CREATED: 	Wed 26-Nov-2014
# LAST REVISED:	Wed 26-Nov-2014
#
##############
# DISCLAIMER #
##############
# Anyone is free to copy, modify, use, or distribute this script for any purpose, and by any means. However, Please take care THIS IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND AND YOU SHOULD USE IT AT YOUR OWN RISK.

import ConfigParser
import sys,os.path
from Get_toggl_events import Get_toggl_events
from Gcal_create_event import Gcal_create_event

class Toggl_to_Gcal:

	def __init__(self):
	
		# Get day
		self.day=sys.argv[1]

		# Import configuration	
		dir_name=os.path.dirname(os.path.realpath(__file__))
		conf_file=os.path.join(dir_name,"settings.conf")
		
		config = ConfigParser.ConfigParser()
		file=config.read(conf_file)

		if not file:
			print "ERROR: unable to read settings.conf file, Please run: \"python setup.py\" to fix issue"
			sys.exit(1)
		
		if not config.has_section("Gcal"):
			print "ERROR: Gcal settings section misssing from settings.conf file, Please run: \"python setup.py\" to fix issue" 
			sys.exit(1)

		if not config.has_section("Toggl"):
			print "ERROR: Toggl settings section misssing from settings.conf file, Please run: \"python setup.py\" to fix issue" 
			sys.exit(1)

		calendar_address=self.get_option(config,'Gcal','calendar_address')
		#client_id=self.get_option(config,'Gcal','client_id')
		#client_secret=self.get_option(config,'Gcal','client_secret')
		client_id='449544381405-cvobene3kc8qbtt4t1e7vba1hqe13pd7.apps.googleusercontent.com'
		client_secret='f7OgS57kU6AfaxzUiK22sQ14'
		
		toggl_api_token=self.get_option(config,'Toggl','toggl_api_token')
		workspace_id=self.get_option(config,'Toggl','workspace_id')
		
		# Get the list of events from Toggl
		events=Get_toggl_events(toggl_api_token,workspace_id,self.day).events

		#print events[1]['start']
		#print events[1]['end']
		#print events[1]['project']
		#print events[1]['description']
		

		# Create the events on Gcal

		cal=Gcal_create_event(calendar_address,client_id,client_secret)

		for event in events:

			color=""
			if config.has_section("Color_mapping"):
				if config.has_option("Color_mapping",event['project']):
					color=config.get("Color_mapping",event['project']).lstrip('"').rstrip('"').lstrip('\'').rstrip('\'') 

			print "Creating event \""+event['description']+" | "+event['project']+"\""+" from "+event['start']+" until "+event['end']
			cal.create_event(summary=event['description']+" | "+event['project'],start_time=event['start'],end_time=event['end'],colorId=color)

	def get_option(self,config,section,option):
		if config.has_option(section,option):
			value=config.get(section,option).lstrip('"').rstrip('"').lstrip('\'').rstrip('\'')	
			if value == "" or value is None:
				print "ERROR: \""+option+"\" value is missing from the settings.conf file, Please run: \"python setup.py\" to fix issue"
				sys.exit(1)
			else:
				return value
		else:
			print "ERROR: \""+option+"\" value is missing from the settings.conf file, Please run: \"python setup.py\" to fix issue"
			sys.exit(1)


if __name__ == '__main__':
	obj=Toggl_to_Gcal()

