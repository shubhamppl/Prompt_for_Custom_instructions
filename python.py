def FirstReverse(strParam):
    strParam=strParam[::-1]
    return strParam


print(FirstReverse(input()))
sas
sas
def FirstFactorial(num):
    k=1
    for i in range(num,0,-1):
        k *= i
    
    return k

# keep this function call here 
print(FirstFactorial(int(input())))
4
24
# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string.
# If there are two or more words that are the same length, return the first word from the string with that length.
# Ignore punctuation and assume sen will not be empty.

import re

def LongestWord(sen):
    # Remove punctuation from the string
    sen = re.sub(r'[^\w\s]', '', sen)

    # Split the string into words
    words = sen.split()

    # Find the longest word using the max function
    longest_word = max(words, key=len)

    return longest_word

# Example usage:
print(LongestWord("fundjd))(&!! time"))  # This will print "time"
fundjd
import re
def remove(s):
    s= re.sub(r'[^\w\s]','',s)
    word=s.split()
    long=max(word,key=len)
    return long
print(remove("fundjd))(&!! time"))  # This will print "time
fundjd
import re
def remove(s):
    s = re.sub(r'[^\w\s]', '', s)  # Remove non-alphanumeric characters
    words = s.split()  # Split the string into words
    longest_word = max(words, key=len)  # Find the longest word
    return longest_word
print(remove("fundjd))(&!! time"))  # This will print "time"
fundjd
def LetterChanges(a_string):
    result = ''
    for char in a_string:
        if char.isalpha():
            if char.lower() in 'aeiou':
                result += char.upper()
            else:
                if char.lower() == 'z':
                    result += 'a'
                elif char.lower() == 'd':
                    result += 'E'
                elif char.lower() == 'h':
                    result += 'I'
                elif char.lower() == 'n':
                    result += 'O'
                elif char.lower() == 't':
                    result += 'U'
                elif char.lower() == 'j':
                    result += 'J'
                else:
                    result += chr(ord(char) + 1)
        else:
            result += char
    return result

# Example usage
print(LetterChanges(input()))
dddd
EEEE
def letterchange(stringg):
    result=''
    for ch in stringg:
        if ch.isalpha():
            if ch.lower() in 'aeiou':
                result += ch.upper()
            elif ch.lower() == 'z':
                result += ch.upper()
            else:
                result += chr(ord(ch)+1)
            
    else:
        result += ch
        

    return result
print(letterchange(input())) 
lkdoijoidjqpojdpoqwjpd
mleOIkOIekrqOkeqOrxkqed
# Have the function SimpleAdding(num) add up all the numbers from 1 to num. For the test cases,
# the parameter num will be any number from 1 to 1000.

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def summ(x):
    k=[]
    for i in range(x+1):
        k.append(i)
    r=sum(k)
    return r
print(summ(int(input())))
3
6
# Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each
# word. Words will be separated by only one space.
def capp(x):
    k=x.title()
    return k

print(capp(input()))
djkjd kjjs
Djkjd Kjjs
# Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence
#  by either returning the string true or false. The str parameter will be composed of + and = symbols with several
# letters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol.
# So the string to the left would be false. The string will not be empty and will have at least one letter.
def SimpleSymbols(s):
    if s[0].isalpha() or s[-1].isalpha():  # Check if the first or last character is a letter
        return "false"

    for i in range(1, len(s) - 1):
        if s[i].isalpha():
            if s[i - 1] != '+' or s[i + 1] != '+':  # Check if the letter is not surrounded by '+'
                return "false"

    return "true"

# Example usage
print(SimpleSymbols(input()))  # This will print "false"
print(SimpleSymbols("+a+b+="))  # This will print "true"
++d+===+c++==a
false
true
def checkk(char):
    let='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    k = list(char)
    if k[0] != '+' or k[-1] != '+':
        return "False"
    for i in range(1,len(k)-1):
        if k[i] in letters:
            if k[i-1] !='+' or  k[i + 1] != '+':
                return "False"
    return 'true'    


print(checkk(input())) 
+a+b+=
False
def checkk(char):
    k = list(char)
    if k[0] != '+':
        return "false"
    if k[-1] != '+':
        return "false"
    for i in range(1, len(k) - 1):
        if k[i].isalpha():
            if k[i - 1] != '+' or k[i + 1] != '+':
                return "false"
    return 'true'

print(checkk(input()))
+a+b+=
false
def CheckNums(num1,num2):
   
    if num1 == num2:
        return -1
    return num2 > num1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Example usage
result = CheckNums(num1,num2)
print(result)
Enter the first number: 2
Enter the second number: 2
-1
# Using the Python language, have the function TimeConvert(num) take the num parameter being passed and return the
# number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3).
# Separate the number of hours and minutes with a colon.


def TimeConvert(num):
    hours = num // 60
    minutes = num % 60
    print(hours,':',minutes)

# Example usage
num = int(input("Enter the number to convert: "))
result = TimeConvert(num)
print(result)
Enter the number to convert: 33
0 : 33
0:33
# Have the function AlphabetSoup(str) take the str string parameter being passed and return the string with the letters
# in alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string.
def AlphabetSoup(str):
    
    return ''.join(sorted(str))

# Example usage
input_string = input("Enter a string: ")
result = AlphabetSoup(input_string)
print(result)
Enter a string: dsjdkj
ddjjks
string = input("Enter a string: ")
sorted_string = ''.join(sorted(string))
print(sorted_string)
Enter a string: KJDjdakjsljdA
ADJKaddjjjkls
def ABCheck(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] == 'a':
            if i + 4 < len(s) and s[i + 4] == 'b':
                return 'true'
    return 'false'

# Example usage
string = input("Enter a string: ")
result = ABCheck(string)
print(result)
Enter a string: djsj
false
def VowelCount(a_string):
    vowels = 'aeiou'
    vowel_count = 0
    for char in a_string.lower():
        if char in vowels:
            vowel_count += 1
    return vowel_count
def countv(a_string):
    vovel='aeiouAEIOU'
    kd=0
    for i in a_string:
        if i in vovel:
            kd += 1
    return kd
print(countv(input()))
aaaa
4
# Using the Python language, have the function WordCount(str) take the str string parameter being passed and return the
# number of words the string contains (ie. "Never eat shredded wheat" would return 4). Words will be separated by
# single spaces.
def WordCount(string):
    words = string.split(" ")
    return len(words)

print(WordCount(input()))
ajs s
2
#  Using the Python language, have the function ExOh(str) take the str parameter being passed and return the string true
# if there is an equal number of x's and o's, otherwise return the string false. Only these two letters will be entered
# in the string, no punctuation or numbers. For example: if str is "xooxxxxooxo" then the output should return false
# because there are 6 x's and 5 o's.
def countch(x):
    kk=0
    dd=0
    for i in x:
        if i == 'x':
            kk += 1
        elif i== 'o':
            dd += 1
    return dd==kk
            

print(countch(input()))
xoxo
True
def ArithGeo(arr):
    is_arithmetic = True
    is_geometric = True

    diff_arithmetic = arr[1] - arr[0]
    ratio_geometric = arr[1] / arr[0]

    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != diff_arithmetic:
            is_arithmetic = False

        if arr[i] / arr[i - 1] != ratio_geometric:
            is_geometric = False

    if is_arithmetic:
        return "Arithmetic"
    elif is_geometric:
        return "Geometric"
    else:
        return -1

# Example usage
test_array = [2, 4, 6, 8]  # Change this array to test with other inputs
print(ArithGeo(test_array))
Arithmetic
#  Using the Python language, have the function ArrayAdditionI(arr) take the array of numbers stored in arr and return
# the string true if any combination of numbers in the array can be added up to equal the largest number in the array,
# otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true
# because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the same elements, and may contain
def ArrayAdditionI(arr):
    max_num = max(arr)
    possible_totals = []
    arr.remove(max_num)

    for num in arr:
        possible_totals.append(num)
        num_total = num
        arr.remove(num)

        for other_num in arr:
            possible_totals.append(num + other_num)
            num_total += other_num
            possible_totals.append(num_total)

    if max_num in possible_totals:
        return "true"
    return "false"
false
#  Using the Python language, have the function SecondGreatLow(arr) take the array of numbers stored in arr and return
# the second lowest and second greatest numbers, respectively, separated by a space. For example: if arr contains
# [7, 7, 12, 98, 106] the output should be 12 98. The array will not be empty and will contain at least 2 numbers.
# It can get tricky if there's just two numbers!
def SecondGreatLow(arr):
    arr = sorted(set(arr))
    if len(arr) == 2:
        return f"{arr[1]} {arr[0]}"
    else:
        return f"{arr[1]} {arr[-2]}"

# Example usage
test_array = [7, 7, 12, 98, 106]  # Change this array to test with other inputs
print(SecondGreatLow(test_array))
