from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import os
import sys

class Decryptor:
    def __init__(self, key=None):
        if key is None:
            self.key = self.generate_random_key()  # Default random key (replace with actual ransomware key)
        else:
            self.key = key

    def generate_random_key(self):
        """ Generate a random AES-256 key """
        return get_random_bytes(32)

    def decrypt_file(self, encrypted_file_path, output_file_path):
        """ Decrypt an encrypted file using AES """
        try:
            # Open the encrypted file in binary mode
            with open(encrypted_file_path, 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()
            
            # Extract IV (first 16 bytes)
            iv = encrypted_data[:16]
            encrypted_message = encrypted_data[16:]

            # Create AES cipher object
            cipher = AES.new(self.key, AES.MODE_CBC, iv)

            # Decrypt and remove padding
            decrypted_data = unpad(cipher.decrypt(encrypted_message), AES.block_size)

            # Save the decrypted content
            with open(output_file_path, 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)
            
            print(f"✅ File successfully decrypted and saved to: {output_file_path}")
        
        except Exception as e:
            print(f"❌ Error decrypting file: {e}")
            sys.exit(1)

# Example Usage (For Testing)
if __name__ == "__main__":
    encrypted_file_path = "C:/Users/Mohit/OneDrive/Desktop/Project/Ransomeware/data/testfile.enc"
    output_file_path = "C:/Users/Mohit/OneDrive/Desktop/Project/Ransomeware/data/file1"

    decryptor = Decryptor()  # Create Decryptor instance with a random key
    decryptor.decrypt_file(encrypted_file_path, output_file_path)
