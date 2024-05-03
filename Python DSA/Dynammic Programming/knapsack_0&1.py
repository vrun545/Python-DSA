
def knapsack(W, weights, val, n):
    if n == 0 or W == 0:
        return 0
    elif weights[n-1] > W:
        return knapsack(W, weights, val, n-1)
    elif weights[n-1] <= W: 
        return max( val[n-1] + knapsack(W-weights[n-1], weights ,val, n-1), knapsack(W, weights, val, n-1))


if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(knapsack(W, wt, val, n))