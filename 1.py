import os
import Project as Project

if __name__ == "__main__":
    sistem_operasi = os.name
    
    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        
        print(f"{"="*40:<40}")
        print(f"{"SELAMAT DATANG DI PROGRAM":^40}")
        print(f"{"DATABASE PERPUSTAKAAN":^40}")
        print(f"{"="*40:<40}\n")





        print(f"    1. Read Data")
        print(f"    2. Create Data")
        print(f"    3. Update Data")
        print(f"    4. Delete Data\n")

        user_option = input("Masukan opsi: ")

        print("\n=========================\n")

        match user_option:
            case "1": print("Read Data")
            case "2": print("Create Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")

        print("\n=========================\n")
        is_done = input("Apakah Selesai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

    print(20*('='), ('Ending'), ('=')*20,"\n\n\n")