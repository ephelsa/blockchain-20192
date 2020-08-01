module Merkle
  require 'digest'
  require 'pp'

  class MerkleTree
    attr_reader :merkle_hash

    def initialize(hashes)
      @merkle_hash = compute_merkle_tree_hash(hashes)
    end

    def calculate_hash(data)
      sha = Digest::SHA256.new
      sha.update(data)
      sha.hexdigest
    end

    def compute_merkle_tree_hash(hashes)
      if hashes.empty?
        return '0'
      elsif hashes.size == 1
        return hashes[0]
      else
        while hashes.size > 1
          hashes << hashes[-1] if hashes.size % 2 != 0
          new_hashes = []
          hashes.each_slice(2) do |slice|
            hash = calculate_hash(slice[0] + slice[1])
            new_hashes << hash
          end
          hashes = new_hashes
        end
        hashes[0]
      end
    end
  end
end
