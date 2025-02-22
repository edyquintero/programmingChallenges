def calculateTime(timeOnlySeconds):
    hours = timeOnlySeconds // 3600
    remainingSeconds = timeOnlySeconds % 3600
    minutes = remainingSeconds // 60
    seconds = remainingSeconds % 60
    return "{}:{}:{}".format(hours, minutes, seconds)


time = int(input())
print(calculateTime(time))
