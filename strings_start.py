# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)
    
    s = "This is a string"
    print(s)
    
    # TODO: Try combining them. 
    b2 = b.decode('UTF-8')
    print(s+b2)
    # TODO: Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    s2=s.encode('UTF-8')
    print(s2+b)
    # TODO: encode the string as UTF-32
    combined = s+b2
    finalS = combined.encode('UTF-32')
    print(finalS)
if __name__ == "__main__":
    main()
