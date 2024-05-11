import csv

def parse_csv_file(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

# Example usage:
file_path = 'example.csv'  # Replace 'example.csv' with the path to your CSV file
parsed_data = parse_csv_file(file_path)
for row in parsed_data:
    print(row)
