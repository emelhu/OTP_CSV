import sys
import os
import CSVtoDB

from   colorist import Color                  # pip install colorist   --- https://github.com/jakob-bagterp/colorist-for-python/blob/master/README.md
from   colorist import BgColor
from   colorist import BrightColor
from   colorist import BgBrightColor
from   colorist import Effect

import Texts  
from   Texts import T



def DisplayHelpText(param):    
    if (param == "HELP"):
        DisplayHelpParams()
    elif (param == "CSV"):
        DisplayCSVparams()
    elif (param == "LANG"):
        DisplayLangParams()
    else:
        DisplayCommands()        
        DisplayLangParams()
        DisplayHelpParams()
        DisplayCSVparams()


def DisplayCommands():    
    print()
    print(f"{Color.BLUE}{T('List of executable commands')}:")                                                              # A végrehajtható parancsok listája
    print(f"{Color.GREEN}   HELP    {BrightColor.BLACK} ({T('show info for this app')}) ")
    print(f"{Color.GREEN}   LANG    {BrightColor.BLACK} ({T('select a language for display text')}) ")
    print(f"{Color.GREEN}   CSV     {BrightColor.BLACK} ({T('insert rows of CSV files in DATA directory to a Database')}) ")
    print(f"{Color.GREEN}   <empty> {BrightColor.BLACK} ({T('exit app')}) ")
    print()
    print(str(Color.OFF))

#

def DisplayCSVparams():    
    print()
    print(f"{Color.BLUE}A CSV parancs paramétereinek listája:")
    print(f"{Color.GREEN}   CLEAR   {BrightColor.BLACK} (clear database table (delete data) before insert rows) ")
    print(f"{Color.GREEN}   UPDATE  {BrightColor.BLACK} (add only new rows if any, duplicate in CSV isn't a problem) ")
    print(f"{Color.GREEN}   <empty> {BrightColor.BLACK} (default, add new and unique rows of new CSVs ) ")
    print()
    print(str(Color.OFF))

def CheckCSVparam(param) -> bool:    
    return (not param) or (param == "CLEAR") or (param == "UPDATE")    

def ProcessCSV(param):
    print()
    print(f"CSV parancs, Ezt a paramétert kérte: {param}")
    print()

#

def DisplayLangParams():    
    print()
    print(f"{Color.BLUE}A LANG parancs paramétereinek listája:")
    print(f"{Color.GREEN}   HUN   {BrightColor.BLACK} (Hungarian) ")
    print(f"{Color.GREEN}   ENG   {BrightColor.BLACK} (English) ")
    print()
    print(str(Color.OFF))

def CheckLangParam(param) -> bool:    
    return (param == "HUN") or (param == "ENG")    

def ProcessLang(param) :
    if (param == "HUN"):
        None
    elif (param == "ENG"):
        None
    else:
        print()
        print(f"{Effect.BLINK}{Effect.BOLD}{Color.RED}Belső programhiba! ({param}){Color.OFF}{Effect.OFF}")        
        print()
        DisplayLangParams()
        exit()
    
    file = open(Texts.parameterFileName, "w")
    file.write(param)
    file.close()

    print(f"{Color.BLUE}A LANG parancs paramétere ({param}) elmentve.")

#

def DisplayHelpParams():    
    print()
    print(f"{Color.BLUE}A HELP parancs paramétereinek listája:")
    print(f"{Color.GREEN}   HELP    {BrightColor.BLACK} ({T('show info for this app')})")
    print(f"{Color.GREEN}   LANG    {BrightColor.BLACK} ({T('select a language for display text')})")
    print(f"{Color.GREEN}   CSV     {BrightColor.BLACK} ({T('insert rows of CSV files in DATA directory to a Database')})")
    print()
    print(str(Color.OFF))

def CheckHelpParam(param) -> bool:    
    return (param == "HELP") or (param == "LANG") or (param == "CSV")   

#

#----------------------------------

def main():
    print()
    print()
    print(f"--- {Effect.BOLD}{Color.BLUE}{BgBrightColor.CYAN} OTP Bank csv forgalmi kivonat feldolgozása {BgBrightColor.OFF}{Color.OFF}{Effect.OFF} --- {BrightColor.BLACK}(c) eMeL.hu{Color.OFF} ---")
    print()
    
    Texts.InitTextLanguage()

    if len(sys.argv) > 1:
        command = sys.argv[1].upper().strip()

        if len(sys.argv) > 2:
            param = sys.argv[2].upper().strip()
    else:
        while True:           
            DisplayCommands()

            command = input("Végrehajtandó parancs neve: ").upper().strip()

            if (not command):
                exit()

            if (command == "HELP"):
                DisplayHelpParams();               

                param = input("A HELP parancs paramétere: ").upper().strip()

                if CheckHelpParam(param):
                    break

            if (command == "LANG"):
                DisplayLangParams();               

                param = input("A LANG parancs paramétere: ").upper().strip()

                if CheckLangParam(param):
                    break

            if (command == "CSV"):
                DisplayCSVparams();               

                param = input("A CSV parancs paramétere: ").upper().strip()

                if CheckCSVparam(param):
                    break


    if (command == "CSV") :
        ProcessCSV(param)
    elif (command == "LANG") :
        ProcessLang(param)
    elif (command == "HELP") :
        DisplayHelpText(param)
    else :
        DisplayHelpText()


#--------------------------------------------------------------------------------

if __name__ == "__main__":
    main()



