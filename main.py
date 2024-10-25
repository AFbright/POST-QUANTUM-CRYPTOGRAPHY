import time
from ntru_algorithm import NTRU
from rainbow_algorithm import Rainbow
from mceliece_algorithm import McEliece
from pandes import save_results_to_excel

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return str(hash(str(self.index) + str(self.previous_hash) + str(self.transactions) + str(self.timestamp)))

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", [], time.time())

    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, transactions, time.time())
        self.chain.append(new_block)
        return new_block

def measure_performance(algorithm, algo_type, message=None):
    if algo_type == "encryption":
        public_key, private_key = algorithm.generate_keypair()
        encrypted_message = algorithm.encrypt(public_key, message)
        decrypted_message = algorithm.decrypt(private_key, encrypted_message)
    elif algo_type == "signature":
        public_key, private_key = algorithm.generate_keypair()
        signature = algorithm.sign(private_key, message)
        verification = algorithm.verify(public_key, message, signature)

    return {"public_key": public_key, "private_key": private_key, "result": encrypted_message if algo_type == "encryption" else verification}

def main():
    blockchain = Blockchain()

    ntru = NTRU()
    rainbow = Rainbow()
    mceliece = McEliece()

    algorithms = {
        "NTRU": {"algorithm": ntru, "type": "encryption"},
        "Rainbow": {"algorithm": rainbow, "type": "signature"},
        "McEliece": {"algorithm": mceliece, "type": "encryption"}
    }

    for algo_name, algo_info in algorithms.items():
        print(f"Running {algo_name} algorithm...")

        if algo_info["type"] == "encryption":
            message = algo_info["algorithm"].generate_message()
        else:
            message = algo_info["algorithm"].generate_message()

        result = measure_performance(algo_info["algorithm"], algo_info["type"], message)

def main():
    # Display and save results to Excel
    save_results_to_excel()

if __name__ == "__main__":
    main()
