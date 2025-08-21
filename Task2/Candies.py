def candy(ratings):
    candies = [1, 1, 1]  # each child gets at least one candy

    # Left to right
    if ratings[1] > ratings[0]:
        candies[1] = candies[0] + 1
    if ratings[2] > ratings[1]:
        candies[2] = candies[1] + 1

    # Right to left
    if ratings[1] > ratings[2]:
        candies[1] = max(candies[1], candies[2] + 1)
    if ratings[0] > ratings[1]:
        candies[0] = max(candies[0], candies[1] + 1)

    return sum(candies)

ratings = list(map(int, input().split()))
print(candy(ratings))