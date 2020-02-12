import hashlib
import time
from datetime import datetime
from pprint import pprint as pp


class Block():
  def __init__(self, index, transactions, previous_hash, difficulty):
    self.index = index
    self.transactions = transactions
    self.transactions_count = len(transactions)
    self.previous_hash = previous_hash
    self.difficulty = difficulty
    self.nonce, self.timestamp, self.found_date = self._proof_of_work()

    self.block = self._block()

  def _calc_hash(self, nonce, timestamp):
    sha = hashlib.sha256()
    sha.update(
      str(self.index).encode() +
      str(nonce).encode() +
      str(timestamp).encode() + 
      str(self.transactions).encode() +
      str(self.transactions_count).encode() +
      str(self.previous_hash).encode()
    )

    return sha.hexdigest()

  def _proof_of_work(self):
    nonce = 0
    timestamp = datetime.now().timestamp()

    while(True):
      hash_value = self._calc_hash(nonce, timestamp)
      if str(hash_value).startswith(self.difficulty):
        self.hash = hash_value

        return [nonce, timestamp, datetime.now().strftime("%B %d, %Y - %H:%M:%S")]
      else:
        nonce += 1

  def _block(self):
    header = { 'prev_hash': self.previous_hash, 'nonce': self.nonce }
    body = { 'total_ttxs': self.transactions_count, 'ttxs': self.transactions }
    return { 'header': header, 'body': body }

  def _to_show(self):
    return { 
      'hash': self.hash, 
      'block': self.block, 
      'index': self.index, 
      'found_date': self.found_date,
      'timestamp': self.timestamp }

  def genesis(transactions, difficulty):
    block_created = Block(0, transactions, '00000000000000000000000000000000000000000000000000000000000000', difficulty)
    return block_created._to_show()

  def new_block(previous_block, transactions, difficulty):
    block_created = Block(previous_block['index'] + 1, transactions, previous_block['hash'], difficulty)
    return block_created._to_show()
