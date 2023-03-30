import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
   
our_AP = [30,30,30,29,29,28,28,27,27,26,26,25,25,23.5,23.5,22,22,22,21.5,21,21]
Gou_AP = [28,27,26,26,26,26,24,22,22,22,20,18,15,13,12,12,10,6,6,5,5]
Fang_AP = [27,27,26,25,25,25,23,20,20,20,18,15,15,11,11,10,10,5,5,5,4]
GPD_AP = [24,24,23,22,20,20,20,17,17,15,13,13.5,9,8.5,8,7,6,4.5,4,3,2]

occlusion = [50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90]

plt.rcParams.update({'font.size': 30})
plt.xlim(48, 92)
plt.plot(occlusion, our_AP, linewidth=3)
plt.plot(occlusion, Gou_AP, linewidth=3)
plt.plot(occlusion, Fang_AP, linewidth=3)
plt.plot(occlusion, GPD_AP, linewidth=3)
#plt.xlabel('invisible surface percentage threshold (<%)')
plt.xlabel('percentage of object surface occluded (<%)')
plt.ylabel('Average Precision (%)')
plt.legend(['Ours', "[42]", "[39]", "GPD"], loc="lower left",fontsize = 30)
plt.show()
