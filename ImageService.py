import time


def main():

    time.sleep(10)

    file = open("PRNG", "r")
    num = file.read()

    newNum = int(num)

    file.close()


    if newNum > 10:
        picNum = newNum % 10
    
    print(picNum)

    writefile = open("PRNG", "w")
    writefile.truncate(0)
    writefile.write(f"./flowers/{picNum}.jpg")

    file.close()

    secondfile = open("ImageService", "w")
    secondfile.truncate(0)
    secondfile.write(f"flowers/{picNum}.jpg")


    
main()