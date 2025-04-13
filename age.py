drive = input('請問你有沒有開過車? (請回答"有"或"沒有")')
if drive != '有' and drive != '沒有':
	print('只能輸入"有"或"沒有"')
	raise SystemExit

age = input('請輸入你的年齡:')
age = int(age)
if drive == '有':
	if age >= 18:
		print('你通過測驗了')
	else : 
		print('你怎麽開過車?')
elif drive == '沒有':
	if age >= 18:
		print('你可以去考駕照呀!')
	else :
		print('等到滿18嵗，就可以考駕照了!')