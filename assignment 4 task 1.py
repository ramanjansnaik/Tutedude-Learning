try:
    file1 = open('sample.txt','r+')
    write_file = file1.write("This is a sample text file\n" + "it contains multiple lines")
    file1.close()

    file1 = open('sample.txt','r+')
    read_file = file1.read()
    print(read_file)
    file1.close()

except SyntaxError:
    print("Error: the file Sample.txt is not found")

finally:
    print ("Thank you")