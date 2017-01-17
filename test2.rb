
a = ARGV[0].to_i
k = ARGV[1].to_i
n = Array(ARGV[2].to_I)
p n
count = 0

comb =  n.repeated_combination(2).to_a
x = comb.size

