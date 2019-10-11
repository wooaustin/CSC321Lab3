from Crypto.Hash import SHA256
import math
from itertools import product
import os
import binascii
import time


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
    

def main():
    # Task 1a
    #d1, d2 = task1_generate_digest()

    # Task 1b
    task_1b()
    

main()
