import math

wrt = 100000000

def factor(N):
    limit = int(math.sqrt(N))
    pairs = []
    for i in range(1, limit+1):
        quotient = N/i
        if i*quotient == N:
            pairs.append((i, quotient))
            if quotient != i:
                pairs.append((quotient, i))

    return pairs

def alternating_sum_of_subsequent_squares(start, N):
    end = start + N - 1
    odd = sum_of_squares_of_odd_integers_up_to(end) - sum_of_squares_of_odd_integers_up_to(start-1)
    even = sum_of_squares_of_even_integers_up_to(end) - sum_of_squares_of_even_integers_up_to(start-1)
    if end%2 == 0:
        return even - odd
    else:
        return odd - even


def sum_of_squares_of_even_integers_up_to(N):
    upper_limit = N/2
    return ((2*(upper_limit%wrt)*((upper_limit%wrt)+1)*(2*(upper_limit%wrt)+1))/3)%wrt

def sum_of_squares_of_odd_integers_up_to(N):
    if N%2 == 0:
        N -= 1
    factors = [N, (N+1)/2, 2*N+1]

    numerator = 1
    for factor in factors:
        numerator = (numerator*(factor%wrt))%wrt

    all = (numerator/3)%wrt
    even = sum_of_squares_of_even_integers_up_to(N)
    return all - even

def P(f, r):
    initial_floor_entry = int((f**2)/2)
    if f == 1:
        initial_floor_entry = 1

    if r == 1:
        return initial_floor_entry % wrt

    if f == 1:
        starting_square = 4
    elif f%2 == 0:
        starting_square = (f+1)**2
    else:
        starting_square = f**2

    starting_point = int(math.sqrt(starting_square))
    entry = alternating_sum_of_subsequent_squares(starting_point, r-1)
    if r%2 == 0:
        entry = (entry - initial_floor_entry) % wrt
    else:
        entry = (entry + initial_floor_entry) % wrt

    return entry

objective = 71328803586048

floor_room_pairs = factor(objective)
entries = [P(floor, room) for floor, room in floor_room_pairs]

solution = 0
for i in range(len(entries)):
    solution = (solution + entries[i]) % wrt

print solution
