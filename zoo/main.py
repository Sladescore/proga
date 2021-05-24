class Animal():

    zoo = []

    def __init__(self, name, food):
        self.name = name
        self.food = food
        Animal.zoo.append(self)

    @staticmethod
    def create_animal(name, food):
        anim = Animal(name, food)

    @staticmethod
    def delete_animal():
        name = (input('Введите имя животного: ')).title()
        for i in Animal.zoo:
            if i.name == name:
                Animal.zoo.pop(Animal.zoo.index(i))
                print(f'Животное "{name}" удалено')
                break
        else:
                print(f'Животное "{name}" не найдено')
        print()

    @staticmethod
    def show_zoo():
        for animal in Animal.zoo:
            keys = list(animal.food.keys())
            values = list(animal.food.values())
            print(animal.name, end = " ")
            for i in range(len(keys)):
                print(keys[i], values[i], end = " ")
            print()    

    @staticmethod
    def all_food():
        result = {}
        all_food = []
        all_values = []

        for animal in Animal.zoo:
            food_keys = list(animal.food.keys())
            food_values = list(animal.food.values())

            for item in food_keys:
                if item not in all_food:
                    all_food.append(item)
                    all_values.append(0)

            for i in all_food:  
                if i in food_keys:
                    all_values[all_food.index(i)] += food_values[food_keys.index(i)]
        
        for item in all_food: 
            result[item] = all_values[all_food.index(item)]
        
        test = list(result.items()) 
        test.sort(key=lambda i: i[1])

        result = dict(test)
        
        return result
    
    @staticmethod
    def food_search():
        food = (input('Введите название еды: ')).title()
        result = []
        for i in Animal.zoo:
            if food in list(i.food.keys()):
                result.append(i.name)
                
        if result == []:
            print("Животные не найдены")
        else:
            for i in result:
                print(f'Еду "{food}" ест животное {i}')

Animal.create_animal('Обезьяна', {'Яблоки': 10, 'Бананы': 5})
Animal.create_animal('Слон', {'Трава': 200,'Яблоки': 40,'Бананы': 50})
Animal.create_animal('Акула', {'Мясо': 100})
Animal.create_animal('Тигр', {'Мясо': 40})

print('Добро пожаловать в систему учета животных зоопарка!')

def Begin():
    x = input(' (1) Добавить животное  \n (2) Удалить животное  \n (3) Список животных \n (4) Потребление всех продуктов\n '
    '(5) Поиск животных по еде  \n (6) Завершить сеанс \n Введите номер команды: ')
    print()
    
    if x == "1": #Добавить животное
        name = (input('Введите имя животного: ')).title()
        animal_list = []

        for i in Animal.zoo:
            animal_list.append(i.name)
        if name in animal_list:
            print("Уже есть \n")
            Begin()
        else:
            quantity = int(input('Введите рацион животного: \nВведите количество продуктов: '))
            r = {}
            print('Введите рацион животного: ')
            for i in range(quantity):
                b = input('Название еды: ')
                c = float(input('Количество еды: '))
                r[b] = c
            Animal.create_animal(name, r)
        Begin()

    elif x == "2": #Удалить животное
        Animal.delete_animal()
        print()
        Begin()

    elif x == "3": #Список животных
        Animal.show_zoo()
        print()
        Begin()
    elif x == "4": #Потребление всех продуктов
        for i in range(len(Animal.all_food())):
            print(list(Animal.all_food().keys())[i], list(Animal.all_food().values())[i])
        print()
        Begin()

    elif x == "5": #Поиск животных по еде
        Animal.food_search()
        print()
        Begin()

    elif x == "6": #Завершить сеанс
        print('Всего доброго')
    
    else:
        print(f'Команда "{x}" отсутствует')
        Begin()    
Begin()