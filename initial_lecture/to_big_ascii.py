import sys
import time

def to_big_ascii(c):
    # Check if the character is an alphabet letter
    c = chr(c)
    if c.isalpha():
        # Convert to big ASCII character
        return chr(ord(c.upper()) - ord('A') + 65)
    else:
        # Return None for non-alphabetic characters
        return None

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py filename.txt")
        sys.exit(1)

    # Get the filename from the command line arguments
    filename = sys.argv[1]

    try:
        # Open the file in read mode
        with open(filename, 'rb') as file:
            # Infinite loop for continuous output
            while True:
                # Move the file pointer to the beginning of the file
                file.seek(0)

                # Read the content of the file
                content = file.read()

                # Convert each character to big ASCII and print to stdout
                for char in content:
                    result = to_big_ascii(char)
                    if result is not None:
                        print(result, end='', flush=True)

                # Add a delay to control the output speed (adjust as needed)
                time.sleep(0.1)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
