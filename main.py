from sparse_matrix import SparseMatrix
from datetime import datetime
import os

def print_menu():
    print("\nSparse Matrix Operations")
    print("1. Add matrices")
    print("2. Subtract matrices")
    print("3. Multiply matrices")
    print("4. Exit")
    return input("Select operation (1-4): ")

def get_matrix_file(prompt):
    while True:
        file_path = input(prompt)
        try:
            print(f"Loading matrix from {file_path}...")
            matrix = SparseMatrix(file_path=file_path)
            print(f"Matrix loaded successfully. Dimensions: {matrix.rows}x{matrix.cols}")
            return matrix
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found. Please try again.")
        except ValueError as e:
            print(f"Error: {str(e)}. Please try again.")

def get_output_filename(operation):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join("output", f"matrix_{operation}_{timestamp}.txt")

def check_multiplication_size(matrix1, matrix2):
    """Check if the multiplication would result in a reasonable size matrix."""
    max_dimension = 5000  # Maximum dimension we want to allow
    if matrix1.rows > max_dimension or matrix2.cols > max_dimension:
        print(f"\nWarning: The resulting matrix would be {matrix1.rows}x{matrix2.cols}")
        print(f"This is larger than our maximum allowed dimension of {max_dimension}x{max_dimension}")
        print("Please choose smaller matrices for multiplication.")
        return False
    return True

def main():
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)
    
    while True:
        choice = print_menu()
        
        if choice == '4':
            print("Goodbye!")
            break
            
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please try again.")
            continue
            
        try:
            # Get input matrices
            matrix1 = get_matrix_file("Enter path to first matrix file: ")
            matrix2 = get_matrix_file("Enter path to second matrix file: ")
            
            # Perform operation
            print("\nPerforming operation...")
            if choice == '1':
                result = matrix1.add(matrix2)
                operation = "addition"
            elif choice == '2':
                result = matrix1.subtract(matrix2)
                operation = "subtraction"
            else:  # choice == '3'
                if not check_multiplication_size(matrix1, matrix2):
                    continue
                result = matrix1.multiply(matrix2)
                operation = "multiplication"
            
            print(f"Operation completed. Result matrix dimensions: {result.rows}x{result.cols}")
            
            # Save result with timestamp
            output_file = get_output_filename(operation)
            print(f"Saving result to {output_file}...")
            result.save_to_file(output_file)
            print(f"\nMatrix {operation} completed successfully!")
            print(f"Result saved to: {output_file}")
            
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main() 