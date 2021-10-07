message = input('Enter a message. ')
for i in range(len(message)):
    coded_letter_asci = (ord(message[i]) + 1)
    coded_letter_char = chr(coded_letter_asci)
    print(coded_letter_char, end='')
    
