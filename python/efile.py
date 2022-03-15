# def longest_Common_Prefix(str1):

#   if not str1:
#      return ""

# short_str = min(str1,key=len)

# for i, char in enumerate(short_str):
#   for other in str1:
#      if other[i] != char:
#         return short_str[:i]

# return short_str

# print(longest_Common_Prefix(["abcdefgh","abcefgh"]))
# print(longest_Common_Prefix(["w3r","w3resource"]))
#print(longest_Common_Prefix(["Python","PHP", "Perl"]))
#print(longest_Common_Prefix(["Python","PHP", "Java"]))

# def reverse_vowels(str1):
#	vowels = ""
#	for char in str1:
#		if char in "aeiouAEIOU":
#			vowels += char
#	result_string = ""
#	for char in str1:
#		if char in "aeiouAEIOU":
#			result_string += vowels[-1]
#			vowels = vowels[:-1]
#		else:
#			result_string += char
#	return result_string
# print(reverse_vowels("THOMAS"))
# print(reverse_vowels("Python"))
# print(reverse_vowels("HINT"))
# print(reverse_vowels("KENYA"))

# def is_Palindrome(n):
#   return str(n) == str(n)[::-1]
# print(is_Palindrome(100))
# print(is_Palindrome(252))
# print(is_Palindrome(-838))

# def is_Palindrome(n):
#   return str(n) == str(n)[::-1]
# print(is_Palindrome(100))
# print(is_Palindrome(252))
# print(is_Palindrome(-838))

# def remove_duplicates(nums):
#   for i in range (len(nums)-1, 0, -1):
#      if nums[i] == nums[i-1]:
#         del nums[i-1]
# return len(nums)

# print(remove_duplicates([0,0,1,1,2,2,3,3,4,4,4]))
#print(remove_duplicates([1, 2, 2, 3, 4, 4]))

# def buy_and_sell(stock_price):
#   max_profit_val, current_max_val = 0, 0
#  for price in reversed(stock_price):
#     current_max_val = max(current_max_val, price)
#    potential_profit = current_max_val - price
#   max_profit_val = max(potential_profit, max_profit_val)

# return max_profit_val

#print(buy_and_sell([8, 10, 7, 5, 7, 15]))
#print(buy_and_sell([1, 2, 8, 1]))
# print(buy_and_sell([]))

# def remove_element(array_nums, val):
#   i = 0
#  while i < len(array_nums):
#     if array_nums[i] == val:
#        array_nums.remove(array_nums[i])

#   else:
#      i += 1

# return len(array_nums)
#print(remove_element([1, 2, 3, 4, 5, 6, 7, 5], 5))
#print(remove_element([10,10,10,10,10], 10))
#print(remove_element([10,10,10,10,10], 20))
#print(remove_element([], 1))

# def search_Range(array_nums, target_val):
# result_arra = []
# start_pos = 0
#end_pos = 0
# for i in range(len(array_nums)):
#   if target_val == array_nums[i] and start_pos == -1:
#      start_pos = i
#     end_pos = i
# elif target_val == array_nums[i] and start_pos != -1:
#    end_pos = i
# result_arra.append(start_pos)
# result_arra.append(end_pos)
# return result_arra
#print(search_Range([5, 7, 7, 8, 8, 8], 8))
#print(search_Range([1, 3, 6, 9, 13, 14], 4))
#print(search_Range([5, 7, 7, 8, 10], 8))


# def max_profit(stock_price):
#	max_profit_amt = 0

#	for i in range(len(stock_price)):
#		profit_amt = 0
#		for j in range(i+1, len(stock_price)):
#			profit_amt = stock_price[j] - stock_price[i]
#			if  profit_amt > max_profit_amt:
#				max_profit_amt = profit_amt
#	return max_profit_amt
#print(max_profit([224, 236, 247, 258, 259, 225]))

# def print_matrix(nums):
#   flag = True

#  for line in nums:

#     if flag == True:
#        i = 0
#       while i < len(line):
#          print(line[i])
#         i += 1
#    flag = False

# else:
#   i = -1
#  while i > -1 * len(line) - 1:
#     print(line[i])
#    i = i - 1
#flag = True
# print_matrix([[1, 2, 3, 4],
#             [5, 6, 7, 8],
#            [0, 6, 2, 8],
#           [2, 3, 0, 2]])

# def largest_product_of_three(nums):
# max_val = nums[1]

# for i in range(len(nums)):
#   for j in range(i+1, len(nums)):
#      for k in range(j+1, len(nums)):
#         max_val = max(nums[i] * nums[j] * nums[k], max_val)

# return max_val

#print(largest_product_of_three([-10, -20, 20, 1]))
#print(largest_product_of_three([-1, -1, 4, 2, 1]))
#print(largest_product_of_three([1, 2, 3, 4, 5, 6]))


# def first_missing_number(nums):
#   if len(nums) == 0:
#      return 1

# nums.sort()
#smallest_int_num = 0

# for i in range(len(nums) - 1):

#   if nums[i] <= 0 or nums[i] == nums[i + 1]:
#      continue
# else:
#    if nums[i + 1] - nums[i] != 1:
#       smallest_int_num = nums[i] + 1
#      return smallest_int_num
# if smallest_int_num == 0:
#   smallest_int_num = nums[-1] + 1
# return smallest_int_num

#print(first_missing_number([2, 3, 7, 6, 8, -1, -10, 15, 16]))
#print(first_missing_number([1, 2, 4, -7, 6, 8, 1, -10, 15]))
#print(first_missing_number([1, 2, 3, 4, 5, 6, 7]))
#print(first_missing_number([-2, -3, -1, 1, 2, 3]))

#import random
# print(random.sample([i for i in range(1,100) if i

#def cal_median(nums):
 # nums.sort()
  #n = len(nums)
  #m = n // 2
  #if n % 2 == 0:
   # return (nums[m - 1] + nums[m]) / 2
  #else:
   # return nums[m]
#print(cal_median([1,2,3,4,5]))
#print(cal_median([1,2,3,4,5,6]))
#print(cal_median([6,1,2,4,5,3]))
#print(cal_median([1.0,2.11,3.3,4.2,5.22,6.55]))
#print(cal_median([1.0,2.11,3.3,4.2,5.22]))
#print(cal_median([2.0,12.11,22.3,24.12,55.22]))

#def is_symmetrical_num(n):
 # return str(n) == str(n)[::-1]
#print(is_symmetrical_num(121))
#print(is_symmetrical_num(0))
#print(is_symmetrical_num(122))
#print(is_symmetrical_num(990099))

#def count_sum(nums):
 #   if not nums: return []
  #  return [len([n for n in nums if n < 0]), sum(n for n in nums if n > 0)]

#print(count_sum([1, 2, 3, 4, 5]))
#print(count_sum([-1, -2, -3, -4, -5]))
#print(count_sum([1, 2, 3, -4, -5]))
#print(count_sum([1, 2, -3, -4, -5])) 


#def check_isogram(str1):
 #   return len(str1) == len(set(str1.lower()))

#print(check_isogram("w3resource"))
#print(check_isogram("w3r"))
#print(check_isogram("Python"))
#print(check_isogram("Java"))


#def test_three_equal(x, y, z):
 # result= set([x, y, z])
  #if len(result)==3:
   # return 0
  #else:
   # return (4 - len(result))

#print(test_three_equal(1, 1, 1))
#print(test_three_equal(1, 2, 2))
#print(test_three_equal(-1, -2, -3))
#print(test_three_equal(-1, -1, -1))

#def is_valid_emp_code(emp_code):
 # return len(emp_code) in [8, 12] and emp_code.isdigit()
#print(is_valid_emp_code('12345678'))
#print(is_valid_emp_code('1234567j'))
#print(is_valid_emp_code('12345678j'))
#print(is_valid_emp_code('123456789123'))
#print(is_valid_emp_code('123456abcdef'))

#def string_letter_check(list_data):
 # return all([char in list_data[0].lower() for char in list_data[1].lower()])
#print(string_letter_check(["python", "ypth"]))
#print(string_letter_check(["python", "ypths"]))
#print(string_letter_check(["python", "ypthon"]))
#print(string_letter_check(["123456", "01234"]))
#print(string_letter_check(["123456", "1234"]))

#def sum_three_smallest_nums(lst):
#	return sum(sorted([x for x in lst if x > 0])[:3])

#print(sum_three_smallest_nums([10, 20, 30, 40, 50, 60, 7]))
#print(sum_three_smallest_nums([1, 2, 3, 4, 5]))
#print(sum_three_smallest_nums([0, 1, 2, 3, 4, 5]))

#def mask_string(str1):
 # return '*'*(len(str1)-5) + str1[-5:]

#print(mask_string("kdi39323swe"))
#print(mask_string("12345abcdef"))
#print(mask_string("12345")) 

#def num_of_args(*args):
#	return(len(args))
#print(num_of_args())
#print(num_of_args(1))
#print(num_of_args(1, 2))
#print(num_of_args(1, 2, 3))
#print(num_of_args(1, 2, 3, 4))
#print(num_of_args([1, 2, 3, 4]))

#def nums_cumulative_sum(nums_list):
 # return [sum(nums_list[:i+1]) for i in range(len(nums_list))]

#print(nums_cumulative_sum([10, 20, 30, 40, 50, 60, 7]))
#print(nums_cumulative_sum([1, 2, 3, 4, 5]))
#print(nums_cumulative_sum([0, 1, 2, 3, 4, 5]))

#def middle_char(txt):
#   return txt[(len(txt)-1)//2:(len(txt)+2)//2]
#print(middle_char("Python"))
#print(middle_char("PHP"))
#print(middle_char("Java"))

#def adjacent_num_product(list_nums):
 #   return max(a*b for a, b in zip(list_nums, list_nums[1:]))
#print(adjacent_num_product([1,2,3,4,5,6]))
#print(adjacent_num_product([1,2,3,4,5]))
#print(adjacent_num_product([2,3]))

#def odd_even_position(nums):
#	return all(nums[i]%2==i%2 for i in range(len(nums)))
#print(odd_even_position([2, 1, 4, 3, 6, 7, 6, 3]))
#print(odd_even_position([2, 1, 4, 3, 6, 7, 6, 4]))
#print(odd_even_position([4, 1, 2]))

#def is_narcissistic_num(num):
#	return num == sum([int(x) ** len(str(num)) for x in str(num)])

#print(is_narcissistic_num(153))
#print(is_narcissistic_num(370))
#print(is_narcissistic_num(407))
#print(is_narcissistic_num(409))
#print(is_narcissistic_num(1634))
#print(is_narcissistic_num(8208))
#print(is_narcissistic_num(9474))
#print(is_narcissistic_num(9475))

#def highest_lowest_num(str1):
 # num_list = list(map(int, str1.split()))
  #return max(num_list), min(num_list)

#print(highest_lowest_num("1 4 5 77 9 0"))
#print(highest_lowest_num("-1 -4 -5 -77 -9 0"))
#print(highest_lowest_num("0 0"))

#def increasing_trend(nums):
#    if (sorted(nums) == nums):
 #       return True
  #  else:
   #     return False

#print(increasing_trend([1,2,3,4]))
#print(increasing_trend([1,2,5,3,4]))
#print(increasing_trend([-1,-2,-3,-4]))
#print(increasing_trend([-4,-3,-2,-1]))
#print(increasing_trend([1,2,3,4,0]))

#def find_string(txt, str1):
#	return txt.find(str1, txt.find(str1)+1)

#print(find_string("The quick brown fox jumps over the lazy dog", "the"))
#print(find_string("the quick brown fox jumps over the lazy dog", "the"))

#def sum_index_multiplier(nums):
#	return sum(j*i for i, j in enumerate(nums))

#print(sum_index_multiplier([1,2,3,4]))
#print(sum_index_multiplier([-1,-2,-3,-4]))
#print(sum_index_multiplier([]))def oldest_student(students):
	
#def oldest_student(students):
#	return max(students, key=students.get)

#print(oldest_student({"Bernita Ahner": 12, "Kristie Marsico": 11, 
  #                    "Sara Pardee": 14, "Fallon Fabiano": 11, 
   #                   "Nidia Dominique": 15})) 
#print(oldest_student({"Nilda Woodside": 12, "Jackelyn Pineda": 12.2, 
 #                     "Sofia Park": 12.4, "Joannie Archibald": 12.6, 
  #                    "Becki Saunder": 12.7})) 


#def no_consecutive_letters (txt):
 #   return txt[0] + ''.join(txt[i] for i in range(1,len(txt)) if txt[i] != txt[i-1])

#print(no_consecutive_letters("PPYYYTTHON"))
#print(no_consecutive_letters("PPyyythonnn"))
#print(no_consecutive_letters("Java"))
#print(no_consecutive_letters("PPPHHHPPP")) 


#def parallel_lines(line1, line2):
 # return line1[0]/line1[1] == line2[0]/line2[1]
#2x + 3y = 4, 2x + 3y = 8
#print(parallel_lines([2,3,4], [2,3,8]))
#2x + 3y = 4, 4x - 3y = 8
#print(parallel_lines([2,3,4], [4,-3,8])) 

# Lucky number in a Matrix: Maximum in its column and minimum in its row.

#def lucky_Numbers(matrix):
 #   result = set(map(min, matrix)) & set(map(max, zip(*matrix)))
  #  return list(result)

#m1 = [[1,2], [2,3]]
#print("Original matrix:",m1)
#print("Lucky number(s) in the said matrix: ",lucky_Numbers(m1))

#m1 = [[1,2,3], [3,4,5]]
#print("\nOriginal matrix:",m1)
#print("Lucky number(s) in the said matrix: ",lucky_Numbers(m1))

#m1 = [[7,5,6], [3,4,4], [6,5,7]]
#print("\nOriginal matrix:",m1)
#print("Lucky number(s) in the said matrix: ",lucky_Numbers(m1))

#def Seq_Linear_Quadratic_Cubic(seq_nums):
 # seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
  #if len(set(seq_nums)) == 1: return "Linear Sequence"
  #seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
  #if len(set(seq_nums)) == 1: return "Quadratic Sequence"
  #seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
  #if len(set(seq_nums)) == 1: return "Cubic Sequence"
  
#print(Seq_Linear_Quadratic_Cubic([0,2,4,6,8,10]))
#print(Seq_Linear_Quadratic_Cubic([1,4,9,16,25]))
#print(Seq_Linear_Quadratic_Cubic([0,12,10,0,-12,-20]))
#print(Seq_Linear_Quadratic_Cubic([1,2,3,4,5]))


#def is_pandigital_num(n):
 #   return len(set(str(n))) == 10

#print(is_pandigital_num(1023456897))
#print(is_pandigital_num(1023456798))
#print(is_pandigital_num(1023457689))
#print(is_pandigital_num(1023456789))
#print(is_pandigital_num(102345679))

#def oddish_evenish_num(n):
#	return 'Oddish' if sum(map(int, str(n))) % 2 else 'Evenish'
#print(oddish_evenish_num(120))
#print(oddish_evenish_num(321))
#print(oddish_evenish_num(43))
#print(oddish_evenish_num(4433))
#print(oddish_evenish_num(373))

#def check_last_digit(x, y, z):
 # return str(x*y)[-1] == str(z)[-1]

#print(check_last_digit(12, 22, 44))
#print(check_last_digit(145, 122, 1010))
#print(check_last_digit(0, 22, 40))
#print(check_last_digit(1, 22, 40))
#print(check_last_digit(145, 122, 101))

#def indices_in_list(nums_list, n):
	#return [idx for idx, i in enumerate(nums_list) if i == n]

#print(indices_in_list([1,2,3,4,5,2], 2))
#print(indices_in_list([3,1,2,3,4,5,6,3,3], 3))
#print(indices_in_list([1,2,3,-4,5,2,-4], -4))

#def two_unique_nums(nums):
 # return [i for i in nums if nums.count(i)==1]
#print(two_unique_nums([1,2,3,2,3,4,5]))
#print(two_unique_nums([1,2,3,2,4,5]))
#print(two_unique_nums([1,2,3,4,5]))

#def is_circle_collision(circle1, circle2):
 #  x1, y1, r1 = circle1
 #  x2, y2, r2 = circle2
 #  distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
 #  return distance <= r1 + r2
#print(is_circle_collision([1,2, 4], [1,2, 8]))
#print(is_circle_collision([0,0, 2], [10,10, 5]))

#def digit_distance_nums(n1, n2):
 #        return sum(map(int,str(abs(n1-n2))))
#print(digit_distance_nums(123, 256))
#print(digit_distance_nums(23, 56))
#print(digit_distance_nums(1, 2))
#print(digit_distance_nums(24232, 45645))

#def reverse_even(txt):
 #        return ' '.join(i[::-1] if not len(i)%2 else i for i in txt.split())
#print(reverse_even("The quick brown fox jumps over the lazy dog"))
#print(reverse_even("Python Exercises"))

#import string
#print("Alphabet from a-z:")
#for letter in string.ascii_lowercase:
 #  print(letter, end =" ")
#print("\nAlphabet from A-Z:")
#for letter in string.ascii_uppercase:
 #  print(letter, end =" ")

#nums = range(1,10)
#print(list(nums))
#print(list(map(str, nums)))

#import math
#def is_not_prime(n):
 #   ans = False
  #  for i in range(2, int(math.sqrt(n)) + 1):
   #     if n % i == 0:
    #        ans = True
    #return ans
#print("Nonprime numbers between 1 to 100:")
#for x in filter(is_not_prime, range(1, 101)):
 #   print(x)

#def gcd(p,q):
# Create the gcd of two positive integers.
 #   while q != 0:
  #      p, q = q, p%q
   # return p
#def is_coprime(x, y):
 #   return gcd(x, y) == 1
#print(is_coprime(17, 13))
#print(is_coprime(17, 21))
#print(is_coprime(15, 21))
#print(is_coprime(25, 45))

#def test(str):
#	return str.translate(str.maketrans('PTSHA', '90168'))
#str = "PHP"
#print("Original string: ",str)
#print("Coded string: ",test(str))
#str = "JAVASCRIPT"
#print("\nOriginal string: ",str)
#print("Coded string: ",test(str))

#def test(str):
 #   return str.islower() or str.isupper()

#str = "PHP"
#print("Original string: ",str)
#print("Coded string: ",test(str))
#str = "javascript"
#print("\nOriginal string: ",str)
#print("Coded string: ",test(str))
#str = "JavaScript"
#print("\nOriginal string: ",str)
#print("Coded string: ",test(str))

#def test(str):
 #   return str if len(str) < 3 else str[1:-1]
#str = "PHP"
#print("Original string: ",str)
#print("Removing the first and last elements from the said string: ",test(str))
#str = "Python"
#print("\nOriginal string: ",str)
#print("Removing the first and last elements from the said string: ",test(str))
#str = "JavaScript"
#print("\nOriginal string: ",str)
#print("Removing the first and last elements from the said string: ",test(str))


#def test(str1):
 #   return any(c1 == c2 for c1, c2 in zip(str1, str1[1:]))
#str = "PHP"
#print("Original string: ",str)
#print("Check for consecutive similar letters! ",test(str))
#str = "PHHP"
#print("\nOriginal string: ",str)
#print("Check for consecutive similar letters! ",test(str))
#str = "PHPP"
#print("\nOriginal string: ",str)
#print("Check for consecutive similar letters! ",test(str))

#def test(str1):
 #   return str1[::-1].lower()
#str = "PHP"
#print("Original string:",str)
#print("Reverse the said string in lower case:",test(str))
#str = "JavaScript"
#print("\nOriginal string:",str)
#print("Reverse the said string in lower case:",test(str))
#str = "PHPP"
#print("\nOriginal string:",str)
#print("Reverse the said string in lower case:",test(str)) 

#def test(str1):
 #   return ''.join(sorted(str1))

#str1 = "PHP"
#print("Original string:",str1)
#print("Convert the letters of the said string into alphabetical order:",test(str1))
#str1 = "javascript"
#print("\nOriginal string:",str1)
#print("Convert the letters of the said string into alphabetical order:",test(str1))
#str1 = "python"
#print("\nOriginal string:",str1)
#print("Convert the letters of the said string into alphabetical order:",test(str1))

#import array as arr
#def test(nums):
#    return sum(nums) % len(nums) == 0
#array_num = arr.array('i', [1, 3, 5, 7, 9])
#print("Original array:")
#for i in range(len(array_num)):    
#    print(array_num[i], end=' ')
#print("\nCheck the average value of the elements of the said array is a whole number or not:\n",test(array_num))
#array_num = arr.array('i', [2, 4, 2, 6, 4, 8])
#print("\nOriginal array:")
#for i in range(len(array_num)):    
 #   print(array_num[i], end=' ')
#print("\nCheck the average value of the elements of the said array is a whole number or not:\n",test(array_num)) 

#import re
#def test(text):
 #   return re.sub(r'[aeiou]+', '', text, flags=re.IGNORECASE)
#text = "Python";
#print("Original string:",text)
#print("After removing all the vowels from the said string: " + test(text))
#text = "C Sharp"
#print("\nOriginal string:",text)
#print("After removing all the vowels from the said string: " + test(text))
#text = "JavaScript"
#print("\nOriginal string:",text)
#print("After removing all the vowels from the said string: " + test(text))

#def test(text):
 #  return [x for x in range(len(text)) if text[x].islower()]
#text = "Python";
#print("Original string:",text)
#print("Indices of all lower case letters of the said string:\n",test(text))
#text = "JavaScript";
#print("Original string:",text)
#print("Indices of all lower case letters of the said string:\n",test(text))
#text = "PHP";
#print("Original string:",text)
#print("Indices of all lower case letters of the said string:\n",test(text))

#from datetime import date
#def test(month, year): 
 #   return str(date(year,month,13).strftime("%A")=='Monday')

#month = 11;
#year = 2022;            
#print("Month No.: ", month, " Year: ", year);
#print("Check whether the said month and year contains a Monday 13th.: " + test(month, year));
#month = 6;
#year = 2022;            
#print("\nMonth No.: ", month, " Year: ", year);
#print("Check whether the said month and year contains a Monday 13th.: " + test(month, year)); 


#def test(num):
 #   ones =  bin(num). replace("0b", "").count('1')
  #  zeros = bin(num). replace("0b", "").count('0')
   # return "Number of zeros: " + str(zeros) + ", Number of ones: " + str(ones);

#n = 12; 
#print("Original number: ",n);
#print("Number of ones and zeros in the binary representation of the said number:");
#print(test(n));
#n = 1234;
#print("\nOriginal number: ",n);
#print("Number of ones and zeros in the binary representation of the said number:");
#print(test(n));

#Source https://bit.ly/3w492zp

#from functools import reduce

#def test(n):    
 #   return set(reduce(list.__add__, 
  #              ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

#'''
#sqrt(x) * sqrt(x) = x. So if the two factors are the same, they're both 
#the square root. If you make one factor bigger, you have to make the other 
#factor smaller. This means that one of the two will always be less than or 
#equal to sqrt(x), so you only have to search up to that point to find one 
#of the two matching factors. You can then use x / fac1 to get fac2.

#The reduce(list.__add__, ...) is taking the little lists of [fac1, fac2] 
#and joining them together in one long list.

#The [i, n/i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0 returns 
#a pair of factors if the remainder when you divide n by the smaller one 
#is zero (it doesn't need to check the larger one too; it just gets that 
#by dividing n by the smaller one.)

#The set(...) on the outside is getting rid of duplicates, which only 
#happens for perfect squares. For n = 4, this will return 2 twice, so 
#set gets rid of one of them.
#'''

#def test(lst):
 # pos_sum = 0
 # neg_sum = 0
 # for n in lst:
   # if n > 0:
    #  pos_sum += n
   # elif n < 0:
      #neg_sum += n
 # r#eturn max(pos_sum, neg_sum, key=abs)

#nums = { 0, -10, -11, -12, -13, -14, 15, 16, 17, 18, 19, 20 };
#print("Original array elements:");
#print(nums)
#print("Largest sum - Positive/Negative numbers of the said array: ", test(nums));
#nums = { -11, -22, -44, 0, 3, 4 , 5, 9 };
#print("\nOriginal array elements:");
#print(nums)
#print("Largest sum - Positive/Negative numbers of the said array: ", test(nums))

#def test(txt):
 #   result_str = ""
  #  s = True
   # for i in txt:
    #    result_str += i.upper() if s else i.lower()
     #   if i.isalpha():
      #      s = not s
    #return result_str
#str1 = "Python Exercises";
#print("Original string: ", str1);
#print("After alternating the case of each letter of the said string:")
#print(test(str1))
#str1 = "C# is used to develop web apps, desktop apps, mobile apps, games and much more.";
#print("\nOriginal string: ", str1);
#print("After alternating the case of each letter of the said string:")
#print(test(str1))  

#from functools import reduce
#def test(nums):
 #   return reduce(lambda x,y:lcm(x,y),nums)
#def gcd(a, b):
 #   while b:
  #      a, b = b, a%b
   # return a
#def lcm(a, b):
 #   return a*b // gcd(a, b)
#nums = [ 4, 6, 8 ]
#print("Original list elements:")
#print(nums)
#print("LCM of the numbers of the said array of positive integers: ", test(nums))
#nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
#print("\nOriginal list elements:")
#print(nums)
#print("LCM of the numbers of the said array of positive integers: ", test(nums))
#nums = [ 48, 72, 108  ]
#print("\nOriginal list elements:")
#print(nums)
#print("LCM of the numbers of the said array of positive integers: ", test(nums))

#def test(txt):
#	return ' '.join(i[::-1] if len(i)%2 else i for i in txt.split())
 
#text = "The quick brown fox jumps over the lazy dog"
#print("Original string:")
#print(text)
#print("Reverse all the words of the said string which have odd length:")
#print(test(text))
#text = "Python Exercises"
#print("\nOriginal string:")
#print(text)
#print("Reverse all the words of the said string which have odd length:")
#print(test(text))

#def test(str1, str2):
 #   for i in range(len(str2)):
  #      while str2[i:] in str1 and str2[-1]==str1[-1]:
   #         return str2[i:]
    #return ""

#str1 = "running";
#str2 = "ruminating";
#print("Original strings: " + str1 + "  " + str2);
#print("Common ending between said two strings: " + test(str1, str2));
#str1 = "thisisatest";
#str2 = "testing123testing";
#print("\nOriginal strings: " + str1 + "  " + str2);
#print("Common ending between said two strings: " + test(str1, str2));

#def test(n):
 #   return int(bin(n)[::-1][:-2], 2)

#n = 13
#print("Original number: ", n);
#print("Reverse the binary representation of the said integer and convert it into an integer:\n",test(n));
#n = 145
#print("Original number: ", n);
#print("Reverse the binary representation of the said integer and convert it into an integer:\n",test(n));
#n = 1342
#print("Original number: ", n);
#print("Reverse the binary representation of the said integer and convert it into an integer:\n",test(n));

#def test(n):
 #   x = n
  #  y = n
   # while True:
    #    if str(x) == str(x)[::-1]:
     #       return x
      #  x -=  1
       # if str(y) == str(y)[::-1]:
        #    return y
        #y += 1
    #return int(bin(n)[::-1][:-2], 2)

#n = 120;
#print("Original number: ", n);
#print("Closest Palindrome number of the said number: ",test(n));
#n = 321;
#print("Original number: ", n);
#print("Closest Palindrome number of the said number: ",test(n));
#n = 43;
#print("Original number: ", n);
#print("Closest Palindrome number of the said number: ",test(n));
#n = 1234;
#print("Original number: ", n);
#print("Closest Palindrome number of the said number: ",test(n));

#nums = ['0.49', '0.54', '0.54', '0.54', '0.54', '0.54', '0.55', '0.54', '0.54',  '0.54', 
#'0.55', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54']
#print("Original list:")
#print(nums)
#print("\nList of Floats:")
#nums_of_floats = []
#for item in nums:
 #   nums_of_floats.append(float(item))
#print(nums_of_floats)

def get_domain_name(ip_address):
  import socket
  result=socket.gethostbyaddr(ip_address)
  return list(result)[0]
print("Domain name using PTR DNS:")
print(get_domain_name("8.8.8.8"))
print(get_domain_name("13.251.106.90"))
print(get_domain_name("8.8.4.4"))
print(get_domain_name("23.23.212.126"))