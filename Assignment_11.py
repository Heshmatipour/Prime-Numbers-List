prime_list = []
for prime in range(100):
    if prime > 1:
        for i in range(2, prime):
            if (prime % i) == 0:
                break
        else:
            prime_list.append(prime)
print(prime_list)
