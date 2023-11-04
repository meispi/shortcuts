import pyperclip

text = pyperclip.paste()
encoded_text = "".join("%{:02x}".format(ord(char)) for char in text)
pyperclip.copy(encoded_text)