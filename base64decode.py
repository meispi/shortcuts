import pyperclip, base64

text = pyperclip.paste()
decoded_text = base64.b64decode(text.encode("utf-8"))
pyperclip.copy(decoded_text.decode('utf-8'))