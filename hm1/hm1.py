# === ВАРИАНТ ===
# ДЗ1 · вариант для: DISatrat
# Календарь вашей планеты. Годы считаются с нулевого.
#
# Високосность: год високосный, если делится на LEAP_A, кроме тех,
# что делятся на LEAP_B, но делящиеся на LEAP_C — снова високосные.
LEAP_A = 7
LEAP_B = 49
LEAP_C = 245

# Месяцы по порядку: (название, дней в обычный год, дней в високосный год).
# Пользователь вводит номер месяца, первый месяц — номер 1.
MONTHS = [
    ("Житей", 31, 31),
    ("Бигир", 25, 25),
    ("Кабиль", 25, 26),
    ("Долуна", 21, 22),
    (" Данодарь", 29, 31),
    ("Тидинь", 30, 30),
    ("Зажур", 24, 24),
    ("СТАРОКУКУЗОДАРЬ", 20, 20),
    ("жокар", 30, 30),
    ("Жеружурь", 21, 21),
]

# Дни недели по порядку. Сколько названий — столько дней в неделе.
WEEKDAYS = [
    "Ларник", "Генунка", "Шикеца", "Шишола", "Кепурник", "Шасила", "Дасула",
]

# Каким днём недели было 1-е число первого месяца года 0:
# индекс в списке WEEKDAYS (считая с нуля).
FIRST_WEEKDAY = 0

# Проверьте себя:
#   год 3675 — високосный, в нём 260 дней;
#   год 3969 — не високосный, в нём 256 дней;
#   1-е число месяца №5 в 2017 году — Шишола.
# === КОНЕЦ ВАРИАНТА ===

year = max(int(input('Введите год: ')), 0)
m_row = input('Введите месяц (по желанию): ').strip()

month = 0

if m_row:
    month = int(m_row)

if month <= 0 or month > len(MONTHS):
    print("Такого месяца не существует", end="\n\n")

# Расчет весокосного года
is_leap = (year % LEAP_A == 0 and year % LEAP_B != 0) or (year % LEAP_C == 0)

if is_leap:
    print("Год високосный", end="\n\n")
else:
    print("Год не високосный", end="\n\n")

#Расчет дней в году 
days_year = 0

for name, n_day, l_day in MONTHS:
    if is_leap:
        days_year += l_day
    else:
        days_year+= n_day

print(f"Количество дней в {year} году - {days_year} дней ", end="\n\n")

if month==0:
    raise SystemExit

# Построение календаря
month_index = month - 1

# Сколько дней прошло от 0 года до year 
total_days = 0
for y in range(year):
    y_leap = (y % LEAP_A == 0 and y % LEAP_B != 0) or (y % LEAP_C == 0)
    for name, n_day, l_day in MONTHS:
        total_days += l_day if y_leap else n_day

# Дни предыдущих месяцев текущего года
for i in range(month_index):
    name, n_day, l_day = MONTHS[i]
    total_days += l_day if is_leap else n_day

first_wd = (FIRST_WEEKDAY + total_days) % len(WEEKDAYS)

name, n_day, l_day = MONTHS[month_index]
days_month = l_day if is_leap else n_day

# Сокращения
k = 1
while len({wd[:k] for wd in WEEKDAYS}) < len(WEEKDAYS):
    k += 1
short = [wd[:k] for wd in WEEKDAYS]

cell = max(len(s) for s in short) + 1

# Заголовок
print(" " * cell*2 + f"{name.strip()} {year}")

# Шапка: каждое сокращение по центру/справа в клетке шириной cell
print("".join(f"{s:^{cell}}" for s in short))

line = " " * (first_wd * cell)
for day in range(1, days_month + 1):
    line += f"{day:^{cell}}"
    if (first_wd + day) % len(WEEKDAYS) == 0:
        print(line)
        line = ""
if line.strip():
    print(line)
