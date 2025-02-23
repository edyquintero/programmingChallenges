time = input().split()

start_hour = int(time[0])
start_min = int(time[1])
end_hour = int(time[2])
end_min = int(time[3])

def calculate_hours(s_h, e_h, s_m, e_m):
    if s_h == e_h and s_m == e_m:
        return [24, 0]

    total_minutes_start = s_h * 60 + s_m
    total_minutes_end = e_h * 60 + e_m

    if total_minutes_end <= total_minutes_start:
        total_minutes_end += 24 * 60

    total_duration = total_minutes_end - total_minutes_start
    return [total_duration // 60, total_duration % 60]

time_calculated = calculate_hours(start_hour, end_hour, start_min, end_min)

print(f"O JOGO DUROU {time_calculated[0]} HORA(S) E {time_calculated[1]} MINUTO(S)")
