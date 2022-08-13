# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 02:18:00 2022

@author: 林則廷
"""
import hashlib

def sha1():
    sha1 = hashlib.sha1()                #SHA1加密法
    print('\n--SHA1加密法--')
    data = input('\n輸入欲加密明文:')
    sha1.update(data.encode('utf-8'))
    sha1_data = sha1.hexdigest()
    print('加密密文:',sha1_data)

if __name__ == '__main__':
    while True:
        sha1()
        out = input('\n欲結束程式請輸入out:')
        if(out == 'out'):
            break