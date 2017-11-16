import pandas as pd

import utils

def benchmark_sort(n_ids, min_card, max_card, fill_size, side):
    output_dir = utils.get_output_dir()
    utils.create_dir(output_dir)


    input_filename = utils.generate_input_filename(n_ids, min_card, max_card, fill_size, side)
    sorted_filename = utils.generate_sorted_filename(n_ids, min_card, max_card, fill_size, side)
    print(input_filename)
    print(sorted_filename)

    ds = pd.read_csv(input_filename, sep=";", header=None, names=['id', 'load'])
    ds_sorted = ds.sort_values('id')
    ds_sorted.to_csv(sorted_filename, sep=";", header=False)



if __name__ == "__main__":
    benchmark_sort(10, 1, 10, 128, "left")