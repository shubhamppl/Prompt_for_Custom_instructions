# Have the function PrimeTime(num) take the num parameter being passed and return the string true if the parameter is
# a prime n as mumber, otherwise return the string false. The range will be between 1 and 2^16.
import math as m
def primetim(num):
    if num <2:
        return True
    else:
        print('false')
    for i in range(2,int(m.sqrt(num))):
        if num%i == 0:
            return False
        else :
            return True
print(primetim(int(input())))

#Have the function RunLength(str) take the str parameter being passed and return a compressed version of the string
# using the Run-length encoding algorithm. This algorithm works by taking the occurrence of each repeating character
# and outputting that number along with a single character of the repeating sequence. For example: "wwwggopp" would
# return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols.

def RunLength(s):
    result=''
    count = 1
    for i in range(1,len(s)):
        if s[i]== s[i-1]:
            count +=1
        else:
            result = str(count)+ s[i-1]
            count= 1
    result +=str(count) +s[-1]
    return result
print(RunLength(input("")))


#number of repeated letters
def RunLength(s):
    result = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += str(count) + s[i - 1]
            count = 1
    result += str(count) + s[-1]
    return result
print(RunLength(input("Enter a string: ")))

# Have the function PrimeMover(num) return the numth prime number. The range will be from 1 to 10^4.
# For example: if num is 16 the output should be 53 as 53 is the 16th prime number.
def PrimeMover(num):
    k=[]
    for i in range(1000):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            k.append(i)
    return k[num+1]
print(PrimeMover(int(input())))

# Have the function PalindromeTwo(str) take the str parameter being passed and return the string true if the parameter
# is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. The parameter
# entered may have punctuation and symbols but they should not affect whether the string is in fact a palindrome.
# For example: "Anne, I vote more cars race Rome-to-Vienna" should return true.
def PalindromeTwo(check):
    spec=('!@#$%^&*()_+{}|:"<>?/.,;]\[]')
    spec=list(spec)
    check =list(check)
    a = [x for x in check if x not in spec]
    if a == a[::-1]: 
        return True
    return False

print(PalindromeTwo("paigegi@@#ap"))


#  Have the function Division(num1,num2) take both parameters being passed and return the Greatest Common Factor........
# That is, return the greatest number that evenly goes into both numbers with no remainder. For example: 12 and 16 both.
# are divisible by 1, 2, and 4 so the output should be 4. The range for both parameters will be from 1 to 10^3..........
import math
def Division(num1, num2):
    d= math.gcd(num1,num2)
    return d
# Taking two inputs and calling the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(Division(num1, num2))


#  Using the Python language, have the function StringScramble(str1,str2) take both parameters being passed and return
# the string true if a portion of str1 characters can be rearranged to match str2, otherwise return the string false.
# For example: if str1 is "rkqodlw" and str2 is "world" the output should return true. Punctuation and symbols will
# not be entered with the parameters.

def StringScramble(str1,str2):
    str1=list(str1)
    str2=list(str2)
    a = [x for x in str2 if x not in str1]
    if len(a) ==0:
        return True
    return False
str1=input("")
str2=input("")
print(StringScramble(str1,str2))

# Have the function ArithGeoII(arr) take the array of numbers stored in arr and return the string "Arithmetic" if the
# sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern. If the sequence
# doesn't follow either pattern return -1. An arithmetic sequence is one where the difference between each of the
# numbers is consistent, where as in a geometric sequence, each term after the first is multiplied by some constant
# or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. Negative numbers may be
# entered as parameters, 0 will not be entered, and no array will contain all the same elements.aa
# Use the Parameter Testing feature in the box below to test your code with different arguments.
def Arr(arr):
#    arr = arr.split(',')
 #   arr = list(map(int, arr))
    is_arithmetic = True
    is_geometric = True

    for i in range(len(arr) - 2):
        if arr[i] - arr[i + 1] != arr[i + 1] - arr[i + 2]:
            is_arithmetic = False
        if arr[i] / arr[i + 1] != arr[i + 1] / arr[i + 2]:
            is_geometric = False

    if is_arithmetic:
        return 'Arithmetic'
    elif is_geometric:
        return 'Geometric'
    else:
        return "Invalid"
#arr=[5,10,15]
print(Arr(arr))
#print(Arr(input("Enter elements separated by commas: ")))


#  Using the Python language, have the function CaesarCipher(str,num) 
# take the str parameter and perform a Caesar Cipher
# shift on it using the num parameter as the shifting number. 
# A Caesar Cipher works by shifting each letter in the
# string N places down in the alphabet (in this case N will be num). 
# Punctuation, spaces, and capitalization should remain intact.
# For example if the string is "Caesar Cipher" and
# num is 2 the output should be "Ecguct Ekrjgt".



def CaesarCipher(string, num):
    result = ""
    for char in string:
        if char.isalpha():  
            shift = 65 if char.isupper() else 97  
            result += chr((ord(char) - shift + num) % 26 + shift)  
        else:
            result += char  
    return result
string = "Caesar Cipher"
num = 2
print(CaesarCipher(string, num))


# Using the Python language, have the function Consecutive(arr) take the array of integers stored in arr and return the
# minimum number of integers needed to make the contents of arr consecutive from the lowest number to the highest
# number. For example: If arr contains [4, 8, 6] then the output should be 2 because two numbers need to be added to the
#  array (5 and 7) to make it a consecutive array of numbers from 4 to 8. Negative numbers may be entered as parameters
# and no array will have less than 2 elements.
def Consecutive(arr):
    arr.sort()  # Sort the array in ascending order
    min_num, max_num = arr[0], arr[-1]  # Get the minimum and maximum values
    required_numbers = max_num - min_num + 1 - len(arr)  # Calculate the required numbers
    return required_numbers if required_numbers > 0 else 0

# Test the function
arr = [4, 6,10]
print(Consecutive(arr))


# Have the function NumberSearch(str) take the str parameter, search for all the numbers in the string, add them
# together, then return that final number divided by the total amount of letters in the string. For example: if str is
# "Hello6 9World 2, Nic8e D7ay!" the output should be 2. First if you add up all the numbers, 6 + 9 + 2 + 8 + 7 you get
# 32. Then there are 17 letters in the string. 32 / 17 = 1.882, and the final answer should be rounded to the nearest
# whole number, so the answer is 2. Only single digit numbers separated by spaces will be used throughout the whole
# string (So this won't ever be the case: hello44444 world). Each string will also have at least one letter.


def NumberSearch(a_str):
    num_total = 0
    num_letters = 0
    for char in a_str:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            num_letters += 1
        elif char in "0123456789":
            num_total += int(char)
    return round(float(num_total)/num_letters)

#  Using the Python language, have the function TripleDouble(num1,num2) take both parameters being passed, and return 1
# if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.
# For example: if num1 equals 451999277 and num2 equals 41177722899, then return 1 because in the first parameter you
# have the straight triple 999 and you have a straight double, 99, of the same number in the second parameter.
#  If this isn't the case, return 0.
def TripleDouble(num1, num2):
    num1_str, num2_str = str(num1), str(num2)
    for i in range(len(num1_str) - 2):
        if num1_str[i] == num1_str[i + 1] == num1_str[i + 2]:
            if num1_str[i] * 2 in num2_str:
                return 1
    return 0

# Test the function
num1 = 451999277
num2 = 41177722899
print(TripleDouble(num1, num2))

# Using the Python language, have the function LookSaySequence(num) take the num parameter being passed and return the
# next number in the sequence according to the following rule: to generate the next number in a sequence read off the
# digits of the given number, counting the number of digits in groups of the same digit. For example, the sequence
# beginning with 1 would be: 1, 11, 21, 1211, ... The 11 comes from there being "one 1" before it and the 21 comes
# from there being "two 1's" before it. So your program should return the next number in the sequence given num.

def LookSaySequence(num):
    num_str = str(num)
    result = ''
    count = 1

    for i in range(1, len(num_str)):
        if num_str[i] == num_str[i - 1]:
            count += 1
        else:
            result += str(count) + num_str[i - 1]
            count = 1

    result += str(count) + num_str[-1]

    return int(result)

# Test the function
num = 1211
print(LookSaySequence(num))


# Using the Python language, have the function NumberEncoding(str) take the str parameter and encode the message
# according to the following rule: encode every letter into its corresponding numbered position in the alphabet.
# Symbols and spaces will also be used in the input. For example: if str is "af5c a#!" then your program should
# return 1653 1#!.
def NumberEncoding(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_string = ""
    for char in s:
        if char.isalpha():
            if char.islower():
                encoded_string += str(alphabet.index(char) + 1)
            else:
                encoded_string += str(alphabet.index(char.lower()) + 1).upper()
        else:
            encoded_string += char
    return encoded_string

# Test the function
s = "af5c a#!"
print(NumberEncoding(s))

###array adddition nnn
def ArrayAddition(arr):
    max_num = max(arr)
    arr.remove(max_num)
    return arr

# Helper function to recursively check for combinations
def can_sum_to_target(target, numbers):
    if target == 0:
        return True
    if target < 0 or not numbers:
        return False
    return can_sum_to_target(target - numbers[0], numbers[1:]) or can_sum_to_target(target, numbers[1:])

# Check if combination sums up to the maximum number
def test_can_sum_to_max(arr):
    max_num = max(arr)
    return can_sum_to_target(max_num, arr)

# Example usage
arr = [6, 6, 23, 10, 1, 31]
result = ArrayAddition(arr)
print(result)  # This should print the array after removing the maximum number

#check alphabett
def StringChallenge(strParam):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in strParam:
            return "false"
    return "true"

# Example usage
print(StringChallenge("zacxyjbbkfgtbhdaielgrm45pnsowtu v")) 

##camel case
import re

def CamelCase(string):
    k='!@#$%^&*()_+=-[]{}|\:;<>?/.,'
    a=[x for x in word if x not in k]
    g="".join(a).upper()
    g=g.replace(' ',"")
    check =g[0].lower()
    kk=g.replace(g[0], check)
    return kk
print(CamelCase(input()))

