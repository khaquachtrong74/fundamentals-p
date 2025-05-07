import pyfiglet
text = pyfiglet.figlet_format(text='The Wizard', font='avatar')
with open('./logo.txt', 'w') as f:
    f.write(text)
print(text)

