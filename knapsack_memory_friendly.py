def knapsack(arr, weight):
    memory = [0] * (weight+1)

    for i in range(len(arr)):
        for w in reversed(range(weight+1)):
            if w-arr[i][1] >= 0:
                if memory[w] <= memory[w-arr[i][1]] + arr[i][0]:
                    memory[w] = memory[w-arr[i][1]] + arr[i][0]
    return memory[-1], find_path(arr, memory)

def find_path(arr, memory):
    path = []
    w = len(memory) - 1
    curr_value = memory[-1]
    for i in reversed(range(len(arr))):
        if w >= arr[i][1]:
            if curr_value - arr[i][0] <= memory[w - arr[i][1]]:
                curr_value = curr_value - arr[i][0]
                path.append(i)
                w -= arr[i][1]
    return path
