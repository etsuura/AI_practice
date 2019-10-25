def levenshtein(s1, s2):
    n, m = len(s1), len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,         # insertion
                           dp[i][j - 1] + 1,         # deletion
                           dp[i - 1][j - 1] + cost)  # replacement

    return dp

def main():
    s1 = "りつめいかん"
    s2 = "はつめいか"

    dp = levenshtein(s1, s2)

    s1 = list(s1)
    s2 = list(s2)
    for i in range(len(s1)):
        for j in range(len(s2)):
            print(dp[i][j] + 1, end="  ")
        print("")

    print("Levenshtein Distance is %d" %(dp[len(s1)][len(s2)] + 1))

if __name__ == '__main__':
    main()