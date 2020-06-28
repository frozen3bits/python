import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

#1定义语言变量和术语
x_room_temp = np.arange(50, 90, 1)
x_target_temp = np.arange(50, 90, 1)
x_control_temp = np.arange(50, 90, 1)

#2构造隶属函数
room_temp_lo    = fuzz.trimf(x_room_temp, [50, 50, 70])
room_temp_md    = fuzz.trimf(x_room_temp, [50, 70, 90])
room_temp_hi    = fuzz.trimf(x_room_temp, [70, 70, 90])
target_temp_lo  = fuzz.trimf(x_room_temp, [50, 50, 70])
target_temp_md  = fuzz.trimf(x_room_temp, [50, 70, 90])
target_temp_hi  = fuzz.trimf(x_room_temp, [70, 90, 90])
control_temp_lo = fuzz.trimf(x_room_temp, [50, 50, 70])
control_temp_md = fuzz.trimf(x_room_temp, [50, 70, 90])
control_temp_hi = fuzz.trimf(x_room_temp, [70, 90, 90])

#3建立规则集
#规则1如果房间温度是cold，目标温度是confortable,命令是heat
active_rule1 = np.fmin(room_temp_lo, target_temp_md)
control_activation_1 = np.fmin(active_rule1, control_temp_hi)
#规则2如果房间温度是cold, 目标温度是hot, 命令是heat
active_rule2 = np.fmin(room_temp_lo, target_temp_hi)
control_activation_2 = np.fmin(active_rule2, control_temp_hi)
#规则3如果房间温度是confortable, 目标温度是cold, 命令是cool
active_rule3 = np.fmin(room_temp_md, target_temp_lo)
control_activation_3 = np.fmin(active_rule3, control_temp_lo)
#规则4如果房间温度是confortable, 目标温度是hot, 命令是heat
active_rule4 = np.fmin(room_temp_md, target_temp_hi)
control_activation_4 = np.fmin(active_rule4, control_temp_hi)
#规则5如果房间温度是hot, 目标温度是cold, 命令是cool
active_rule5 = np.fmin(room_temp_hi, target_temp_lo)
control_activation_5 = np.fmin(active_rule5, control_temp_lo)
#规则3如果房间温度是hot, 目标温度是confortable, 命令是cool
active_rule6 = np.fmin(room_temp_hi, target_temp_md)
control_activation_6 = np.fmin(active_rule6, control_temp_lo)

#接受用户输入
room_temp = input('输入房间温度从50到90华氏度')
target_temp = input('输入目标温度50到90华氏度')

#4计算隶属度（模糊化）
room_temp_level_lo = fuzz.interp_membership(x_room_temp, room_temp_lo, float(room_temp))
room_temp_level_md = fuzz.interp_membership(x_room_temp, room_temp_md, float(room_temp))
room_temp_level_hi = fuzz.interp_membership(x_room_temp, room_temp_hi, float(room_temp))

target_temp_level_lo = fuzz.interp_membership(x_target_temp, target_temp_lo, float(target_temp))
target_temp_level_md = fuzz.interp_membership(x_target_temp, target_temp_md, float(target_temp))
target_temp_level_hi = fuzz.interp_membership(x_target_temp, target_temp_hi, float(target_temp))

#5聚焦6个规则的输出函数(选出隶属度最高的control
c1 = np.fmax(control_activation_1, control_activation_2)
c2 = np.fmax(control_activation_3, control_activation_4)
c3 = np.fmax(control_activation_5, control_activation_6)
c4 = np.fmax(c2, c3)
aggregated = np.fmax(c1, c4)

#6计算去模糊化结果，用方法centroid
control_value = fuzz.defuzz(x_control_temp, aggregated, 'centroid')

#输出结果
print(control_value)
























