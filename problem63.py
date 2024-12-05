import itertools

def compute():
    total_count = 0
    for i in range(1,1000):
        count = 0
        for n in itertools.count(1):
            digit_count = len(str(n**i))
            if (digit_count == i):
                count += 1
            if (digit_count > i):
                break;
        total_count += count;
        print(f"For exponent {i} found {count} matches")
    print(f"In total, {total_count} matches")

compute()