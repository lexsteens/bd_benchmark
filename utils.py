import os




def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def get_data_dir():
    dir = "data"
    create_dir(dir)
    return dir

def get_input_dir():
    dir = os.path.sep.join([get_data_dir(), "input"])
    create_dir(dir)
    return dir

def get_output_dir():
    dir = os.path.sep.join([get_data_dir(), "output"])
    create_dir(dir)
    return dir

def get_result_dir():
    dir = os.path.sep.join([get_data_dir(), "results"])
    create_dir(dir)
    return dir






########################################


def generate_characteristics(n_ids, min_card, max_card, fill_size):
    return "_n" + str(n_ids).zfill(8) + "_size" + str(fill_size).zfill(5) + "_card" + str(min_card).zfill(3) + "-" + str(max_card).zfill(3)

def generate_input_filename(n_ids, min_card, max_card, fill_size, side):
    filename = "ds" + generate_characteristics(n_ids, min_card, max_card, fill_size) + "_" + side + ".csv"
    return os.path.sep.join([get_input_dir(), filename])

def generate_sorted_filename(n_ids, min_card, max_card, fill_size, side):
    filename = "ds_sorted" + generate_characteristics(n_ids, min_card, max_card, fill_size) + "_" + side + ".csv"
    return os.path.sep.join([get_output_dir(), filename])

def generate_sorted_result_filename(n_ids, min_card, max_card, fill_size, side):
    filename = "sorted_result" + generate_characteristics(n_ids, min_card, max_card, fill_size) + "_" + side + ".txt"
    return os.path.sep.join([get_result_dir(), filename])

def generate_joined_filename(n_ids, min_card, max_card, fill_size):
    filename = "ds_joined" + generate_characteristics(n_ids, min_card, max_card, fill_size) + ".csv"
    return os.path.sep.join([get_output_dir(), filename])

def generate_joined_result_filename(n_ids, min_card, max_card, fill_size):
    filename = "joined_result" + generate_characteristics(n_ids, min_card, max_card, fill_size) + ".txt"
    return os.path.sep.join([get_result_dir(), filename])






########################################


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped