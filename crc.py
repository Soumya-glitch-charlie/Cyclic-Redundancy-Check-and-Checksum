def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def crc(data, divisor):
    div_len = len(divisor)
    temp = data[0: div_len]
    while div_len < len(data):
        if temp[0] == '1':
            temp = xor(divisor, temp) + data[div_len]
        else:
            temp = xor('0' * div_len, temp) + data[div_len]
        div_len += 1
    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * div_len, temp)
    check = temp
    return check


#---------------------------------------- <Driver code> --------------------------------------------
data = "100100001"
divisor = "1101"
appended_data = data + '0' * (len(divisor) - 1)
check = crc(appended_data, divisor)
print("The check is:", check)

# --------------------------------------- <Sender Side> --------------------------------------------
data = "100100001"
divisor = "1101"
appended_data = data + '0' * (len(divisor) - 1)
checksum = crc(appended_data, divisor)
print("Checksum at sender side:", checksum)

# -------------------------------------- <Receiver Side> -------------------------------------------
data = "100100001"
divisor = "1101"
checksum = crc(data, divisor)
if checksum == '000':
    print("No error in data.")
else:
    print("Error in data.")
