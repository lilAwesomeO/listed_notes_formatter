# reverse?
# alternate star/dash
import os
import sys 
import re



def addHashDecor(line):
    
    border = ""
    i = 0
    
    while i < (len(line) + 4):
        border += "#"
        i += 1
    
    newLine = "#~" + line + "~:"
    
    return border + "\n" + newLine + "\n" + border


def addSingleSymbol(line, tabs, symbol):
    
    line = line.strip()
    newLine = ""
    
    for i in range(0, tabs):
        newLine += "\t"
        
    return newLine + symbol + " " + line


def addBox(line, tabs):
    return addSingleSymbol(line, tabs, "¤")   


def addStar(line, tabs):
    return addSingleSymbol(line, tabs, "*")



def addDash(line, tabs):
    return addSingleSymbol(line, tabs, "-")


def whitespaceOnly(line):
    return re.search("[abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ0987654321]+", line) == None


def countTabs(line):
    
    depth = 0
    
    for c in line:
        if c == "\t":
            depth += 1
    
    return depth


def save(filepath, content):
    with open(filepath, "a+") as f:
        f.write(content)


def formatTxt(txtfile):
    
    formatted = ""
    with open(txtfile, "r") as f:
        
        for line in f:
            
            if not whitespaceOnly(line):
                line = line.rstrip()
                tabs = countTabs(line)
                        
                # alternate stars and dash later.
                if tabs == 0:
                    formatted += addHashDecor(line)
                    formatted += "\n"          
                
                elif tabs == 1:
                    formatted += addBox(line, tabs)
                    formatted += "\n"

                elif tabs % 2 == 0:
                        formatted += addDash(line, tabs)
                        formatted += "\n"          
         
                elif tabs % 2 == 1:
                    formatted += addStar(line, tabs)
                    formatted += "\n"          
            else:
                
                formatted += "\n"
    
    return formatted       


def main():
    
    for a in sys.argv:
        
        if os.path.isfile(a) and a != "./" + __file__.split("\\")[-1]:        
            
            workingDir = os.path.dirname(os.path.realpath(__file__))
            fName = a.split("./")[-1]
            save(workingDir + "\\formatted_" + fName, formatTxt(a))


if __name__ == "__main__":
    main()
