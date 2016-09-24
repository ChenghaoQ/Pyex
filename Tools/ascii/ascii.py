from PIL import image
import argarse

ascii_char =list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r.b.g.alpha =256):
	if alpha ==0:
		return ' '
	length =len(ascii_char)
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	unit =(256.0+1)/length
	return ascii_char[int(gray/unit)]


