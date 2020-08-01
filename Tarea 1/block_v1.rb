module Block
  require 'digest'
  require 'pp'

  class BlockV1
    attr_reader :version
    attr_reader :index
    attr_reader :timestamp
    attr_reader :transactions
    attr_reader :transactions_counter
    attr_reader :previous_hash
    attr_reader :hash
    attr_reader :difficulty

    def initialize(index, transactions, previous_hash, difficulty = '00000', version = '1')
      @version = version
      @index = index
      @transactions = transactions
      @transactions_counter = transactions.size
      @previous_hash = previous_hash
      @difficulty = difficulty  # Modify to compact binary format
      @nonce, @timestamp, @human_time = proof_of_work(difficulty)
    end

    def self.genesis_block(*transactions)
      self.new(0, transactions, '0000000000000000000000000000000000000000000000000000000000000000')
    end
      
    def self.next_block(previous_hash, *transactions)
      self.new(previous_hash.index + 1, transactions, previous_hash.hash)
    end

    def proof_of_work(difficulty)
      nonce = 0
      timestamp = Time.now.to_i
      loop do
        hash = calculate_hash(nonce, timestamp)
        if hash.start_with?(difficulty)
          @hash = hash
          return [nonce, timestamp, Time.at(timestamp)]
        else
          nonce += 1
        end
      end
    end

    def calculate_hash(nonce, timestamp)
      sha256 = Digest::SHA256.new
      sha256.update(@index.to_s +
                    nonce.to_s + 
                    timestamp.to_s + 
                    @difficulty + 
                    @previous_hash +
                    @transactions.to_s + 
                    @transactions_counter.to_s)
      sha256.hexdigest
    end
  end
end
