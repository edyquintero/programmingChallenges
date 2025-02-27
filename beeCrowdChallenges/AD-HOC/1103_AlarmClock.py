while True:
    time = input().split()

    h1, m1, h2, m2 = map(int, time)

    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break

    start_minutes = h1 * 60 + m1
    end_minutes = h2 * 60 + m2

    if end_minutes <= start_minutes:
        end_minutes += 24 * 60

    sleep_time = end_minutes - start_minutes
    print(sleep_time)
