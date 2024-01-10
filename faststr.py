def string_to_little_endian_hex(s):
    byte_representation = s.encode()
    
    if len(byte_representation) > 64:
        raise ValueError("The string is too long (> 512 bytes)")
    
    hex_representation = byte_representation[::-1].hex()
    
    return hex_representation

if __name__ == "__main__":
    s = input("Enter a string (up to 512 bytes): ")
    print(string_to_little_endian_hex(s))
