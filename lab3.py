from Crypto.Hash import SHA256

def process_sha(input):
    h = SHA256.new()
    h.update(input)
    print(h.hexdigest())
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
    
    
def truncate_digest(d1, d2):
    b = bytearray()
    d1_bytes = b.extend(map(ord,d1))
    d2_bytes = b.extend(map(ord,d2))
    truncate_d1 = return_bits(d1_bytes)
    truncate_d2 = return_bits(d2_bytes)
    
    
def task1_generate_digest():
    a = process_sha(b'tesr')
    b = process_sha(b'tess')
    compare_strings(a, b)
    return a,b


def main():
    # Task 1a
    d1, d2 = task1_generate_digest()
    
    # Task 1b
    truncate_digest(d1, d2)

main()
