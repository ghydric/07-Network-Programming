"""
A-Z 0-25
a-z 26-51
0-9 52-62
+,/ 63,64
"""
# the encoded string to decode
encoded_string = ""
# function that creates and returns a base64 dictionary with [key = char, value = index]
def create_base64_dict():
    # setup all base64 characters
    u_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l_alpha = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    sp_chars = "+/="

    # base64 character groups
    groups64 = [u_alpha, l_alpha, digits, sp_chars]

    # initialize index value
    index = 0

    # initialize base64 dictionary
    base64_dict = {}

    # loop through each group
    for group in groups64:
        # loop through each character in each group and assign the correct index value to it
        for c in group:
            # add to base64 dictionary
            base64_dict.update({c: index})
            # increment index
            index += 1
    
    # return the base64_list
    return base64_dict

# function that takes in a base64 encoded string and returns a list of correlating indices
def convert_string_to_indices(enc_str, dict_64):
    # instantiate list of indices
    indices_list = []
    # loop through each letter in encoded string and add correct index to indices_list
    for letter in enc_str:
        indices_list.append(dict_64[letter])
    return indices_list


# function that takes in list of indices and returns a concatenated binary string
def create_binary_string(ind_list):
    for i in ind_list:
        pass




# create the base64 dictionary
base64 = create_base64_dict()

# get a list of indices for each encoded character
indices = convert_string_to_indices(encoded_string, base64)