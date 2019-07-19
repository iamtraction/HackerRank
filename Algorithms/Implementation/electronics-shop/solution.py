def getMoneySpent(keyboards, drives, b):
    return max([ k + d for k in keyboards for d in drives if k + d <= b ], default=-1)
