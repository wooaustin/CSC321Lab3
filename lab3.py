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

    
def truncate_digest(d1, d2):
    mask_8 = 255
    masked_d1 = (b d1) & mask_8
    masked_d2 = ord(d2) & mask_8
    
    
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
