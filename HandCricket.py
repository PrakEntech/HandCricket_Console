import os
from random import randint
n=int(input("Player \n0 OR 1 - "))
n1=randint(0,1)
if n1==n:
    print('Player Won The Toss')
    n1=int(input("0.Bowl OR 1.Bat - "))
    if n1==0:
        print('Player Won The Toss\nand Choose to Bowl')
        s=0
        while True:
            print('Computer(Runs) - '+str(s)+'/0')
            n=0
            while n not in [1,2,3,4,5,6]:n=int(input("Player - "))
            n1=randint(1,6)
            print('Computer - '+str(n1))
            os.system('cls')
            if n1!=n:
                s+=n1
            else:
                print('Player needs '+str(s+1)+' Runs to Win')
                break
        s1=0
        while True:
            print('Player(Runs) - '+str(s1)+'/0')
            n=0
            while n not in [1,2,3,4,5,6]:n=int(input("Player - "))
            n1=randint(1,6)
            print('Computer - '+str(n1))
            os.system('cls')
            if n1!=n:
                s1+=n
                if s1>s:
                    print('Computer - ' + str(s) + '/1')
                    print('Player - ' + str(s1) + '/0')
                    print('Player Won by a Wicket')
                    break
            else:
                print('Computer - ' + str(s) + '/1')
                print('Player - ' + str(s1) + '/1')
                if s>s1:print('Computer Won by '+str(s-s1)+' Runs')
                else :print('Draw')
                break
    else:
        print('Player Won The Toss\nand Choose to Bat')
        s=0
        while True:
            print('Player(Runs) - '+str(s)+'/0')
            n=0
            while n not in [1,2,3,4,5,6]:n=int(input("Player - "))
            n1=randint(1,6)
            print('Computer - '+str(n1))
            os.system('cls')
            if n1!=n:
                s+=n
            else:
                print('Computer needs '+str(s+1)+' Runs to Win')
                break
        s1=0
        while True:
            print('Computer(Runs) - '+str(s1)+'/0')
            n=0
            while n not in [1,2,3,4,5,6]:n=int(input("Player - "))
            n1=randint(1,6)
            print('Computer - '+str(n1))
            os.system('cls')
            if n1!=n:
                s1+=n1
                if s1>s:
                    print('Player - ' + str(s) + '/1')
                    print('Computer - ' + str(s1) + '/0')
                    print('Computer Won by a Wicket')
                    break
            else:
                print('Player - ' + str(s) + '/1')
                print('Computer - ' + str(s1) + '/1')
                if s>s1:print('Player Won by '+str(s-s1)+' Runs')
                else :print('Draw')
                break
else:
    n1=randint(0,1)
    if n1==0:
        print('Computer Won The Toss\nand Choose to Bowl')
        s=0
        while True:
            print('Player(Runs) - '+str(s)+'/0')
            n=0
            while n not in [1,2,3,4,5,6]:n=int(input("Player - "))
            n1=randint(1,6)
            print('Computer - '+str(n1))
            os.system('cls')
            if n1!=n:
                s+=n
            else:
                print('Computer needs '+str(s+1)+' Runs to Win')
                break
        s1=0
        while True:
            print('Computer(Runs) - '+str(s1)+'/0')
            n=0
            while n not in [1,2,3,4,5,6]:n=int(input("Player - "))
            n1=randint(1,6)
            print('Computer - '+str(n1))
            os.system('cls')
            if n1!=n:
                s1+=n1
                if s1>s:
                    print('Player - ' + str(s) + '/1')
                    print('Computer - ' + str(s1) + '/0')
                    print('Computer Won by a Wicket')
                    break
            else:
                print('Player - ' + str(s) + '/1')
                print('Computer - ' + str(s1) + '/1')
                if s>s1:print('Player Won by '+str(s-s1)+' Runs')
                else :print('Draw')
                break
    else:
        print('Computer Won The Toss\nand Choose to Bat')
        s=0
        while True:
            print('Computer(Runs) - '+str(s)+'/0')
            n=0
            while n not in [1,2,3,4,5,6]:n=int(input("Player - "))
            n1=randint(1,6)
            print('Computer - '+str(n1))
            os.system('cls')
            if n1!=n:
                s+=n1
            else:
                print('Player needs '+str(s+1)+' Runs to Win')
                break
        s1=0
        while True:
            print('Player(Runs) - '+str(s1)+'/0')
            n=0
            while n not in [1,2,3,4,5,6]:n=int(input("Player - "))
            n1=randint(1,6)
            print('Computer - '+str(n1))
            os.system('cls')
            if n1!=n:
                s1+=n
                if s1>s:
                    print('Computer - ' + str(s) + '/1')
                    print('Player - ' + str(s1) + '/0')
                    print('Player Won by a Wicket')
                    break
            else:
                print('Computer - ' + str(s) + '/1')
                print('Player - ' + str(s1) + '/1')
                if s>s1:print('Computer Won by '+str(s-s1)+' Runs')
                else :print('Draw')
                break
input()
