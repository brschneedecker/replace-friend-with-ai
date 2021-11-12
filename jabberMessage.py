# Jabber message class and associated functions

import datetime
from bs4 import BeautifulSoup
import glob

class JabberMessage:

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
	Given and HTML file, parse contents and return a list of message objects
	"""

	html_file = open(filepath, "r")
	index = html_file.read()

	soup = BeautifulSoup(index, 'html.parser')

	for message in soup.find_all('div'):
		message_text = message.text.strip()

		if message_text:
			yield JabberMessage(None, None, None, message_text)

def parse_all_html_files(directory:str):
	"""
	Given a directory, search for all HTML files and parse them, returning a 
	list of message objects
	"""
	messages = []

	for html_file in glob.glob("{}/*.html".format(directory)):
		for message in parse_html_file(html_file):
			messages.append(message)

	return messages

if __name__ == "__main__":
	current_time = datetime.datetime.now()
	test_msg = JabberMessage("msg_id_0000", "Captain Fartz", current_time, "Hello!")
	print(test_msg)