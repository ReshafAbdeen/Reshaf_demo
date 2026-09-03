import string


class Cipher:

    def __init__(self, shift=3):
        self.shift = shift % 26
        self.alphabet = string.ascii_lowercase

    def encrypt(self, text):
        result = []
        for char in text:
            if char.lower() in self.alphabet:
                base = "a" if char.islower() else "A"
                shifted = chr((ord(char) - ord(base) + self.shift) % 26 + ord(base))
                result.append(shifted)
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, text):
        original_shift = self.shift
        self.shift = -self.shift
        decrypted = self.encrypt(text)
        self.shift = original_shift
        return decrypted


caesar = Cipher(shift=5)
secret_msg = "Hello, World! Python 101."
encrypted = caesar.encrypt(secret_msg)
decrypted = caesar.decrypt(encrypted)

print(f"Original:  {secret_msg}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")