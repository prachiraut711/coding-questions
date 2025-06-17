def midElement(list):
    stack = []

    while list:
        stack.append(list.pop())  # list.pop ni last element first append hoilmag 50,40,30,20,10bheten

    mid = len(stack) // 2

    stack.pop(mid)

    return stack

print(midElement([10, 20, 30, 40, 50]))