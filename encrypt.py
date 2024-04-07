alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

step = int(input("Enter the encryption step: "))
message = input("Enter the message to be encrypted: ").upper()
encrypted_message = ''


for i in message:
    position = alphabet.find(i)
    new_position = position + step
    if i in alphabet:
        encrypted_message += alphabet[new_position]
    else:
        encrypted_message += i


print("Encrypted message: ",encrypted_message.capitalize())