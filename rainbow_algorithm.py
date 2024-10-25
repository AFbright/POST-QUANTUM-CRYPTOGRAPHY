import random
import hashlib


class Rainbow:
    def __init__(self, num_vars=12):
        self.num_vars = num_vars

    def generate_keypair(self):
        private_key = self.__generate_private_key()
        public_key = self.__generate_public_key(private_key)
        return public_key, private_key

    def sign(self, private_key, message):
        hashed_message = self.__hash_message(message)
        signature = self.__apply_private_key(private_key, hashed_message)
        return signature

    def verify(self, public_key, message, signature):
        hashed_message = self.__hash_message(message)
        verification = self.__apply_public_key(public_key, signature)
        return hashed_message == verification

    def __generate_private_key(self):
        return [random.randint(1, 255) for _ in range(self.num_vars)]

    def __generate_public_key(self, private_key):
        return [x * 2 for x in private_key]

    def __apply_private_key(self, private_key, message):
        return [x + y for x, y in zip(private_key, message)]

    def __apply_public_key(self, public_key, signature):
        return [s - p for s, p in zip(signature, public_key)]

    def __hash_message(self, message):
        return list(hashlib.sha256(message.encode()).digest())[:self.num_vars]

    def generate_message(self):
        return ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10))

    def verify_signature(self, original_message, signature, public_key):
        return self.verify(public_key, original_message, signature)


def demo_rainbow():
    rainbow = Rainbow()
    public_key, private_key = rainbow.generate_keypair()
    message = rainbow.generate_message()
    signature = rainbow.sign(private_key, message)
    verification = rainbow.verify(public_key, message, signature)

    print(f"Message: {message}")
    print(f"Signature: {signature}")
    print("Verification:", verification)


if __name__ == "__main__":
    demo_rainbow()
