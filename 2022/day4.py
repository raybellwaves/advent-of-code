sample = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
_l = []
sample_splitted = sample.split("\n")
for i in sample.split("\n"):
    if i != "":
        e1 = i.split(",")[0]
        start1 = int(e1.split("-")[0])
        stop1 = int(e1.split("-")[1])
        e2 = i.split(",")[1]
        start2 = int(e2.split("-")[0])
        stop2 = int(e2.split("-")[1])
        if (
            len(
                set(range(start1, stop1 + 1)).intersection(
                    set(range(start2, stop2 + 1))
                )
            )
            > 0
        ):
            # overlapping
            # check for fully contained
            if (
                start1 <= start2
                and stop1 >= start2
                or start2 <= start1
                and stop2 >= start1
            ):
                _l.append(True)
            # if (start2 >= start1) & (stop2 <= stop1):
            #     _l.append(True)
len(_l)


with open("day4.txt") as f:
    sample = f.read()


def get_range(r):
    n = tuple(int(c) for c in r.split("-"))
    return range(n[0], n[1] + 1)


def subset(x, y):
    return not (False in [z in y for z in x])


subset_pairs, overlaps = 0, 0

# https://www.reddit.com/r/adventofcode/comments/zc0zta/comment/iyxpvbl/?utm_source=share&utm_medium=web2x&context=3
with open("day4.txt") as f:
    for line in f:
        ar, br = line.split(",")
        a, b = get_range(ar), get_range(br)

        if subset(a, b) or subset(b, a):  # part 1
            subset_pairs += 1

        if set(a).intersection(set(b)) != set():  # part 2
            overlaps += 1

print("part 1:", subset_pairs, "\npart 2:", overlaps)
