## What is SecureSymmetric ?

In general it's just a cool name for the project but actually it's just a simple program that encrypts file using 
*fernet's symmetric `secret key` based authenticated cryptography.*

Learn more about **Fernet** at https://cryptography.io/en/latest/fernet/

## DISCLAIMER

This program is intended for educational and legitimate purposes only. It provides encryption and decryption functionalities using Fernet cryptography, designed to protect data privacy and security. However, it is crucial to note that misuse of this software for malicious activities such as ransomware attacks is strictly prohibited and unlawful.

The developers of this program, do not endorse, promote, or encourage any illegal or unethical use of this software. Users are solely responsible for their actions and must comply with applicable laws and regulations in their jurisdictions.

By using this software, you agree to use it responsibly and ethically. The developer shall not be held liable for any misuse or unlawful activities conducted using this program.

## PERSONAL NOTE

As said earlier, this is just a simple code that i wrote to learn about how symmetric encrytion works and the usage of fernet. This is totally a personal project and i am not a good developer at all, so please test the code on test files before using on your important files. Feel free to make necessary changes from your side. 

Personally i don't like storing data on cloud storage, so it's better for me to store it offline but that too can be vulnerable, specially in case of a ransomeware attack. So if you are willing to save to the cloud and also encrypt it, this tool can help, or better use [cryptomator](https://cryptomator.org/).

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

----

Made with <3 by [Syrine](https://github.com/syr1ne) and [8bitBoy](https://github.com/1byteBoy)