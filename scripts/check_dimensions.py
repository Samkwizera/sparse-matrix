import os

def get_dimensions(file_path):
    with open(file_path, 'r') as f:
        rows_line = f.readline().strip()
        cols_line = f.readline().strip()
        rows = int(rows_line.split('=')[1])
        cols = int(cols_line.split('=')[1])
    return rows, cols

def main():
    sample_input_dir = 'sample_input'
    files = os.listdir(sample_input_dir)
    dimensions = {}
    for file in files:
        file_path = os.path.join(sample_input_dir, file)
        try:
            rows, cols = get_dimensions(file_path)
            dimensions[file] = (rows, cols)
        except Exception as e:
            print(f"Error reading {file}: {e}")
    print("File dimensions:")
    for file, (rows, cols) in dimensions.items():
        print(f"{file}: rows={rows}, cols={cols}")
    print("\nCompatible pairs for multiplication:")
    for file1, (rows1, cols1) in dimensions.items():
        for file2, (rows2, cols2) in dimensions.items():
            if cols1 == rows2:
                print(f"{file1} ({rows1}x{cols1}) * {file2} ({rows2}x{cols2})")

if __name__ == "__main__":
    main() 