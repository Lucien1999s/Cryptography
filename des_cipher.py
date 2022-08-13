# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 02:42:48 2022

@author: 林則廷
"""

import binascii

from pyDes import des, CBC, PAD_PKCS5         #DES加密法
       
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

if __name__ == '__main__':
    while True:
        txt = input('\n輸入欲加密明文:')                  

        encrypt_txt = des_encryption('12345678', txt)            #第一欄為金鑰 須為 8 bytes
        print('\n加密密文:',encrypt_txt)
        clear_str = des_decryption('12345678', encrypt_txt)
        print('\n解密密文:',clear_str)
        out = input('\n結束請輸入out:')
        if(out == 'out'):
            break
