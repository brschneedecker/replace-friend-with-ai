# Jabber message class and associated functions

import datetime

class JabberMessage:

	def __init__(self, msg_id:str, msg_sender:str, timestamp:datetime.datetime, msg_text):
		self.msg_id = msg_id
		self.msg_sender = msg_sender
		self.timestamp = timestamp
		self.msg_text = msg_text

	def __str__(self):
		return "{} ({}): {}".format(self.msg_sender, self.timestamp, self.msg_text)

if __name__ == "__main__":
	current_time = datetime.datetime.now()
	test_msg = JabberMessage("msg_id_0000", "Captain Fartz", current_time, "Hello!")
	print(test_msg)