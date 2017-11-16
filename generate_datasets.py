import uuid
import random
import string

def generate_datasets(n_ids=1000, min_card_left=1, max_card_left=10, min_card_right=1, max_card_right=10, fill_size=128):
    name = "ds"
    filename = name + "_n" + str(n_ids).zfill(8) + "_size" + str(fill_size).zfill(5)
    filename_left = filename + "_card" + str(max_card_left).zfill(3) + "_left"
    filename_right = filename + "_card" + str(max_card_right).zfill(3) + "_right"
    print(filename_left)
    print(filename_right)


    fl = open(filename_left, "w")
    fr = open(filename_right, "w")

    for n in range(0, n_ids):
        id = uuid.uuid4()
        card_left = random.randint(min_card_left, max_card_left)
        card_right = random.randint(min_card_right, max_card_right)

        for i in range(0, card_left):
            fill = ''.join(random.choice(string.ascii_lowercase) for x in range(fill_size))
            fl.write(str(id) + ';' + fill + "\n")

        for i in range(0, card_right):
            fill = ''.join(random.choice(string.ascii_lowercase) for x in range(fill_size))
            fr.write(str(id) + ';' + fill + "\n")

    fl.close()
    fr.close()


if __name__ == "__main__":

    for n in [1000, 10000, 100000, 1000000]:
        generate_datasets(n_ids = n, max_card_left=10, max_card_right=10, fill_size=128)
