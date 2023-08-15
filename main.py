# script for creating file with a specified size
from pathlib import Path

fi = open("testingfile.txt", "a")


def create_random_sentences(size):
    for i in range(0, size):
        if Path("testingfile.txt").stat().st_size != (i + 1):
            fi.write("A")


if __name__ == '__main__':
    open(fi.name, "w").close()

    while True:
        filesize = input("File size: ")
        if filesize.isnumeric():
            break
        else:
            print("The value needs to be a number!")
    create_random_sentences(int(filesize))
    print("Successful input")
