from cipher import BookCipher
from LFSR import generate_lfsr_key
from build_histogram import BuildHistogram


def read_file():
    with open("text.txt", 'r') as file:
        return file.read()


if __name__ == "__main__":
    text = read_file()

    constant_key = chr(14) * len(text)

    proverb = "Проживет Фаддей и без затей"
    proverb_key = (proverb * (len(text) // len(proverb) + 1))[:len(text)]

    lfsr_key = generate_lfsr_key(seed=0b10101, taps=[0, 2, 3, 4], length=len(text))

    BuildHistogram(BookCipher().encrypt(text, constant_key), 'Constant key')
    BuildHistogram(BookCipher().encrypt(text, proverb_key), 'Proverb key')
    BuildHistogram(BookCipher().encrypt(text, proverb_key), 'LFSR key')
