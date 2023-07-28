system_msg = """Имеется текст, распознанный из чека.  В распознанном тексте могут быть опечатки и лишние символы, которые должны быть удалены. Нужно преобразовать это в следующий формат:
1) Название позиции в чеке -> сумма за позицию
2) ...
Кроме перечисления позиций чека и стоимости каждой позиции никакой дополнительной информации писать не нужно.

Вот несколько примеров:
На входе:
'''
Йдрес:ул.Байтурсынова а 159 кв

Тел 8(727) 2928738
Чек # Стол # 25 Гостей 3
10-03-2023 Открыт 19:40 — Закрыт

Кассир:
Официант: Йружан

Биюдо Кол-во Сумма

Роли Филадельфия вауна ы 16350.00
Ропл Канадский Н 5650.00)
Чай Семь самураев 11 72 5000.00
Споуа Ог19ла] ние у 17000.00
Всего; 44000.00
Обсиьживание 10% 44400.00

Итого к оплате: 48400.00

48400.00

Вознаграждение официанты приветствуется
но всегда остается на Ваше усмотрение.
'''

На выходе:
'''
Роли Филадельфия рауна -> 16350
Ропл Канадский -> 5650
Чай Семь самураев -> 5000
Choya Original White -> 17000
'''
На входе:
'''
Рег’ 8
РАеавап" Геа{Иег
Епо\АэА Руб
‚, Пр, Достык 116
7711 980-81-81
Стол # 109 Гостей 3
Открыт 18:55 Печать 29:40
ур: Влад Великан
Официант: Влад Великан

Блюдо Я
Сырные шарики 2.00 Бо. 00
Стейк миньон 1.00 5490.00
фуллер’с Хани Дью 12.00 23880.00
560мл

Стейк рибай б/к 1.00 — 5990.00
Утиная грудка 1.00 — 2990.00

41930.00
3774.00
45704.00

45704.00

тенге на чай,
'''
На выходе:
'''
Сырные шарики -> 3680
Стейк миньон -> 5490
фуллер’с Хани Дью -> 23880
Стейк рибай б/к -> 5990
Утиная грудка -> 2990
'''
На входе:
'''
Е5ргеззо Ваг Азкапа 1
Чек #184440 Стол 10 51
22.12.2020 Открыт 16:46 Печат
Кассир: — стажер
Официант: Анастасия

Сумма
Блюдо

Гляссе р
д 900.
Латте большой . 200.00
4 ‚Маршмеллоу т . 1800.00
Чай имбирно-мятный
длЯ двоих

3900.00


'''
На выходе:
'''
Гляссе -> 1000
Латте большой -> 900
Маршмеллоу -> 200
Чай имбирно-мятный длЯ двоих -> 1800
''''
"""