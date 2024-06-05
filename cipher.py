class BookCipher:
    def encrypt(self, text, key):
        encrypted = []
        for i, char in enumerate(text):
            encrypted_char = chr((ord(char) + ord(key[i % len(key)])) % 256)
            encrypted.append(encrypted_char)
        return ''.join(encrypted)
