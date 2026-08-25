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
PARTABLE_NOT_FOUND = "partition_table.csv not found, please load partition table via ./espfb use-local-table path/to/partition_table.csv"
COMMAND_NO_READY = "Command not ready, command has been added soon"
BINARY_FILL_ALL = "Binary file filled entire section, we skip erasure."
ABORT_FLASH = "Firmware greather big than partition, flashing aborted"