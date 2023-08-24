def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

def fast_function():
    return sum(range(1000000))

if __name__ == "__main__":
    import cProfile
    cProfile.run("slow_function()")
    cProfile.run("fast_function()")
