#!/usr/bin/env python3

one = ["", "one ", "two ", "three ", "four ",
       "five ", "six ", "seven ", "eight ",
       "nine ", "ten ", "eleven ", "twelve ",
       "thirteen ", "fourteen ", "fifteen ",
       "sixteen ", "seventeen ", "eighteen ",
       "nineteen "]

ten = ["", "", "twenty ", "thirty ", "forty ",
       "fifty ", "sixty ", "seventy ", "eighty ",
       "ninety "]


def numToWords(n, s):
    str = ""
    if (n > 19):
        str += ten[n // 10] + one[n % 10]
    else:
        str += one[n]
    if (n):
        str += s
    return str


def convertToWords(n):
    out = ""
    if n >= 100:
        out += numToWords((n // 10000000), "crore ")
        out += numToWords(((n // 100000) % 100), "lakh ")
        out += numToWords(((n // 1000) % 100), "thousand ")
        out += numToWords(((n // 100) % 10), "hundred ")
        if (n > 100 and n % 100):
            out += "and "
            out += numToWords((n % 100), "")
    else:
        out += numToWords(n, "")
    return out


with open("numbers.txt", "r") as f:
    numbers = f.read().split("\n")[:-1]
for n in numbers:
    print(convertToWords(int(n)))
