# --------------------------------<Sender Code>-------------------------------
def checksum(binary_value):
    checksum_value = 0
    for i in range(0, len(binary_value), 4):
        checksum_value += int(binary_value[i:i + 4], 2)
        if checksum_value > 15:
            checksum_value = (checksum_value % 16) + 1
    checksum_value = bin(checksum_value ^ 15)[2:].zfill(4)
    return checksum_value


binary_value = "1010101100111100"  # Example binary value
checksum_value = checksum(binary_value)
print("Binary value: " + binary_value)
print("Checksum value: " + checksum_value)
sender_data = binary_value + checksum_value
print("Data sent: " + sender_data)


# ------------------------------<Receiver Code>--------------------------------
def verify_checksum(data):
    binary_value = data[:-4]
    received_checksum = data[-4:]
    calculated_checksum = checksum(binary_value)
    return received_checksum == calculated_checksum


received_data = "10101011001111000110"  # Example received data
print("\nReceived data: " + received_data)
if verify_checksum(received_data):
    print("Checksum verified. Data is error-free.")
else:
    print("Checksum verification failed. Data may be corrupted.")
