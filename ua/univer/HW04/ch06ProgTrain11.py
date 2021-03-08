# 11. Personal Web Page Generator
# Write a program that asks the user for his or her name, then asks the user to enter a sentence that describes himself or herself. Here is an example of the program’s screen:
# Enter your name: Julie Taylor Enter
# Describe yourself: I am a computer science major, a member of the
# Jazz club, and I hope to work as a mobile app developer after I
# graduate. Enter
# Once the user has entered the requested input, the program should create an HTML file,
# containing the input, for a simple Web page. Here is an example of the HTML content,
# using the sample input previously shown:
# <html>
# <head>
# </head>
# <body>
#  <center>
#  <h1>Julie Taylor</h1>
#  </center>
#  <hr />
#  I am a computer science major, a member of the Jazz club,
#  and I hope to work as a mobile app developer after I graduate.
#  <hr />
# </body>
# </html>

def nameInput():
    name = input("Enter your name: ")
    return name


def descrInput():
    descr = input("Enter a sentence that describes you: ")
    return descr


def main():
    name = nameInput()
    descr = descrInput()
    toFile = open("webpage.txt", 'w')
    toFile.write("<html>\n")
    toFile.write("<head>\n")
    toFile.write("</head>\n")
    toFile.write("<body>\n")
    toFile.write("  <center>\n")
    toFile.write("      <h1>"+name+"</h1>\n")
    toFile.write("  </center>\n")
    toFile.write("  <hr />\n")
    toFile.write("  "+descr+'\n')
    toFile.write("  <hr />\n")
    toFile.write("</body>\n")
    toFile.write("</html>\n")
    toFile.close()
    print("Updated")


if __name__ == '__main__':
    main()
