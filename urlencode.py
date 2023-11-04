from urllib.parse import quote_plus
import pyperclip

text = pyperclip.paste()
encoded_text = quote_plus(text)
pyperclip.copy(encoded_text)