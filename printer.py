#!/usr/bin/env python
#TODO need to implement funny quotes getter
lineWidth = 20
maxChars = 80
HOST = "130.225.24.203"
PORT = 9100
text = ''
import sys
import socket
#import 
try:
        text = str.rsplit(sys.argv[1])
except:
        print "Usage: "+sys.argv[0]+" <your whitty quote>"
        raise SystemExit

def format(textToFormat):
        lineUse = 0
        line = ''
        for word in textToFormat:
                if (lineUse + len(word)) > lineWidth:
                        line += ' '*(20-lineUse)+word+' '
                        lineUse = len(word)+1
                else:
                        lineUse += len(word)
                        line += word
                        if lineUse % 20 != 0:
                            lineUse += 1
                            line +=' '
        printFormatted(line)
        line = unicode(line, "utf-8").encode("hp-roman8")
        if (len(line) > maxChars):
            print "Formatted line exceeds display size: %d chars" % maxChars
            raise SystemExit
        return line

def wrapText(inputText):
        text = "\033%-12345X@PJL RDYMSG DISPLAY = \""
        text += inputText
        text += "\"\r\n\033%-12345X\r\n"
        return text

def sendToPrinter(textToSend):
        formattedText = format(textToSend)
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((HOST, PORT))
        finalText = wrapText(formattedText)
        soc.send(finalText)
        soc.close()

def printFormatted(text):
        i = 0
        for c in text:
                i += 1
                sys.stdout.write(c)
                if i % 20 == 0:
                        sys.stdout.write('\n')
        sys.stdout.write('\n')

sendToPrinter(text)
