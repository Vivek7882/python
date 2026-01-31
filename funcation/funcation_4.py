import shutil as st 
width=st.get_terminal_size().columns
 # 1	 Without return value without argument

def printline():
    print("_"*width)

#  2	Without return value with argument 

def printmassage(massage):
    print(massage.center(width))


printline()
printmassage("vivek solanki")
printline()
