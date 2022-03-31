import datetime
import hashlib
import time
import os
import pathlib
import random
import string
from random import randint

iter=1
hashin = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
hashout = hashlib.sha256(hashin.encode()).hexdigest()


def datastream(): 
# This can be used to allow any input, I have used 10 random integers to demonstrate
	v1 = int(randint(1200, 1500))
	v2 = int(randint(1300, 1700))
	v3 = int(randint(1100, 1500))
	v4 = int(randint(4000, 5600))
	v5 = int(randint(4000, 5600))
	v6 = int(randint(1900, 2400))
	v7 = int(randint(1920, 2300))
	v8 = int(randint(1850, 2200))
	v9 = int(randint(1900, 2300))
	v10 = int(randint(1800, 2200))
	return [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10];   
 
 
class Block:
	blockNo = 0
	count = iter
	data = None
	next = None
	hash = "None"
	previous_hash = "None"
	timestamp = datetime.datetime.now()

	def __init__(self, data):
		self.data = datastream()

	def hash(self):
	#start of device token check
		file = pathlib.Path("TToken")
		if file.exists():
			tier=open("TToken").readline().rstrip()
		else:
			with open("benchmark.py") as infile:
				exec(infile.read())
			tier=open("TToken").readline().rstrip()
		if tier=="T1":
			h = hashlib.md5()
		elif tier=="T2":
			h = hashlib.sha1()
		elif tier=="T3":
			h = hashlib.blake2s()
		elif tier=="T4":
			h = hashlib.sha3_256()
	#end of device token check
		h.update(
		str(self.nonce).encode('utf-8') +
		str(self.data).encode('utf-8') +
		str(self.previous_hash).encode('utf-8') +
		str(self.timestamp).encode('utf-8') +
		str(self.blockNo).encode('utf-8')
		)
		return h.hexdigest()

	def __str__(self):
		return "Block Number: " + str(self.blockNo) + "\nHistory Count: " + str(self.count) + "\nBlock Data: " + str(self.data) + "\nBlock Hash: " + str(self.hash) + "\nPrevious Hash: " + str(self.previous_hash) + "\n--------------"

class Blockchain:
	block = Block("Genesis")
	dummy = head = block

	def add(self, block):
		if (self.block.blockNo ==0):
			block.previous_hash =  "Origin"
		else:
			block.previous_hash = self.block.hash
		block.blockNo = self.block.blockNo + 1

		self.block.next = block
		self.block = self.block.next

	def mine(self, block):
		global iter
		global hashin
		global hashout
		delay = 18
		cont = 1
		while(cont == 1):
			if int(iter%(2**delay) == 0):
				block.count = iter
				block.hash = hashout
				self.add(block)
				print(block)
				iter += 1
				hashin=hashout
				hashout = hashlib.sha256(hashin.encode()).hexdigest()
				cont = 0
				break
			else:
				iter += 1
				hashin=hashout
				hashout = hashlib.sha256(hashin.encode()).hexdigest()
t_initial = time.perf_counter()
blockchain = Blockchain()
b=int(input('Enter the number of Blocks for this simulation:'))

for n in range(b):
	blockchain.mine(Block(n+1))
t_final = time.perf_counter()
delta_t = t_final - t_initial
delta_unit = delta_t*1000/b
print("Computation Time per Block(ms):"+str(delta_unit))
input('Press ENTER to exit')