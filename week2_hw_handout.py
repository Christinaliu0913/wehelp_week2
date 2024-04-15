#Task1


#建立捷運清單
MRT_list=['Songshan','Nanjing Sanmin','Taipei Arena','Nanging Fuxing','Songjiang Nanjing','Zhongshan','Beimen','Ximen','Xiaonanmen','Chiang Kai-Shek Memorial Hall','Guting','Taipower Building','Gongguan','Wanlong','Jingmei','Dapinglin','Qizhang','Xiaobitan','Xindian City Hall','Xindian']

messages={
    "Leslie":"I'm at home near Xiaobitan station.",
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Vivian":"I'm at Xindian station waiting for you."
    }

#建立一個搜尋關鍵字後的地名字典
loca_station=dict()
for key, value in messages.items():
    for station in MRT_list:
        if station in value:
            loca_station[key]=station
        else:
            continue
# print(loca_station)

new_dict={value:key for key,value in loca_station.items()}
# print(new_dict)

#分為有沒有人從小碧潭出發、出發地為小碧潭、現在地為小碧潭
#五個朋友現在正在的車站與輸入車站的距離 = j(有可能有正負之分)
def find_and_print(messages, current_station):
    min_distance=20
    find_friend =[ ]

    for i in loca_station.values():
        j= MRT_list.index(i) - MRT_list.index(current_station)
        
        if current_station=='Xindian City Hall' or 'Xindian':
            #如果現在正位置超過七張的話且朋友沒有在小碧潭
            if i != 'Xiaobitan':
                if abs(j)< min_distance:
                    min_distance = abs(j)-1
                    # print(min_distance)
                    find_friend.append(i)
                else: 
                    continue
            #如果現在位置超過七張且朋友在小碧潭
            if i == 'Xiaobitan':
                if abs(j)< min_distance:
                    min_distance = abs(j)+1
                    # print(min_distance)
                    find_friend.append(i)
                else: 
                    continue
        else:
            #目的地與現在地都沒有包含小碧潭
            if abs(j)< min_distance:
                min_distance = abs(j)
                # print(min_distance)
                find_friend.append(i)
            else: 
                continue
        
    print(new_dict[find_friend[-1]])



find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian


#Task2

consultants=[
    {"name":"John", "rate":4.5, "price":1000}, 
    {"name":"Bob", "rate":3, "price":1200}, 
    {"name":"Jenny", "rate":3.8, "price":800}
]

#建立每個consultants的時間表
res_time=dict()
for i in range(0,len(consultants)):
    time=[]
    for j in range(0,24):
        time.append(j)
    res_time[consultants[i]['name']]=time
# print(res_time)

def book(consultants, hour, duration, criteria):
    #判斷此客人要以價錢還是評價為預約優先標準
    if criteria == 'price':
        list_order = sorted(consultants, key=lambda x: x['price'])
        # print(list_order)
    else:
        list_order = sorted(consultants,key=lambda x: x['rate'],reverse=True)
    
    for i in range(0, len(list_order)):
        # print(i)
        cons_name = list_order[i]['name']
        reserved = True
        #判斷是否有時間
        for j in range(0,duration):
            if res_time[cons_name][hour+j] == -1:
                reserved = False

        if reserved:
            print(cons_name)
            for j in range(0,duration):
                res_time[cons_name][hour+j] = -1
            return
    print('No service')

#task3
def func(*data):
    name_list=[]
    for x in (data):
        if len(x) == 3:
            name_list.append(x[1]) 
        elif len(x) == 2:
            name_list.append(x[1]) 
        else:
            name_list.append(x[2]) 
    # print(name_list)
    
    loca=0
    for i in (name_list):
        # print(name_list.count(i))
        if name_list.count(i)==2:
            loca+=1
        else:
            break
    if loca >= len(name_list):
        print('沒有')
    else:
        print(data[int(loca)])
    

    
func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有 
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安


#Task4

def get_number(index):
    sum=0
    for x in range(50):
        if x==index+1:
            break
        elif x==0:
            sum+=0
        elif x%3==1:
            sum+=4
        elif x%3==2:
            sum+=4
        else:
            sum-=1
    return print(sum)

get_number(1) # print 4
get_number(5) # print 15 
get_number(10) # print 25 
get_number(30) # print 70







# Example usage
book(consultants, 15, 1, "price") # Jenny 
book(consultants, 11, 2, "price") # Jenny 
book(consultants, 10, 2, "price") # John 
book(consultants, 20, 2, "rate") # John 
book(consultants, 11, 1, "rate") # Bob 
book(consultants, 11, 2, "rate") # No Service 
book(consultants, 14, 3, "price") # John