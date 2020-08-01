require_relative 'merkle_tree'
require_relative 'block_v1'

b0 = Block::BlockV1.genesis_block(
  { from: "Leonardo", to: "Xiaomi", msg: "Xiaomi Redmi 8", price: 560, quantity: 1 },
  { from: "Leonardo", to: "D1", msg: "Gomitas", price: 1.3, quantity: 4 },
  { from: "Karen", to: "D1", msg: "Leche Latti", price: 2.3, quantity: 12 },
)

b1 = Block::BlockV1.next_block(b0,
  { from: "Leonardo", to: "Restaurante La 80", msg: "Mongondo", price: 12, quantity: 1 },
  { from: "Leonardo & Karen", to: "Restaurante La 80", msg: "Ejecutivo", price: 7.5, quantity: 3 },
  { from: "Leonardo", to: "Taurent Computadores", msg: "Pantalla Samsung 22\"", price: 283, quantity: 1 },
)

b2 = Block::BlockV1.next_block(b1, 
  { from: "Leonardo", to: "Brazilia", msg: "Tiquete MED - SNJ", price: 140, quantity: 2 },
)

blockchain = [b0, b1, b2]
hashes = blockchain.map { |block| block.hash }
merkle_tree = Merkle::MerkleTree.new(hashes)

pp blockchain
puts '--' * 20
puts 'Merkle Tree hash: ' + (merkle_tree.merkle_hash).to_s
