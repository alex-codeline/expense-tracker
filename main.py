expenses=[]
while True:
    try:
        menu=int(input("Выберите фукнцию из меню:\n 1 - добавить расход\n 2 - показать все расходы\n 3 - показать итог\n 4 - итог по одной категории\n 5 - список категорий\n 0 - выход\n"))
        if menu not in (1,2,3,4,5,0):
            print("Введите число,соответствущее предложенным функциям!")
    except ValueError:
        print("Нужно вводить числа,а не буквы или пустоту!")
        continue
    if menu==1:
        while True:
            expend={}
            expend["category"]=input("Введите категорию расходов: ").strip().lower()
            if expend["category"].strip() =="":
                print("Введите название категории!")
                continue
            while True:
                try:
                    amount=float(input("Введите потраченную сумму: "))
                    if amount<=0:
                        print("Введите хотя бы какую то сумму.")
                        continue
                except ValueError:
                    print("Сумму нужно ввести цифрами!")
                    continue
                break
            expend["amount"]=amount
            expend["description"]=input("Опишите свои расходы(по желанию): ")
            expenses.append(expend)
            break
    elif menu==2:
        if expenses==[]:
            print("Пока нет никаких расходов!")
        else:
            number=1
            for expend in expenses:
                
                if expend['description']=="":
                    print(f"{number}. {expend['amount']} ₽ - {expend['category']}")
                else:
                    print(f"{number}. {expend['amount']} ₽ - {expend['category']} ({expend['description']})")
                number+=1
    elif menu==3:
        if expenses==[]:
            print("Пока нет расходов.")
        else:
            total=0
            for expend in expenses:
                total+=expend['amount']
            print(f"Сумма всех расходов - {total}! Общее количество расходов - {len(expenses)}")
    elif menu==4:
        if expenses==[]:
            print("Еще нет ни одной категории.")
        else:
            category=input("Введите название улицы: ").strip().lower()
            counter=0
            total=0
            for expend in expenses:
                if expend['category']==category:
                    counter+=1
                    total+=expend['amount']
            if counter==0:
                print("Категория не найдена.") 
            else:
                print(f"Сумма расходов по данной категории - {total}")
    elif menu==5:
        categories=set()
        if expenses==[]:
            print("Расходов пока нет.")
        else:
            for expend in expenses:
                categories.add(expend["category"])
            print(f"Разных категорий - {len(categories)}")
            for category in categories:
                print("-", category)
    elif menu==0:
        print("Буду ждать Вас,до новых встреч!")
        break