import pandas as pd




# show use of list.index() method
# create a list
list1 = ['physics', 'chemistry', 'mathematics']
# call index() method
# returns index of 'chemistry'
print('Index of chemistry:', list1.index('chemistry'))


list1.insert(1, 'geography')
print('Updated List:', list1)

list1.extend(['history', 'civics'])
print('Updated List:', list1)

list1.pop(1)
print('Updated List:', list1)










