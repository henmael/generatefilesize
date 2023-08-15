# script for creating file with a specified size
from pathlib import Path

fi = open("testingfile.txt", "a")
def create_random_sentences(filesize):
    for i in range(0, filesize):
        if Path("testingfile.txt").stat().st_size != (i+1):
            fi.write("a")


if __name__ == '__main__':
    open(fi.name, "w").close()
    create_random_sentences(20000)
