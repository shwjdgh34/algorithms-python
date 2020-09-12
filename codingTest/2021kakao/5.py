def solution(play_time, adv_time, logs):
    def timeToSecond(t):
        tArr = list(map(int, t.split(':')))
        return tArr[0]*3600 + tArr[1]*60 + tArr[2]
    timeBar = [0] * timeToSecond(play_time)

    for time in logs:
        timeArr = list(map(timeToSecond, time.split('-')))
        start, end = timeArr[0], timeArr[1]
        timeBar.insert

    answer = ''
    return answer


print(solution("02:03:55",	"00:14:15",	[
      "01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
