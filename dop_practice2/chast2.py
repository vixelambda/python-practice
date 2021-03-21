import os
import pyfiglet

def search():
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        # все папки
        for dirname in dirnames:
            print(" " + os.path.basename(dirpath) + " -> " + dirname)
        # все файлы
        for filename in filenames:
            print(" " + os.path.basename(dirpath) + " -> " + f'"{filename}"')

def generate():
    print("digraph G {")
    search()
    print("}")

def ascii_banner(banner):
    return pyfiglet.figlet_format(banner)

print(ascii_banner("KisPython"))
generate()