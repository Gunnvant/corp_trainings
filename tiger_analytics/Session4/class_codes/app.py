from utils import Reader
path = "/Users/gunnvantsaini/Library/CloudStorage/OneDrive-Personal/Work/Vired/Content/corp_trainings/tiger_analytics/data/file_data.csv"

r = Reader(path)
data = r.read_flat_file(delimiter = ",")
col_names = r.col_names
num_rows = r.rows

print(f'The file has {num_rows} rows')
print(f'The column names are {col_names}')
print(data[0:5])