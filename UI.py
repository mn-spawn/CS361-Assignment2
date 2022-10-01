
def main():
    user = input("For new picure press 1 press any other key to cancel: ")

    if user == '1':
        writefile = open("PRNG", "w")
        writefile.truncate(0)
        writefile.write("run") 


   

    else: 
        print("canceled")


main()