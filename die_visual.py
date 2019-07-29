from die import Die

# Моделирование броска одного кубика сохранением результатов в списке.
def die6_1():
    # Создание кубика D6.
    die = Die()
    # Моделирование серии бросков с сохранением результатов в списке.
    results = []

    for roll_num in range(10):
        result = die.roll()
        results.append(result)
    print("Бросок кубика D6 = " + str(results))

    # Анализ результатов.
    frequencies = []
    for value in range(1, die.num_sides+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    #print(frequencies)


# Моделирование броска двух кубиков сохранением результатов в списке.
def die6_2():
    # Создание двух кубиков D6.
    die_1 = Die()
    die_2 = Die()
    # Моделирование серии бросков с сохранением результатов в списке.
    results = []

    for roll_num in range(10):
        result = die_1.roll() + die_2.roll()
        results.append(result)
    print("Бросок двух кубиков D6 = " + str(results))

    # Анализ результатов.
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    #print(frequencies)

def die10_1():
    # Создание кубика D10.
    die = Die(10)
    # Моделирование серии бросков с сохранением результатов в списке.
    results = []

    for roll_num in range(10):
        result = die.roll()
        results.append(result)
    print("Бросок кубика D10 = " + str(results))

    # Анализ результатов.
    frequencies = []
    for value in range(1, die.num_sides+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    #print(frequencies)

die6_1()
die6_2()
die10_1()