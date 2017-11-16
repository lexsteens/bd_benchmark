import pandas as pd
import timeit

import utils



def benchmark_sort(n_ids, min_card, max_card, fill_size, side):

    input_filename = utils.generate_input_filename(n_ids, min_card, max_card, fill_size, side)
    sorted_filename = utils.generate_sorted_filename(n_ids, min_card, max_card, fill_size, side)
    result_filename = utils.generate_sorted_result_filename(n_ids, min_card, max_card, fill_size, side)

    wrapped = utils.wrapper(execute_sort, input_filename, sorted_filename)
    t = timeit.timeit(wrapped, number=1)

    print(n_ids, t)
    with open(result_filename, "w") as rf:
        rf.write(str(t) + "\n")



def execute_sort(input_filename, sorted_filename):
    ds = pd.read_csv(input_filename, sep=";", header=None, names=['id', 'load'])
    ds_sorted = ds.sort_values('id')
    ds_sorted.to_csv(sorted_filename, sep=";", header=False)




if __name__ == "__main__":
    for n in [10, 1000, 10000, 100000, 1000000]:
        benchmark_sort(n, 1, 10, 128, "left")

