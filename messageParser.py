import datetime
import re
import glob
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET
import re


class Message:
	'''
	Chat message object
	'''

	def __init__(self, msg_id:str, msg_sender:str, timestamp:datetime.datetime, msg_text):
		self.msg_id = msg_id
		self.msg_sender = msg_sender
		self.timestamp = timestamp
		self.msg_text = msg_text

	def __str__(self):
		return "{} ({}): {}".format(self.msg_sender, self.timestamp, self.msg_text)

	def get_msg_text(self):
		return self.msg_text
	

def parse_html_file(filepath:str):
	"""
	Given an HTML file, parse contents and return a list of message objects

	Args:
	  - filepath: path to the HTML file to parse

	Returns:
	  - Yields Message objects with text parsed from the input data.
	"""

	html_file = open(filepath, "r")
	index = html_file.read()

	soup = BeautifulSoup(index, 'html.parser')

	for message in soup.find_all('div'):
		message_text = message.text.strip()

		if message_text:
			yield Message(None, None, None, message_text)


def parse_xml_file(filepath:str, my_name:str, buddy_name:str, buddy_number:str):
	'''
	Parses XML backups for SMS text messages exported from Android

	Args:
	  - filepath: Location of XML files
	  - my_name: Name of person running the app
	  - buddy_name: Name of the friend app-runner texted with
	  - buddy_number: Phone number of the friend app-runner texted with
	'''

	parser = ET.iterparse(filepath)

	# Traverse XML
	for event, element in parser:
		# Filter to SMS messages (no group chats)
		if element.tag == 'sms':
			address = element.attrib['address']
			address = re.sub('[()-]', '', address)
			address = address.replace('+1','')
			address = address.replace(' ','')
	        
			# Filter to texts to/from friend
			if address == buddy_number:
				msg_type = element.attrib['type']
				date = element.attrib['date']
				readable_date = element.attrib['readable_date']
				message_text = element.attrib['body']

				if msg_type == '1':
					msg_sender = buddy_name
				elif msg_type == '2':
					msg_sender = my_name
				else:
					raise ValueError

				yield Message(None, msg_sender, readable_date, message_text)

		# then clean up
		element.clear()
			
			
def parse_all_html_files(directory:str):
	"""
	Given a directory, search for all HTML files and parse them
	"""
	for html_file in glob.glob("{}/*.html".format(directory)):
		for message in parse_html_file(html_file):
			yield message


def parse_all_xml_files(directory:str, my_name:str, buddy_name:str, buddy_number:str):
	"""
	Given a directory, search for all XML files and parse them
	"""
	for xml_file in glob.glob("{}/*.xml".format(directory)):
		for message in parse_xml_file(xml_file, my_name, buddy_name, buddy_number):
			yield message