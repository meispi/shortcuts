import pyperclip, base64

text = pyperclip.paste()
encoded_text = base64.b64encode(text.encode("utf-8"))
pyperclip.copy(encoded_text.decode('utf-8'))