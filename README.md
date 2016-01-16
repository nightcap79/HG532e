# HG532e


The firmware under test is HG532eV100R001C81B025_upgrade_packet.bin.

[Binwalk](https://github.com/devttys0/binwalk) Analysis:
```bash
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
8792          0x2258          LZMA compressed data, properties: 0x5D, dictionary size: 8388608 bytes, uncompressed size: 97664 bytes
70016         0x11180         LZMA compressed data, properties: 0x5D, dictionary size: 8388608 bytes, uncompressed size: 2783096 bytes
979072        0xEF080         Squashfs filesystem, big endian, lzma signature, version 3.0, size: 2746714 bytes, 197 inodes, blocksize: 65536 bytes, created: 2014-04-17 02:44:10
```

#####EF080 Squashfs filesystem
Partition extracted using [sasquatch](https://github.com/devttys0/sasquatch)
The extracted folder has base linux file system with some empty folders and links to file system, and some important files.
List of folders:
```bash
bin  dev  etc  init  lib  mnt  proc  sbin  tmp  usr  var
```

important files are inside /etc:
defaultcfg.xml > an encrypted configuration file, a very important file which has all usernames and passwords of  the system and the default settings of the device.
I've looked into a project to decrypt the configuration file from a similar system hg658c.wordpress.com and found that it's not easy, you need some keys and RSAs 


#####2258  LZMA compressed data

#####11180 LZMA compressed data


[HG532e folder on mediafire](https://www.mediafire.com/folder/71l98mn7wagi3/HG532e)

####Things you need to know:

Note: you need to replace the brackets with the text inside (*****) to the suitable variable.

To extract a part of a firmware image use:
```bash
$ dd if=(imageName) bs=1 skip=(decimal address of the beginning of the file) of=(outPartName)
```

To check the file type use:
```bash
$ file (the name of the file you need to check)
```

To read all strings in a file use:
```bash
$ strings -n 10 (the name of the file you need to check)  >  (name_of_the_output_file)
```

To read a file in hex form including a space with (*) to indicate a repeated code use:
```bash
$ hexdump -C (the name of the file you need to check)  >  (name_of_the_output_file)
```

You can limit the hex form lines to a certain number of lines using:
```bash
$  hexdump -C (the name of the file you need to check) | head -n (number of requested lines)
```

To search for a file name in a directory and its subdirectories use:
```bash
$ find . -name (the name of the wanted file)
```

To search for a text inside the files in a directory and its subdirectories use:
```bash
$ grep "(the wanted text)" -r .
```


