import subprocess as sp
#cli methods
def read(args:list,esptool,partitions):
    target_partition = args[1]
    target_binary = args[2]
    remove_first_elements(args,3)
    command_to_run = [esptool,"read-flash",get_offset(partitions,target_partition),get_size(partitions,target_partition),target_binary]
    #insert_args(command_to_run,args)
    run(command_to_run)
def use_local_table(path2table:str):
    try:
        with open(path2table,"r",encoding="utf-8") as input:
            with open("partition_table.csv","w+",encoding="utf-8") as output:
                output.write(input.read())
    finally:
        print("PASS!")
def wipe(args:list,esptool,partitions):
    target_offset = get_offset(partitions,args[1])
    target_size = get_size(partitions,args[1])
    remove_first_elements(args,2)
    command_to_run = [esptool,"erase-region",target_offset,target_size]
    #insert_args(command_to_run,args)
    run(command_to_run)

#code methods
def optimize_csv(string:str):
    output = {}
    splited = string.split("\n")
    for i in range(len(splited)-1):
        if splited[i][0] == "#":continue
        splited_line = splited[i].split(",")
        output[splited_line[0]] = {"offset":splited_line[3],"size":ptsize2bytes(splited_line[4])}
    return output
def ptsize2bytes(string_size:str):
    last_symbol = string_size[-1]
    size = int(string_size[:-1])
    if last_symbol == "K":
        return hex(size * 1024)
    elif last_symbol == "M":
        return hex(size * 1024 * 1024)
def run(args:list,shell=True,**kwargs):
    print(">>",end="")
    for i in args:print(i,end=' ')
    print()
    sp.run(args,shell=shell,**kwargs)
def get_size(part_table,part):return part_table[part]["size"]
def get_offset(part_table,part):return part_table[part]["offset"]
def insert_args(list_:list,args):list_.insert(1,args)
def remove_first_elements(target:list,count = 1):
    for i in range(count):target.pop(0)

if __name__ == "__main__":
    with open("partition_table.csv","r") as file:
        print(optimize_csv(file.read()))