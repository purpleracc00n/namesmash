#!/usr/bin/env python3

'''
NameMash by superkojiman

Generate a list of possible usernames from a person's first and last name. 

https://blog.techorganic.com/2011/07/17/creating-a-user-name-list-for-brute-force-attacks/
'''

import sys
import os.path

if __name__ == '__main__': 
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} names.txt')
        sys.exit(0)

    if not os.path.exists(sys.argv[1]): 
        print(f'{sys.argv[1]} not found')
        sys.exit(0)

    with open(sys.argv[1]) as f:
        for line in enumerate(f): 

            # remove anything in the name that aren't letters or spaces
            name = ''.join([c for c in line[1] if  c == ' ' or  c.isalpha()])
            tokens = name.lower().split()

            if len(tokens) < 1: 
                # skip empty lines
                continue
            
            # assume tokens[0] is the first name
            fname = tokens[0]

            # remaining elements in tokens[] must be the last name
            lname = ''

            if len(tokens) == 2: 
                # assume traditional first and last name
                # e.g. John Doe
                lname = tokens[-1]

            elif len(tokens) > 2: 
                # assume multi-barrelled surname
                # e.g. Jane van Doe

                # remove the first name
                del tokens[0]

                # combine the multi-barrelled surname
                lname = ''.join([s for s in tokens])

            # create possible usernames
            print(fname + lname)           # johndoe
            print(lname + fname)           # doejohn
            print(fname + '.' + lname)     # john.doe
            print(fname + '_' + lname)     # john_doe
            print(lname + '.' + fname)     # doe.john
            print(lname + fname[0])        # doej
            print(fname[0] + lname)        # jdoe
            print(lname[0] + fname)        # djohn
            print(fname[0] + '.' + lname)  # j.doe
            print(fname[0] + '_' + lname)  # j_doe
            print(lname[0] + '.' + fname)  # d.john
            print(lname[0] + '_' + fname)  # d_john
            print(fname)                   # john
            print(lname)                   # joe
            
            # add 1 at the end
            print(fname + lname + "1")           # johndoe1
            print(lname + fname + "1")           # doejohn1
            print(fname + '.' + lname + "1")     # john.doe1
            print(fname + '_' + lname + "1")     # john_doe1
            print(lname + '.' + fname + "1")     # doe.john1
            print(lname + fname[0] + "1")        # doej1
            print(fname[0] + lname + "1")        # jdoe1
            print(lname[0] + fname + "1")        # djohn1
            print(fname[0] + '.' + lname + "1")  # j.doe1
            print(fname[0] + '_' + lname + "1")  # j_doe1
            print(lname[0] + '.' + fname + "1")  # d.john1
            print(lname[0] + '_' + fname + "1")  # d_john1
            print(fname + "1")                   # john1
            print(lname + "1")                   # joe1
            
            # take only the first 2 characters from the fname
            if len(fname) >= 2:
                print(fname[:1] + lname)           # jodoe
                print(lname + fname[:1])           # doejo
                print(fname[:1] + '.' + lname)     # jo.doe
                print(fname[:1] + '_' + lname)     # jo_doe
                print(lname + '.' + fname[:1])     # doe.jo
                print(lname[0] + '.' + fname[:1])  # d.jo
                print(lname[0] + '_' + fname[:1])  # d_jo
                
            # take only the first 2 characters from the fname and adds 1 at the end
            if len(fname) >= 2:
                print(fname[:1] + lname + "1")           # jodoe1
                print(lname + fname[:1] + "1")           # doejo1
                print(fname[:1] + '.' + lname + "1")     # jo.doe1
                print(fname[:1] + '_' + lname + "1")     # jo_doe1
                print(lname + '.' + fname[:1] + "1")     # doe.jo1
                print(lname[0] + '.' + fname[:1] + "1")  # d.jo1
                print(lname[0] + '_' + fname[:1] + "1")  # d_jo1                
              
            # take only the first 3 characters from the fname
            if len(fname) >= 3:
                print(fname[:2] + lname)           # johdoe
                print(lname + fname[:2])           # doejoh
                print(fname[:2] + '.' + lname)     # joh.doe
                print(fname[:2] + '_' + lname)     # joh_doe
                print(lname + '.' + fname[:2])     # doe.joh
                print(lname[0] + '.' + fname[:2])  # d.joh
                print(lname[0] + '_' + fname[:2])  # d_joh
                
            # take only the first 3 characters from the fname and adds 1 at the end
            if len(fname) >= 3:
                print(fname[:2] + lname + "1")           # johdoe1
                print(lname + fname[:2] + "1")           # doejoh1
                print(fname[:2] + '.' + lname + "1")     # joh.doe1
                print(fname[:2] + '_' + lname + "1")     # joh_doe1
                print(lname + '.' + fname[:2] + "1")     # doe.joh1
                print(lname[0] + '.' + fname[:2] + "1")  # d.joh1
                print(lname[0] + '_' + fname[:2] + "1")  # d_joh1
                
                
            # take only the first 4 characters from the fname
            if len(fname) >= 4:
                print(fname[:3] + lname)           # johndoe
                print(lname + fname[:3])           # doejohn
                print(fname[:3] + '.' + lname)     # john.doe
                print(fname[:3] + '_' + lname)     # john_doe
                print(lname + '.' + fname[:3])     # doe.john
                print(lname[0] + '.' + fname[:3])  # d.john
                print(lname[0] + '_' + fname[:3])  # d_john
                
            # take only the first 4 characters from the fname and adds 1 at the end
            if len(fname) >= 4:
                print(fname[:3] + lname + "1")           # johndoe1
                print(lname + fname[:3] + "1")           # doejohn1
                print(fname[:3] + '.' + lname + "1")     # john.doe1
                print(fname[:3] + '_' + lname + "1")     # john_doe1
                print(lname + '.' + fname[:3] + "1")     # doe.john1
                print(lname[0] + '.' + fname[:3] + "1")  # d.john1
                print(lname[0] + '_' + fname[:3] + "1")  # d_john1
            
            # take only the first 2 characters from the lname
            if len(lname) >= 2:
                print(fname + lname[:1])           # johndo
                print(lname[:1] + fname)           # dojohn
                print(lname[:1] + '_' + fname)     # do_john
                print(lname[:1] + '.' + fname)     # do.john                
                print(fname + '.' + lname[:1])     # john.do
                print(fname + '_' + lname[:1])     # john_do
                print(lname[:1] + fname[0])        # doj
                print(fname[0] + lname[:1])        # jdo
                print(fname[0] + '.' + lname[:1])  # j.do
                print(fname[0] + '_' + lname[:1])  # j_do

            # take only the first 2 characters from the lname and adds 1 at the end
            if len(lname) >= 2:
                print(fname + lname[:1] + "1")           # johndo1
                print(lname[:1] + fname + "1")           # dojohn1
                print(lname[:1] + '_' + fname + "1")     # do_john1
                print(lname[:1] + '.' + fname + "1")     # do.john1              
                print(fname + '.' + lname[:1] + "1")     # john.do1
                print(fname + '_' + lname[:1] + "1")     # john_do1
                print(lname[:1] + fname[0] + "1")        # doj1
                print(fname[0] + lname[:1] + "1")        # jdo1
                print(fname[0] + '.' + lname[:1] + "1")  # j.do1
                print(fname[0] + '_' + lname[:1] + "1")  # j_do1
                
            # take only the first 3 characters from the lname
            if len(lname) >= 2:
                print(fname + lname[:2])           # johndoe
                print(lname[:2] + fname)           # doejohn
                print(lname[:2] + '_' + fname)     # doe_john
                print(lname[:2] + '.' + fname)     # doe.john                
                print(fname + '.' + lname[:2])     # john.doe
                print(fname + '_' + lname[:2])     # john_doe
                print(lname[:2] + fname[0])        # doej
                print(fname[0] + lname[:2])        # jdoe
                print(fname[0] + '.' + lname[:2])  # j.doe
                print(fname[0] + '_' + lname[:2])  # j_doe
                
            # take only the first 3 characters from the lname and adds 1 at the end
            if len(lname) >= 2:
                print(fname + lname[:2] + "1")           # johndoe1
                print(lname[:2] + fname + "1")           # doejohn1
                print(lname[:2] + '_' + fname + "1")     # doe_john1
                print(lname[:2] + '.' + fname + "1")     # doe.john1             
                print(fname + '.' + lname[:2] + "1")     # john.doe1
                print(fname + '_' + lname[:2] + "1")     # john_doe1
                print(lname[:2] + fname[0] + "1")        # doej1
                print(fname[0] + lname[:2] + "1")        # jdoe1
                print(fname[0] + '.' + lname[:2] + "1")  # j.doe1
                print(fname[0] + '_' + lname[:2] + "1")  # j_doe1

            # take only the first 4 characters from the lname
            if len(lname) >= 2:
                print(fname + lname[:3])           # johndoee
                print(lname[:3] + fname)           # doeejohn
                print(lname[:3] + '_' + fname)     # doee_john
                print(lname[:3] + '.' + fname)     # doee.john                
                print(fname + '.' + lname[:3])     # john.doee
                print(fname + '_' + lname[:3])     # john_doee
                print(lname[:3] + fname[0])        # doeej
                print(fname[0] + lname[:3])        # jdoee
                print(fname[0] + '.' + lname[:3])  # j.doee
                print(fname[0] + '_' + lname[:3])  # j_doee
                
                
            # take only the first 4 characters from the lname and adds 1 at the end
            if len(lname) >= 2:
                print(fname + lname[:3] + "1")           # johndoee1
                print(lname[:3] + fname + "1")           # doeejohn1
                print(lname[:3] + '_' + fname + "1")     # doee_john1
                print(lname[:3] + '.' + fname + "1")     # doee.john1              
                print(fname + '.' + lname[:3] + "1")     # john.doee1
                print(fname + '_' + lname[:3] + "1")     # john_doee1
                print(lname[:3] + fname[0] + "1")        # doeej1
                print(fname[0] + lname[:3] + "1")        # jdoee1
                print(fname[0] + '.' + lname[:3] + "1")  # j.doee1
                print(fname[0] + '_' + lname[:3] + "1")  # j_doee1
