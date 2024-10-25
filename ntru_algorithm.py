import random


class NTRU:
    def __init__(self, N=11, p=3, q=32):
        self.N = N
        self.p = p
        self.q = q

    def generate_keypair(self):
        f = self.__generate_polynomial()
        g = self.__generate_polynomial()
        public_key = self.__polynomial_mod(f, g)
        private_key = f
        return public_key, private_key

    def encrypt(self, public_key, message):
        e = self.__generate_polynomial()
        return self.__polynomial_mod(message * public_key + e)

    def decrypt(self, private_key, ciphertext):
        return self.__polynomial_mod(ciphertext * private_key)

    def __generate_polynomial(self):
        return [random.randint(-1, 1) for _ in range(self.N)]

    def __polynomial_mod(self, a, b=None):
        if b:
            return [(ai * bi) % self.q for ai, bi in zip(a, b)]
        return [ai % self.q for ai in a]

    def __polynomial_add(self, a, b):
        return [(ai + bi) % self.q for ai, bi in zip(a, b)]

    def __polynomial_multiply(self, a, b):
        result = [0] * (len(a) + len(b) - 1)
        for i in range(len(a)):
            for j in range(len(b)):
                result[i + j] = (result[i + j] + a[i] * b[j]) % self.q
        return result[:self.N]

    def generate_message(self):
        return [random.randint(0, self.p - 1) for _ in range(self.N)]

    def verify(self, original_message, decrypted_message):
        return original_message == decrypted_message


def demo_ntru():
    ntru = NTRU()
    public_key, private_key = ntru.generate_keypair()
    message = ntru.generate_message()
    ciphertext = ntru.encrypt(public_key, message)
    decrypted_message = ntru.decrypt(private_key, ciphertext)

    print(f"Original Message: {message}")
    print(f"Decrypted Message: {decrypted_message}")
    print("Verification:", ntru.verify(message, decrypted_message))


if __name__ == "__main__":
    demo_ntru()
