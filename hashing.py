import hashlib
import binascii
import zlib

def get_sha256_hash(data):
    sha256_hash = hashlib.sha256(data.encode()).hexdigest()
    return sha256_hash

def get_md5_hash(data):
    md5_hash = hashlib.md5(data.encode()).hexdigest()
    return md5_hash

def get_crc32_hash(data):
    crc32_hash = zlib.crc32(data.encode())
    return hex(crc32_hash)

def main():
    print("Hashing Algorithm Menu:")
    print("1. SHA-256")
    print("2. MD5")
    print("3. CRC32")
    
    choice = input("Select a hashing algorithm (1/2/3): ")
    
    if choice == '1':
        algorithm = "SHA-256"
        hash_function = get_sha256_hash
    elif choice == '2':
        algorithm = "MD5"
        hash_function = get_md5_hash
    elif choice == '3':
        algorithm = "CRC32"
        hash_function = get_crc32_hash
    else:
        print("Invalid choice")
        return
    
    data = input("Enter the string to be hashed: ")
    hash_value = hash_function(data)
    
    print(f"Hash value using {algorithm}: {hash_value}")

if __name__ == "__main__":
    main()
