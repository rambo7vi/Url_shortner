# Importing Python Modules
import pyshorteners

long_link = input("Your Link: ")
shortener = pyshorteners.Shortener()
short_link =shortener.tinyurl.short(long_link)
print(short_link)