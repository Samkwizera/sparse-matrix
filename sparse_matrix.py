class SparseMatrix:
    def __init__(self, rows=None, cols=None, file_path=None):
        """
        Initialize a sparse matrix either from dimensions or from a file.
        
        Args:
            rows (int, optional): Number of rows for empty matrix
            cols (int, optional): Number of columns for empty matrix
            file_path (str, optional): Path to input file
        """
        if file_path:
            self._load_from_file(file_path)
        else:
            if rows is None or cols is None:
                raise ValueError("Both rows and cols must be specified for empty matrix")
            self.rows = rows
            self.cols = cols
            self.elements = {}  # Dictionary to store non-zero elements: (row, col) -> value

    def _load_from_file(self, file_path):
        """Load matrix from file with format:
        rows=<num>
        cols=<num>
        (row, col, value)
        ...
        """
        self.elements = {}
        try:
            with open(file_path, 'r') as f:
                # Read dimensions
                line = f.readline().strip()
                if not line.startswith('rows='):
                    raise ValueError("Invalid file format: missing rows")
                self.rows = int(line.split('=')[1])
                
                line = f.readline().strip()
                if not line.startswith('cols='):
                    raise ValueError("Invalid file format: missing cols")
                self.cols = int(line.split('=')[1])
                
                # Read elements
                for line in f:
                    line = line.strip()
                    if not line:  # Skip empty lines
                        continue
                    if not (line.startswith('(') and line.endswith(')')):
                        raise ValueError(f"Invalid element format: {line}")
                    
                    # Parse (row, col, value)
                    content = line[1:-1].split(',')
                    if len(content) != 3:
                        raise ValueError(f"Invalid element format: {line}")
                    
                    row = int(content[0].strip())
                    col = int(content[1].strip())
                    value = float(content[2].strip())
                    
                    if value != 0:  # Only store non-zero elements
                        self.elements[(row, col)] = value
                        
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except ValueError as e:
            raise ValueError(f"Error parsing file: {str(e)}")

    def get_element(self, row, col):
        """Get value at specified position."""
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise ValueError("Index out of bounds")
        return self.elements.get((row, col), 0.0)

    def set_element(self, row, col, value):
        """Set value at specified position."""
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise ValueError("Index out of bounds")
        if value == 0:
            self.elements.pop((row, col), None)  # Remove if exists
        else:
            self.elements[(row, col)] = value

    def add(self, other):
        """Add two sparse matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition")
        
        result = SparseMatrix(self.rows, self.cols)
        # Copy all elements from self
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value)
        
        # Add elements from other
        for (row, col), value in other.elements.items():
            current = result.get_element(row, col)
            result.set_element(row, col, current + value)
        
        return result

    def subtract(self, other):
        """Subtract two sparse matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for subtraction")
        
        result = SparseMatrix(self.rows, self.cols)
        # Copy all elements from self
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value)
        
        # Subtract elements from other
        for (row, col), value in other.elements.items():
            current = result.get_element(row, col)
            result.set_element(row, col, current - value)
        
        return result

    def multiply(self, other):
        """Multiply two sparse matrices."""
        if self.cols != other.rows:
            raise ValueError("Invalid dimensions for matrix multiplication")
        
        result = SparseMatrix(self.rows, other.cols)
        
        # For each non-zero element in self
        for (i, k), value1 in self.elements.items():
            # For each non-zero element in other's k-th row
            for (k2, j), value2 in other.elements.items():
                if k == k2:  # Only multiply if column of self matches row of other
                    current = result.get_element(i, j)
                    result.set_element(i, j, current + value1 * value2)
        
        return result

    def save_to_file(self, file_path):
        """Save matrix to file in the specified format."""
        with open(file_path, 'w') as f:
            f.write(f"rows={self.rows}\n")
            f.write(f"cols={self.cols}\n")
            # Sort elements by row and column for consistent output
            for (row, col) in sorted(self.elements.keys()):
                value = self.elements[(row, col)]
                f.write(f"({row}, {col}, {value})\n") 