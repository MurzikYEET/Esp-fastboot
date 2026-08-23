#cli methods
def read(args:list,esptool,partitions):
    target_partition = args[1]
    target_binary = args[2]
    args.pop(0)
    args.pop(0)
    command_to_run = [esptool,"read-flash",partitions[target_partition]["offset"],partitions[target_partition]["size"],target_binary]
    print(command_to_run)
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
    
if __name__ == "__main__":
    with open("partition_table.csv","r") as file:
        print(optimize_csv(file.read()))