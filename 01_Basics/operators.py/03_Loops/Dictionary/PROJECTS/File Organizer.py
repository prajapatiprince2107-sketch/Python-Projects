import os
import shutil

files = os.listdir()

for file in files:

    if os.path.isfile(file):

        extension = os.path.splitext(file)[1].lower()

        if extension == ".py":
            folder = "Python_Files"

        elif extension == ".txt":
            folder = "Text_Files"

        elif extension == ".jpg" or extension == ".png":
            folder = "Images"

        elif extension == ".csv":
            folder = "CSV_Files"

        elif extension == ".json":
            folder = "JSON_Files"

        else:
            folder = "Other_Files"

        if not os.path.exists(folder):
            os.mkdir(folder)

        shutil.move(file, os.path.join(folder, file))

        print(file, "->", folder)

print("\nFiles organized successfully! ✅")