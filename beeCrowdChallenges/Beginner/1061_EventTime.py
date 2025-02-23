start_day = int(input().split()[1])
start_hour, start_minute, start_second = map(int, input().split(" : "))

end_day = int(input().split()[1])
end_hour, end_minute, end_second = map(int, input().split(" : "))

start_total_seconds = (start_day * 86400) + (start_hour * 3600) + (start_minute * 60) + start_second
end_total_seconds = (end_day * 86400) + (end_hour * 3600) + (end_minute * 60) + end_second

duration_seconds = end_total_seconds - start_total_seconds

days = duration_seconds // 86400
duration_seconds %= 86400
hours = duration_seconds // 3600
duration_seconds %= 3600
minutes = duration_seconds // 60
seconds = duration_seconds % 60

print(f"{days} dia(s)")
print(f"{hours} hora(s)")
print(f"{minutes} minuto(s)")
print(f"{seconds} segundo(s)")
