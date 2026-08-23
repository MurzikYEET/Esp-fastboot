import sys
import espfb_methods as fnc
import espfb_constants as const
import espfb_settings as settings

args = sys.argv[1:]
esptool = settings.ESPTOOL_BIN
with open("partition_table.csv","r") as file:
    partitions = fnc.optimize_csv(file.read())

def main():
    global args
    if len(args) <= 0:
        print(const.HELP)
        return
    match args[0]:
        case "about":print(const.ABOUT)
        case "read":fnc.read(args,esptool,partitions)
        case "about_esptool":fnc.run([esptool,"version"])
        case _:print(const.UNKNOW_COMMANDS)

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(const.ERROR,error)
        sys.exit(1)
        