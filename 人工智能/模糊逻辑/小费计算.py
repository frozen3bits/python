import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

food_qual = input('Rate the food quality, 0 to 10: ')
service_qual = input('Rate the service quality, 0 to 10: ')

#食物质量和服务评分从0到10
#小费范围从0到25
x_qual = np.arange(0, 11, 1)
x_serv = np.arange(0, 11, 1)
x_tip = np.arange(0, 26, 1)

#生成模糊隶属函数
qual_lo = fuzz.trimf(x_qual, [0, 0, 5])
qual_md = fuzz.trimf(x_qual, [0, 5, 10])
qual_hi = fuzz.trimf(x_qual, [5, 10, 10])
serv_lo = fuzz.trimf(x_serv, [0, 0, 5])
serv_md = fuzz.trimf(x_serv, [0, 5, 10])
serv_hi = fuzz.trimf(x_serv, [5, 10, 10])
tip_lo = fuzz.trimf(x_tip, [0, 0, 13])
tip_md = fuzz.trimf(x_tip, [0, 13, 25])
tip_hi = fuzz.trimf(x_tip, [13, 25, 25])

qual_level_lo = fuzz.interp_membership(x_qual, qual_lo, float(food_qual))
qual_level_md = fuzz.interp_membership(x_qual, qual_md, float(food_qual))
qual_level_hi = fuzz.interp_membership(x_qual, qual_hi, float(food_qual))
serv_level_lo = fuzz.interp_membership(x_serv, serv_lo, float(service_qual))
serv_level_md = fuzz.interp_membership(x_serv, serv_md, float(service_qual))
serv_level_hi = fuzz.interp_membership(x_serv, serv_hi, float(service_qual))

#可视化隶属函数
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(x_qual, qual_lo, 'b', linewidth=1.5, label='Bad')
ax0.plot(x_qual, qual_md, 'g', linewidth=1.5, label='Decent')
ax0.plot(x_qual, qual_hi, 'r', linewidth=1.5, label='Great')
ax0.set_title('Food quality')
ax0.legend()

ax1.plot(x_serv, serv_lo, 'b', linewidth=1.5, label='Poor')
ax1.plot(x_serv, serv_md, 'g', linewidth=1.5, label='Acceptable')
ax1.plot(x_serv, serv_hi, 'r', linewidth=1.5, label='Amazing')
ax1.set_title('serve quality')
ax1.legend()

ax2.plot(x_tip, tip_lo, 'b', linewidth=1.5, label='Low')
ax2.plot(x_tip, tip_md, 'g', linewidth=1.5, label='Medium')
ax2.plot(x_tip, tip_hi, 'r', linewidth=1.5, label='High')
ax2.set_title('tip')
ax2.legend()


#应用规则1:服务差或食物质量差->小费低
active_rule1 = np.fmax(qual_level_lo, serv_level_lo)
tip_activation_lo = np.fmin(active_rule1, tip_lo)

#应用规则2：如果服务可以接受，那么小费将是中等
tip_activation_md = np.fmin(serv_level_md, tip_md)

#应用规则3：如果食物质量很好或服务令人满意->小费高
active_rule3 = np.fmax(qual_level_hi, serv_level_hi)
tip_activation_hi = np.fmin(active_rule3, tip_hi)
tip0 = np.zeros_like(x_tip)

#可视化应用规则
fig, ax0 = plt.subplots(figsize=(8,3))
ax0.fill_between(x_tip, tip0, tip_activation_lo, facecolor='b',alpha=0.7)
ax0.plot(x_tip, tip_lo, 'b', linewidth=0.5, linestyle='--',)
ax0.fill_between(x_tip, tip0, tip_activation_md, facecolor='b',alpha=0.7)
ax0.plot(x_tip, tip_md, 'g', linewidth=0.5, linestyle='--',)
ax0.fill_between(x_tip, tip0, tip_activation_hi, facecolor='b',alpha=0.7)
ax0.plot(x_tip, tip_hi, 'r', linewidth=0.5, linestyle='--',)
ax0.set_title('output membership activity')

#turn off right/top axes
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()

#聚集3个输出函数
aggregated = np.fmax(tip_activation_lo, np.fmax(tip_activation_md, tip_activation_hi))

#计算模糊结果
tip = fuzz.defuzz(x_tip, aggregated, 'centroid')
print(tip)
tip_activation = fuzz.interp_membership(x_tip, aggtegated, tip)

#可视化结果
fig, ax0 = plt.subplots(figsize(8,3))

ax0.plot(x_tip, tip_lo, 'b', linewidth=0.5, linestyle='--',)
ax0.plot(x_tip, tip_md, 'g', linewidth=0.5, linestyle='--',)
ax0.plot(x_tip, tip_hi, 'r', linewidth=0.5, linestyle='--',)
ax0.fill_between(x_tip, tip0, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([tip, tip], [0, tip_activation], 'k', linewidth=1.5, alpha=0.9)
ax0,set_title('Aggregated membership and result (line)')

#turn off right/top axes
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_buttom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()

      




























