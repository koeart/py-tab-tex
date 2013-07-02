# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:47:53 2013

@author: koeart

"""
__author__ = "Paul Schwanse <ps@zwoelfelf.org>"
__version__ = "0.0.1"
__date__ = "Tue 02 Jul 2013 18:23:42 CET"
__copyright__ = "Copyright (c) 2013 Paul Schwanse"
__license__ = "Python"


import csv
import os
import sys
from optparse import OptionParser

    



# hier muesste man eigtl. die headline nur den "name" key rauspopeln



def alle(dr, f, w, delimiters):
    """ ein DictReader objekt und zwei files übergeben"""
    line = delimiters['line']
    between = delimiters['between']
    ende = delimiters['ende']
    for key in dr.fieldnames:
        f.seek(0)
        line = '' + key + between
        dr.next()
        for row in dr:
            line += row[key] + between
        line = line[:-2]
        line += ende
        print line
        w.write(line)
        f.seek(0)
    w.close()

def einzeln(dr, f, w, delimiters):
    """ ein dict reader objekt und ein 2 files übergeben"""
    line = delimiters['line']
    between = delimiters['between']
    ende = delimiters['ende']
    for protokoll in dr:
        line = ''
        for key in dr.fieldnames:
            line += key + between + protokoll[key] + ende
        print line
        w.write(line)
    f.seek(0)
    w.close()

def init_parser():
    """ -e setzt multi auf false -> einzeln"""
    parser = OptionParser()
    parser.add_option(
        "--einzeln",
        "-e",
        dest="multi",
        help=u"Jedes Protokoll einzeln in Tabelle",
        action="store_false",
        default=True
        )
        
    parser.add_option(
        "--multi",
        "-m",
        dest="multi",
        help=u"eine große Tabelle (Default)",
        action="store_true",
        default=True
        )
        
    parser.add_option(
        "--file",
        "-f",
        dest="infile",
        help=u"File aus dem Daten gelesen werden sollen. Default: $default",
        action="store",
        default="daten.csv",
        metavar="FILE")
    
    parser.add_option(
        "--out",
        "-o",
        dest="outfile",
        help=u"File in das gespeichert wird. Default: $default",
        action="store",
        default="tabelle.tex",
        metavar="FILE")
        
    options = parser.parse_args()[0]
    return options
    
def main():
    delimiters = dict(between = ' & ',
                  ende = '\\\\\n',
                  line = '')
    data = "daten.csv"
    outfile = "tabelle.tex"
    f = open(data, 'rb')
    w = open(outfile, 'wb')
    mydialect = csv.Sniffer().sniff(f.readline(1024))
    
    
    f.seek(0)
    
    dr = csv.DictReader(f, dialect=mydialect)
    
    options = init_parser()
    
    if options.multi:
        alle(dr, f, w, delimiters)
    elif not options.multi:
        einzeln(dr, f, w, delimiters)
    else:
        print u"Irgendwas läuft schief"
        
    

        


if __name__ == "__main__":
    main()
    
    

