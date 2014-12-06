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

import requests
import csv
import json
import sys
import datetime
 
class  Get_toggl_events:

	#def usage(self):
	#	print "USAGE: "+sys.argv[0]+" toggl_api_token workspace_id day"
	#	print "TIME FORMAT: %d-%b-%Y, e.g. 02-Aug-2014"

	def __init__(self,toggl_api_token,workspace_id,day):
		
		# Variables and input validation

		self.date_fmt="%d-%b-%Y"
		self.day=datetime.datetime.strptime(day,"%d-%b-%Y")

		self.start=self.day.strftime("%Y-%m-%d")
		#self.end=(self.day + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

		# Fetch date from toggl
		r = requests.get('https://toggl.com/reports/api/v2/details?workspace_id='+workspace_id+'&since='+self.start+'&until='+self.start+'&user_agent=get_report',
                 auth=(toggl_api_token, 'api_token'))
		data = r.json()
		self.events=data['data']

		# Write data to out file
		#keys=data['data'][0].keys()
		

		#f = csv.writer(self.out_file)
		#f.writerow(keys) 
		#for item in data['data']:
		#	f.writerow(item.values())


#if __name__ == '__main__':
#    obj=Get_toggl_report()
