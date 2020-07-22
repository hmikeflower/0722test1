import sys 
l1 =sys.argv
l2 = []
b = 0
for i in range(1,len(l1)): #先將list 裡面的 str 轉成 int
    l2.append(int(l1[i]))  #小問題 遇到字串會掛調 所以從1 開始
l2.sort()    #對l2 進行排序 結果回傳到l2
for i in range(0,len(l2)):
    b += l2[i]
c=b/len(l2)



print("your input (in ascending order):",l2)
print("sum------",b)
print("mean------",c)
print("med-------") #還沒做
print("min-------",min(l2)) 
print("max-------",max(l2)) 


