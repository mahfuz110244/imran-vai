#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
from smtplib import *
import time
import pandas as pd

data = {
    'Bar Number' : [],
    'Address' : [],
    'Phone Number' : [],
    'Fax Number' : [],
    'e-mail' : [],
	'County' : [],
	'Undergraduate School' : [],
	'District' : [],
	'Effective Date': [],
	'Status Change' : []
	}
count = 310000;
while count!=312000:
# while count!=999999:
	# print count
	page = requests.get("http://members.calbar.ca.gov/fal/Member/Detail/"+str(count))
	#print page
	#print page.content
	soup = BeautifulSoup(page.content, 'html.parser')
	[s.extract() for s in soup([ 'script', '[document]', 'head', 'title'])]
	visible_text = soup.getText()
	if visible_text.find("Active")!=-1:
		# print "active"
		# print visible_text
		table = soup.find("table", { "class" : "tblMemberDetail"})
		all_col = soup.findAll('td')
		i = 0
		if len(all_col)==34:
			data['Bar Number'].append( all_col[1].getText().strip() )
			data['Address'].append( all_col[5].getText().strip() )
			data['Phone Number'].append( all_col[7].getText().strip() )
			data['Fax Number'].append( all_col[9].getText().strip() )

			all_style = unicode(soup.findAll('style'))
			# print all_style
			style = all_style.split('#')
			id = ''
			for s in style:
				if "inline" in s:
					email_id = s.split('{')[0]

			# print email_id
			email_span = soup.findAll(id=email_id)
			# print email_span
			if email_span:
				email = soup.select('span#'+email_id)[0].text
			else:
				email = all_col[11].getText().strip()
			# email = soup.select('span#'+email_id)[0].text
			# email = soup.find_all("span", {"id": email_id})[0].text.strip()
			# print email
			data['e-mail'].append( email)
			data['County'].append( all_col[13].getText().strip() )
			data['Undergraduate School'].append( all_col[15].getText().strip() )
			data['District'].append( all_col[17].getText().strip() )
			data['Effective Date'].append( all_col[28].getText().strip() )
			data['Status Change'].append( all_col[29].getText().strip() )
			# print data
	count = count+1
docData = pd.DataFrame( data )
docData.to_excel("bar_data_310000_312000.xlsx")
print "complete"