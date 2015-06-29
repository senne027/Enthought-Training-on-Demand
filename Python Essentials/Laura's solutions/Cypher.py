from string import maketrans

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
shifted = letters[10:] + letters[:10]

message = "HELLO WORD" 

encoded_message = message.translate(maketrans(letters, shifted))
print encoded_message

secret_message = "ZIDRYX SC KGOCYWO"
decoded_message = secret_message.translate(maketrans(shifted, letters))
print decoded_message

def encode_tool(message, shift):
     shift = shift % 26
     letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
     shifted_letters = letters[shift:] + letters[:shift]
     encoded = message.translate(maketrans(letters, shifted_letters))
     return encoded