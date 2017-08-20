#!/bin/python3


def compare(a, b):
    return a > b and 1 or 0


def solve(a0, a1, a2, b0, b1, b2):
    alice_points = compare(a0, b0) + compare(a1, b1) + compare(a2, b2)
    bob_points = compare(b0, a0) + compare(b1, a1) + compare(b2, a2)
    return alice_points, bob_points

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]

result = solve(a0, a1, a2, b0, b1, b2)

print(" ".join(map(str, result)))
