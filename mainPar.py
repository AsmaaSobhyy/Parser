import sys
import re

from parser1 import *

def runParser():
 file_name = sys.argv[1] if len(sys.argv)>1 else 'assets/tiny.txt'
 types= []
 tokens = []
 file = open(file_name,"r")
 linedata = filter(None, (line.rstrip() for line in file))
 #print(linedata)
 
 for word in linedata:
   data= word.split(",")
   t_type=data[0].strip()
   t_value = data[1].strip()
   data[0]=t_type
   data[1]=t_value
   tokens.append(data[0])
   #print(tokens)
   types.append(data[1])
   #print(types)
 file.close()
 start()
 p = parser1 (tokens, types)
 if (p.get_wrong_flag()):
  f=open("assets/output.txt", "w+")
  f.write(p.get_error_message())
  f.close()
       #print(p.get_error_message()) #code to write message in file 
 else:    
  p.drow()
 #p.drow()

# if __name__ == "__main__":
#     main()
