'''
file = open('Output.txt','r+')
write_file = file.write(input("please enter the input: \n" + "please enter additional data to same file: "))
print(write_file)
file.close()
'''

input1 = str(input("please enter first input to append to file: "))
input2 = str(input("please input additional data to input in file: "))

try:
    file = open('output.txt','a')
    write_file = file.write((input1) + (input2))
    file.close()

    file = open('sample.txt', 'r+')
    read_file = file.read()
    print(read_file)
    file.close()

except SyntaxError:
    print("file not found")

finally:
    print("Thank You")