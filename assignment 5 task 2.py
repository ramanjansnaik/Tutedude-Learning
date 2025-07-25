'''
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

'''

numbers = [1,2,3,4,5,6,7,8,9,10]
first_five = numbers[:5]
rev_num = first_five[::-1]

print("the first five numbers are: ", first_five)

print("the reverse of the numbers are : ", rev_num)