# ESP-FASTBOOT
Esp-fastboot is a “module” for esptool that allows you to flash an ESP32 like an Android phone by simply specifying the partition for flashing.
## WARNINGS !!!
WARNING: I AM NOT RESPONSIBLE FOR DAMAGE TO YOUR ESP32; USE THIS TOOL AT YOUR OWN RISK.
## How to install
1. Install [Python 3.10+](https://www.python.org/downloads/release/python-3147/)
2. Clone this repo to esptool directory 
```bash
git clone https://github.com/MurzikYEET/Esp-fastboot.git
```
3. Open espfb_settings.py and change pathes of ESPTOOL_BIN and GEN_PART_BIN (default `..\esptool` and `..\gen_esp32part`).
4. Setup partition table for flashing 
```bash
python espfb.py use-local-table path/to/partition_table.csv
```
5. Use :)
## Commands
`flash <partition> <path/to/firmware.bin>` : Flashing binary to partition\
`wipe <partition>` : Erasing partition\
`read <partition> <path/to/output.bin>` : Reading partition and save it to .bin file\
`use-local-table <path/to/table.csv>` : Copying ESP-IDF partition table to directory of Esp-fastboot\
`use-esp-table` (unfinished, not working) : Dumping partition table from connected ESP32 and using her for flashing\
You can also add esptool arguments after Esp-fastboot commands. For example, `python espfb.py wipe spiffs -b 115200` will turn into `esptool -b 115200 erase-region <spiffs address> <spiffs size>`.
## Credits
[Espressif Systems](https://github.com/espressif) : this company made esptool and ESP32 platform\
[Python Software Foundation](https://github.com/psf) : made Python laungage
## License
Esp-fastboot and esptool licensed under GNU GPLv2