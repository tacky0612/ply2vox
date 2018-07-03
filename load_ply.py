
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def  load_ply(filename):
    with open(filename, "r",encoding='utf-8') as f: 
        data = f.readlines()
        
    #３D座標のはじまりの位置を取得
    for i in range(len(data)):
        #ヘッダーの終わり判定
        if "end_header" in data[i]:
            start = i
        #３Dの終わり判定（雑）
        if data[i][0]== "3"and data[i][1]== " " :
            end = i
            break

    start += 1


    #３D座標を配列に
    ply = []
    for i in range(end-start):
        i =  i + start
        a = data[i].split(" ")
        x = [a[0],a[1],a[2]]
        ply.append(x)
    ply = np.array(ply).astype(np.float32)

    return ply

