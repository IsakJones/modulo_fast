from is_prime import is_prime

cases = [
    (2, True),
    (3, True),
    (6, False),
    (7, True),
    (11, True),
    (12, False),
    (21, False),
    (37, True),
    (87, False),
    (89, True),
    (111, False),
    (191, True),
    (307, True),
    (309, False),
    (427, False),
    (433, True),
    (521, True),
    (528, False),
    (677, True),
    (763, False),
    (877, True),
    (940, False),
    (941, True),
    (997, True),
]

for ind, case in enumerate(cases):

    if is_prime(case[0]) == case[1]:
        print(f"Test {ind} passed!")
    else:
        print(f"Test {ind} didn't pass...")