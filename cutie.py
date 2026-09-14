class CaesarCipher:

    def __init__(self, shift: int):
        self.shift = shift % 26

    def _transform(self, text: str, shift: int) -> str:
        result = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shift) % 26 + base
                result.append(chr(shifted))
            else:
                result.append(char)
        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return self._transform(plaintext, self.shift)

    def decrypt(self, ciphertext: str) -> str:
        return self._transform(ciphertext, -self.shift)


cipher = CaesarCipher(shift=3)
message = "Hello, World! 2026"

encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")