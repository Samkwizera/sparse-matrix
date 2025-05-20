# Sparse Matrix Operations

This program implements efficient sparse matrix operations including addition, subtraction, and multiplication. It is designed to handle large matrices while optimizing memory usage by only storing non-zero elements.

## Features

- Load sparse matrices from files
- Perform matrix addition
- Perform matrix subtraction
- Perform matrix multiplication
- Save results to files
- Memory-efficient implementation
- Strict input validation
- User-friendly interface

## File Format

Input files should follow this format:
```
rows=<number_of_rows>
cols=<number_of_columns>
(row, col, value)
(row, col, value)
...
```

Example:
```
rows=3
cols=3
(0, 0, 1.0)
(1, 1, 2.0)
(2, 2, 3.0)
```

## Usage

1. Run the program:
   ```
   python main.py
   ```

2. Select an operation:
   - 1: Add matrices
   - 2: Subtract matrices
   - 3: Multiply matrices
   - 4: Exit

3. Enter the paths to your input matrix files when prompted
   - Example files: sample_input/matrixfile1.txt and sample_input/matrixfile3.txt

4. Enter the path for the output file

## Requirements

- Python 3.6 or higher

## Implementation Details

- Uses a dictionary-based sparse matrix representation
- Only stores non-zero elements
- Validates matrix dimensions before operations
- Handles file I/O with proper error checking
- Sorts output elements for consistent results
- Optimized for large matrices (tested with files >6MB)

## Error Handling

The program handles various error cases:
- Invalid file formats
- Missing files
- Dimension mismatches
- Invalid matrix operations
- Out-of-bounds indices

## Example Files

The program comes with two large test matrices in the `sample_input` directory:
- sample_input/matrixfile1.txt (6.2MB)
- sample_input/matrixfile3.txt (12MB)

These files can be used to test the program's performance with real-world data sizes.

## Example

Input file 1 (matrix1.txt):
```
rows=2
cols=2
(0, 0, 1.0)
(1, 1, 2.0)
```

Input file 2 (matrix2.txt):
```
rows=2
cols=2
(0, 0, 3.0)
(1, 1, 4.0)
```

Result of addition (output.txt):
```
rows=2
cols=2
(0, 0, 4.0)
(1, 1, 6.0)
``` 