#!/usr/bin/env python3
import argparse
import logging
import random

#-------------------------------------------------------------------------------
# Logging related common code
def initialize_log_settings(loglevel):
    log_levels = {
            "debug" : logging.DEBUG,
            "warning" : logging.WARN,
            "critical" : logging.CRITICAL,
            "info": logging.INFO
    }

    logging.basicConfig(format='%(asctime)s - %(name)s %(levelname)s:%(message)s', level=log_levels[loglevel])

#-------------------------------------------------------------------------------
def register_common_arguments():
    description = 'Is a math excersize to improve mental math'
    parser = argparse.ArgumentParser()

    parser.add_argument('--loglevel', choices=['debug', 'info', 'warning', 'critical'], help='logging level for diagnostics, default=critical', default='critical')

    return parser

def register_program_arguments(parser):
    parser.add_argument('--digitsNum', type=int, help='the amount of digits to do the operations with', default="2")

def mathGame(args):
    digits = args.digitsNum
    minNum=[1]
    correct=0
    wrong=0
    while(len(minNum)<digits):
        minNum.append(0)
    maxNum=[9]
    while(len(maxNum)<digits):
        maxNum.append(9)

    minNum=listToint(minNum)
    maxNum=listToint(maxNum)
    counter=1
    print("[1] short game(10 questions)")
    print("[2] infinite game(enter quit to quit)")
    inputMain = input(": ")

    if inputMain=="1":
        while counter<=10:
            num1=random.randint(minNum, maxNum)
            num2=random.randint(minNum, maxNum)
            operation=random.randint(1, 3)
            if operation==1:#addition
                print(num1, "+", num2)

            elif operation==2:#subtraction
                print(num1, "-", num2)

            elif operation==3:#multiplication
                print(num1, "*", num2)

            inputMain = input(": ").lower().strip()
            if inputMain == "exit":
                print("correct:", correct)
                print("wrong:", wrong)
                print("bye")
                sys.exit()

            elif inputMain == "":
                wrong+=1

            elif operation == 1 and num1+num2 == int(inputMain):
                correct+= 1
            elif operation == 1 and num1+num2 != int(inputMain):
                wrong += 1

            elif operation == 2 and num1-num2 == int(inputMain):
                correct += 1
            elif operation == 2 and num1-num2 != int(inputMain):
                wrong += 1

            elif operation == 3 and num1*num2 == int(inputMain):
                correct += 1
            elif operation == 3 and num1*num2 != int(inputMain):
                wrong += 1


            counter +=1

    elif inputMain=="2":
        while True:
            num1=random.randint(minNum, maxNum)
            num2=random.randint(minNum, maxNum)
            operation=random.randint(1, 3)
            if operation==1:#addition
                print(num1, "+", num2)

            elif inputMain == "":
                wrong+=1

            elif operation==2:#subtraction
                print(num1, "-", num2)

            elif operation==3:#multiplication
                print(num1, "*", num2)

            inputMain = input(": ").lower().strip()
            if inputMain == "exit":
                print("correct:", correct)
                print("wrong:", wrong)
                print("bye")
                sys.exit()
            elif operation == 1 and num1+num2 == int(inputMain):
                correct+= 1
            elif operation == 1 and num1+num2 != int(inputMain):
                wrong += 1

            elif operation == 2 and num1-num2 == int(inputMain):
                correct += 1
            elif operation == 2 and num1-num2 != int(inputMain):
                wrong += 1

            elif operation == 3 and num1*num2 == int(inputMain):
                correct += 1
            elif operation == 3 and num1*num2 != int(inputMain):
                wrong += 1

            elif inputMain == "":
                wrong+1
    print("correct:", correct)
    print("wrong:", wrong)

def listToint(list_a):
    strings = [str(integer) for integer in list_a]
    a_string = "".join(strings)
    return int(a_string)

def main():
    parser = register_common_arguments()
    register_program_arguments(parser)

    args = parser.parse_args()

    initialize_log_settings(args.loglevel)

    mathGame(args)

if __name__ == '__main__' :
    main()
