import csv

def read_statistics():
    unique_users = set()
    
    # Открываем CSV файл для чтения
    with open('/root/volleyball-bot/user_statistics.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            user_id = row[0]  # user_id из каждой строки
            unique_users.add(user_id)
    
    print(f"Всего уникальных пользователей: {len(unique_users)}")
    return len(unique_users)

# Пример использования
if __name__ == '__main__':
    total_users = read_statistics()
    print(f"Общее количество пользователей, которые нажали /start: {total_users}")
