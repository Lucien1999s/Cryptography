# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 22:00:44 2022

@author: 林則廷
"""

def txt_shift(txt,shift):                 #凱薩加密法
    result = ''
    for i in range(0,len(txt)):
        char = txt[i]
        if char.isalpha():
            if char.isupper():
                s = ord(char) -65 + shift
                s %= 26
                s += 65
            elif char.islower():
                s = ord(char) -97 + shift
                s %= 26
                s += 97
            char = chr(s)
        result += char
    return result
def caesar_encryption(txt,shift):
    return txt_shift(txt,shift)
def caesar_decryption(txt,shift):
    return txt_shift(txt,-1*shift)

while True:
    p_txt = input('\n輸入欲轉換文字:')        
    shift_set = int(input('\n輸入位移量:'))

    print(f"\n原始明文:{p_txt}")
    cipher_txt = caesar_encryption(p_txt, shift_set)
    print(f"\n加密密文:{cipher_txt}")
    decryption_txt = caesar_decryption(cipher_txt, shift_set)
    print(f"\n解密結果:{decryption_txt}")
    out = input('\n結束請輸入out:')
    if(out == 'out'):
        break
