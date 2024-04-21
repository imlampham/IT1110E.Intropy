n = int(input())

def collatz_sequence(i):
    sequence = [i]
    while i != 1:
        if i % 2 == 0:
            i = i // 2
        else:
            i = 3 * i + 1
        sequence.append(i)
    return sequence
sequence = collatz_sequence(n)
for n in sequence:
	print(n, end=' ')
        
        
    