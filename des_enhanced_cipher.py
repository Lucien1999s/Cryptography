# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 02:20:42 2022

@author: 林則廷
"""
import binascii
import random

from pyDes import des, CBC, PAD_PKCS5         #強化版DES加密法
       
def des_encryption(secret_key, s):
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)
def des_decryption(secret_key, s):
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de
def generate_key(length):                       #產生金鑰
    key = ""
    for i in range(0, length):
        key += str(random.randint(0, 1))
    return key

if __name__ == '__main__':
    while True:
        txt = input('\n輸入欲加密明文:')
        key = generate_key(8)

        encrypt_txt = des_encryption(key, txt)
        print('\n加密密文:',encrypt_txt)
        clear_str = des_decryption(key, encrypt_txt)
        print('\n解密密文:',clear_str)
        out = input('\n結束請輸入out:')
        if(out == 'out'):
            break