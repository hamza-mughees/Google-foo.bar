import base64

# key is your username
key = "hamzamughees"

# encryption is your encrypted message from Google
encryption = "E0YeDwIOEBQbQkVJSEYKCAQMAUBERUIQBw0BHwAKAAJPRV9TTwQeDgQIGAIMQklTTwQLHA4fARRP RV9TTwgDGRMIEQ4KCQBUREFKGwIFHAIeAAgWBhVKWltNUhIGCQoQAwQJXU1NUhUJBwcaHBJKWltN UhQJAwBUREFKHA4CUkdSRUIEAQ9MXRw="

decryption = []

for i, j in enumerate(base64.b64decode(encryption)):
    ch = chr(j ^ ord(key[i % len(key)]))
    decryption.append(ch)

print(''.join(decryption))