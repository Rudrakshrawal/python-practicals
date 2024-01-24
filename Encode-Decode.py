import random

#ENCODE
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def encode(code):
    if len(code)<=3 :
        return code[1]+ code[0]#Takes the first letter & put it in th last
    else:
     random_prefix = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz')for _  in range(3))#This i got from GPT
     random_suffix = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz")for _  in range(3))#Random.choice selects random digits,, for _ selects 3 from the given set of words and join joins them 
     return random_suffix+code[::-1]+random_suffix

code = input('Enter a message to encode it:  ')
chuppa_do = encode(code)
print(f"the encoded statement is \n{chuppa_do}\n  ")



# # #DECODE

def decode(matlab):
    if len(matlab)<=3:
        return matlab[1]+ matlab[0]
    else:
        return matlab[3:-3][::-1]
matlab = input('Message you want to decode:  ')
khol_do = decode(matlab)
print(f"the decoded one is \n {khol_do}")
# DONE
