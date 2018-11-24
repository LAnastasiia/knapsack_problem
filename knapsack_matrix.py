def knapsack(arr, weight):
    """
    This function implements solving for the Knapsack problem using dynamic programming approach to efficiently fit
    elements with maximum value but suitable weight into a knapsack.

    :param arr:         array (list) of lists [value, weight]
    :param weight:      total weight of knapsack, which can not be exceeded by any fitted element
    :return:            array (list) of indexes of fitted element (indexation from the input array arr)
    """
    mtrx_len = weight+1
    prev = [0] * mtrx_len                                                # List for already fitted elements.
    prev_pathes = dict([(w, []) for w in range(weight+1)])               # Dict of pathes of fitted elements.

    curr = []                                                            # Intialize curr row for further usage.
    curr_pathes = []


    def take_prev():
        """
        Auxiliary function to add only previously fitted elements to the matrix row.
        """
        curr[w] = prev[w]
        path = prev_pathes[w]
        curr_pathes[w].extend(path)

    def take_element():
        """
        Auxiliary function to add an element and some fitting previous elements to the matrix row.
        """
        path = prev_pathes[w-element[1]] + [i]
        curr[w] = r2
        curr_pathes[w].extend(path)

    for i in range(len(arr)):                                            # Search for optimal way to fit each element.
        curr = [0] * mtrx_len                                            # Nullify current row of matrix to add content.
        curr_pathes = dict([(w, []) for w in range(weight+1)])
        for w in range(weight+1):
            element = arr[i]                                             # Current element.
            if w - element[1] < 0:
                take_prev()
            else:
                r1 = prev[w]                                             # Can't take this element.
                r2 = prev[w - element[1]] + element[0]                   # Take element + try to fit previous ones.
                if r2 > r1:
                    take_element()
                else:
                    take_prev()
        prev = curr                                                      # Update previous row for the next iteration.
        prev_pathes = curr_pathes
        # print(">>", curr)
        # print("--", curr_pathes)
    optimal_values = curr[-1]
    return optimal_values, curr_pathes[weight]


if __name__ == "__main__":
    arr = [[7, 5], [8, 4], [9, 3], [10, 2], [1, 10], [3, 15], [8, 10], [6, 4], [5, 3], [7, 3]]
    # arr = [[7, 5], [8, 4], [9, 3], [10, 2], [1, 10]]
    print('\n', knapsack(arr, 20))







