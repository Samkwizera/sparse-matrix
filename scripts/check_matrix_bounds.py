import os

def check_matrix_bounds(file_path):
    print(f"\nChecking file: {file_path}")
    try:
        with open(file_path, 'r') as f:
            # Read dimensions
            rows_line = f.readline().strip()
            cols_line = f.readline().strip()
            
            if not rows_line.startswith('rows=') or not cols_line.startswith('cols='):
                print(f"Error: Invalid format in {file_path}")
                print(f"First line: {rows_line}")
                print(f"Second line: {cols_line}")
                return
            
            rows = int(rows_line.split('=')[1])
            cols = int(cols_line.split('=')[1])
            print(f"Matrix dimensions: {rows} rows x {cols} columns")
            
            # Check each element
            line_num = 2  # Start after the dimension lines
            invalid_entries = []
            
            for line in f:
                line_num += 1
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                    
                if not (line.startswith('(') and line.endswith(')')):
                    print(f"Warning: Invalid format at line {line_num}: {line}")
                    continue
                
                try:
                    # Parse (row, col, value)
                    content = line[1:-1].split(',')
                    if len(content) != 3:
                        print(f"Warning: Invalid element format at line {line_num}: {line}")
                        continue
                    
                    row = int(content[0].strip())
                    col = int(content[1].strip())
                    value = float(content[2].strip())
                    
                    # Check bounds
                    if row < 0 or row >= rows:
                        invalid_entries.append(f"Line {line_num}: Row index {row} out of bounds [0, {rows-1}]")
                    if col < 0 or col >= cols:
                        invalid_entries.append(f"Line {line_num}: Column index {col} out of bounds [0, {cols-1}]")
                        
                except ValueError as e:
                    print(f"Warning: Could not parse line {line_num}: {line}")
                    print(f"Error: {str(e)}")
            
            # Report results
            if invalid_entries:
                print("\nFound invalid entries:")
                for entry in invalid_entries:
                    print(entry)
            else:
                print("\nAll entries are within bounds!")
                
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except Exception as e:
        print(f"Error processing file: {str(e)}")

def main():
    # Check all files in sample_input directory
    sample_input_dir = 'sample_input'
    for file in os.listdir(sample_input_dir):
        if file.endswith('.txt'):
            file_path = os.path.join(sample_input_dir, file)
            check_matrix_bounds(file_path)

if __name__ == "__main__":
    main() 