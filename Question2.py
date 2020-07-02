'''
(a) Write a program that converts Roman numerals into ordinary numbers. Here are the
conversions: M=1000, D=500, C=100, L=50, X=10, V=5 I=1. Don’t forget about things
like IV being 4 and XL being 40.
(b) Write a program that converts ordinary numbers into Roman numerals
'''

roman_numerals_dict = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
roman_to_number = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}

# Function converts number to roman numerals.
def convert(user_input):
    roman_numerals = []
    for key in roman_numerals_dict.keys():
        x, y = divmod(user_input, key)
        roman = roman_numerals_dict[key] * x
        roman_numerals.append(roman)

        user_input -= (key * x)

        if user_input <= 0:
            break

    return "".join(roman_numerals)

# Function converts roman numberals to number.
def to_numbers(user_input):
    number = []
    k = 0

    while k < len(user_input):
        if k+1 < len(user_input) and user_input[k:k+2] in roman_to_number:
            x = roman_to_number[user_input[k:k+2]]
            number.append(x)
            k += 2
        else:
            x = roman_to_number[user_input[k]]
            number.append(x)
            k += 1

    return(sum(number))

user_input = input("Enter a roman numeral: ")

print(to_numbers(user_input))








