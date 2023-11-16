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



*             CODERBYTE SCALE BALANCING CHALLENGE              *
 *                                                              *
 * Problem Statement                                            *
 * Have the function ScaleBalancing(strArr) read strArr which   *
 * will contain two elements, the first being the two positive  *
 * integer weights on a balance scale (left and right sides)    *
 * and the second element being a list of available weights as  *
 * positive integers. Your goal is to determine if you can      *
 * balance the scale by using the least amount of weights from  *
 * the list, but using at most only 2 weights.                  *
def ScaleBalancing(strArr):
    # Parse the input
    weights_str, available_weights_str = strArr

    # Extract the weights on both sides of the scale
    left_weight, right_weight = map(int, weights_str[1:-1].split(','))

    # Extract the list of available weights
    available_weights = list(map(int, available_weights_str[1:-1].split(',')))

    # Check for trivial solutions
    difference = right_weight - left_weight
    if difference in available_weights:
        return str(difference)

    # Brute-force search
    for weight1 in available_weights:
        for weight2 in available_weights:
            if left_weight + weight1 == right_weight - weight2:
                return f"{weight1},{weight2}"

    # If no solution is found, return "not possible"
    return "not possible"
strArr = ["[3, 4]", "[1, 2, 7, 7]"]
output = ScaleBalancing(strArr)
print(output)  # Output: 1

