require 'digest'

def proof_of_work(prev, data, difficulty)
  nonce = 0
  time = Time.now.to_i
  loop do
    hash = Digest::SHA256.hexdigest("#{nonce}#{time}#{difficulty}#{prev}#{data}")
    if hash.start_with?(difficulty)
      return [nonce, hash]
    else
      nonce += 1
    end
  end
end

hash = '0000000000000000000000000000000000000000000000000000000000000000'
(1..7).each do |factor|
  difficulty = '0' * factor
  puts "Difficulty: #{difficulty} (#{difficulty.length * 4} bits)"

  puts 'Starting search...'
  t_o = Time.now
  nonce, hash = proof_of_work(hash, 'Leonardo', difficulty)
  t_e = Time.now

  delta = t_e - t_o
  puts "Elapset Time: %.4f seconds - Hashes Calculated: %d" % [delta, nonce]

  if delta > 0
    hashrate = Float(nonce/delta)
    puts "Hash Rate: %d hashes per second" % hashrate
  end
  puts '-' * 10
end 


