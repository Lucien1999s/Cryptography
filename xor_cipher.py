# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 23:48:40 2022

@author: 林則廷
"""

import random

def string_to_bytes(input):                     
    input = bytearray(input, 'utf-8')
    result = ""
    for byte in input:
        for i in range(7, -1, -1):
            result += str((byte >> i) & 1)
    return result

def bytes_to_string(input):
    result = ""
    for idx in range(0, int(len(input)/8)):
        binary = input[8*idx:8*(idx+1)]
        result += chr(int(binary, 2))
    return result

def generate_key(length):                       #產生金鑰
    key = ""
    for i in range(0, length):
        key += str(random.randint(0, 1))
    return key

def xor_operation(text, key):                   #xor運算
    if text == key:
        return "0"
    else:
        return "1"

def xor_en_decrypt(text, key):                  #xor長度判斷
    result = ""
    len_txt = len(text)
    len_key = len(key)
    for idx in range(0, len_txt):
        if idx >= len_key:
            key_idx = idx % len_key
        else:
            key_idx = idx
        xor_result = xor_operation(text[idx], key[key_idx])
        result += xor_result
    return result


if __name__ == "__main__":
    while True:
        message = input('\n輸入欲加密訊息:')
        print(f"\n原始明文: {message}")
        message = string_to_bytes(message)
        print(f"\n明文編碼: {message}")

        key = generate_key(len(message))
        print(f"\n產生金鑰: {key}")

        encryption = xor_en_decrypt(message, key)
        print(f"\n加密過後: {encryption}")

        decryption = xor_en_decrypt(encryption, key)
        print(f"\n解密過後: {decryption}")

        txt = bytes_to_string(decryption)
        print(f"\n解密文: {txt}")
    
        
        out = input('\n結束請輸入out:')
        if(out == 'out'):
            break
    
