import time
from PIL import Image


def main():
    user = input("For new picure press 1 press any other key to cancel: ")

    if user == '1':
        writefile = open("PRNG", "w")
        writefile.truncate(0)
        writefile.write("run") 
        print("You selected to have a new picture!")

    else: 
        print("canceled")

    time.sleep(15)

    file = open("ImageService", "r")
    path = file.read()
    print(path)

main()