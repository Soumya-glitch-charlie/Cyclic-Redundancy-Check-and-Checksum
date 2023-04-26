# Write a Python code to perform the Cyclic Redundancy Check (with error vector and without error vector).
def crc(data, divisor):  # defining a function crc#
    div_len = len(divisor)  # length of divisor#
    temp = data[0: div_len]
    while div_len < len(data):  # while the length of data is greater than divisor length #
        # if the first bit of temp i.e. data is 1 then this if loop goes into execution #
        if temp[0] == '1':
            temp = xor(divisor, temp) + data[
                div_len]  # taking the xor between divisor and the first bits of data so that the MSB is not a 0 then adding the next bit as divisor length increases in the next iteration #
        # if the first bit of temp i.e. data is 0 then this else loop goes into execution #
        else:
            temp = xor('0' * div_len, temp) + data[
                div_len]  # taking the xor between divisor of 0's and the first bits of data so that the MSB is not a 0 and by adding the 0's the value doesn't get changed then adding the next bit as divisor length increases in the next iteration #
        div_len += 1  # incrementing the div length value by 1 #

    # So as the calculation reaches the last iteration the following condition checks the validity #
    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * div_len, temp)
    check = temp  # assigning temp to a variable called check #
    return check


def xor(a, b):  # defining a function xor between two variables#
    result = []  # taking an empty array #
    # taking a for loop for iteration through 1 to the length of b#
    for i in range(1, len(b)):
        # if the 1st bit of each variable is equal then the xor results in 0#
        if a[i] == b[i]:
            result.append('0')
        # if the 1st bit of each variable is not equal then the xor results in 1#
        else:
            result.append('1')
    return ''.join(result)  # returning the boolean true value for the XOR func#


# --------------------------------------- <Sender Side> -------------------------------------------
data = "100100001"
divisor = "1101"
appended_data = data + '0' * (
            len(divisor) - 1)  # appending the value of remaining checksum to the original data for the correct receiver sequence#
checksum = crc(appended_data, divisor)  # calling the function crc#
print("Checksum at sender side:", checksum)

# -------------------------------------- <Receiver Side> -------------------------------------------
data = "100100001"
divisor = "1101"
checksum = crc(data, divisor)  # calling the function crc#
print("Checksum at receiver side:", checksum)
# checking if the sender side value matches the receiver end as well......if yes then the if block gets executed#
if checksum == '000':
    print("No error in data.")
# and if not then the else block gets executed#
else:
    print("Error in data.")
