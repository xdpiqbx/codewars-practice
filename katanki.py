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

# ================================== Basic variable assignment 0093
# a = "code"
# b = "wa.rs"
# name = a + b

# ================================== Capitalization and Mutability 0094
# def capitalize_word(word):
#     return word[0].upper()+word[1:]
#     # return word.capitalize() # for the first word in the string
#     # return word.title()  # for each word in the string

# ================================== 101 Dalmatians - squash the bugs, not the dogs! 0095
# def how_many_dalmatians(n):
#     dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
#     return dogs[sum([n > 10, n > 50, n == 101])]

# ================================== Spacify 0096
# def spacify(string):
#     return " ".join(char for char in string)
#     # return " ".join(string)
# spacify = " ".join

# ================================== Spacify 0097
# NATO = {
#   'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
#   'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
#   'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
#   'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey',
#   'X': 'Xray', 'Y': 'Yankee', 'Z': 'Zulu'}
# def to_nato(words):
#     # words = words.replace(" ", "")
#     # result = []
#     # for char in words:
#     #     if char.upper() in NATO.keys():
#     #         result.append(NATO.get(char.upper()))
#     #     else:
#     #         result.append(char)
#     # return " ".join(result)
#     # # return ' '.join(NATO.get(char, char) for char in words.upper() if char != ' ')

# ================================== Grasshopper - Debug 0098
# def weather_info(temp):
#     c = convert_to_celsius(temp)
#     return f"{c} is above freezing temperature" if c > 0 else f"{c} is freezing temperature"
# def convert_to_celsius(temperature):
#     return (temperature - 32) * (5 / 9)

# ================================== Is this my tail? 0099
# def correct_tail(body, tail):
#     return tail in body[-1]

# ================================== String Templates - Bug Fixing #5 0100
# def build_string(*args):
#     return "I like {}!".format(", ".join(args))

# ================================== _FIXME: Replace all dots 0101
# def replace_dots(str):
#     return str.replace(".", "-")

# ================================== Fix your code before the garden dies! 0102
# def rain_amount(rain_amount):
#     if rain_amount < 40:
#         return f"You need to give your plant {40 - rain_amount} mm of water"
#     return "Your plant has had more than enough water for today!"

# ================================== Swap Values 0103
# def swap_values(args):
#     temp = args[0]
#     args[0] = args[1]
#     args[1] = temp
#     # ------
#     # args[0], args[1] = args[1], args[0]
#     # args[:]=args[::-1]
#     # args.reverse()

# ================================== Incorrect division method 0104
# def divide_numbers(x,y):
#     return x / y

# ================================== Multiply the number 0105
# def multiply(n):
#     return n * (5 ** len(str(abs(n))))

# ================================== Fix the Bugs (Syntax) - My First Kata 0106
# def my_first_kata(a, b):
#     if a == 0 or b == 0:
#         return False
#     if isinstance(a, int) and isinstance(b, int):
#         return a % b + b % a
#     return False

# ================================== Return to Sanity 0107
# def mystery():
#     results = {'sanity': 'Hello'}
#     return results

# ================================== Unexpected parsing 0108
# def get_status(is_busy):
#     return {"status": "busy" if is_busy else "available"}

# ================================== Switch/Case - Bug Fixing #6 0109
# def eval_object(v):
#     match v.get("operation"):
#         case "+":
#             return v["a"] + v["b"]
#         case "-":
#             return v["a"] - v["b"]
#         case "/":
#             return v["a"] / v["b"]
#         case "*":
#             return v["a"] * v["b"]
#         case "%":
#             return v["a"] % v["b"]
#         case "**":
#             return v["a"] ** v["b"]
#         case _:
#             return 1

# ================================== Semi-Optional 0110
# def wrap(value):
#     return {"value": value}

# ================================== How do I compare numbers? 0111
# def what_is(x):
#     if x == 42:
#         return 'everything'
#     elif x == 42 * 42:
#         return 'everything squared'
#     else:
#         return 'nothing'

# ================================== Filtering even numbers (Bug Fixes) 0112
# def kata_13_december(lst):
#     return [num for num in lst if num % 2 != 0]

# ================================== Invalid Login - Bug Fixing #11 0113
# def validate(username, password):
#     database = Database()
#     return database.login(username, password)

# ================================== They say that only the name is long enough to attract attention.
# They also said that only a simple Kata will have someone to solve it.
# This is a sadly story #1: Are they opposite? 0114
# def is_opposite(s1, s2):
#     if not (s1 or s2):
#         return False
#     if s1.lower() != s2.lower():
#         return False
#     for i in range(len(s1)):
#         if s1[i] == s2[i]:
#             return False
#     return True
#     # return False if not (s1 or s2) else s1.swapcase() == s2

# ================================== Training JS #7: if..else and ternary operator 0115
# def sale_hotdogs(n):
#     return n * [100, 95, 90][sum([n >= 5, n >= 10])]
#     # return n * [100, 95, 90][(n >= 5) + (n >= 10)]
#     # if n < 5:
#     #     return n * 100
#     # elif 5 <= n < 10:
#     #     return n * 95
#     # else:
#     #     return n * 90

# ================================== Count by X 0116
# def count_by(x, n):
#     return [num for num in range(x, n * x + x) if num % x == 0]
#     # return [i * x for i in range(1, n + 1)]

# ================================== If you can't sleep, just count sheep!! 0117
# def count_sheep(n):
#     # res = ""
#     # for num in range(n):
#     #     res += f"{num+1} sheep..."
#     # return res
#     return "".join([f"{num+1} sheep..." for num in range(n)])

# ================================== You Can't Code Under Pressure #1 0118
# def doubleInteger(i):
#     # return i * 2
#     # return i + i
#     # return i << 1

# ================================== Rock Paper Scissors! 0119
# def rps(p1, p2):
#     if p1 == p2:
#         return 'Draw!'
#
#     if (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'):
#         return "Player 1 won!"
#
#     return "Player 2 won!"

# def rps(p1, p2):
#     beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
#     if beats[p1] == p2:
#         return "Player 1 won!"
#     if beats[p2] == p1:
#         return "Player 2 won!"
#     return "Draw!"

# ================================== Total amount of points 0120
# def points(games):
#     sum = 0
#     for team1, separator, team2 in games:
#         if team1 > team2:
#             sum += 3
#         elif team1 == team2:
#             sum += 1
#     return sum

# def points(games):
#     return sum(3 * (team1 > team2) + (team1 == team2) for team1, _, team2 in games)

# print(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']))

# ================================== Get the mean of an array 0121
# def get_average(marks):
#     return sum(marks) // len(marks)

# ================================== Get the mean of an array 0122
# def sum_array(arr):
#     return sum(sorted(arr)[1:-1]) if arr else 0

# ================================== Grasshopper - Grade book 0123
# def get_grade(s1, s2, s3):
#     avg = sum([s1, s2, s3]) // 3
#     return ['F', 'D', 'C', 'B', 'A'][sum([avg >= 60, avg >= 70, avg >= 80, avg >= 90])]

# ================================== Never visit a . . . !? 0124
# def subtract_sum(number):
#     raw = number
#     num_sum = 0
#     while number > 0:
#         digit = number % 10
#         num_sum += digit
#         number //= 10
#     if raw - num_sum < 100:
#         print(raw - num_sum)
#         return raw - num_sum
#     else:
#         subtract_sum(raw - num_sum)

# ================================== Count the Monkeys! 0125
# def monkey_count(n):
#     return [n for n in range(1, n + 1)]
#     # return list(range(1, n+1))

# ================================== Grasshopper - Personalized Message 0126
# def greet(name, owner):
#     return 'Hello boss' if name == owner else 'Hello guest'

# ================================== Sum Mixed Array 0127
# def sum_mix(arr):
#     return sum([int(num) for num in arr])
#     # return sum(map(int, arr))

# ================================== Area or Perimeter 0128
# def area_or_perimeter(l, w):
#     return l * w if l == w else (l + w) * 2

# ================================== Do I get a bonus? 0129
# def bonus_time(salary, bonus):
#     return f"${salary * 10}" if bonus else f"${salary}"

# ================================== The Feast of Many Beasts 0130
# def feast(beast, dish):
#     return beast[0]+beast[-1] == dish[0]+dish[-1]
#     # return beast.startswith(dish[0]) and beast.endswith(dish[-1])

# ================================== Remove exclamation marks 0131
# def remove_exclamation_marks(s):
#     return s.replace("!", "")
#     # return ''.join([x for x in s if x != '!'])

# ================================== Transportation on vacation 0132
# def rental_car_cost(d):
#     return d * 40 - [0, 20, 50][sum([d >= 7, d >= 3])]
#
#     # cost = 0
#     # if d >= 7:
#     #     cost = d * 40 - 50
#     # elif d >= 3:
#     #     cost = d * 40 - 20
#     # else:
#     #     cost = d * 40
#     # return cost
#
#     # return d * 40 - (d > 2) * 20 - (d > 6) * 30

# ================================== Thinkful - Logic Drills: Traffic light 0133
# def update_light(current):
#     # traffic_lights = ["green", "yellow", "red"]
#     # for i in range(3):
#     #     if traffic_lights[i] == current:
#     #         print(traffic_lights[i + 1] if i < 2 else "green")
#
#     traffic_lights = ["green", "yellow", "red"]
#     return [traffic_lights[i + 1] if i < 2 else "green" for i in range(3) if traffic_lights[i] == current][0]
#
#     # return {"green": "yellow", "yellow": "red", "red": "green"}[current]
#     # return traffic_lights[(traffic_lights.index(current) + 1) % len(traffic_lights)]
#     # update_light = lambda c, l=["yellow", "green", "red"]: l[l.index(c) - 1]
#
# print(update_light('green'))
# print(update_light('yellow'))
# print(update_light('red'))

# ================================== Digital cypher (encode) 0134
# def encode(message, key):
#     # msg_len = len(message)
#     # str_key = str(key)
#     # full_key = []
#     # i = 0
#     # for _ in range(msg_len):
#     #     if len(str_key) == i:
#     #         i = 0
#     #     full_key.append(int(str_key[i]))
#     #     i += 1
#     # return [(ord(message[i]) - 96) + full_key[i] for i in range(msg_len)]
#
#     msg_len = len(message)
#     str_key = str(key)
#     full_key = []
#     i = 0
#     for _ in range(msg_len):
#         full_key.append(int(str_key[i]))
#         i = (i + 1) % len(str_key)
#     return [(ord(message[i]) - 96) + full_key[i] for i in range(msg_len)]

# from itertools import cycle
# def encode(message, key):
#     return [
#         ord(a) - 96 + int(b)
#         for a, b in zip(
#             message, cycle(str(key))
#         )
#     ]

# ================================== Digital cypher vol 2 (decode) 0135
# from itertools import cycle
# def decode(code, key):
#     return "".join(chr(a - int(b) + 96) for a, b in zip(code, cycle(str(key))))
#
# print(decode([20, 12, 18, 30, 21], 1939)) # scout
# print(decode([14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8], 1939))

# ================================== The Barksdale Code 0135
# def decode(string):
#     keys = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0', '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}
#     return "".join(keys.get(char) for char in string)
#     # return s.translate(str.maketrans("1234567890", "9876043215"))

# https://www.codewars.com/kata/search/python?q=&r%5B%5D=-7&tags=Cryptography&xids=played&beta=false&order_by=popularity%20desc





