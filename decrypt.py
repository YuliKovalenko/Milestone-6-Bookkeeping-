alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

step = int(input("Enter the encryption step: "))
message = input("Enter the message to be decrypted: ").upper()
decrypted_message = ''


for i in message:
    position = alphabet.find(i)
    new_position = position - step
    if i in alphabet:
        decrypted_message += alphabet[new_position]
    else:
        decrypted_message += i


print("Decrypted message: ",decrypted_message.capitalize())
