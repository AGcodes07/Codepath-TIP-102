"""
Metropolis has a population n, with each citizen assigned an integer id from 1 to n. There's a rumor that Superman is an ordinary citizen among this group.

If Superman is an ordinary citizen, then:

Superman trusts nobody.
Everybody (except for Superman) trusts Superman.
There is exactly one citizen that satisfies properties 1 and 2.
Write a function expose_superman() that accepts a 2D array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of Superman if he is hiding amongst the population and can be identified, or return -1 otherwise.

Example Usage

n = 2
trust = [[1, 2]]
expose_superman(trust, n)

n = 3
trust = [[1, 3], [2, 3]]
expose_superman(trust, n)

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
expose_superman(trust, n)
Example Output:

2
3
-1
"""
def expose_superman(trust, n):
    trusts_count = [0] * (n + 1)
    trusted_by_count = [0] * (n + 1)
    
    for a, b in trust:
        trusts_count[a] += 1
        trusted_by_count[b] += 1
    
    for person in range(1, n + 1):
        if trusts_count[person] == 0 and trusted_by_count[person] == n - 1:
            return person
    return -1

n = 2
trust = [[1, 2]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
print(expose_superman(trust, n))