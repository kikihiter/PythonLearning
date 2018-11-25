#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#python chineseFormat.py
import sys

if __name__=="__main__":
    try:
        fpi = open("data.in", "r",encoding='UTF-8')
    except IOError:
        print >> sys.stderr, "failed to open file."
        sys.exit(1)

    try:
        fpo = open("data.out", "w",encoding='UTF-8')
    except IOError:
        print >> sys.stderr, "failed to open file."
        sys.exit(1)

    while True:
        line = fpi.readline()
        iline = line.lstrip()
        if not line:
            break
        try:
            a = int(iline[0])
            line = '\n'+iline
            #continue
        except:
            line = line.rstrip('\n')
        
        
        
        #if line[-1] == '-':
        #    line = line.rstrip('-')
        #elif line[-1] != '-':
        #    line = line + " "
        #print (line[-1])
        fpo.write(line)
        #fpo.close()
        #if line[-1] == '-':
            #line
        #fpo.write(line.rstrip('\n')+" ")
        
