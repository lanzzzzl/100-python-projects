
def binary_to_decimal(num):
    binary_list = list(str(num))
    # print(binary_list)
    decimal_amount = 0
    for i in range(len(binary_list)):
        digit = binary_list.pop()
        # print(f'digit is {digit}')
        # print(f'i = {i}')
        deci_val = 2**i
        # print(deci_val)
        decimal_amount += deci_val * int(digit)
    return decimal_amount


if __name__ == "__main__":
    num = input('Please input a number you want to convert. ')
    num_type = input('Please input the type of that number. (decimal/binary)').lower()
    if num_type == 'decimal':
        print(f'Decimal number {num} convert to binary is {bin(int(num))}.')
    elif num_type == 'binary':
        binary_converted = binary_to_decimal(num)
        print(f'Binary number {num} convert to decimal is {binary_converted}.')
    else:
        print('The number typr you entered is invalid.')
