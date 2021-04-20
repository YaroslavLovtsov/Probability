
def find_position(my_list, new_value):
    left_border = 0
    right_border = len(my_list)

    while True:
        middle_position = (left_border + right_border) // 2

        middle_value = my_list[middle_position]
        if middle_position + 1 == len(my_list):
            return len(my_list) - 1

        elif (middle_position == 0) & (my_list[middle_position] > new_value):
            return 0

        elif middle_value > new_value:
            right_border = middle_position

        elif (middle_value < new_value) & (my_list[middle_position + 1] >= new_value):
            return middle_position + 1

        elif middle_value == new_value:
            return middle_position

        else:
            left_border = middle_position


def median_detect_list_transform(median_detect_list, to_del, to_add):
    to_del_pos = find_position(median_detect_list, to_del)
    to_add_pos = find_position(median_detect_list, to_add)

    mll = len(median_detect_list)

    if to_del_pos < to_add_pos:
        for el1 in range(to_add_pos - to_del_pos):
            if to_del_pos + el1 + 1 < mll:
                median_detect_list[to_del_pos + el1] = median_detect_list[to_del_pos + el1 + 1]
        median_detect_list[to_add_pos] = to_add
    elif to_add_pos < to_del_pos:
        for el2 in range(to_del_pos - to_add_pos):
            if to_del_pos - el2 - 1 >= 0:
                median_detect_list[to_del_pos - el2] = median_detect_list[to_del_pos - el2 - 1]
        median_detect_list[to_add_pos] = to_add
    else:
        median_detect_list[to_add_pos] = to_add

rates = []
medianes = []
with open('usd_rates.txt') as file_1:
    for line in file_1:
        a = tuple([el for el in line.strip().split(' ') if el != ''])[1]
        rates.append(float(a.replace("'", '').replace(",", '.')))

T = len(rates)
N = 100

median_detect_list = rates[:N]
median_detect_list.sort()

for inx in range(T-N):
    to_del = rates[inx]
    to_add = rates[inx + N]
    if N % 2 == 0:
        current_median = 0.5 * (median_detect_list[N // 2 - 1] + median_detect_list[N // 2])
    else:
        current_median = median_detect_list[N // 2 + 1]
    medianes.append(current_median)
    median_detect_list_transform(median_detect_list, to_del, to_add)

for inx2 in range(T):
    if inx2 < N:
        print("{:8.5f}".format(rates[inx2]))
    elif inx2 + N >= T:
        print("{:8.5f}".format(rates[inx2]))
    else:
        print("{:8.5f}".format(rates[inx2]), "{:8.5f}".format(medianes[inx2 - N]))