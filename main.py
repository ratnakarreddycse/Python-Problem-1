import csv

def parse_spec_file(spec_file):
    spec = []
    with open(spec_file, 'r') as f:
        for line in f:
            field, length = line.strip().split(':')
            spec.append((field, int(length)))
    return spec

def parse_fixed_width_file(spec, input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    parsed_data = []
    for line in lines:
        record = []
        start = 0
        for field, length in spec:
            record.append(line[start:start + length].strip())  # Slicing based on length
            start += length
        parsed_data.append(record)
    return parsed_data

def write_csv_file(output_file, spec, parsed_data):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        headers = [field for field, length in spec]
        writer.writerow(headers)
        writer.writerows(parsed_data)

if __name__ == "__main__":
    spec = parse_spec_file('spec.txt')
    parsed_data = parse_fixed_width_file(spec, 'fixed_width_file.txt')
    write_csv_file('output.csv', spec, parsed_data)
    print("CSV file generated successfully!")
