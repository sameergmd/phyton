import random

def roll_dice(n=1):
    return [random.randint(1, 6) for _ in range(n)]

counts = {i: 0 for i in range(1, 7)}

while True:
    ans = input("Roll the dice? (y/n): ").lower()
    if ans != "y":
        break
    d = roll_dice(2)
    for v in d:
        counts[v] += 1
    print("You rolled:", d, "Sum =", sum(d))

print("\nFace frequency:")
for face, c in counts.items():
    print(f"{face}: {c}")
