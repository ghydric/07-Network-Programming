"""
## Challenge 1 – the Caesar cipher
Your challenge is to decipher this string: MYXQBKDEVKDSYXC
"""
# alphabet letters
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# string to decipher
str_in = "MYXQBKDEVKDSYXC"
# length of string to decipher
l = len(str_in)
# set the character shift start
shift = 1
# loop and add 1 to shift until you have reached the max shift of 25
while shift <= 25:
    # deciphered string
    str_out = ""
    # start looping through each index of string to decipher
    for i in range(l):
        # save the current character in string to decipher
        c = str_in[i]
        # find the location in the alphabet list
        loc = alpha.find(c)
        #print(i, c, loc, end="")
        # new location of character after shift
        new_loc = (loc + shift)%26
        # add letter to output string
        str_out += alpha[new_loc]
    print(f'{shift} {str_out}')
    # add 1 to shift
    shift += 1

# The answer is shift = 16 to make the string "CONGRATULATIONS"