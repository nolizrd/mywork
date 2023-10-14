#Функция для открытия файла
def open_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()
    
img1=open_file(f"C:/new/img1.txt")
img2=open_file(f"C:/new/img2.txt")

for i,line in enumerate(img1):
    if "1" in line:
        x1=line.index("1")
        y1=i
        break

for i,line in enumerate(img2):
    if "1" in line:
        x2=line.index("1")
        y2=i
        break
        
print(f"Смещение по вертикали {y2-y1}, Смещение по горизонтали {x2-x1}")