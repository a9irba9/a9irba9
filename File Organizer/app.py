import os

BASE_FOLDER =(r'File Organizer\\Files')

def create_file(filename):
    try:
        file_path = os.path.join(BASE_FOLDER, filename)
        with open(file_path, 'x') as f:
            print(f"File '{filename}' created successfully!")
    except FileExistsError:
        print(f"File '{filename}' already exists!")
    except Exception as e:
        print(f"An error occurred! {e}")

def view_all_files():
    files = os.listdir(BASE_FOLDER)
    if not files:
        print("No files found!")
    else:
        print("Files in Directory:")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        file_path = os.path.join(BASE_FOLDER, filename)
        os.remove(file_path)
        print("File deleted successfully!")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist!")
    except Exception as e:
        print(f"An error occurred! {e}")

def read_file(filename):
    try:
        file_path = os.path.join(BASE_FOLDER, filename)
        with open(file_path, 'r') as f:
            content = f.read()
            print(f"Content of file '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist!")
    except Exception as e:
        print(f"An error occurred! {e}")

def edit_file(filename):
    try:
        file_path = os.path.join(BASE_FOLDER, filename)
        content = input('Enter data to add = ')
        with open(file_path, 'a') as f:
            f.write(content + "\n")
            print(f"Content added to '{filename}' successfully!")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist!")
    except Exception as e:
        print(f"An error occurred! {e}")

def organize_file(filename):
    extension = filename.split('.')[-1]
    folder_path = os.path.join(BASE_FOLDER, extension)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(BASE_FOLDER, filename)
    new_path = os.path.join(folder_path, filename)
    if os.path.exists(file_path):
        os.rename(file_path, new_path)
        print(f"File '{filename}' has been organized into '{folder_path}'.")
    else:
        print(f"The file '{filename}' does not exist!")

def main():
    while True:
        print('\n')
        print("Welcome to File Handler!")
        print("1: Create File")
        print("2: View All Files")
        print("3: Delete Files")
        print("4: Read Files")
        print("5: Edit Files")
        print("6: Organize Files")
        print("7: Exit")

        choice = input("Enter your choice = ")

        if choice == '1':
            filename = input('Enter the name of file to create = ')
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input('Enter the name of file to delete = ')
            delete_file(filename)
        elif choice == '4':
            filename = input('Enter the name of file to read = ')
            read_file(filename)
        elif choice == '5':
            filename = input('Enter the name of file to edit = ')
            edit_file(filename)
        elif choice == '6':
            filename = input('Enter the name of file to organize = ')
            organize_file(filename)
        elif choice == '7':
            print("Closing File Handler!")
            break
        else:
            print("Invalid Choice Entered! Try Again!")

if __name__ == '__main__':
    main()
