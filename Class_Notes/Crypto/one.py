# plain text ABCDEFGHIJKLMNOPQRSTUVWXYZ
# cyphertext DEFGHIJKLMNOPQRSTUVWXYZABC
# So "HELLO" becomes "KHOOR"

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = input("Enter Message, Like Hello: ")
shift = int(input("Shift value, like 13: "))
l = len(str_in)

str_out = ""

for i in range(l):
    c = str_in[i]
    loc = alpha.find(c)
    print(i, c, loc, end="")
    new_loc = (loc + shift)%26
    str_out += alpha[new_loc]
    print(f' {new_loc} {str_out}')

print("Obfuscated version: ", str_out)