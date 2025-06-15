import os

folder_name = "farda"
os.makedirs(folder_name, exist_ok=True)

file_path = os.path.join(folder_name, "farda.txt")
with open(file_path, "w") as file:
    file.write("nama: farda\n")
    file.write("usia: 21\n")
    file.write("alamat: Sukabumi\n")

with open(file_path, 'r') as file:
    data = file.read()
    print(data)
    