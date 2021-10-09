with open("input.txt", "r+") as file:
    file.seek(0)
    text = file.readlines()
    # text.pop(0)

goodies_list=[]
price_list=[]
m=int(input('Number of employees: '))
for i in text:
    temp=str(i).split(":")
    goodies_list.append({"goodie":temp[0],"price":str(temp[1]).strip().split('\n')[0]})
    price_list.append(int(str(temp[1]).strip().split('\n')[0]))
    # print(temp)


for i in range(len(price_list)):
    for j in range(i+1,len(price_list)):
        if price_list[j]<price_list[i]:
            temp=price_list[j]
            price_list[j]=price_list[i]
            price_list[i]=temp

# print("sort_list")
# print(price_list)

min_list=[]
for i in range(0,len(price_list)):
    if m+i<len(price_list):
        min=price_list[i]
        max=price_list[m+i-1]
        diff=max-min
        # print(min,max,diff)
        min_list.append([min,max,diff])
# print(min_list)

smallest_difference=min_list[0][2]
for i in range(0,len(min_list)):
    if smallest_difference>min_list[i][2]:
        smallest_difference=min_list[i][2]
# print(smallest_difference)


for i in min_list:
    if i[2]==smallest_difference:
        definite_value=i

# print(definite_value)

sorted_goodies=[]
for j in price_list:
    for i in goodies_list:
        if int(i['price'])==int(j):
            sorted_goodies.append(i)


# print(sorted_goodies)

final_dict=[]
count=0
for i in range(0,len(sorted_goodies)):
    if int(sorted_goodies[i]['price'])==definite_value[0]:
        count=1
    if count==1:
        final_dict.append(sorted_goodies[i])
    if int(sorted_goodies[i]['price'])==definite_value[1]:
        count=0

f = open("output.txt", "a")
f.write("Number of Employees:  "+str(m)+"\n")
f.write("Here the goodies that are selected for distribution are:\n")
for i in final_dict:
    f.write(i['goodie']+": "+i["price"]+"\n")
# f.write("Now the file has more content!")
f.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(smallest_difference)+"\n")
f.write("\n")
f.close()

print("\nFile Generated as otput.txt\n")
f = open("output.txt", "r")
print(f.read())

print("\nDifference=",smallest_difference)