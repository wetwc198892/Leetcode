count = {'A': [1, 2, 1], 'B': [1, 1, 2]}
votes = 'AB'
print(sorted(votes, key=count.__getitem__))
