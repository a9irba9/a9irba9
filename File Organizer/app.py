import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File name {filename}: created successfully!")

    except FileExistsError as e:
        print(f"File name {filename}: already exists!")
    except Exception as E:
        print("An error occured!")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No file found!")
    else:
        print("Files in Directory!")
        for file in files:
            print(file)
            
def delete_file(filename):
    try:
        os.remove(filename)
        print("File deleted successfully!")
    except FileNotFoundError:
        print("The file does not exist!")
    except Exception as e: 
        print("An error occured!")
        
def read_file(filename):
    try:
        with open("sample.txt", "r") as f:
            content = f.read()
            print(f"Content of file '{filename}':\n{content}!")
            
    except FileNotFoundError:
        print(f"{filename} does not exist!")
    except Exception as e:
        print(F"An error occured!\n{e}")
        
def edit_file(filename):
    try:
        with open("sample.txt", "a") as f:
            content = input('Enter data to add = ')
            f.write(content + "\n")
            print(f"Content added to '{filename}' successfully!")
    
    except FileNotFoundError:
        print(f"{filename}  does not exist!")

    except Exception as e:
        print(f"An error occured!\n{e}")
        
def main():
    while True:
        print('\n')
        print("Welcome to File Handler!")
        print("1: Create File")
        print("2: View All Files")
        print("3: Delete Files")
        print("4: Read Files")
        print("5: Edit Files")
        print("6: Exit")
        
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
            print("Closing File Handler!")
            break
        else:
            print("Invalid Choice Entered! Try Again!")
            
if __name__ == '__main__':
    main()
        



