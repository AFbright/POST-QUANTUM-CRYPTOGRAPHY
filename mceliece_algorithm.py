import random


class McEliece:
    def __init__(self, n=10, t=3):
        self.n = n
        self.t = t

    def generate_keypair(self):
        public_key = self.__generate_matrix(self.n)
        private_key = self.__generate_error_vector(self.n, self.t)
        return public_key, private_key

    def encrypt(self, public_key, message):
        error_vector = self.__generate_error_vector(self.n, self.t)
        encoded_message = self.__encode_message(public_key, message, error_vector)
        return encoded_message

    def decrypt(self, private_key, encoded_message):
        return self.__decode_message(encoded_message, private_key)

    def __generate_matrix(self, n):
        return [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]

    def __generate_error_vector(self, n, t):
        error_vector = [0] * n
        error_indices = random.sample(range(n), t)
        for i in error_indices:
            error_vector[i] = 1
        return error_vector

    def __encode_message(self, public_key, message, error_vector):
        encoded_message = [(sum(m * p for m, p in zip(row, message)) + e) % 2 for row, e in
                           zip(public_key, error_vector)]
        return encoded_message

    def __decode_message(self, encoded_message, private_key):
        return [(m - e) % 2 for m, e in zip(encoded_message, private_key)]

    def generate_message(self):
        return [random.randint(0, 1) for _ in range(self.n)]

    def verify(self, original_message, decrypted_message):
        return original_message == decrypted_message


def demo_mceliece():
    mceliece = McEliece()
    public_key, private_key = mceliece.generate_keypair()
    message = mceliece.generate_message()
    encoded_message = mceliece.encrypt(public_key, message)
    decoded_message = mceliece.decrypt(private_key, encoded_message)

    print(f"Original Message: {message}")
    print(f"Decoded Message: {decoded_message}")
    print("Verification:", mceliece.verify(message, decoded_message))


if __name__ == "__main__":
    demo_mceliece()
