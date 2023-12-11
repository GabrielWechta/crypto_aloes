import sys

def shift_cipher(text, shift):
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def main():
    if len(sys.argv) != 2:
        print("Usage: python shift_cipher.py <shift_key>")
        sys.exit(1)

    try:
        shift_key = int(sys.argv[1])
    except ValueError:
        print("Error: Shift key must be an integer.")
        sys.exit(1)

    buffer_size = 1024
    input_buffer = sys.stdin.buffer
    output_buffer = sys.stdout.buffer

    while True:
        chunk = input_buffer.read(buffer_size)
        if not chunk:
            break
        print(shift_key)
        encrypted_chunk = shift_cipher(chunk.decode('utf-8'), shift_key)
        output_buffer.write(encrypted_chunk.encode('utf-8'))
        output_buffer.flush()

if __name__ == "__main__":
    main()
