deck = [17,13,11,2,3,5,7]
res = [0] * len(deck)
deck.sort(reverse=True)
N = len(deck)
evenodd = 1  # 1 for odd, 2 for even
# index = 0
positions = [i for i in range(N)]


def odd():
    global positions
    positions_copy = positions[:]  # Create a copy of positions list
    for index in positions_copy:
        if index % 2 != 0:
            res[index] = deck.pop()
            positions.remove(index)
    if positions:  # If there are remaining positions, continue to fill them recursively
        even()



def even():
    global positions
    positions_copy = positions[:]  # Create a copy of positions list
    for index in positions_copy:
        if index % 2 == 0:
            res[index] = deck.pop()
            positions.remove(index)
    # return res
    if positions:
        odd()
    return res


print(even())

