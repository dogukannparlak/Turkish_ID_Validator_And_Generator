def tr_identity_no(turksh_republic_idedtification_number):
    number = [int(i) for i in turksh_republic_idedtification_number]
    if ((sum(number[:10:2]) * 7 - sum(number[1:9:2])) % 10 != number[9]):
        return False
    elif(sum(number[:10]) % 10 != number[10]):
        return False
    else:
        print(f"{turksh_republic_idedtification_number} : it is a Repuplic of Türkiye identification number. ")
        return True

def sequential_11_digit_numbers(start):
    current = start
    while True:
        yield current
        current += 1

with open('potential_TR_id_numbers.txt', 'w') as file:
    generator = sequential_11_digit_numbers(10000000000)
    for i in range(100): #İn this section,enter how many numbers you want to query for #
        turksh_republic_idedtification_number = str(next(generator))
        if tr_identity_no(turksh_republic_idedtification_number):
            file.write(f'{turksh_republic_idedtification_number}\n')