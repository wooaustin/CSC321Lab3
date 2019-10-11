from Crypto.Hash import SHA256

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
def truncate_digest(d1, x):
    scale = 16
    num_bits = 8
    h = SHA256.new()
    h.update(d1)
    digest = h.hexdigest()
    digest_array = digest[:3]
    print(digest_array)
    bit_str = bin(int(digest_array, scale))[x:].zfill(num_bits)
    num_bits = 10
    bit_str_msb = bit_str[:num_bits]
    print(bit_str_msb, bit_str_lsb)
    #truncate_d1 = return_bits(d1_bytes)
    #truncate_d2 = return_bits(d2_bytes)
    
    
def task1_generate_digest():
    a = process_sha(b'tesr')
    b = process_sha(b'tess')
    compare_strings(a, b)
    return a,b


def main():
    # Task 1a
    #d1, d2 = task1_generate_digest()
    
    # Task 1b
    truncate_digest(b"test", 2)

main()
