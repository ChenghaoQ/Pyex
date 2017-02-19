import pylab as plt

proj_A = [-1500,450,450,450,450,450,450]
proj_B = [-1200,0,0,0,0,0,3000]

cost_of_capital_rate =[i/100 for i in range(0,21)]
proj_A_npv = [plt.npv(i,proj_A) for i in cost_of_capital_rate]
proj_B_npv = [plt.npv(i,proj_B) for i in cost_of_capital_rate]
'''
proj_A_npv = []
proj_B_npv = []



for i in cost_of_capital:
	proj_A_npv.append(plt.npv(i,proj_A))
	proj_B_npv.append(plt.npv(i,proj_B)) '''


plt.figure('A / B NPV Profile')

plt.clf()

plt.plot(cost_of_capital_rate,proj_A_npv,'#92e3d7',label = 'Project A',linewidth = 2.0)
plt.plot(cost_of_capital_rate,proj_B_npv,'#f4ab84',label = 'Project B',linewidth = 2.0)




plt.ylim(0,2000)
plt.yticks(plt.arange(0, 2000+1, 400))
plt.xticks(plt.arange(0,0.24+0.01,0.02))

#plt.legend()
plt.legend(loc = 'upper right')

plt.title('Project A/B NPV Analysis')

a= plt.array(proj_A)
#array([-1500,   450,   450,   450,   450,   450,   450])


b= plt.array(proj_B)
#array([-1200,     0,     0,     0,     0,     0,  3000])
intersection = a-b
#array([ -300,   450,   450,   450,   450,   450, -2550])
intersection_irr = plt.irr(intersection)
#0.11005666742719433
intersection_npv =plt.npv(intersection_irr,a)

plt.annotate("intersection = %.4f"%intersection_irr,xy=(intersection_irr,intersection_npv),xytext=(intersection_irr+0.02,intersection_npv+100),arrowprops=dict(facecolor='black', shrink=0.05))





plt.show()




