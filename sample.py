def probability_below(data, bound):
    count_below = sum(1 for d in data if d < bound)
    total_data_points = len(data)
    probability = count_below / total_data_points
    return probability

data = [0, 1, 2, 3, 4]
bound = 1.5
print(probability_below(data, bound))

