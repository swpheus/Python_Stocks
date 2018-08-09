kospi_top10 = ['삼성전자', 'SK하이닉스', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER', '현대모비스']

print("시가총액 5위:",kospi_top10[4])

kospi_top5=kospi_top10[0:5]
kospi_top5to10=kospi_top10[5:10]
# [5:] [:5]
print(kospi_top5)
print(kospi_top5to10)
# 리스트에 데이터 삽입하기
kospi_top10.append('SK텔레콤')
print(kospi_top10)
kospi_top11 =kospi_top10

kospi_top11.insert(3,'SK 텔레콤')
print(kospi_top11)
print(kospi_top10)
print(kospi_top5to10)

kospi_top10.insert(6,'기아자동차')
print(kospi_top5to10)

print(len(kospi_top10))

del kospi_top11[-1]
del kospi_top10[-2]
print(len(kospi_top11))