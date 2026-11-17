def sum_to_goal(numbers_list, goal):
    for i in range(len(numbers_list)):
        for j in range(i + 1, len(numbers_list)):
            if numbers_list[i] + numbers_list[j] == goal:
                return (numbers_list[i] * numbers_list[j])
    return None