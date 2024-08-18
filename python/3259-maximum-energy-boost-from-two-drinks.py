class Solution:
    def maxEnergyBoost(self, v1, v2):
        n = len(v1)
        dp = [[0] * 2 for _ in range(n)]

        # Initialize the first elements in the dp table
        dp[0][0] = v1[0]
        dp[0][1] = v2[0]

        # Fill the dp table
        for i in range(1, n):
            # Choose from v1 and v2 based on previous values
            dp[i][0] = v1[i] + dp[i - 1][0]
            dp[i][1] = v2[i] + dp[i - 1][1]

            if i - 2 >= 0:
                dp[i][0] = max(dp[i][0], v1[i] + dp[i - 2][1])
                dp[i][1] = max(dp[i][1], v2[i] + dp[i - 2][0])

        # Return the maximum energy boost possible
        return max(dp[n - 1][0], dp[n - 1][1])
