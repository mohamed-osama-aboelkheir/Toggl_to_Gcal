#! /usr/bin/python
#
# DESCRIPTION:	
# AUTHOR: 	Mohamed Osama (mohamed.osama.aboelkheir@gmail.com)
# CREATED: 	Sat 02-Aug-2014
# LAST REVISED:	Sat 02-Aug-2014
#
##############
# DISCLAIMER #
##############
# Anyone is free to copy, modify, use, or distribute this script for any purpose, and by any means. However, Please take care THIS IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND AND YOU SHOULD USE IT AT YOUR OWN RISK.

import gflags
import httplib2

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run
import os.path

FLAGS = gflags.FLAGS


#############
# OPTIONS	#
#############


class Gcal_create_event:
	
	def __init__(self,calendar_address,client_id,client_secret):

		self.calendar_address=calendar_address
		self.client_id=client_id
		self.client_secret=client_secret
		
		# Set up a Flow object to be used if we need to authenticate. This
		# sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
		# the information it needs to authenticate. Note that it is called
		# the Web Server Flow, but it can also handle the flow for native
		# applications
		# The client_id and client_secret can be found in Google Developers Console
		FLOW = OAuth2WebServerFlow(
		    client_id=self.client_id,
		    client_secret=self.client_secret,
		    scope='https://www.googleapis.com/auth/calendar',
		    user_agent='Toggl_to_gcal/1.0')
		
		# To disable the local server feature, uncomment the following line:
		# FLAGS.auth_local_webserver = False
		
		# If the Credentials don't exist or are invalid, run through the native client
		# flow. The Storage object will ensure that if successful the good
		# Credentials will get written back to a file.
		#storage = Storage('calendar.dat')
		dir_name=os.path.dirname(os.path.realpath(__file__))
		storage=Storage(os.path.join(dir_name,"calendar.dat"))
		credentials = storage.get()
		if credentials is None or credentials.invalid == True:
		  credentials = run(FLOW, storage)
		
		# Create an httplib2.Http object to handle our HTTP requests and authorize it
		# with our good Credentials.
		http = httplib2.Http()
		http = credentials.authorize(http)
		
		# Build a service object for interacting with the API. Visit
		# the Google Developers Console
		# to get a developerKey for your own application.
		#self.service = build(serviceName='calendar', version='v3', http=http,developerKey='TOGGL_TO_GCAL')
		self.service = build(serviceName='calendar', version='v3', http=http)
		       #developerKey='Toggl_to_Gcal')
		       #developerKey='YOUR_DEVELOPER_KEY')
		
		#summary='Toggl_to_Gcal test 3'
		
		#1 ->  blue
		#2 ->  cyan
		#3 ->  purple
		#4 ->  red
		#5 ->  yellow
		#6 ->  orange
		#7 ->  turquoise
		#8 ->  grey
		#9 ->  bold blue
		#10 -> bold green
		#11 -> bold red
		
		#color = 8

	def create_event(self,summary,start_time,end_time,colorId):
		
		if colorId != "":
			event = {
			  'summary': summary,
			  #'location': 'Somewhere',
			  'start': {
			    #'dateTime': '2014-11-26T01:00:00.000-07:00',
			    'dateTime': start_time,
			    #'timeZone': 'Africa/Cairo'
			  },
			  'end': {
			    #'dateTime': '2014-11-26T02:00:00.000-07:00',
			    'dateTime': end_time,
			    #'timeZone': 'Africa/Cairo'
			  },
			  'colorId' : colorId
			  #'recurrence': [
			  #  'RRULE:FREQ=WEEKLY;UNTIL=20110701T100000-07:00',
			  #],
			  #'attendees': [
			  #  {
			  #    'email': 'attendeeEmail',
			  #    # Other attendee's data...
			  #  },
			  #  # ...
			  #],
			}
		else:
			event = {
			  'summary': summary,
			  #'location': 'Somewhere',
			  'start': {
			    #'dateTime': '2014-11-26T01:00:00.000-07:00',
			    'dateTime': start_time,
			    #'timeZone': 'Africa/Cairo'
			  },
			  'end': {
			    #'dateTime': '2014-11-26T02:00:00.000-07:00',
			    'dateTime': end_time,
			    #'timeZone': 'Africa/Cairo'
			  },
			  #'recurrence': [
			  #  'RRULE:FREQ=WEEKLY;UNTIL=20110701T100000-07:00',
			  #],
			  #'attendees': [
			  #  {
			  #    'email': 'attendeeEmail',
			  #    # Other attendee's data...
			  #  },
			  #  # ...
			  #],
			}
		event = self.service.events().insert(calendarId=self.calendar_address, body=event).execute()
		
		#print event['id']
