# Python File Handling Assignment

def read_and_modify_file(filename):
    """
    Reads a file, modifies its content (example: convert to uppercase),
    and writes it to a new file.
    """
    try:
        # Open the original file for reading
        with open(filename, "r") as file:
            content = file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Define the new filename
        new_filename = "modified_" + filename
        
        # Write the modified content to a new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
        
        print(f"File has been modified and saved as '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
def main():
    print("📄 File Read & Write Challenge + Error Handling Lab 🧪")
    user_file = input("Enter the filename to read: ")
    read_and_modify_file(user_file)

if __name__ == "__main__":
    main()
