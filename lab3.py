from Crypto.Hash import SHA256

def process_sha(input):
    h = SHA256.new()
    h.update(input)
    print(h.hexdigest())


def main():
    # Task 1
    process_sha(b'tesr')
    process_sha(b'tess')

main()
