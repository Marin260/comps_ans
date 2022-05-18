digits = int(input())
words = input().split()

help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero' : '0'
}
numbers = ""
for i in range(digits):
    numbers += help_dict[words[i]]

numbers = int(numbers)
age = (numbers*525600)
print(age%1000000007)