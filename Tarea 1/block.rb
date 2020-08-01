require 'digest'
require 'pp'

class Block
  attr_reader :data
  attr_reader :prev
  attr_reader :difficulty
  attr_reader :time
  attr_reader :nonce

  def initialize(data, prev, difficulty = '0000')
    @data = data
    @prev = prev
    @difficulty = difficulty
    @nonce, @time = proof_of_work(difficulty)
  end

  def hash
    Digest::SHA256.hexdigest("#{nonce}#{time}#{difficulty}#{prev}#{data}")
  end

  def proof_of_work(diff='00')
    nonce = 0
    time = Time.now.to_i
    loop do
      hash = Digest::SHA256.hexdigest("#{nonce}#{time}#{diff}#{prev}#{data}")
      if hash.start_with?(diff)
        return [nonce, time]
      else
        nonce += 1
      end
    end
  end
end

b0 = Block.new('Genesis', '0000000000000000000000000000000000000000000000000000000000000000')
b1 = Block.new('Leonardo', b0.hash)
b2 = Block.new('Karen', b1.hash)
b3 = Block.new('Hai', b2.hash)


blockchain = [b0, b1, b2, b3]

pp blockchain
# pp b0
# puts '===' * 10
# pp b1
# puts '===' * 10
# pp b2
# puts '===' * 10
# pp b3
# puts '===' * 10