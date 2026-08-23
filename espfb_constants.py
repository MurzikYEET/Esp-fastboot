UNKNOW_COMMANDS = "Unknow command"
ABOUT = "Esp-fastboot by MurzikYYET (GitHub)\nLicensed under GNU GPLv2\nUses esptool and gen_esp32part by Espressif"
HELP = """
Help for Esp-fastboot
flash <partition> <path/to/firmware.bin> <esptool-args> : flash .bin file to target partition
wipe <partition> <esptool-args> : write 0xFF in target partition
read <partition> <path/to/output.bin> <esptool-args> : read partition and save to output path
use-local-table <path/to/table.csv> : use partition table for defining partition
use-esp-table : dump esp32 table and use for defining partition
"""
ERROR = "ERR0R!!!! Error logs : \n"