import datetime
import hashlib
from flask import Flask, request, render_template

class Block:
	blockNo = 0
	data = None
	next = None
	hash = None
	nonce = 0
	previous_hash = 0*0
	timestamp = datetime.datetime.now()
	
	def __init__(self, data, name):
		self.data = data
		self.blockName = name
		
	def hash(self):
		h = hashlib.sha256()
		h.update(
		str(self.nonce).encode('utf8')+
		str(self.data).encode('utf8')+
		str(self.previous_hash).encode('utf8')+
		str(self.timestamp).encode('utf8')+
		str(self.blockName).encode('utf8'))
		
		return h.hexdigest()
		
	def __str__(self):
		return "Block Hash: " + str(self.hash()) + "\nBlockName: " + str(self.blockName)+ "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

# This is Demo code. For Full Project Code Please Mail at vatshayan007@gmail.com 
# For Project : vatshayan007@gmail.com 
