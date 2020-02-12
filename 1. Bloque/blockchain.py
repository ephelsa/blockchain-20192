from block import Block
from pprint import pprint as pp

class Blockchain():
  def __init__(self, difficulty='0000'):
    self.total_blocks = 0
    self.difficulty = difficulty
    self.blocks = []

  def new_block(self, ttxs):
    if self.total_blocks == 0:
      block = Block.genesis(ttxs, difficulty=self.difficulty)
    else:
      block = Block.new_block(self.previous_block, ttxs, difficulty=self.difficulty)

    self.total_blocks += 1
    self.previous_block = block
    self.blocks.append(block)

    return block
    

blockchain = Blockchain('00')

b0 = blockchain.new_block([
  { 'from': 'Karen', 'to': 'Leonardo', 'msg': 'Estas en la U?' },
  { 'from': 'Leonardo', 'to': 'Karen', 'msg': 'Si' },
  { 'from': 'Karen', 'to': 'Leonardo', 'msg': 'Ah bueno' }
])

b1 = blockchain.new_block([
  { 'from': 'Ping', 'to': 'Pong', 'msg': 'Socket test!' }
])

b2 = blockchain.new_block([
  { 'from': 'Leonardo', 'to': 'Karen', 'msg': 'Ya llegaste?' },
  { 'from': 'Karen', 'to': 'Leonardo', 'msg': 'Hace 40 min' },
  { 'from': 'Leonardo', 'to': 'Karen', 'msg': 'Nice. Como te fue?' },
])



pp(blockchain.blocks)