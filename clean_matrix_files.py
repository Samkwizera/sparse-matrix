import os

def clean_matrix_file(file_path, output_path):
    with open(file_path, 'r') as f_in, open(output_path, 'w') as f_out:
        rows_line = f_in.readline().strip()
        cols_line = f_in.readline().strip()
        if not rows_line.startswith('rows=') or not cols_line.startswith('cols='):
            print(f"Skipping {file_path}: invalid header format.")
            return
        rows = int(rows_line.split('=')[1])
        cols = int(cols_line.split('=')[1])
        f_out.write(rows_line + '\n')
        f_out.write(cols_line + '\n')
        line_num = 2
        removed = 0
        kept = 0
        for line in f_in:
            line_num += 1
            line = line.strip()
            if not line:
                continue
            if not (line.startswith('(') and line.endswith(')')):
                continue
            try:
                content = line[1:-1].split(',')
                if len(content) != 3:
                    continue
                row = int(content[0].strip())
                col = int(content[1].strip())
                value = float(content[2].strip())
                if 0 <= row < rows and 0 <= col < cols:
                    f_out.write(line + '\n')
                    kept += 1
                else:
                    removed += 1
            except Exception:
                removed += 1
        print(f"{file_path}: kept {kept}, removed {removed} out-of-bounds entries. Cleaned file: {output_path}")

def main():
    sample_input_dir = 'sample_input'
    for file in os.listdir(sample_input_dir):
        if file.endswith('.txt'):
            file_path = os.path.join(sample_input_dir, file)
            output_path = os.path.join(sample_input_dir, file[:-4] + '_cleaned.txt')
            clean_matrix_file(file_path, output_path)

if __name__ == "__main__":
    main() 