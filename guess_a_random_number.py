# 產生一個隨機數字１～１００（不要印出來）
# 讓使用者去重複輸入數字去猜
# 猜對，印出“終於猜對了！”
# 猜錯，要告訴使用者比答案大或小

import random
start = int(input('請輸入隨機數字範圍起始值： '))
end = int(input('請輸入隨機數字範圍終止值： '))

ans = random.randint(start,end)
i = 0
while True:
	r = int(input('請輸入一個數字：'))
	i += 1 # i = i + 1
	if ans == r:
		print('猜了', i, '次，終於猜對了！！')
		break
	elif ans > r:
		print('猜大一點的數字！')
	elif ans < r:
		print('猜小一點的數字！')