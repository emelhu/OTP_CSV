import hashlib
import string
import os

from   datetime import datetime

from   colorist import Color                  # pip install colorist   --- https://github.com/jakob-bagterp/colorist-for-python/blob/master/README.md
from   colorist import BgColor
from   colorist import BrightColor
from   colorist import BgBrightColor
from   colorist import Effect

#

separator = "\n"

languageParameter = "HUN"
parameterFileName = ".\\lang_param.txt"
translateTextPath = ".\\Texts\\"

valid_chars = "-_%s%s" % (string.ascii_letters, string.digits)

textCache = {
    "OK": "Rendben"                                                     # language order in dictionary: ENG key, HUN content
}                      

#

def InitTextLanguage():
    global languageParameter
    global parameterFileName

    if (os.path.isfile(parameterFileName)):
        file = open(parameterFileName, "r")
        languageParameter = file.read().strip().upper()[0:3]
        file.close()

    # print(f"{BgBrightColor.CYAN}Nyelv: ({languageParameter}){Color.OFF}")        


def GetID (engText: str) -> str :
    md5  = hashlib.md5(engText.encode('utf-8')).hexdigest()
    abr  = ''.join(c for c in engText.strip()  if c in valid_chars)

    return abr[0:30] + "~" + md5  


def Load (engText: str) -> str :   
    fileName = translateTextPath + GetID(engText) + ".txt"

    if (os.path.isfile(fileName)):
        file  = open(fileName, "r")
        lines = file.readlines()
        file.close()

        if (not lines) or (len(lines) < 1) or (lines[0].strip() != engText.strip()) :
            os.rename(fileName, fileName + "~save_" + datetime.now().strftime("%y%m%d_%H%M%S_%f"))
            Save(fileName, engText)                                       
        elif (len(lines) > 1) :
            return lines[1].strip()    
    else :
        Save(fileName, engText)

    return None


def Save (fileName: str, engText: str) :
    file = open(fileName, "w")
    file.write(engText + separator)
    file.close()


def T (engText) -> str:
    if (languageParameter == "ENG") :
        return engText
    
    if (not engText in textCache) :
        textCache[engText] = Load(engText)

    retText = textCache.get(engText)

    if (retText):
        return retText.strip()
        
    return engText
    
    



















  # List of executable commands