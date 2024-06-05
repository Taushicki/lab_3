class LFSR:
    def __init__(self, seed, taps):
        self.state = seed
        self.taps = taps
        self.n = len(bin(seed)) - 2

    def next(self):
        bit = sum([(self.state >> t) & 1 for t in self.taps]) % 2
        self.state = (self.state >> 1) | (bit << (self.n - 1))
        return self.state


def generate_lfsr_key(seed, taps, length):
    lfsr = LFSR(seed, taps)
    key = []
    for _ in range(length):
        key.append(chr(lfsr.next() % 256))
    return ''.join(key)
