
def main():
    file = open("PRNG", "r")
    num = file.read()

    newNum = int(num)

    if newNum > 10:
        picNum = newNum % 10

    print(picNum)
    picNum = newNum


    
main()