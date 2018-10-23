import random
import math

# 随机一个开始时间点，保证每次情况不同。
# 整段路的正常行驶时间，路程/速度。
# 到达路口的时间点 = 开始时间点 + 行驶时间
# 如果遇到绿灯，总耗时 = 行驶时间， 当前时间点 = 到达路口时间点 = 开始时间点 + 行驶时间
# 如果遇到红灯，等红灯的时间 = 交通灯时间周期 - 当前时间点对每个交通灯周期时间取余，
#             总耗时 = 行驶时间 + 等红灯时间
#             当前时间点 = 到达路口时间点 + 等红灯时间

def drive_to_next_crossroad(time_start,v,distance,length_green,length_waiting):
    total_time = 0
    time_leave = 0
    _driving_time = math.ceil(distance/v)
    _length_total = length_green + length_waiting
    _time_arrival = time_start + _driving_time
    if 0 <= _time_arrival%_length_total <= length_green:
        total_time = _driving_time
        time_leave = _time_arrival
        # print('Green Light !')
    elif _length_total >= _time_arrival%_length_total > length_green:
        _waiting_time = _length_total - _time_arrival%_length_total
        total_time = _driving_time + _waiting_time
        time_leave = _time_arrival + _waiting_time
        # print('Red Light !')
    return [time_leave,total_time]

result_thousand = 0
for j in range(10000):
    result = 0
    time_start = random.randint(0, 60)
    for i in range(5):
        if i == 0:
            time_leave, total_time = drive_to_next_crossroad(time_start=time_start, v=9.72, distance=1000,
                                                             length_green=15, length_waiting=45)
        else:
            time_leave, total_time = drive_to_next_crossroad(time_start=time_leave, v=9.72, distance=1000,
                                                             length_green=15, length_waiting=45)
        result += total_time
    result_thousand += result

print(result_thousand/10000)

# 结果

# 9.72m/s (35km/h) 5段路每段1000米 红灯15秒 除红灯外45秒
# 平均时间597秒 10分钟

# 12.5m/s (45km/h) 同上
# 平均时间575秒 不到10分钟

# 15.27m/s (55km/h) 同上
# 平均时间392秒 6分半

# 18m/s (65km/h) 同上
# 平均时间310秒 5分钟！！！

