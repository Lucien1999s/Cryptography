# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 22:55:24 2022

@author: 林則廷
"""

from random import sample

def txt_shift(txt, shift):                  #單字母替代式密碼
    result = ""
    for idx in range(0, len(txt)):
        char = txt[idx]
        if char.isalpha():
            s = ord(char)
            if char.isupper():
                s -= 65
                s = shift[s]
                s += 65
            elif char.islower():
                s -= 97
                s = shift[s]
                s += 97
            char = chr(s)
        result += char
    return result

def monoalpha_encryption(txt, shift):
    return txt_shift(txt, shift)

def monoalpha_decryption(txt, shift):
    inverse_shift = [0] * 26
    for idx, value in enumerate(shift):
        inverse_shift[value] = idx
    return txt_shift(txt, inverse_shift)

while True:
    plain_txt = input('\n輸入欲加密明文:')
    shift_array = sample(range(0,26), 26)

    print(f"\n原始明文: {plain_txt}")
    print(f"\nMonoalphabetic sheet: {shift_array}")
    cipher_txt = monoalpha_encryption(plain_txt, shift_array)
    print(f"\n加密密文: {cipher_txt}")
    decryption_cipher_txt = monoalpha_decryption(cipher_txt, shift_array)
    print(f"\n解密結果: {decryption_cipher_txt}")
    out = input('\n欲結束程式請輸入out:')
    if(out == 'out'):
        break