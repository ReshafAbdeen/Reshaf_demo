import hashlib
import json
import time


class SimpleBlockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof=100, previous_hash="1")

    def create_block(self, proof, previous_hash):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "proof": proof,
            "previous_hash": previous_hash,
        }
        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def proof_of_work(self, last_proof):
        new_proof = 1
        while not (
            hashlib.sha256(
                str(new_proof**2 - last_proof**2).encode()
            ).hexdigest()[:4]
            == "0000"
        ):
            new_proof += 1
        return new_proof


bc = SimpleBlockchain()
print("Mining block 1...")
last_block = bc.get_last_block()
proof = bc.proof_of_work(last_block["proof"])
previous_hash = bc.hash(last_block)
block = bc.create_block(proof, previous_hash)

print(f"Block Mined! {json.dumps(block, indent=2)}")