from urllib.parse import unquote_plus
import pyperclip

text = pyperclip.paste()
decoded_text = unquote_plus(text)
pyperclip.copy(decoded_text)