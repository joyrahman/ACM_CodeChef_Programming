import sys
 
##Process Input
read_line = input().split()
T = int(read_line[0])
BYTELAND = read_line[1]
#DICT Mapping
ENGLISH="abcdefghijklmnopqrstuvwxyz"
trans_dict = {'_':' '}
for byte_char, eng_char in zip(BYTELAND,ENGLISH):
    trans_dict[eng_char]=byte_char
    trans_dict[eng_char.upper()]=byte_char.upper()
 
##Translate the Sentences
for z in range(1,T+1):
    byte_sentence= input()
    english_sentence =''
    for char in byte_sentence:
        try:
            english_sentence = english_sentence+trans_dict[char]
        except KeyError:
            english_sentence = english_sentence+char
    print (english_sentence) 
