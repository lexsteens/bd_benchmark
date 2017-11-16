import pandas as pd
import timeit
import os

import utils





def benchmark_join(n_ids, min_card, max_card, fill_size):

    input_left_filename = utils.generate_input_filename(n_ids, min_card, max_card, fill_size, "left")
    input_right_filename = utils.generate_input_filename(n_ids, min_card, max_card, fill_size, "right")
    joined_filename = utils.generate_joined_filename(n_ids, min_card, max_card, fill_size)
    result_filename = utils.generate_joined_result_filename(n_ids, min_card, max_card, fill_size)

    wrapped = utils.wrapper(execute_join, input_left_filename, input_right_filename, joined_filename)
    t = timeit.timeit(wrapped, number=1)

    print(n_ids, t)
    with open(result_filename, "w") as rf:
        rf.write(str(t) + "\n")



def execute_join(input_left_filename, input_right_filename, joined_filename):
    dsl = pd.read_csv(input_left_filename, sep=";", header=None, names=['id', 'load'])
    dsr = pd.read_csv(input_right_filename, sep=";", header=None, names=['id', 'load'])
    ds_joined = pd.merge(dsl, dsr, on='id')
    ds_joined.to_csv(joined_filename, sep=";", header=False)




if __name__ == "__main__":
    print(os.path.dirname(os.path.realpath(__file__)))

    for n in [10, 1000, 10000, 100000]:
        benchmark_join(n, 1, 10, 128)

