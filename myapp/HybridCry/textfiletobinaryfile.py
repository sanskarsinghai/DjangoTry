#-,bullet dots of list, 's or 't
def TxtToBin():
    with open('myapp\HybridCry\F2\d2.txt', 'r') as txtfile:
        mytextstring = txtfile.read()

    mytextstring = mytextstring.encode('utf-8')

    binarray = ' '.join(format(ch, 'b') for ch in bytearray(mytextstring))

    with open('myapp\HybridCry\F2\BinfileName1.bin', 'w') as binfile:
        binfile.write(binarray)