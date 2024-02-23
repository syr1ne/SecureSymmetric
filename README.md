## What is SecureSymmetric ?

In general it's just a cool name for the project but actually it's just a simple program that encrypts file using 
*fernet's symmetric 'secret key' based authenticated cryptography.*

Learn more about **Fernet** at https://cryptography.io/en/latest/fernet/

## Usage

```
$ python3 secure.py
 
usage: secure.py [OPTIONS...] [PATH...]

Encrypts and Decrypts plain-text data

options:
  -h, --help          show this help message and exit
  -e, --encrypt       Encrypt the file
  -d, --decrypt       Decrypt the file
  -D, --dir           Work with a whole directory of files
  -x , --extensions   Specify specific file extensions
  -o , --output       Output file path
  -r, --remove        Removes original file after encryting or decrypting

Made with <3 by @Syrine && @1byteBoy
```
-----

***While main options are self-explainatory but let me explain some of them a bit clearly***

`-D` or `--dir` is used if we want to encrypt or decrypt all the files present in a perticular directory

```
python3 secure.py -e -D Documents/
```

`-x` or `--extensions` is used if we want to encrypt or decrypt files with specific file extension. 

```
python3 secure.py -e -D Documents/Coding/ -x txt,py
```

`-o` or `--output` is used to specify a custom directory where we want to save our encrypted or decrypted files.

```
python3 secure.py -e -D Documents/Coding/ -x txt,py -o /tmp
```

`-r` or `--remove` is used to remove the files after they are either encrypted or decrptred

## ToDo

- [ ] Might add support for verbosity as an option
- [ ] Support for binary files, since now it only supports plain text encryption

----

Made with <3 by [Syrine](https://github.com/syr1ne) and [8bitBoy](https://github.com/1byteBoy)