#!/usr/bin/env python3

def minOperations(n):
    # If n is less than 2, it's impossible to achieve
    if n < 2:
        return 0

    # Initialize an array to store minimum operations
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        # Initialize dp[i] with a maximum possible value
        dp[i] = float('inf')

        # Find factors of i
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                # Calculate operations needed to get to i from j
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
