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

# ================================== Multiply 0023
# def multiply(a, b):
#     return a * b

# ================================== Return Negative 0024
# def make_negative( number ):
#     if number == 0:
#         return 0
#     return number * -1 if number > 0 else number
#
# def make_negative( number ):
#     return -abs(number)

# ================================== Reversed Strings 0025
# def solution(string):
#     return string[::-1]
# OR
# for char in range(len(string)-1,-1,-1):
#     return string[char]

# ================================== Convert boolean values to strings 'Yes' or 'No'. 0026
# def bool_to_word(boolean):
#     return "Yes" if boolean else "No"
#
# def bool_to_word(bool):
#     return ['No', 'Yes'][bool]

# ================================== Convert a Number to a String! 0027
# def number_to_string(num):
#     return str(num)  # "{n}".format(n=num) # f"{num}" # "%s" % num

# ================================== Opposite number 0028
# def opposite(number):
#     return number * -1

# ================================== Remove First and Last Character 0029
# def remove_char(s):
#     return s[1:len(s)-1:]
# def remove_char(s):
#     return s[1:-1]

# ================================== String repeat 0030
# def repeat_str(repeat, string):
#     return string * repeat

# ================================== Square(n) Sum 0031
# def square_sum(numbers):
#     return sum(num ** 2 for num in numbers)

# ================================== Grasshopper - Summation 0032
# def summation(num):
#     return sum(n for n in range(num + 1)) # num*(num+1) / 2 # return sum(range(1,num+1))

# ================================== Remove String Spaces 0033
# def no_space(x):
#     return "".join(x.split(" "))  # return x.replace(' ' ,'')

# ================================== Find the smallest integer in the array 0034
# def find_smallest_int(arr):
#     return min(arr)

# ================================== Counting sheep... 0035
# def count_sheeps(sheep):
#     return sum(1 for s in sheep if s)  # sheep.count(True)

# ================================== Counting sheep... 0036
# def count_sheeps(sheep):
#     return sum(1 for s in sheep if s)  # sheep.count(True)

# ================================== Keep Hydrated! 0037
# def litres(time):
#     return int(time * 0.5)

# ================================== Basic Mathematical Operations 0038
# def basic_op(operator, value1, value2):
#     calc = {
#         '+': value1 + value2,
#         '-': value1 - value2,
#         '*': value1 * value2,
#         '/': value1 / value2,
#     }
#     return calc[operator]
# # return eval(str(value1) + operator + str(value2))

# ================================== Century From Year 0039
# def century(year):
#     return year // 100 if year % 100 == 0 else year // 100 + 1  # return (year + 99) // 100

# ================================== Abbreviate a Two Word Name 0040
# def abbrev_name(name):
#     words = name.upper().split(" ")
#     return f"{words[0][0]}.{words[1][0]}"

# first, last = name.upper().split(' ')

# return '.'.join(w[0] for w in name.split()).upper()

# ================================== Convert a String to a Number! 0041
# def string_to_number(s):
#     return int(s)

# ================================== Convert number to reversed array of digits 0042
# def digitize(n):
#     return [int(num) for num in str(n)[::-1]]
#     # return map(int, str(n)[::-1])
#     # return map(int, reversed(str(n)))

# ================================== Is n divisible by x and y? 0043
# def is_divisible(n, x, y):
#     return True if n % x == 0 and n % y == 0 else False
#     # return n % x == 0 and n % y == 0

# ================================== Returning Strings 0044
# def greet(name):
#     return f"Hello, {name} how are you doing today?"
#     # return "Hello, %s how are you doing today?" % name
# # greet = lambda name: f'Hello, {name} how are you doing today?'

# ================================== Function 1 - hello world 0045
# def greet():
#     return "hello world!"
# # greet = lambda: "hello world!"

# ================================== Beginner - Lost Without a Map 0046
# def maps(a):
#     return [i * 2 for i in a]

# ================================== Opposites Attract 0047
# def lovefunc(flower1, flower2):
#     all_even = flower1 % 2 == 0 and flower2 % 2 == 0
#     all_odd = flower1 % 2 != 0 and flower2 % 2 != 0
#     return not (all_even or all_odd)
#
#     # return (flower1 + flower2) % 2

# ================================== Convert a Boolean to a String 0048
# def boolean_to_string(b):
#     return str(b)

# ================================== Beginner Series #2 Clock 0049
# def past(h, m, s):
#     return (s + m * 60 + h * 60 * 60) * 1000
#     # return timedelta(hours=h, minutes=m, seconds=s) // timedelta(milliseconds=1)

# ================================== Up and down, the string grows 0050
# STRANGE_STRING = "ß"
# STRANGE_STRING = 'ΰ'

# ================================== Up and down, the string grows 0051
# def mul_by_n(lst, n):
#     result = (x * n for x in lst)
#     return list(result)

# ================================== Quadrants 0052
# def quadrant(x, y):
#     quadrants = {
#         1: x > 0 and y > 0,
#         2: x < 0 < y,
#         3: x < 0 and y < 0,
#         4: x > 0 > y,
#     }
#     return [i for i in quadrants if quadrants[i]][0]

# ================================== Quadrants 0053
# import sys
# def total_bytes(object):
#     return sys.getsizeof(object)

# ================================== Floating point comparison 0054
# def approx_equals(a, b):
#     return abs(a - b) < 0.001

# ================================== Gravity Flip 0055
# def flip(d, a):
#     a.sort(reverse=d == "L")
#     return a
# # return sorted(a, reverse=d=='L')

# ================================== Name Your Python! 0056
# class Python:
#     def __init__(self, name):
#         self.name = name

# ================================== Color Ghost 0057
# import random
# class Ghost:
#     def __init__(self):
#         self.color = random.choice(["white", "yellow", "purple", "red"])

# ================================== Barking mad 0058
# class Dog():
#     def __init__(self, breed):
#         self.breed = breed
#     def bark(self):
#         return "Woof"
#
# snoopy = Dog("Beagle")
# scoobydoo = Dog("Great Dane")

# ================================== Are there any arrows left? 0059
# def any_arrows(arrows):
#     all_arrows = len(arrows)
#     if all_arrows == 0:
#         return False
#
#     damaged_arrows = 0
#
#     for arrow in arrows:
#         if 'damaged' in arrow.keys() and arrow['damaged']:
#             damaged_arrows += 1
#
#     return damaged_arrows != all_arrows
# def any_arrows(arrows):
#     return sum([1 for arrow in arrows if 'damaged' in arrow.keys() and arrow['damaged']]) != len(arrows)
#     # return any(not arrow.get("damaged", False) for arrow in arrows)

# ================================== Fix the loop! 0060
# def list_animals(animals):
#     list = ''
#     for i in range(len(animals)):
#         list += str(i + 1) + '. ' + animals[i] + '\n'
#     return list

# ================================== Grasshopper - Array Mean 0061
# def find_average(nums):
#     return sum(nums) / len(nums) if len(nums) else 0

# ================================== Javascript filter - 1 0062
# def search_names(logins):
#     return [creds for creds in logins if creds[0].endswith("_")]
#     # return list(filter(lambda a: a[0].endswith('_'), logins))

# ================================== Return a sorted list of objects 0063
# def sort_list(sort_by, lst):
#     lst.sort(reverse=True, key=lambda item: item[sort_by])
#     return lst
#     # return sorted(lst, reverse=True, key=lambda item: item[sort_by])

# ================================== Unpacking Arguments 0064
# def spread(func, args):
#     return func(*args)

# ================================== Lazily executing a function 0065
# def make_lazy(f, *args, **kwargs):
#     return lambda: f(*args, **kwargs)

# ================================== Multiples of 3 or 5 0066
# def solution(number):
#     if number < 0:
#         return 0
#     return sum(num for num in range(number) if num % 3 == 0 or num % 5 == 0)

# ================================== Vowel Count 0067
# def get_count(sentence):
#     return sum(1 for letter in sentence if letter in "aeiou")

# ================================== Find the odd int 0068
# def find_it(seq):
#     dict_nums = {}
#     for num in seq:
#         dict_nums[num] = seq.count(num)
#     for item in dict_nums.items():
#         if item[1] % 2 != 0:
#           return item[0]

# def find_it(seq):
#     for num in seq:
#         if seq.count(num) % 2 != 0:
#             return num

# ================================== Find the odd int 0069
# def two_sort(array):
#     array.sort()
#     return "***".join(list(array[0]))
#     # return '***'.join(sorted(arr)[0])
#     # return '***'.join(min(array))

# ================================== Find the odd int 0070
# def sorter(textbooks):
#     return sorted(textbooks, key=lambda s: s.lower())
#     # return sorted(textbooks, key=str.lower)

# ================================== Find the odd int 0071
# greek_alphabet = (
#     'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
#     'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
#     'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
#     'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
# def greek_comparator(lhs, rhs):
#     # the tuple greek_alphabet is defined in the global namespace
#     return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)
#
# greek_comparator('alpha', 'beta')

# ================================== Draw stairs 0072
# def draw_stairs(n):
#     # stairs = ""
#     # for step in range(n):
#     #     stairs += " " * step + "I\n"
#     # print(stairs)
#     # return stairs[:-1]
#     return "\n".join(" " * step + "I" for step in range(n))

# ================================== average 0073
# def find_average(numbers):
#     return sum(numbers) / len(numbers) if len(numbers) else 0

# ================================== Beginner Series #1 School Paperwork 0074
# def paperwork(n, m):
#     return 0 if n < 0 or m < 0 else n * m
#     # return n * m if n > 0 and m > 0 else 0
#     # return max(n, 0)*max(m, 0)

# ================================== Are You Playing Banjo? 0075
# def are_you_playing_banjo(name):
#     return name + " plays banjo" if name[0].lower() == "r" else name + " does not play banjo"

# ================================== Invert values 0076
# def invert(lst):
#     return [num * -1 for num in lst]

# ================================== Count of positives / sum of negatives 0077
# def count_positives_sum_negatives(arr):
#     positive_nums = sum(1 for num in arr if num > 0)
#     negative_nums = sum(num for num in arr if num < 0)
#     return [positive_nums, negative_nums] if arr else []

# ================================== Count of positives / sum of negatives 0078
# def sum_array(a):
#     return sum(a)
#     # res = 0
#     # for num in a:
#     #     res += num
#     # return res

# ================================== You only need one - Beginner 0079
# def check(seq, elem):
#     return elem in seq

# ================================== Beginner - Reduce but Grow 0080
# def grow(arr):
#     res = 1
#     for num in arr:
#         res *= num
#     return res
# ----
# from functools import reduce
# def grow(arr):
#     return reduce(lambda x, y: x * y, arr)
# ----
# import math
# def grow(arr):
#     return math.prod(arr)

# ================================== Beginner - Reduce but Grow 0081
# def bmi(weight, height):
#     bmi = round(weight / (height ** 2), 1)
#     check_dict = {
#         "Underweight": bmi <= 18.5,
#         "Normal": bmi <= 25,
#         "Overweight": bmi <= 30,
#         "Obese": bmi > 30,
#     }
#     return [result for result in check_dict if check_dict[result]][0]
#     # return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]

# ================================== Reversed sequence 0082
# def reverse_seq(n):
#     return [num for num in range(n, 0, -1)]
#     # return list(range(n, 0, -1))
#     # return range(n, 0, -1)

# ================================== Reversed Words 0083
# def reverse_words(s):
#     return " ".join(s.split(" ")[::-1])
#     # return ' '.join(reversed(str.split(' ')))

# ================================== Simple multiplication 0084
# def simple_multiplication(number) :
#     return number * 8 if number % 2 == 0 else number * 9

# ================================== Simple multiplication 0085
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return fuel_left * mpg >= distance_to_pump

# ================================== DNA to RNA Conversion 0086
# def dna_to_rna(dna):
#     return dna.replace("T", "U")

# ================================== Find Maximum and Minimum Values of a List 0087
# def minimum(arr):
#     return min(arr)
#
# def maximum(arr):
#     return max(arr)

# ================================== Jenny's secret message 0088
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)

# ================================== Array plus array 0089
# def array_plus_array(arr1,arr2):
#     # return sum([sum(arr1), sum(arr2)])
#     return sum(arr1+arr2)

# ================================== Get Planet Name By ID 0090
# def get_planet_name(id):
#
#     planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
#     return planets[id - 1]
#
#     # name=""
#     # match id:
#     #     case 1: name = "Mercury"
#     #     case 2: name = "Venus"
#     #     case 3: name = "Earth"
#     #     case 4: name = "Mars"
#     #     case 5: name = "Jupiter"
#     #     case 6: name = "Saturn"
#     #     case 7: name = "Uranus"
#     #     case 8: name = "Neptune"
#     # return name

# ================================== Unfinished Loop - Bug Fixing #1 0091
# def create_array(n):
#     res=[]
#     i=1
#     while i<=n:
#         res+=[i]
#         i += 1
#     return res

# ================================== Grasshopper - If/else syntax debug 0092
# def check_alive(health):
#     if health <= 0:
#         return False
#     else:
#         return True

# https://www.codewars.com/kata/search/python?order_by=popularity+desc&q=&r%5B%5D=-8&tags=Debugging&xids=played

# https://www.codewars.com/kata/search/python?q=&r%5B%5D=-8&xids=played&beta=false&order_by=popularity%20desc
