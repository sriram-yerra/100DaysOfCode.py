def findMissingRepeatingNumbers(a: [int]) -> [int]:
    n = len(a)  # Size of array 'a'

    count = [0 for i in range(n + 1)]
    # 'count' array
    for i in range(n):
        # Incrementing the frequency of current element
        count[a[i]] += 1
    missing, repeating = 0, 0
    for i in range(1, n + 1):
        if count[i] == 0:
            missing = i
        elif count[i] == 2:
            repeating = i
    ans = []
    ans.append(repeating)
    ans.append(missing)
    return ans