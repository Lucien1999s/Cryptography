# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 02:51:47 2022

@author: 林則廷
"""

def vigenere():                       #維吉尼亞加密法
    from string import ascii_lowercase, ascii_uppercase
    low = ascii_lowercase  
    up = ascii_uppercase      

    choose = int(input('\n1.加密 2.解密 (輸入1 or 2)：'))
    if choose == 1:
        print('\n--加密--')
    else:
        print('\n--解密--')

    key = list(input("\n輸入金鑰：").lower())   #以列表來改變字符
    txt = list(input("\n請輸入文本："))

    len_s = len(txt)
    len_key = len(key)
    z = len_s // len_key
    y = len_s % len_key
    key = iter(key * z + key[:y])

    if choose == 1:                  #加密法
        for i in range(len_s):
            v = key.__next__()              #從key中依序將值給到v
            if v.isalpha():
                n = low.index(v)            #凱薩加密 確定每次的前進位數
            else:
                print('\n金鑰必須為字母組成')
                break
                                            #空格、大寫、小寫分開操作
            if txt[i] == ' ':
                continue
            elif txt[i].islower():
                new_low = low[n:] + low[:n]
                g = ''.maketrans(low, new_low)
            else:
                new_up = up[n:] + up[:n]
                g = ''.maketrans(up, new_up)
            txt[i] = txt[i].translate(g)
        encry_str = ''.join(txt)                  #將列表轉為字符串
        return encry_str

    else :                          #解密法
        for i in range(len_s):
            v = key.__next__()  # 从key中依序字符給定v值

            if v.isalpha():
                n = low.index(v)   #凱薩加密判斷位數
            else:
                print('\n金鑰必須為字母組成')
                break

            if txt[i] == ' ':
                continue
            elif txt[i].islower():
                new_low = low[n:] + low[:n]
                g = ''.maketrans(new_low, low)
            else:
                new_up = up[n:] + up[:n]
                g = ''.maketrans(new_up, up)

            txt[i] = txt[i].translate(g)
        decry_str = ''.join(txt)           
        return decry_str

if __name__ == "__main__":
    while True:
        txt = vigenere()
        print('\n結果:',txt)
        out = input('\n欲結束程式請輸入out:')
        if(out == 'out'):
            break
    
    
    
    
