# ================================== Drink about 0001
# def people_with_age_drink(age):
#     if age < 14:
#         result = f"drink toddy"
#     elif 14 <= age < 18:
#         result = f"drink coke"
#     elif 18 <= age < 21:
#         result = f"drink beer"
#     else:
#         result = f"drink whisky"
#     return result
# ================================== 0002
# def positive_sum(arr):
#     length = len(arr)
#     if length == 0:
#         return 0
#     positive = [num for num in arr if num >= 0]
#     result = 0
#     for num in positive:
#         result += num
#     return result
#
# def positive_sum(arr):
#     return sum(x for x in arr if x > 0)
# ================================== How good are you really? 0003
# def better_than_average(class_points, your_points):
#     return (sum(class_points) / len(class_points)) < your_points
# ================================== Fake Binary 0004
# def fake_bin(x):
#     res = ""
#     for num in x:
#         res += '1' if int(num) >= 5 else '0'
#     return res
# def fake_bin(x):
#     return ''.join('0' if c < '5' else '1' for c in x)
# ================================== Is he gonna survive? 0005
# def hero(bullets, dragons):
#     return False if bullets == 0 else bullets / dragons >= 2
# def hero(bullets, dragons):
#     return bullets >= dragons * 2
# ================================== Simple Fun #1: Seats in Theater 0006
# def seats_in_theater(tot_cols, tot_rows, col, row):
#     return (tot_rows - row) * (tot_cols - col + 1)
# ================================== Triple Trouble 0007
# def triple_trouble(one, two, three):
#     result = ""
#     index = 0
#     for _ in one:
#         result += one[index]+two[index]+three[index]
#         index += 1
#     return result
# def triple_trouble(one, two, three):
#     return [''.join(a) for a in zip(one, two, three)]
# ================================== Regex validate PIN code 0008
# def validate_pin(pin):
#     if (len(pin) == 4) or (len(pin) == 6):
#         return pin.isnumeric()
#     return False
# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()
# ================================== Find the position! 0009
# def position(alphabet):
#     return f'Position of alphabet: {ord(alphabet.lower()) - 96}'
# ================================== get character from ASCII Value 0010
# def get_char(c):
#     return chr(c)
# ================================== Lario and Muigi Pipe Problem 0011
# def pipe_fix(nums):
#     return [i for i in range(nums[0], nums[len(nums)-1] + 1)]
#
# def pipe_fix(nums):
# 	return list(range(nums[0], nums[-1] + 1))
# ================================== Find Multiples of a Number 0012
# def find_multiples(integer, limit):
#     multiplier = int((limit / integer) // 1)
#     return [i * integer for i in range(1, multiplier+1)]
#
# def find_multiples(integer, limit):
#     return list(range(integer, limit+1, integer))
# ================================== Grasshopper - Debug sayHello 0013
# def say_hello(name):
#     return f"Hello, {name}"
# ================================== Is it a palindrome? 0014
# def is_palindrome(s):
#     return s.lower() == s.lower()[::-1]
# ================================== Convert a string to an array 0015
# def string_to_array(s):
#     return s.split(" ")
# ================================== MakeUpperCase 0016
# def make_upper_case(s):
#     return s.upper()
# ================================== A Needle in the Haystack 0017
# def find_needle(haystack):
#     if "needle" in haystack:
#         return f"found the needle at position {haystack.index('needle')}"
# ================================== Sentence Smash 0018
# def smash(words):
#     return " ".join(words)
# ================================== Sentence Smash 0019
# def set_alarm(employed, vacation):
#     return employed and not vacation
# ================================== Price of Mangoes 0020
# def mango(quantity, price):
#     counter = 0
#     for num in range(quantity + 1):
#         if num % 3 == 0:
#             continue
#         counter += 1
#     return counter * price
#
# def mango(quantity, price):
#     return (quantity - quantity // 3) * price
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--[on_true] if [expression] else [on_false]
# ================================== Even or Odd 0021
# def even_or_odd(number):
#     return "Even" if number % 2 == 0 else "Odd"
# ================================== Matrix Multiplier 0022
# def getMatrixProduct(a, b):
#     if len(a) != len(b):
#         return -1
#     result = [
#        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
#        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
#     ]
#     return result
#
#
# print(getMatrixProduct([[0.5, 1],[1.5, 2]], [[0.2, 0.4], [0.6, 0.8]]))
# print(getMatrixProduct([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
# print(getMatrixProduct([[1, 2], [3, 4]], [[2, 4]]))

# https://www.codewars.com/kata/search/python?q=&r%5B%5D=-8&xids=played&beta=false&order_by=popularity%20desc
