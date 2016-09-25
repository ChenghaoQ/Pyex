def main():
	print(''' ******欢迎进入通讯录程序******
	1: 查询联系人资料
	2: 添加新的联系人
	3: 删除已有联系人
	4: 退出程序
	''')

	contacts={}
	while True:
		option= int(input("Please choose an option: "))
		if option==1:
			name= input("please enter the name: ")
			if name in contacts:
				print(name+' : ' + contacts[name])
			else:
				print("Cannot find in contacts")

		elif option ==2:
			name=input('请输入联系人姓名： ')
			if name in contacts:
				print('已经有这个人了哦～ -->>',end='')
				print(name+' : ' + contacts[name])
				if input('是否修改用户资料（YES／NO）：')== 'YES':
					contacts[name]=input('请输入用户联系电话:')
			else:
				contacts[name]=input('请输入用户联系电话:')

		elif option ==3:
			name=input('请输入联系人姓名： ')
			if name in contacts:
				del(contacts[name])    #Also can use dict.pop()
			else:
				print("您输入的用户不存在")

		elif option ==4:
			print("＊＊＊＊＊感谢使用通讯录程序＊＊＊＊＊")
			break
	

