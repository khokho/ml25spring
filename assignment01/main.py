n_sequence: int = int(input("Input number of strings:"))
sequences: list[str] = []
for i in range(n_sequence):
    sequences.append(input(f"Input string #{i}: ").strip())

new_sequence: str = input("Input the target string: ").strip()

best: tuple[int, str] = (-1, "N/A")
for i, seq in enumerate(sequences):
    c: int = 0
    for a, b in zip(seq, new_sequence):
        c += a == b
    best = max(best, (c, seq))

print(f'Most similar sequence with {best[0]} characters matching is "{best[1]}"')
