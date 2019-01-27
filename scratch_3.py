single_digits = ["zero", "one", "two", "three","four", "five", "six", "seven", "eight", "nine"]

    # The first string is not used,
    # it is to make array indexing simple
two_digits = ["", "ten", "eleven", "twelve","thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen","nineteen"]

    # The first two string are not used,
    # they are to make array indexing simple
tens_multiple = ["", "", "twenty", "thirty", "forty","fifty", "sixty", "seventy", "eighty","ninety"]

tens_power = ["hundred", "thousand"];
letter = 0
for i in range (1,1000,1):
    if 1<=i<10:
        letter += len(single_digits[0])
    elif 10<=i<20:
        letter += len(two_digits[0])
    elif 20<=i<100:
        letter += len(tens_multiple[0]+single_digits[0])
    else:
        letter += len(tens_power[0]+tens_multiple[0]+single_digits[0])
print(letter)

