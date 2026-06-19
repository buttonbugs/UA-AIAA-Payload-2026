from datetime import datetime
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta

data_file_prefix = "DATA_"
data_file_suffix = ".CSV"
combined_filename = "combined.csv"
filtered_filename = "filtered.csv"
config_filename = "config.txt"

def get_py_dir():
    # Path dir processing
    py_file_path = Path(__file__).resolve()
    py_dir_path = py_file_path.parent
    return py_dir_path

def get_data_dir(py_dir: Path, data_folder: Path):
    return (py_dir / data_folder).resolve()

def get_data_file_path_list(data_dir: Path):
    # sorted() is important
    data_files = sorted([f.resolve() for f in data_dir.iterdir() if f.is_file() and f.name.startswith(data_file_prefix) and f.name.endswith(data_file_suffix)], key=lambda f: f.name)
    return data_files

def filter_data(data_files, combined_path: str, filtered_path: str):

    # Combine
    combined_str = ""
    column_title = "\n"
    for file in data_files:
        with open(file, "r") as f:
            file_str = f.read()
            file_str_splitted = file_str.split("\n", 1)
            column_title = file_str_splitted[0]
            file_str = file_str_splitted[1]
            combined_str += file_str

    # Filter
    data_packs = combined_str.split(column_title)
    data_packs_line_number = [len(data_pack.split("\n")) for data_pack in data_packs]
    largest_data_pack_index = data_packs_line_number.index(max(data_packs_line_number))
    print("Largest data pack index:", largest_data_pack_index)

    largest_data_pack = data_packs[largest_data_pack_index]
    filtered_str = column_title + largest_data_pack

    # Save files
    with open(combined_path, "w") as f:
        f.write(combined_str)

    with open(filtered_path, "w") as f:
        f.write(filtered_str)

class PayloadData():

    def __init__(self, data_folder:str, load_data:bool = True):

        # dir processing
        self.py_dir = get_py_dir()
        self.data_dir = get_data_dir(self.py_dir, data_folder)
        self.config_file_path = (self.data_dir / config_filename).resolve()

        self.combined_data_path = (self.py_dir / combined_filename).resolve()
        self.filtered_data_path = (self.py_dir / filtered_filename).resolve()

        # organize data files
        data_files = get_data_file_path_list(self.data_dir)
        filter_data(data_files, self.combined_data_path, self.filtered_data_path)

        # load config
        with open(self.config_file_path, "r") as f:
            config_str = f.read()
            self.starting_time = datetime.fromisoformat(config_str)

        if load_data:
            self.get_dict(self.filtered_data_path)
            self.calculate_abs_time()

    def get_dict(self, filtered_data_path):
        df = pd.read_csv(filtered_data_path, keep_default_na=True).fillna(0)    # keep_default_na = True: return NaN if empty; keep_default_na = False: return '' if empty; fillna(0) replace NaN with 0
        self.data = df.to_dict(orient='list')                                   # orient='list': a dictionary of lists; orient='records': a list of dictionaries

    def calculate_abs_time(self):
        self.data["datetime"] = [self.starting_time + timedelta(milliseconds=timestamp) for timestamp in self.data["Timestamp (ms)"]]

if __name__ == "__main__":
    payload_data = PayloadData("testing_20260617142200CDT")
    print(payload_data.data["datetime"])