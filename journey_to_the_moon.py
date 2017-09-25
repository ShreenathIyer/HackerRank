'''

The member states of the UN are planning to send 2 people to the Moon. But there is a problem. In line with their principles of global unity, they want to pair astronauts of 2 different countries.

There are N trained astronauts numbered from 0 to N-1. But those in charge of the mission did not receive information about the citizenship of each astronaut. The only information they have is that some particular pairs of astronauts belong to the same country.

Your task is to compute in how many ways they can pick a pair of astronauts belonging to different countries. Assume that you are provided enough pairs to let you identify the groups of astronauts even though you might not know their country directly. For instance, if 1, 2, 3 are astronauts from the same country; it is sufficient to mention that (1, 2) and (2, 3) are pairs of astronauts from the same country without providing information about a third pair (1, 3).

Input Format:

The first line contains two integers, N and P, separated by a single space. P lines follow. Each line contains 2 integers separated by a single space A and B such that
0 <= A, B <= N - 1

and A and B are astronauts from the same country.

Constraints:

1 <= N <= 10^5
1 <= P <= 10^4

Output Format:

An integer that denotes the number of permissible ways to choose a pair of astronauts.

Sample Input 0

5 3
0 1
2 3
0 4
Sample Output 0

6

'''


def make_sets(node, sets):
    if sets[node] < 0:
        return node
    else:
        sets[node] = make_sets(sets[node], sets)
        return sets[node]


def merge(u, v, sets):
    i = make_sets(u, sets)
    j = make_sets(v, sets)
    sum = sets[i] + sets[j]
    if sets[i] > sets[j]:
        sets[i] = j
        sets[j] = sum
    else:
        sets[j] = i
        sets[i] = sum


if __name__ == "__main__":
    N, P = map(int, raw_input().split())

    country_sets = [-1] * N

    for i in range(0, P):
        a, b = map(int, raw_input().split())
        node_a = make_sets(a, country_sets)
        node_b = make_sets(b, country_sets)

        if node_a != node_b:
            merge(node_a, node_b, country_sets)

    temp = [0] * N
    for i in xrange(0, N):
        if country_sets[i] < 0:
            temp[i] += 1
        else:
            temp[make_sets(country_sets[i], country_sets)] += 1

    total, result = 0, 0
    for i in temp:
        result += i * total
        total += i

    print result