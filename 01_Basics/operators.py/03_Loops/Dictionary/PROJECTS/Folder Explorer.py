from pathlib import Path

folder = input("Enter folder path: ")

path = Path(folder)

if path.exists() and path.is_dir():

    print("\n========== FOLDER CONTENT ==========")

    files = 0
    folders = 0

    for item in path.iterdir():

        if item.is_file():
            print("📄 File:", item.name)
            files += 1

        elif item.is_dir():
            print("📁 Folder:", item.name)
            folders += 1

    print("\n========== REPORT ==========")
    print("Total Files:", files)
    print("Total Folders:", folders)

else:
    print("Folder not found! ❌")