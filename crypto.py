import crypto_module as crypto

encryption_rounds = 10

encrypted_string = crypto.encrypt("MyNameIsThomas", encryption_rounds)

print(encrypted_string)

# WfXkwoSåArywkå

decrypted_string = crypto.decrypt(encrypted_string, encryption_rounds)

print(decrypted_string)

# MyNameIsThomas


