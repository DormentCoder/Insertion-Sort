def insertion_sort(data):
    n = len(data)
    num_sorted = 1
    while num_sorted < n:
        temp = data[num_sorted]
        index = num_sorted
        while index > 0 and temp < data[index - 1]:
            data[index] = data[index - 1]
            index -= 1
        data[index] = temp
        num_sorted += 1

data = [92, 471, -49, 340, 286, 406, 127, 352, 407, 78, 225, 499, 224, 83, 269, -103, 356, 137, -187, 317, 495, 82, 409, 345, 483, -108, 100, 296, 52, 19, 327, 272, 123, 34, 189, 56, 150, 12, 9, 240]
insertion_sort(data)
print(data)