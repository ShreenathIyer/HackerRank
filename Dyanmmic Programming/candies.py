def distribute(N, rating):
    count = 0
    candies = [1] * N
    for i in range(1, N):
        if rating[i] > rating[i - 1] and candies[i] <= candies[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(N - 2, -1, -1):
        if rating[i] > rating[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1
    count = sum(candies)
    return count


if __name__ == "__main__":
    N = int(input())
    rating = []
    for i in xrange(0, N):
        temp = int(input())
        rating.append(temp)
    print distribute(N, rating)