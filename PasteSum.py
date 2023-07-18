v = '''
199999999999999
19999999999999
1999999999999
199999999999
19999999999
1999999999
199999999
19999999
1999999
199999
19999
1999
199
19
1
'''

values = v.strip().split('\n')
array = list(map(int, values))

total_sum = sum(array)
print("The sum of the array is:", total_sum)
