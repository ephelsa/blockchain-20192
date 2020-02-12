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
    

blockchain = Blockchain('0000')

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

'''
Output:

[
   {
      "block":{
         "body":{
            "total_ttxs":3,
            "ttxs":[
               {
                  "from":"Karen",
                  "msg":"Estas en la U?",
                  "to":"Leonardo"
               },
               {
                  "from":"Leonardo",
                  "msg":"Si",
                  "to":"Karen"
               },
               {
                  "from":"Karen",
                  "msg":"Ah bueno",
                  "to":"Leonardo"
               }
            ]
         },
         "header":{
            "nonce":60751,
            "prev_hash":"00000000000000000000000000000000000000000000000000000000000000"
         }
      },
      "difficulty":4,
      "found_date":"February 12, 2020 - 17:35:27",
      "hash":"0000e45f2492d1448995325367e94769c05fd63d74edc5d875ee81828ce67a3d",
      "index":0,
      "timestamp":1581546927.035349
   },
   {
      "block":{
         "body":{
            "total_ttxs":1,
            "ttxs":[
               {
                  "from":"Ping",
                  "msg":"Socket test!",
                  "to":"Pong"
               }
            ]
         },
         "header":{
            "nonce":6840,
            "prev_hash":"0000e45f2492d1448995325367e94769c05fd63d74edc5d875ee81828ce67a3d"
         }
      },
      "difficulty":4,
      "found_date":"February 12, 2020 - 17:35:27",
      "hash":"00001c385d3c4c9f59b4d627ed98fe0a1b2605a75f81bfbd14325af77e45be2f",
      "index":1,
      "timestamp":1581546927.396931
   },
   {
      "block":{
         "body":{
            "total_ttxs":3,
            "ttxs":[
               {
                  "from":"Leonardo",
                  "msg":"Ya llegaste?",
                  "to":"Karen"
               },
               {
                  "from":"Karen",
                  "msg":"Hace 40 min",
                  "to":"Leonardo"
               },
               {
                  "from":"Leonardo",
                  "msg":"Nice. Como te fue?",
                  "to":"Karen"
               }
            ]
         },
         "header":{
            "nonce":17700,
            "prev_hash":"00001c385d3c4c9f59b4d627ed98fe0a1b2605a75f81bfbd14325af77e45be2f"
         }
      },
      "difficulty":4,
      "found_date":"February 12, 2020 - 17:35:27",
      "hash":"0000f884aa35245a036a7587af9593d0f4d49fe1b0524ea0261a5f9dd294f9e7",
      "index":2,
      "timestamp":1581546927.425708
   }
]

'''