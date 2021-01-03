def get_int_values(n)
  n.times.map.with_index { |n|
    print "Enter value ##{ 1 + n }: "
    gets.chomp.to_i 
  }
end

puts "[a]dd, [s]ubstract, [m]ultiply, [d]ivde?"
response = gets.chomp

puts "몇개의 값을 계산하려고 하시나요?(숫자만 입력하세요)"
num_of_values = gets.to_i

case response.downcase
when 'a'
  puts "더하려고 하는 값을 차례로 입력하세요"
  operator = :+

when 's'
  puts "빼려고 하는 값을 차례로 입력하세요"
  operator = :-

when 'm'
  puts "곱하려는 값을 차례로 입력하세요"
  operator = :*

when 'd'
  puts "나누려는 값을 차례로 입력하세요"
  operator = :/

end

answer = get_int_values(num_of_values).inject(operator)
puts "결과값: #{ answer }"
