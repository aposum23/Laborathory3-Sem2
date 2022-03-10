fileptr = open('file2.txt', 'w')

fileptr.write(
    'Python is the modern day language. It makes so simle.\n'
    'it is the fastest-growing programing language'
)

fileptr.close()

with open('file2.txt', 'w') as fileptr:
    fileptr.write(
        'Python is the modern day language. It makes so simle.\n'
        'it is the fastest-growing programing language'
    )