
n_sequence = int(input('Input number of strings:'))
sequences = []
for i in range(n_sequence):
    sequences.append(input(f'Input string #{i}: ').strip())

new_sequence = input(f'Input the target string: ').strip()

best = (-1, None)
for i, seq in enumerate(sequences):
    c = 0
    for (a,b) in zip(seq, new_sequence):
        c += a==b
    best = max(best, (c, seq))

print(f'Most similar sequence with {best[0]} characters matching is "{best[1]}"')




