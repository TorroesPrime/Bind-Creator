import os
import random
con_debug = False
control = "F10 "
channel = " \"L "0
slash = "\\"


def main():
    file_list = []
    list_count = int(input("how many files do you wish to build into binds? "))
    count = 1
    while count <= list_count:
        name= input("please enter a name for this bind set: ")
        file_name = input("please enter the file name you wish to convert to binds: ")
        entry = (name,file_name)
        file_list.append(entry)
        count += 1
    for bind in file_list:
        bindpath = "c:\\binds\\stupids\\"+bind[0]+"\\"
        
        if os.path.exists(bindpath) == True:
                if con_debug == True:
                        print("directory already exists")
        else: 
                if con_debug == True:
                        print("directory created")
                os.mkdir(bindpath)
        BindMaker(bind,bindpath)

def BindMaker(item, bindpath):
        increment = 1
        with open("c:\\binds\\stupids\\"+item[1], 'r') as f:
            for line in f.readlines():
                output_file_name = bindpath+"0"+str(increment)+".txt"
                next_file = bindpath+"0"+str(increment+1)+".txt"
                e = line.strip('\n') 
                e = control+channel+e
                out_file = open(output_file_name,'w')
                line = e+"$$bindloadfile "+next_file+"\""
                out_file.write(line)
                increment += 1

        
        
    
main()
