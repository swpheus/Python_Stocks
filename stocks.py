price = 7000

if price < 1000:
    bid = 1
elif price >= 1000 and price < 5000:
    bid = 5
elif price >= 5000 and price < 10000:
    bid = 10

print(price)

range(1, 10)
print(list(range(1, 10)))

for i in range(0, 11):
    print(i)

interest_stocks = ["Naver", "Samsung", "SK Hynix"]

for company in interest_stocks:
    print("%s : Buy 10" % company)

interest_stocks2 = {"Naver": 10, "Samsung": 5, "SK Hynix": 30}

for company, stocks_num in interest_stocks2.items():
    print("%s buy %s" % (company, stocks_num))

i = 0;
while i <= 10:
    print(i)
    i = i + 1
print(i)  # while 문이 끝나고 어떻게 변하는지 보기
wikibooks = 10000
day = 1
while day < 6:
    wikibooks = wikibooks + wikibooks * 0.3
    day = day + 1

print(wikibooks)
num = 0
num2 =0
while 1:
    print(num)
    if num == 10:
        break
    num += 1

while num<10:
    num2 +=1
    if num2 == 5:
        continue
    print(num2)
