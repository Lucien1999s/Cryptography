# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 14:08:33 2022

@author: 林則廷
"""
import binascii
                          #Feistel 加密法
def rand_key(p):                           #產生隨機bits
	
	import random
	key1 = ""
	p = int(p)
	
	for i in range(p):
		temp = random.randint(0,1)
		temp = str(temp)
		key1 = key1 + temp
		
	return(key1)

def exor(a,b):                    #對bits執行xor
    
	temp = ""
	for i in range(n):
		
		if (a[i] == b[i]):
			temp += "0"
			
		else:
			temp += "1"
			
	return temp

def BinaryToDecimal(binary):             #進位轉換
	
	string = int(binary, 2)
	return string

while True:
    PT = input('\n輸入欲加密密文:')

    PT_Ascii = [ord(x) for x in PT]           #將明文轉換成ASCII

    PT_Bin = [format(y,'08b') for y in PT_Ascii]   #轉換ASCII成 8-bit 二進位型態
    PT_Bin = "".join(PT_Bin)

    n = int(len(PT_Bin)//2)                    #將明文分成兩半
    L1 = PT_Bin[0:n]                        
    R1 = PT_Bin[n::]
    m = len(R1)

    K1= rand_key(m)                          #產生第一輪的金鑰 k1

    K2= rand_key(m)                          #產生第二輪的金鑰 k2

    f1 = exor(R1,K1)                          #第一輪feistel
    R2 = exor(f1,L1)
    L2 = R1

    f2 = exor(R2,K2)                          #第二輪feistel
    R3 = exor(f2,L2)
    L3 = R2

    bin_data = L3 + R3                       #產生加密密文
    str_data =' '

    for i in range(0, len(bin_data), 7):
	
         #切割 bin_data 存至 temp_data
	    temp_data = bin_data[i:i + 7]
		
	    # 將 temp_data 用 BinarytoDecimal() 轉換取得存至decimal_data
	    decimal_data = BinaryToDecimal(temp_data)
		
        #將轉換後的值以字元型態的值加至加密密文結果
	    str_data = str_data + chr(decimal_data)
	
    print("\n加密密文:", str_data)

    L4 = L3                         #解密法
    R4 = R3

    f3 = exor(L4,K2)
    L5 = exor(R4,f3)
    R5 = L4

    f4 = exor(L5,K1)
    L6 = exor(R5,f4)
    R6 = L5
    PT1 = L6+R6


    PT1 = int(PT1, 2)
    RPT = binascii.unhexlify( '%x'% PT1)
    print("\n解密後文: ", RPT)


    out = input('\n結束請輸入out:')
    if(out == 'out'):
        break