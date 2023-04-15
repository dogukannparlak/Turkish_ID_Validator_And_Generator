def TR_ID_No():
    tr_ıd = input("Please enter the number you want to query : ")
    if not tr_ıd.isdigit():
        print("Please enter a string of digits")
        return TR_ID_No()
    elif(len(tr_ıd) != 11):
        print("Please enter a string of 11 digits")
        return TR_ID_No()

    number1 = [int(i) for i in tr_ıd]

    if (number1[0] == 0):
        print("Repuplic of Türkiye identification number cannot start with 0")
        return TR_ID_No()
    elif ((sum(number1[:10:2]) * 7 - sum(number1[1:9:2])) % 10 != number1[9]):
        print("This entry is not a Repuplic of Türkiye identification number")
    elif(sum(number1[:10])%10 != number1[10]):
        print("This entry is not a Repuplic of Türkiye identification number")
    else:
        print("This entry is a Repuplic of Türkiye identification number")
        return TR_ID_No()

TR_ID_No()
