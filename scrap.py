#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import requests
from bs4 import BeautifulSoup
from smtplib import *
from datetime import datetime, timedelta
import time

def send_mail(fromaddr,password,toaddr,subject,body):
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = subject
	 
	body = body
	msg.attach(MIMEText(body, 'plain'))
	try:
	    	server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, password)
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		print "Mail send"
	except SMTPException:
	    	print('Error')

def webScrapping():
	page = requests.get("https://sfbay.craigslist.org/")
	#print page
	#print page.content
	soup = BeautifulSoup(page.content, 'html.parser')
	[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
	visible_text = soup.getText()
	#print visible_text
	search_text = "portable washing machine"
	#search_text = "outdoor"
	index = visible_text.find(search_text)
        fromaddr = "your_mail_address@gmail.com"
	password = "your_password"
	toaddr = "receiver_mail_address@gmail.com"
	if index==-1:
		print "Not Found"
		subject = "Not Found"
		body = "Sorry!!! Your searching keyword "+search_text+" has not been found"
		send_mail(fromaddr,password,toaddr,subject,body)
	
	else:
		print search_text +" Found"
		subject = "Found"
		body = "Congratulations!!! Your searching keyword "+search_text+" has been found"
		send_mail(fromaddr,password,toaddr,subject,body)

while True:
    #Call web scrapping method to check the page has portable washing machine text has or not and send mail every one hour
    webScrapping()

    #dt = datetime.now() + timedelta(seconds=20) #its check the web page every 20 seconds and send mail
    #dt = datetime.now() + timedelta(minutes=1) #its check the web page every 1 minutess and send mail
    dt = datetime.now() + timedelta(hours=1) #its check the web page every 1 hours and send mail
    print dt 
    while datetime.now() < dt:
        time.sleep(1)
