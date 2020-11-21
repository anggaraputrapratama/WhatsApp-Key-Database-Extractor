from os.path import isdir
from shutil import move
from helpers.CustomCI import CustomInput, CustomPrint
import os
from packaging.version import Version
from termcolor import colored, cprint
import subprocess
from subprocess import check_output
import platform
import re
from packaging import version
import wget

# Detect OS
isWindows = False
isLinux = False
if platform.system() == 'Windows' : isWindows = True 
if platform.system() == 'Linux' : isLinux = True

# Global command line helpers
adb = 'bin\\adb.exe'
delete = 'del'
tmp = 'tmp\\'
confirmDelete = '/q'
grep = 'bin\\grep.exe'
curl = 'bin\\curl.exe'
helpers = 'helpers\\'
bin = 'bin\\'
extracted = 'extracted'
tar = 'tar.exe'
if(isLinux) : 
    adb = 'adb'
    delete = 'rm -rf'
    tmp = 'tmp/'
    confirmDelete = ''
    grep = 'grep'
    curl = 'curl'
    helpers = 'helpers/'
    bin = ''
    tar = 'tar'


def main() : 
    ExtractAB()

def CleanTmp() :
        if(os.path.isdir(tmp)) : 
            CustomPrint('Cleaning up tmp folder...')
            os.remove('tmp/whatsapp.tar')
            #os.remove('tmp/whatsapp.ab')
    
def ExtractAB() :
    if(os.path.isfile(tmp + 'whatsapp.ab')) :
        abPass = CustomInput('Please enter password for backup (leave empty for none) : ')
        try : 
            os.system('java -jar ' + bin + 'abe.jar unpack ' + tmp + 'whatsapp.ab ' + tmp + 'whatsapp.tar ' + str(abPass))
            CustomPrint('Successfully \'fluffed\' '+ tmp + 'whatsapp.ab ' + tmp + 'whatsapp.tar ')
            TakingOutMainFiles()
        except Exception as e : 
            CustomPrint(e)
        
def TakingOutMainFiles() : 
    targetName = CustomInput('Enter a reference name for this target. : ') or 'target'
    os.mkdir(extracted + '/' + targetName) if not (os.path.isdir(extracted + '/' + targetName)) else CustomPrint('Folder already exists.')
    CustomPrint('Taking out main files in ' + tmp + ' folder temporaily.')
    try : 
        os.system(bin + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/f/key') ; os.replace('tmp/apps/com.whatsapp/f/key', extracted + '/' + targetName + '/key')
        os.system(bin + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/db/msgstore.db') ; os.replace('tmp/apps/com.whatsapp/db/msgstore.db', extracted + '/' + targetName + '/msgstore.db')
        os.system(bin + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/db/wa.db') ; os.replace('tmp/apps/com.whatsapp/db/wa.db', extracted + '/' + targetName + '/wa.db')
        os.system(bin + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/db/axolotl.db') ; os.replace('tmp/apps/com.whatsapp/db/axolotl.db' , extracted + '/' + targetName + '/axolotl.db')
        os.system(bin + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/db/chatsettings.db') ; os.replace('tmp/apps/com.whatsapp/db/chatsettings.db', extracted + '/' + targetName + '/chatsettings.db')
        CleanTmp()
    except Exception as e : 
        CustomPrint(e)
        CleanTmp()

if __name__ == "__main__":
    main()