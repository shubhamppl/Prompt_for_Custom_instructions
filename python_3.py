*             CODERBYTE ARRAY MIN JUMPS CHALLENGE              *
 * Problem Statement                                            *
 * Have the function ArrayMinJumps(arr) take the array of       *
 * integers stored in arr, where each integer represents the    *
 * maximum number of steps that can be made from that position, *
 * and determine the least amount of jumps that can be made to  *
 * reach the end of the array.                                  *
 * For example: if arr is [1, 5, 4, 6, 9, 3, 0, 0, 1, 3] then   *
def ArrayMinJumps(arr):
    if not arr or arr[0] == 0:
        return -1
    n, jumps, steps, max_reach = len(arr), 1, arr[0], arr[0]
    for i in range(1, n):
        if i == n - 1:
            return jumps
        max_reach = max(max_reach, i + arr[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            if i >= max_reach:
                return -1
            steps = max_reach - i
    return -1
input_array = list(map(int, input().strip('[]').split(',')))
print(ArrayMinJumps(input_array))
