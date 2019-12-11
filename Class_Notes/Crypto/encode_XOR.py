text = input('Enter text: ')
key = input('Enter key: ')
l = len(text)

for i in range(l):
    # get single character from text variable
    t = text[i]
    # get single character of key by getting the remainder after dividing index by length of key.
    # modulus provides the way that you will always get an index of the key to XOR with a character from text
    k = key[i % len(key)]
    # XOR the ord
    x = ord(k) ^ ord(t)
    print(t, k, x, chr(x))