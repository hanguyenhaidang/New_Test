fn=input('Enter a String: ')
def CheckVowelsDigits(n):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    digit = 0
    vowel = 0
    for i in n: 
        if i in numbers:
            digit += 1
        for j in vowels:
                if i == j:
                    vowel += 1

    percentages_vowels = (vowel/len(n)) * 100
    percentages_digits = (digit/len(n)) * 100
    print('Number of vowels: ' , vowel , "%.2f" % percentages_vowels)
    print('Number of digits: ' , digit , " %.2f" % percentages_digits)
CheckVowelsDigits(fn)