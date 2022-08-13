import random 
                                        #SPN加密法
def generate_key(key, rounds):             
    key += key
    keys = []
    for idx in range(rounds):
        key_this_round = key[4*idx+4:4*idx+20]
        keys.append(key_this_round)
    return keys

def xor_operation(text, key):
    if text == key:
        return "0"
    else:
        return "1"

def xor_en_decrypt(text, key):                           
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

def substitution(input, s_box):                         #s-box 替換
    output = ""
    for idx in range(4):
        data = input[4*idx:4*(idx+1)]
        number = int(data, 2)
        number_substitution = s_box[number]
        binary_number = ""
        for i in range(3, -1, -1):
            binary_number += str((number_substitution >> i) & 1)

        output += binary_number
    return output

def permutation(input, p_box):                           #p-box 排列
    output = list("0" * 16)
    for idx, value in enumerate(p_box):
        output[value] = input[idx]
    return "".join(output)

def spn_encrypt(text, rounds, key, s_box, p_box):        #spn加密 xor + s-box + p-box
    output = text
    for idx in range(rounds):
        output = xor_en_decrypt(output, key[idx])
        output = substitution(output, s_box)
        output = permutation(output, p_box)
    output = xor_en_decrypt(output, key[rounds])
    return output

def spn_decrypt(text, rounds, key, s_box, p_box):         #spn解密法   就倒過來
    output = text
    s_box_inverse = [0]*16
    p_box_inverse = [0]*16
    for idx in range(16):
        s_box_inverse[s_box[idx]] = idx
        p_box_inverse[p_box[idx]] = idx
    for idx in range(rounds):
        output = xor_en_decrypt(output, key[rounds-idx])
        output = permutation(output, p_box_inverse)
        output = substitution(output, s_box_inverse)
    output = xor_en_decrypt(output, key[0])
    return output

if __name__ == '__main__':
    while True:
        rounds = 3
        key = "1011101000111110"
        keys = generate_key(key, rounds + 1)
        print(f"\n初始金鑰： {key}")
        print(f"\n產生金鑰： {keys}")

        s_box = random.sample(range(0, 16), 16)
        print(f"\ns_box： {s_box}")
        p_box = random.sample(range(0, 16), 16)
        print(f"\np_box： {p_box}")

        message = "1001001110100101"
        print(f"\n原始明文： {message}")
        encryption = spn_encrypt(message, rounds, keys, s_box, p_box)
        print(f"\n加密密文： {encryption}")
        decryption = spn_decrypt(encryption, rounds, keys, s_box, p_box)
        print(f"\n原始明文： {decryption}")
        out = input('\n欲結束程式請輸入out:')
        if(out == 'out'):
            break
    
    