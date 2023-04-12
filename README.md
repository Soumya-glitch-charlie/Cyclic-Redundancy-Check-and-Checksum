# Cyclic-Redundancy-Check and Checksum
 What Is a Cyclic Redundancy Check (CRC)?
 
answer : The CRC is a network method designed to detect errors in the data and information transmitted over the network. This is performed by performing a binary solution on the transmitted data at the sender’s side and verifying the same at the receiver’s side.
The term CRC is used to describe this method because Check represents the “data verification,” Redundancy refers to the “recheck method,” and Cyclic points to the “algorithmic formula.”

Working of CRC Method :

Sender Side (Generation of Encoded Data from Data and Generator Polynomial (or Key)) : 

The binary data is first augmented by adding k-1 zeros in the end of the data
Use modulo-2 binary division to divide binary data by the key and store remainder of division.
Append the remainder at the end of the data to form the encoded data and send the same

Receiver Side (Check if there are errors introduced in transmission) :
Perform modulo-2 division again and if the remainder is 0, then there are no errors. 

Modulo 2 Division :
The process of modulo-2 binary division is the same as the familiar division process we use for decimal numbers. Just that instead of subtraction, we use XOR here.
In each step, a copy of the divisor (or data) is XORed with the k bits of the dividend (or key).
The result of the XOR operation (remainder) is (n-1) bits, which is used for the next step after 1 extra bit is pulled down to make it n bits long.
When there are no bits left to pull down, we have a result. The (n-1)-bit remainder which is appended at the sender side.

Illustration:
Example 1 (No error in transmission): 

Data word to be sent - 100100
Key - 1101 [ Or generator polynomial x3 + x2 + 1]

Sender Side:

![rational2](https://user-images.githubusercontent.com/127016329/230738816-1a1a9f6b-519e-4a9c-975b-623089e9e86a.jpg)

Therefore, the remainder is 001 and hence the encoded 
data sent is 100100001.

Receiver Side:
Code word received at the receiver side  100100001

![rational2](https://user-images.githubusercontent.com/127016329/230738856-2b2459b2-44d4-4653-a9d3-d8359d5e87f8.jpg)

Therefore, the remainder is all zeros. Hence, the
data received has no error.
