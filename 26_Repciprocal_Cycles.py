

# copied from this somewhere, but I'm not using it
def cycles_detection(funs):
    # Bigger cycle size first
    for size in reversed(range(2, 1 + len(funs) // 2)):
        # Find all consecutive sequences of size `size`
        for start in range(size):
            # Split the list by slices of size `size`, starting at position `start`
            end = size * ((len(funs) - start) // size) + start
            sequences = [tuple(funs[i:i + size]) for i in range(start, end, size)]
            sequences = filter(None, [tuple(funs[:start])] + sequences + [tuple(funs[end:])])

            # Init repetition to 1 then calculate consecutive repetitions
            groups = [(seq, 1) for seq in sequences]
            packing = [groups.pop(0)]
            while groups:
                prev_grp = packing[-1]
                next_grp = groups.pop(0)
                if prev_grp[0] == next_grp[0]:
                    packing[-1] = (prev_grp[0], prev_grp[1] + next_grp[1])
                else:
                    packing.append(next_grp)

            # has cycle if any repetition is greater than 2
            has_cycle = any(grp[1] > 1 for grp in packing)
            if has_cycle:
                return packing


def reduce_denominator_to_min_cycle(list):
    while True:
        temp_results = cycles_detection(list)
        if temp_results == None:
            break
        list = temp_results[0][0]

    return list

def reciprocal_cycles():

    max_cycle_length = 0
    max_cycle = []
    max_i = 0
    for i in range(2, 1000):
        # i cant divide enough integers with this so this way doesnt work
        fraction = 1/i
        decimal = str(fraction)[2:]
        dec = list(decimal)
        cycle_test = cycles_detection(dec)

        if cycle_test is not None:

            for cycle in cycle_test:

                reduced_cycle = reduce_denominator_to_min_cycle(cycle[0])
                all_same = True
                for j in range(1, len(reduced_cycle)):
                    if reduced_cycle[j] != reduced_cycle[j-1]:
                        all_same = False

                if all_same:
                    temp_max= 1
                else:
                    temp_max = len(reduced_cycle)

                if temp_max > max_cycle_length:
                    max_cycle_length = temp_max
                    max_cycle = reduced_cycle
                    max_i = i

    return max_cycle_length, max_cycle, max_i

def detect_cycle_in_numerator(num):
    decimal_list = []
    rem = 1

    length = 0
    while len(decimal_list) < num and rem != 0:

        rem = (rem % num)
        print(rem)
        if rem in decimal_list or rem == 0:
            print('break')
            break
        decimal_list.append(rem)
        rem *= 10
        length+=1

    print(decimal_list)
    return length, num

def get_greatest_cycle_length(limit):
    max = 0
    temp_index = 0
    for i in range(limit):
        cycle_length, index = detect_cycle_in_numerator(i)
        if cycle_length > max:
            max = cycle_length
            temp_index = index

    return max, temp_index



print(get_greatest_cycle_length(1000))