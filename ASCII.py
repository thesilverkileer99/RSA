def ASCII(message):
    message=list(message)
    compt=len(message)
    code=[]
    for i in range(0,compt):
        caract=message[i]
        if caract==" ":
            code=code+[1]
        elif caract=="!":
            code=code+[2]
        elif caract=="#":
            code=code+[3]
        elif caract=="$":
            code=code+[4]
        elif caract=="%":
            code=code+[5]
        elif caract=="&":
            code=code+[6]
        elif caract=="'":
            code=code+[7]
        elif caract=="(":
            code=code+[8]
        elif caract==")":
            code=code+[9]
        elif caract=="*":
            code=code+[10]
        elif caract=="+":
            code=code+[11]
        elif caract==",":
            code=code+[12]
        elif caract=="-":
            code=code+[13]
        elif caract==".":
            code=code+[14]
        elif caract=="/":
            code=code+[15]
        elif caract=="0":
            code=code+[16]
        elif caract=="1":
            code=code+[17]
        elif caract=="2":
            code=code+[18]
        elif caract=="3":
            code=code+[19]
        elif caract=="4":
            code=code+[20]
        elif caract=="5":
            code=code+[21]
        elif caract=="6":
            code=code+[22]
        elif caract=="7":
            code=code+[23]
        elif caract=="8":
            code=code+[24]
        elif caract=="9":
            code=code+[25]
        elif caract==":":
            code=code+[26]
        elif caract==";":
            code=code+[27]
        elif caract=="<":
            code=code+[28]
        elif caract=="=":
            code=code+[29]
        elif caract==">":
            code=code+[30]
        elif caract=="?":
            code=code+[31]
        elif caract=="@":
            code=code+[32]
        elif caract=="A":
            code=code+[33]
        elif caract=="B":
            code=code+[34]
        elif caract=="C":
            code=code+[35]
        elif caract=="D":
            code=code+[36]
        elif caract=="E":
            code=code+[37]
        elif caract=="F":
            code=code+[38]
        elif caract=="G":
            code=code+[39]
        elif caract=="H":
            code=code+[40]
        elif caract=="I":
            code=code+[41]
        elif caract=="J":
            code=code+[42]
        elif caract=="K":
            code=code+[43]
        elif caract=="L":
            code=code+[44]
        elif caract=="M":
            code=code+[45]
        elif caract=="N":
            code=code+[46]
        elif caract=="O":
            code=code+[47]
        elif caract=="P":
            code=code+[48]
        elif caract=="Q":
            code=code+[49]
        elif caract=="R":
            code=code+[50]
        elif caract=="S":
            code=code+[51]
        elif caract=="T":
            code=code+[52]
        elif caract=="U":
            code=code+[53]
        elif caract=="V":
            code=code+[54]
        elif caract=="W":
            code=code+[55]
        elif caract=="X":
            code=code+[56]
        elif caract=="Y":
            code=code+[57]
        elif caract=="Z":
            code=code+[58]
        elif caract=="[":
            code=code+[59]
        elif caract=="|":
            code=code+[60]
        elif caract=="]":
            code=code+[61]
        elif caract=="^":
            code=code+[62]
        elif caract=="_":
            code=code+[63]
        elif caract=="a":
            code=code+[64]
        elif caract=="b":
            code=code+[65]
        elif caract=="c":
            code=code+[66]
        elif caract=="d":
            code=code+[67]
        elif caract=="e":
            code=code+[68]
        elif caract=="f":
            code=code+[69]
        elif caract=="g":
            code=code+[70]
        elif caract=="h":
            code=code+[71]
        elif caract=="i":
            code=code+[72]
        elif caract=="j":
            code=code+[73]
        elif caract=="k":
            code=code+[74]
        elif caract=="l":
            code=code+[75]
        elif caract=="m":
            code=code+[76]
        elif caract=="n":
            code=code+[77]
        elif caract=="o":
            code=code+[78]
        elif caract=="p":
            code=code+[79]
        elif caract=="q":
            code=code+[80]
        elif caract=="r":
            code=code+[81]
        elif caract=="s":
            code=code+[82]
        elif caract=="t":
            code=code+[83]
        elif caract=="u":
            code=code+[84]
        elif caract=="v":
            code=code+[85]
        elif caract=="w":
            code=code+[86]
        elif caract=="x":
            code=code+[87]
        elif caract=="y":
            code=code+[88]
        elif caract=="z":
            code=code+[89]
        elif caract=="é":
            code=code+[90]
        elif caract=="è":
            code=code+[91]
        elif caract=="à":
            code=code+[92]
        elif caract=="û":
            code=code+[93]
        elif caract=="â":
            code=code+[94]
        elif caract=="ê":
            code=code+[95]
        elif caract=="ë":
            code=code+[96]
        elif caract=="ä":
            code=code+[97]
        elif caract=="{":
            code=code+[98]
        elif caract=="}":
            code=code+[99]
    return(code)



def ASCII_decode(code):
    compt=len(code)
    message=""
    for i in range(0,compt):
        caract=code[i]
        if caract==1:
            message=message+" "
        elif caract==2:
            message=message+"!"
        elif caract==3:
            message=message+"#"
        elif caract==4:
            message=message+"$"
        elif caract==5:
            message=message+"%"
        elif caract==6:
            message=message+"&"
        elif caract==7:
            message=message+"'"
        elif caract==8:
            message=message+"("
        elif caract==9:
            message=message+")"
        elif caract==10:
            message=message+"*"
        elif caract==11:
            message=message+"+"
        elif caract==12:
            message=message+","
        elif caract==13:
            message=message+"-"
        elif caract==14:
            message=message+"."
        elif caract==15:
            message=message+"/"
        elif caract==16:
            message=message+"0"
        elif caract==17:
            message=message+"1"
        elif caract==18:
            message=message+"2"
        elif caract==19:
            message=message+"3"
        elif caract==20:
            message=message+"4"
        elif caract==21:
            message=message+"5"
        elif caract==22:
            message=message+"6"
        elif caract==23:
            message=message+"7"
        elif caract==24:
            message=message+"8"
        elif caract==25:
            message=message+"9"
        elif caract==26:
            message=message+":"
        elif caract==27:
            message=message+";"
        elif caract==28:
            message=message+"<"
        elif caract==29:
            message=message+"="
        elif caract==30:
            message=message+">"
        elif caract==31:
            message=message+"?"
        elif caract==32:
            message=message+"@"
        elif caract==33:
            message=message+"A"
        elif caract==34:
            message=message+"B"
        elif caract==35:
            message=message+"C"
        elif caract==36:
            message=message+"D"
        elif caract==37:
            message=message+"E"
        elif caract==38:
            message=message+"F"
        elif caract==39:
            message=message+"G"
        elif caract==40:
            message=message+"H"
        elif caract==41:
            message=message+"I"
        elif caract==42:
            message=message+"J"
        elif caract==43:
            message=message+"K"
        elif caract==44:
            message=message+"L"
        elif caract==45:
            message=message+"M"
        elif caract==46:
            message=message+"N"
        elif caract==47:
            message=message+"O"
        elif caract==48:
            message=message+"P"
        elif caract==49:
            message=message+"Q"
        elif caract==50:
            message=message+"R"
        elif caract==51:
            message=message+"S"
        elif caract==52:
            message=message+"T"
        elif caract==53:
            message=message+"U"
        elif caract==54:
            message=message+"V"
        elif caract==55:
            message=message+"W"
        elif caract==56:
            message=message+"X"
        elif caract==57:
            message=message+"Y"
        elif caract==58:
            message=message+"Z"
        elif caract==59:
            message=message+"["
        elif caract==60:
            message=message+"|"
        elif caract==61:
            message=message+"]"
        elif caract==62:
            message=message+"^"
        elif caract==63:
            message=message+"_"
        elif caract==64:
            message=message+"a"
        elif caract==65:
            message=message+"b"
        elif caract==66:
            message=message+"c"
        elif caract==67:
            message=message+"d"
        elif caract==68:
            message=message+"e"
        elif caract==69:
            message=message+"f"
        elif caract==70:
            message=message+"g"
        elif caract==71:
            message=message+"h"
        elif caract==72:
            message=message+"i"
        elif caract==73:
            message=message+"j"
        elif caract==74:
            message=message+"k"
        elif caract==75:
            message=message+"l"
        elif caract==76:
            message=message+"m"
        elif caract==77:
            message=message+"n"
        elif caract==78:
            message=message+"o"
        elif caract==79:
            message=message+"p"
        elif caract==80:
            message=message+"q"
        elif caract==81:
            message=message+"r"
        elif caract==82:
            message=message+"s"
        elif caract==83:
            message=message+"t"
        elif caract==84:
            message=message+"u"
        elif caract==85:
            message=message+"v"
        elif caract==86:
            message=message+"w"
        elif caract==87:
            message=message+"x"
        elif caract==88:
            message=message+"y"
        elif caract==89:
            message=message+"z"
        elif caract==90:
            message=message+"é"
        elif caract==91:
            message=message+"è"
        elif caract==92:
            message=message+"à"
        elif caract==93:
            message=message+"û"
        elif caract==94:
            message=message+"â"
        elif caract==95:
            message=message+"ê"
        elif caract==96:
            message=message+"ë"
        elif caract==97:
            message=message+"ä"
        elif caract==98:
            message=message+"{"
        elif caract==99:
            message=message+"}"
    return(message)

def cryptage(message,n,e):
    code=ASCII(message)
    k=len(code)
    message_crypte=[]
    for i in range (0,k):
        m=code[i]
        c=0
        while (c-m**e)%n !=0:
            c=c+1
        message_crypte = message_crypte + [c]
    return(message_crypte)
def decryptage(code,n,d):
    k=len(code)
    message_decrypte=[]
    for i in range(0,k):
        c=code[i]
        m=0
        while (c**d-m)%n !=0:
            m=m+1
        message_decrypte=message_decrypte + [m]
        message=ASCII_decode(message_decrypte)
    return(message)
    
def ASCII2(message):
    message=list(message)
    compt=len(message)
    code=[]
    for i in range(0,compt):
        caract=message[i]
        if caract=="t":
            code=code+[7]
        elif caract=="e":
            code=code+[11]
        elif caract=="s":
             code=code+[13]
    return(code)
def ASCII_decodeV2(code):
    compt=len(code)
    message=""
    for i in range(0,compt):
        caract=code[i]
        if caract==7:
            message=message+"t"
        elif caract==11:
            message=message+"e"
        elif caract==13:
            message=message+"s"
        else :
            message=message+"0"
    return(message)
            
def cryptageV2(message,n,e):
    code=ASCII2(message)
    k=len(code)
    message_crypte=[]
    for i in range (0,k):
        m=code[i]
        c=0
        while (c-m**e)%n !=0:
            c=c+1
        message_crypte = message_crypte + [c]
    return(message_crypte)

def decryptageV2(code,n,d):
    k=len(code)
    message_decrypte=[]
    for i in range(0,k):
        c=code[i]
        m=0
        while (c**d-m)%n !=0:
            m=m+1
        message_decrypte=message_decrypte + [m]
        message=ASCII_decodeV2(message_decrypte)
    return(message)
        
