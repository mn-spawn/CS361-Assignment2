from asyncore import write
import random
import time

def main():
    
    time.sleep(3)
    file = open("PRNG", "r")
    status = file.read()
    print(status)
    
    if status == "run":
        time.sleep(3)
        num = random.randint(1,500)
        numtoString = str(num)

        writefile = open("PRNG", "w")
        writefile.truncate(0)
        writefile.write(numtoString) 
            
   
main()
   





