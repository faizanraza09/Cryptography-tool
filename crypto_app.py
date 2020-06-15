import random
import streamlit as st
import nltk
nltk.download('words')
from nltk.corpus import words



# A1Z26
def encrypt_a1z26(txt):
    return " ".join(str(ord(x) - 96) if x.isalpha() else "0" for x in txt.lower() if x.isalpha() or (x == " " or x=='\n'))

def decrypt_a1z26(txt):
    ans= ''.join([chr(int(i)+64) if i!='0' else ' ' for i in txt.split()])
    return ans



# ATBASH
def encrypt_atbash(txt):
    ans=''
    for i in txt:
        if i.isalpha():
            if i.islower():
                ans+=chr(219-ord(i))
            elif i.isupper():
                ans+=chr(155-ord(i))
        else:
            ans+=i
    return ans

def decrypt_atbash(txt):
    return encrypt_atbash(txt)



# Caesar Cipher
eng=set(words.words())

def encrypt_caesar(txt, key):
    key=key%26
    ans=''
    for i in txt:
        if i.isalpha():
            a=ord(i.lower())+key
            if a>122:
                a-=26
            if i.isupper():
                ans+=chr(a-32)
                continue
            ans+=chr(a)
        else:
            ans+=i
    return ans

def decrypt_caesar(txt, key):
    key=key%26
    ans=''
    for i in txt:
        if i.isalpha():
            a=ord(i.lower())-key
            if a<97:
                a+=26
            if i.isupper():
                ans+=chr(a-32)
                continue
            ans+=chr(a)
        else:
            ans+=i
    return ans

def break_caesar(message):
    msg=message.split()
    counts=[]
    for key in range(26):
        count=0
        for i in msg:
            ans=''
            for j in i:
                if j.isalpha():
                    a=ord(j.lower())-key
                    if a<97:
                        a+=26
                    ans+=chr(a)
            if ans.lower() in eng:
                count+=1
        counts.append(count)
    return decrypt_caesar(message,counts.index(max(counts)))



# Vignere Cipher
def encrypt_vigenere(txt,key):
    key=key.upper()
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    txt=[i.upper() for i in txt if i.isalpha()]
    ans=''
    for i in range(len(txt)):
        if txt[i] in alphabet:
            z=(alphabet.index(txt[i])+alphabet.index(key[i%len(key)]))%len(alphabet)
            ans+=alphabet[z]
        else:
            ans+=txt[i]
    return ans

def decrypt_vigenere(txt,key):
    key=key.upper()
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    txt=[i.upper() for i in txt if i.isalpha()]
    ans=''
    for i in range(len(txt)):
        if txt[i] in alphabet:
            z=(alphabet.index(txt[i])-alphabet.index(key[i%len(key)]))%len(alphabet)
            ans+=alphabet[z]
        else:
            ans+=txt[i]
    return ans





if __name__=='__main__':
    st.title('Crypto Tool')
    technique=st.selectbox('Select your desired cryptography technique: ',('A1Z26','Atbash','Caesar Cipher','Vigenere Cipher'))
    option=st.selectbox('Choose whether you want to encrypt or decrypt a message: ',('Encrypt','Decrypt'))


    if technique== 'Caesar Cipher':
        if option== 'Encrypt':
            msg= st.text_area('Enter the text to encrypt: ')
            key= st.slider('Select the key: ',0,25)
            if st.button('Submit'):
                st.text(encrypt_caesar(msg,key))
        else:
            msg= st.text_area('Enter the text to decrypt: ')
            yn= st.radio('Do you have a key or do you want to bruteforce to guess the answer? Keep in mind that you can only decrypt english texts without a key',('Yes','No'))
            if yn == 'Yes':
                key=st.slider('Select the Key: ',0,25)
                if st.button('Submit'):
                    st.text(decrypt_caesar(msg,key))
            else:
                if st.button('Submit'):
                    st.text(break_caesar(msg))

    if technique == 'A1Z26':
        if option == 'Encrypt':
            msg= st.text_area('Enter the text to encrypt: ')
            if st.button('Submit'):
                st.text(encrypt_a1z26(msg))
        else:
            msg= st.text_area('Enter the text to decrypt: ')
            if st.button('Submit'):
                st.text(decrypt_a1z26(msg))

    if technique=='Atbash':
        if option=='Encrypt':
            msg= st.text_area('Enter the text to encrypt: ')
            if st.button('Submit'):
                st.text(encrypt_atbash(msg))
        else:
            msg= st.text_area('Enter the text to decrypt: ')
            if st.button('Submit'):
                st.text(decrypt_atbash(msg))

    if technique == 'Vigenere Cipher':
        if option=='Encrypt':
            msg= st.text_area('Enter the text to encrypt: ')
            key= st.text_input('Enter the key word or phrase: ')
            if st.button('Submit'):
                st.text(encrypt_vigenere(msg,key))
        else:
            msg= st.text_area('Enter the text to decrypt: ')
            key= st.text_input('Enter the key word or phrase: ')
            if st.button('Submit'):
                st.text(decrypt_vigenere(msg,key))
