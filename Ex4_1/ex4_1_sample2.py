"""
:::Author:  Derrick Beckman
:::File:    ex4_1_sample.py
:::Desc:    This program will decode a caesar ciphered document given
            a cipher setting.
"""
import string
import base64
import argparse
from Crypto.Cipher import DES, AES
from hashlib import md5

    
#def rot13Convert(data):
    #"""
    #Takes a text string encodes/decodes it via ROT-13
    #:param data: string text
    #:return: encoded/decoded string
    #"""

    #result = ''
    #for letter in data:
        #if letter.isalpha():
            #base_position = base.find(letter.upper())
            #encoded_position = (base_position - 6) % len(base)
            #result += base[encoded_position]
        #else:
            #result += letter
                 
    #return result

#data = rot13Convert(data)
#print data





def main():
    a = ''
    with open("ex4_1_data.txt") as fin:
        a = fin.read()
        
    #for i in xrange(len(string.ascii_lowercase)): # len(string.ascii it 26, so range is 0-26; xrange is the way to go in 2.7
    #print("{}: {}".format(i,caesarDecode(a, 6))) #keeps cycleing through the decode until it gotes to 26. 
    dcrypt1 = caesarDecode(a, 6)
    atbsh = atbash(dcrypt1)
    #print atbsh
    base_64 = base64Decode(atbsh)
    #print (base_64)
    key = md5('hippopotamus').hexdigest()
    AES = AESEncode(base_64, key)

def caesarEncode(data, shift): #shift is negative
# takes a string input and encodes it into caesar ciphered text
#:param data:string text
#:param shift: integer to shift by
#:return: encoded string
    
    result = ''
    for letter in data:
        if letter.isupper(): #string function
            base_position = string.ascii_uppercase.find(letter) #finds letter in the string
            encoded_position = (base_position + shift) % 26 #base position -6 %26 of -6. shifted position went from being 1 to 21. Now you know what position to pull the letter frim
            result += string.ascii_uppercase[encoded_position]
        elif letter.islower(): #defines the lower cases
            base_position = string.ascii_lowercase.find(letter)
            encoded_position = (base_position + shift) % 26
            result += string.ascii_lowercase[encoded_position]
        else:
            result += letter
    return result
    
def caesarDecode(data, shift):
# takes a string input and encodes it into caesar ciphered text
#:param data:string text
#:param shift: integer to shift by
#:return: encoded string

    return caesarEncode (data, shift * -1)
    
    
def atbash(data):
    """
    Encodes and Decodes atbash cipher text
    :parm data: text string to encode or decode
    :return: encoded or decoded string
    """
    result = ''
    for letter in data:
        if letter.isupper():
            base_position = string.ascii_uppercase.find(letter)
            encoded_position = ((base_position + 1) * -1) #This adds 1 then multiplies by the negative getting the inverse.  Must at 1 in so that 0 is not the 1st number.
            result += string.ascii_uppercase[encoded_position]
        elif letter.islower():
            base_position = string.ascii_lowercase.find(letter)
            encoded_position = ((base_position + 1) * -1)
            result += string.ascii_lowercase[encoded_position]            
        else:
            result += letter
    return result
        
def base64Decode(data):
    coded_string = data.split(':')
    #print coded_string
    decoded_data = base64.b64decode(coded_string[1]) 
    print decoded_data
    
    return decoded_data
    
   
    
    
#def DESEncode(data, key):
    #des = DES.new(key, DES.MODE_ECB)
    #return des.decrypt(data)

    
def MD5Hash():
    md = md5('hippopotamus').hexdigest()
    
    print md
    return md

def AESEncode(data, key):
    coded_string2 = data.split(': ')
    aes = AES.new('9b4609b17fea63f3f3f067fc2f465c6e')
    print aes.decrypt(coded_string2[1])
    #print aes
    return aes

# md5 hash is the key in the AES
if __name__ == "__main__":  # if __name__ --> put the args and args parsing statements after main. Main should always be clean 
    main()          
            
            
            
            
            
            
            
            
            
            
            
    
    





