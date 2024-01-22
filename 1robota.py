from datetime import datetime

def age_dni(age):
    # напишіть свою дату народження "рік-місяць-день"
    rozhsdenie1 = "2000-01-01"
    
    # об'єкт дати з рядка
    rozhsdenie = datetime.strptime(rozhsdenie1, "%Y-%m-%d")
    
    # отримай поточну дату
    potochna_date = datetime.now()
    
    # обчислення років между датами
    age_in_days = age * 365
    
    # повернення результата
    return age_in_days

# введіть свій вік
user_age = int(input("Введіть вік: "))

# отримайте кількість днів які прожили
days_lived = age_dni(user_age)

# ваш результат
print(f"Ви прожили близько {days_lived} днів.")
