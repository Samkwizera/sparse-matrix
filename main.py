from sparse_matrix import SparseMatrix

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
            return SparseMatrix(file_path=file_path)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found. Please try again.")
        except ValueError as e:
            print(f"Error: {str(e)}. Please try again.")

def main():
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
            if choice == '1':
                result = matrix1.add(matrix2)
                operation = "addition"
            elif choice == '2':
                result = matrix1.subtract(matrix2)
                operation = "subtraction"
            else:  # choice == '3'
                result = matrix1.multiply(matrix2)
                operation = "multiplication"
            
            # Save result
            output_file = input("Enter path for output file: ")
            result.save_to_file(output_file)
            print(f"\nMatrix {operation} completed successfully!")
            print(f"Result saved to: {output_file}")
            
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main() 