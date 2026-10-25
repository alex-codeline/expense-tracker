expenses=[]
def expend_add():
    """Добавление расхода"""
    expend={}
    expend["category"]=ask_category()
    expend["amount"]=ask_amount()
    expend["description"]=input("Опишите свои расходы(по желанию): ")
    expenses.append(expend)
def show_expenses():
    """Показать все расходы по списку"""
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
def result_expenses():
    """Итог по всем расходам"""
    if expenses==[]:
        print("Пока нет расходов.")
    else:
        total=calc_total(expenses)
        print(f"Сумма всех расходов - {total}! Общее количество расходов - {len(expenses)}")
def result_onecategory():
    """Итог по одной категории"""
    if expenses==[]:
        print("Еще нет ни одной категории.")
    else:
        category=ask_category()
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
def list_category():
    """Список категорий столбцом"""
    categories=set()
    if expenses==[]:
        print("Расходов пока нет.")
    else:
        for expend in expenses:
            categories.add(expend["category"])
        print(f"Разных категорий - {len(categories)}")
        for category in categories:
            print("-", category)
def ask_category():
    """Спрашивает категорию, пока не введут непустую, и возвращает её."""
    while True:
        category = input("Введите название категории: ").strip().lower()
        if category == "":
            print("Введите название категории!")
            continue
        return category
def ask_amount():
    """Спрашивает сумму,пока не введут какое то число,и возвращает ее"""
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
    return amount
def calc_total(expenses):
    total=0
    for expend in expenses:
        total+=expend['amount']
    return total


while True:
    try:
        menu=int(input("Выберите функцию из меню:\n 1 - добавить расход\n 2 - показать все расходы\n 3 - показать итог\n 4 - итог по одной категории\n 5 - список категорий\n 0 - выход\n"))
        if menu not in (1,2,3,4,5,0):
            print("Введите число,соответствущее предложенным функциям!")
    except ValueError:
        print("Нужно вводить числа,а не буквы или пустоту!")
        continue
    if menu==1:
        expend_add()
    elif menu==2:
        show_expenses()
    elif menu==3:
        result_expenses()
    elif menu==4:
        result_onecategory()
    elif menu==5:
        list_category()
    elif menu==0:
        print("Буду ждать Вас,до новых встреч!")
        break