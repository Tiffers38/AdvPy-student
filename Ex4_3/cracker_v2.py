#!/usr/bin/python

#This program will attempt to crack passwords from a unix shadow file

import crypt

def main():
    crack()

def crack():

    for shdow in open('ex4_3_data.txt', 'r'): #reads the shadow file ex4_3_data.txt
        print shdow
        if '*' in shdow.split(':') or '!' in shdow.split(':'): #splits on the ':' of the shadow file fields
            pass
        else:
            e = shdow.split(':')
            f = e[1].split('$')
            i = 0
            for pwd in open('password.lst', 'r'):
                i = i + 1
                h = crypt.crypt(pwd.strip(), ''.join(["$", f[1], "$", f[2], "$"]))
                if h.split('$')[3] == f[3]:
                    print "Password cracked for {} - {} after {} attempts".format(e[0], pwd, i)


if __name__ == '__main__':
    main()
