import os
import random

def overwrite_file(file_path):
    """Overwrite a file with random data before deleting it"""
    try:
        with open(file_path, 'r+b') as f:
            length = os.path.getsize(file_path)
            for _ in range(length):
                f.write(bytes([random.randint(0, 255)]))
        os.remove(file_path)
        print(f"File {file_path} securely deleted.")
    except Exception as e:
        print(f"Error overwriting file {file_path}: {e}")

# Example usage
overwrite_file('/path/to/suspicious_file.enc')
