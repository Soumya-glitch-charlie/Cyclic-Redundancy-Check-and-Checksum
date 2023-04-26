# --------------------------------<Sender Code>-------------------------------
def checksum(binary_value):  # defining a functon checksum #
    checksum_value = 0  # the value was initially set to 0#
    # taking a for loop for a iteration from 0 to the total length of main binary value and deviding it into 4 sequences#
    for i in range(0, len(binary_value), 4):
        # updating to a new checksum value by taking the first 4 bits of binary value and converting it into a decimal value#
        checksum_value += int(binary_value[i:i + 4], 2)
        print(checksum_value)
        # if the decimal checksum value is greater than 15 the if block gets executed #
        if checksum_value > 15:
            checksum_value = (checksum_value % 16) + 1
            # 15 is the max 4 digit decimal no. that has all 1's in it so any more than that would result in 5 bits which we have to concatenate according to the rules of checksum and ad a 1's complement to it #
    checksum_value = bin(checksum_value ^ 15)[2:].zfill(4)
    # then doing the xor operation between new checksum and 15 and if any bits falls short for next calc. the zfill function fills that up with 0 and the [2:] is used for removing the prefix 0b which naturally adds up with the checksum value#
    return checksum_value


binary_value = "1010101100111100"  # Example binary value
checksum_value = checksum(binary_value)
print("Binary value: " + binary_value)
print("Checksum value: " + checksum_value)
sender_data = binary_value + checksum_value  # adding the binary value and checksum value together#
print("Data sent: " + sender_data)


# ------------------------------<Receiver Code>--------------------------------
def verify_checksum(data):  # defining a functon verify_checksum#
    binary_value = data[:-4]  # taking the all bits excluding only the last 4 bits of the data#
    received_checksum = data[-4:]  # taking only the checksum value of 4 bits#
    calculated_checksum = checksum(binary_value)  # calling the checksum func for the generating the checksum#
    return received_checksum == calculated_checksum  # checking the return value if it is really true or false#


received_data = len(checksum_value)*"1"  # Example received data
print("\nReceived data: " + received_data)
# Calling the verify checksum func and checking if it really received the true data then yes#
if verify_checksum(received_data):
    print("Checksum verified. Data is error-free.")
# Or else if it received the wrong output there must be any interruption of data#
else:
    print("Checksum verification failed. Data may be corrupted.")
