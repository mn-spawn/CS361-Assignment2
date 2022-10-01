from asyncore import write
import random

def main():
    
    num = random.randint(1,500)
    numtoString = str(num)
        
    writefile = open("PRNG", "w")
    writefile.truncate(0)
    writefile.write(numtoString) 
   
main()
   





