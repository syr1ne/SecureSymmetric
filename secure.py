#!/usr/bin/env python3
import os
import base64, hashlib
from getpass import getpass
from cryptography.fernet import Fernet
from argparse import ArgumentParser, SUPPRESS

# Shell colors and style, originally these are light version of the colors
R = '\033[91m' # Light Red
G = '\033[92m' # Light Green
B = '\033[94m' # Light Blue
C = '\033[96m' # Cyan
Y = '\033[93m' # Yellow
r = '\033[0m'  # reset color value

# Success and Error prompt color coding
S = f'{G}*{r}'
E = f'{R}!{r}'

## set if we can write and some functions are able to perfrom
write_file = True

## generates a key with the provided password with fernets symmetric encryption algorithm 
def gen_fernet_key (masterpass:bytes) -> bytes:
    assert isinstance(masterpass, bytes)
    hlib = hashlib.md5()
    hlib.update(masterpass)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))


## takes the master password as to create the original key value 
def input_master_key ():
    if   args.encrypt: icon = '\U0001F512' ## unicode charecters for locked emoji
    elif args.decrypt: icon = '\U0001F513' ## unicode charecters for unlocked emoji
    masterpass = getpass(f"[{icon}] Enter Password: "); print() # <- OCD issue sorry
    key = gen_fernet_key(masterpass.encode('utf-8'))
    return Fernet(key)


## renames encrpted and decrupted file and also stores the directory position
def tweaking (file):

    if file.find("/") > 1 :
        file_name = file.split("/")[-1]
        ## extracts the initial file directory if any
        file_path = '/'.join(file.split("/")[:-1]) 
    else : 
        file_name = file
        file_path = './'

    ## rename the encryped file just for the convinience of understanding
    if  args.encrypt: file_name = "enc_" + file_name
    ## just takes away the 'enc_' from the file name
    ## Todo: might fix this for better logic
    elif args.decrypt: file = file[4:]
    return file_name, file_path


## encryption and decryption in one function
def enc_dec (file, fernet):
    dec_failed = False
    global write_file
    file_name, file_path  = tweaking(file)
    with open(file, 'r') as file:
        file.seek(0)
        data = file.read()
        if args.encrypt:
            enc_data = fernet.encrypt(data.encode('utf-8'))
        elif args.decrypt:
            try:
                dec_data = fernet.decrypt(data.encode('utf-8')).decode('utf-8')
            except:
                print(f"[{E}] Decryption Failed for {R}{file_name}{r}")
                # as the decrytion failed, we don't delete file if '--remove' option is used 
                dec_failed = True # <-  we might not need this cause of the next variable
                # since the decrytion failed, we tell the write method to not write anything
                write_file = False 

    if args.decrypt: file_name = file_name[4:]

    ## this is noob logic for if the process is happening in the current directory or in a diffenet path
    if len(file_path) != 0 : file_path = file_path + '/' + file_name
    else: file_path = file_name

    if args.output : 
        if args.output[-1] != '/':
            file_path = args.output + '/'
            file_path = file_path + file_name
        else: file_path = args.output + file_name

    if write_file == True:
        with open(file_path, 'w') as output_file:
            output_file.seek(0)
            if args.encrypt: 
                output_file.write(str(enc_data.decode('utf-8')))
                print(f"[{S}] Successfully Encrypted {G}{file_name[4:]}{r}")
            elif args.decrypt and dec_failed == False:
                output_file.write(dec_data)
                print(f"[{S}] Successfully Decrypted {G}{file_name}{r}")


# checks if the single file is valid and prints related errors
def is_valid_file (file_path):
    stupid_path = -1 
    try:
        if file_path.find("/") > 1:
            file = file_path.split("/")[-1]
            while(file == '') : 
                file = file_path.split("/")[-1 + stupid_path]
                stupid_path = stupid_path - 1
        else: file = file_path
    except AttributeError: 
        print(f"[{E}] Please provide a file path"); exit(0)

    try:
        with open(file_path, 'r') as theFile:
            _ = theFile.read()
            return True
    except FileNotFoundError : print(f"[{E}] The specified file {C}{file}{r} does not exist")
    except PermissionError   : print(f"[{E}] Permission denied for file {C}{file}{r}")
    except IsADirectoryError : print(f"[{E}] {B}{file}{r} is a directory")
    except UnicodeDecodeError: print(f"[{E}] Sorry, binary file ({G}{file}{r}) support coming soon!")
    return False


## Fancy Directory check errors 
def is_valid_directory (dir_path):
    stupid_path = -1 # to check from the negetive index 
    try:
        if dir_path.find("/") > 1:
            directory = dir_path.split("/")[-1]
            while(directory == '') : 
                directory = dir_path.split("/")[-1 + stupid_path]
                stupid_path = stupid_path - 1
    except AttributeError : 
        print(f"[{E}] Please provide a directory path")
        return False
    try:
        dirContent = os.listdir(dir_path)
        if len(dirContent) > 0 : return True
        else: print(f"[{E}] {B}{is_valid_directory(args.path)}{r} is an empty directory")
    except FileNotFoundError: 
        if args.output: print(f"[{E}] Invalid output directory {B}{directory}{r} "); exit(0)
        else: print(f"[{E}] The specified directory {B}{directory}{r} does not exist")
    except PermissionError   : print(f"[{E}] Permission denied for folder {B}{directory}{r}")
    except NotADirectoryError: print(f"[{E}] {B}{directory}{r} is not a directory")
    return False
    

# lots of flags and arguments 
print(" ") # sorry i have OCD
parser = ArgumentParser (description='\033[3mEncrypts and Decrypts plain-text data\033[0m', 
                         epilog='Made with <3 by @Syrine && @1byteBoy',
                         usage="%(prog)s [OPTIONS...] [PATH...]")

parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt the file")
parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the file")
parser.add_argument("-D", "--dir", action="store_true", help="Work with a whole directory of files") 
parser.add_argument("-x", "--extensions", type=str, metavar='', help="Specify specific file extensions") 
parser.add_argument("-o", "--output", type=str, metavar='', help="Output file path") 
parser.add_argument("-r", "--remove", action="store_true", help="Removes original file after encryting or decrypting")
# parser.add_argument("-v", "--verbose", action="store_true", help="For verbosity")
parser.add_argument('path', type=str, nargs='?', help=SUPPRESS)
args = parser.parse_args()


# initial logic and condition sets
if __name__ == '__main__':
    if not any(vars(args).values()): parser.print_help()
    elif args.encrypt and args.decrypt: print(f"[{R}!{r}] Please use only one cryptographic process")
    elif args.encrypt or args.decrypt:
        try:
            if args.output : 
                if is_valid_directory(args.output): out_dir_path = args.output
                # else : print(f"[!] Invalid Output directory {B}{is_valid_directory(args.output)}{r}"); exit(0)
            if args.dir:
                if args.extensions is not None:
                    ## args.extensions will carry the list of all provided extensions ##
                    args.extensions = [ext.strip() for ext in args.extensions.split(",")]
                if is_valid_directory(args.path):
                    dirContent = os.listdir(args.path)
                    fernet = input_master_key()
                    for content in dirContent:
                        file = os.path.join(args.path,content)
                        if is_valid_file(file):
                            if args.extensions:
                                for extension in args.extensions:
                                    if file.endswith(extension):
                                        enc_dec(file, fernet)
                                        break 
                            else: enc_dec(file, fernet)
                            if args.remove and write_file : os.remove(file)
            else: 
                if is_valid_file(args.path):
                    fernet = input_master_key()
                    enc_dec(args.path, fernet)
                    if args.remove and write_file : os.remove(args.path)
        except KeyboardInterrupt: print("\n\nBye ....")
    else: print(f"[{E}] Please choose a cryptographic process")