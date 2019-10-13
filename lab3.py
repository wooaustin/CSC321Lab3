from Crypto.Hash import SHA256
import math
from itertools import product
import os
import binascii
import time
import bcrypt
import nltk


def process_sha(input):
    h = SHA256.new()
    h.update(input)
    print(type(h.hexdigest()))
    return h.hexdigest()


def compare_strings(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            count += 1
    print(count)




def return_bits(d_bytes):
    a = []
    for i in range(len(d_bytes)):
        if i == 2:
            break
        a.append(d_bytes[i])
    return a

# For a given string input, compute the digest and return the truncated 8-bits
def truncate_digest(str, num_bits):
    scale = 16
    hex_val = math.ceil(num_bits/4)
    h = SHA256.new()
    h.update(str.encode('utf-8'))
    digest = h.hexdigest()
    digest_array = digest[:hex_val]
    #print(digest_array)
    bit_str = bin(int(digest_array, scale))[2:].zfill(num_bits)
    bit_str_msb = bit_str[:num_bits]
    #print(bit_str_msb)
    return bit_str_msb
    #print(bit_str_msb, bit_str_lsb)

# given a length this function will
# create all possible strs of that length
def str_perm_gen(str_len):
    return([''.join(x) for x in product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=str_len)])

def task1_generate_digest():
    a = process_sha(b'tesr')
    b = process_sha(b'tess')
    compare_strings(a, b)
    return a,b

# Finds the collision for the given bit_input_size
def find_collisions(bits):
    string_length = 4
    start = time.time()
    input_size = 0
    bit_size = bits
    while string_length < 50:
        perm_list = str_perm_gen(string_length)
        collision_dict = {}
        # Iterate through all permutations for string_length
        for perm in perm_list:
            input_size += 1
            trunced_dig = truncate_digest(perm,bit_size)
            # Collision is found, reset everything for next bit_size
            if trunced_dig in collision_dict:
                # print(trunced_dig)
                # print(collision_dict[trunced_dig], perm)
                end = time.time()
                print("Digest size: " + str(bit_size) + " Input Number: "+ str(input_size) + " Total Time: " + str(end - start))
                return bit_size, input_size, (end - start)
            else:
                collision_dict[trunced_dig] = perm
        # Only gets here if no collision is found
        string_length += 1


def write_file(bit_size, inputs_size, time):
    f = open("output.dat", "w")
    for i in range(len(bit_size)):
        f.write("Bitsize: " + str(bit_size[i]) + " Input size: " + str(inputs_size[i]) + " Time: " + str(time[i]) + "\n")
    f.close()


def task_1b():
    bits = 8
    b = []
    inputs = []
    time_list = []
    while bits < 52:
        bit_size, input_size, time = find_collisions(bits)
        b.append(bit_size)
        inputs.append(input_size)
        time_list.append(time)
        bits += 2
    write_file(b, inputs, time_list)


def openShadowFile():
    f = open("shadow.txt")
    count = 0
    group1Names = ["Bilbo", "Gandalf", "Thorin"]
    group2Names = ['Fili', 'Kili']
    group3Names = ['Balin', 'Dwalin', 'Oin']
    group4Names = ['Gloin', 'Dori', 'Nori']
    group5Names = ['Ori', 'Bifur', 'Bofur']
    group6Names = ['Durin']
    group1Hash = ['$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnm', '$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC', '$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q']
    group2Hash = ['$M9xNRFBDn0pUkPKIVCSBzuwNDDNTMWlvn7lezPr8IwVUsJbys3YZm', '$M9xNRFBDn0pUkPKIVCSBzuPD2bsU1q8yZPlgSdQXIBILSMCbdE4Im']
    group3Hash = ['$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom','$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be', '$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK']
    group4Hash = ['$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q','$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq', '$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12']
    group5Hash = ['$rMeWZtAVcGHLEiDNeKCz8OiERmh0dh8AiNcf7ON3O3P0GWTABKh0O','$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK', '$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O']
    group6Hash = ['$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay']
    groups_name = []
    groups_hash = []
    groups_name.append(group1Names)
    groups_name.append(group2Names)
    groups_name.append(group3Names)
    groups_name.append(group4Names)
    groups_name.append(group5Names)
    groups_name.append(group6Names)
    groups_hash.append(group1Hash)
    groups_hash.append(group2Hash)
    groups_hash.append(group3Hash)
    groups_hash.append(group4Hash)
    groups_hash.append(group5Hash)
    groups_hash.append(group6Hash)
    print(groups_name, groups_hash)
    return groups_name, groups_hash

def getWords():
    words = []
    for book in nltk.corpus.gutenberg.fileids():
        for word in nltk.corpus.gutenberg.words(book):
            if len(word) >= 6 or len(word) <=10:
                words.append(word.encode('utf-8'))
    return words


def task_2():
    group_user, group_hash = openShadowFile()
    exit()
    words = getWords()
    salts = []
    salts.append("J9FW66ZdPI2nrIMcOxFYI.")
    salts.append("M9xNRFBDn0pUkPKIVCSBzu")
    salts.append("xGKjb94iwmlth954hEaw3O")
    salts.append("/8UByex2ktrWATZOBLZ0Du")
    salts.append("rMeWZtAVcGHLEiDNeKCz8O")
    salts.append("6ypcazOOkUT/a7EwMuIjH.")
    salts_and_hashes = ['$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnm', '$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC', '$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q',
    '$M9xNRFBDn0pUkPKIVCSBzuwNDDNTMWlvn7lezPr8IwVUsJbys3YZm', '$M9xNRFBDn0pUkPKIVCSBzuPD2bsU1q8yZPlgSdQXIBILSMCbdE4Im', '$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom',
    '$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be', '$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK', '$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q',
    '$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq', '$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12', '$rMeWZtAVcGHLEiDNeKCz8OiERmh0dh8AiNcf7ON3O3P0GWTABKh0O',
    '$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK', '$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O', '$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay']
    users = ["Bilbo", "Gandalf", "Thorin",'Fili', 'Kili','Balin', 'Dwalin', 'Oin', 'Gloin', 'Dori', 'Nori','Ori', 'Bifur', 'Bofur','Durin']
    # TODO Finish here salts are indexed according to group
    # group_user is list of string lists
    # group_hash is list of string lists
    # Word is a list of words we are suppose to try
    # 1. Loop through all words for each salt, hash each word
    # 2. Check the output of each hash with the hash for the associated name
    # 3. Check the entire salt group at a time to reduce the amount of hashing
    # 4. If match, remove the name/hash from the list so you reduce comparisons
    # 5. Once you find a match for each person, move onto the next group
    users_and_pws = []
    for word in words:
        for i in range(len(users)):
            # this will check the word to see if it is the pw that resulted
            # in the salt.hash string
            if bcrypt.checkpw(word,salts_and_hashs[i]):
                user_and_pws.add((users[i],word))
                salts_and_hashes.remove(salts_and_hashes[i])
                users.remove(users[i])
                print(users_and_pws)

    with open('users_passwords.txt', 'w') as file:
        file.write(users_and_pws)





def main():
    # Task 1a
    #d1, d2 = task1_generate_digest()

    # Task 1b
    #task_1b()

    # Task 2
    task_2()



main()
