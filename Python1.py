#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 09:48:50 2021

@author: dmitriipodgalo
"""

while True:
    
    commands = ['exit', 'transcribe', 'reverse', 'complement', 'reverse complement']
    while True:
        command = input('Enter command: ').strip().lower()
        if command in commands:
            break
        else:
             print('Invalid command! Please, try again!')
    
    if command == 'exit':
        print('Good luck!')
        break
    
    while True:
        sequence = input('Enter sequence: ')
        if not set(sequence.upper()).issubset("ACGT") and not set(sequence.upper()).issubset("ACGU"):
            print('Invalid alphabet! Please, try again!')
        else:
            break
    
    if command == 'transcribe':
        if 'U' in sequence.upper():
            print(sequence.replace('U', 'T').replace('u', 't'))
        else:
            print(sequence.replace('T', 'U').replace('t', 'u'))
    
    elif command == 'reverse':
        print(sequence[::-1])
        
    elif command == 'complement':
        if 'U' in sequence.upper():
            print(sequence.translate(str.maketrans('AUCG', 'UAGC')).translate(str.maketrans('aucg', 'uagc')))
        else:
            print(sequence.translate(str.maketrans('ATCG', 'TAGC')).translate(str.maketrans('atcg', 'tagc')))
        
    elif command == 'reverse complement':
        if 'U' in sequence.upper():
            print(sequence.translate(str.maketrans('AUCG', 'UAGC')).translate(str.maketrans('aucg', 'uagc'))[::-1])
        else:
            print(sequence.translate(str.maketrans('ATCG', 'TAGC')).translate(str.maketrans('atcg', 'tagc'))[::-1])