import datetime
import hashlib
import pathlib
import time
from random import randint

def fun(): 
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
	data = None
	next = None
	hash = None
	nonce = 0
	previous_hash = 0x0
	timestamp = datetime.datetime.now()

	def __init__(self, data):
		self.data = fun()

	def hash1(self):
		h1 = hashlib.sha256()
		h1.update(
		str(self.nonce).encode('utf-8') +
		str(self.data).encode('utf-8') +
		str(self.previous_hash).encode('utf-8') +
		str(self.timestamp).encode('utf-8') +
		str(self.blockNo).encode('utf-8')
		)
		return h1.hexdigest()

	def hash2(self):
		h2 = hashlib.sha256()
		h2.update(
		str(self.hash1()).encode('utf-8')
		)
		return h2.hexdigest()


	def __str__(self):
		return "Block Number: " + str(self.blockNo) + "\nNonce: " + str(self.nonce) + "\nBlock Data: " + str(self.data) + "\nBlock Hash: " + str(self.hash2()) + "\nPrevious Hash: " + str(self.previous_hash) + "\n--------------"

class Blockchain:

	diff = 18
	maxNonce = 2**32
	target = 2 ** (256-diff)

	block = Block("Genesis")
	dummy = head = block

	def add(self, block):

		block.previous_hash = self.block.hash2()
		block.blockNo = self.block.blockNo + 1

		self.block.next = block
		self.block = self.block.next

	def mine(self, block):
		for n in range(self.maxNonce):
			if int(block.hash2(), 16) <= self.target:
				self.add(block)
				print(block)
				break
			else:
				block.nonce += 1

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