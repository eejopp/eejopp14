# Цель работы: реализовать базовый анализ датасета

import pandas as pd

# Чтение файла CSV
data = pd.read_csv('../prak6/titanic.csv')

# Вывести все уникальные значения
unique_values = data['Survived'].unique()
#print("Уникальные значения:", unique_values)
unique_values=pd.DataFrame(unique_values, columns=['Survived'])
unique_values.to_csv('unique_values.csv', index=False)
# Отсортировать по определенным параметрам
sorted_data = data.sort_values(by='Name')
#print("Отсортированные данные:\n", sorted_data)
sorted_data.to_csv('sorted_data.csv',index=False)
# Удалить ненужные столбцы или строки
cleaned_data = data.drop(['Survived', 'Name'], axis=1)  # удаление столбцов
#cleaned_data = data.drop([0, 1, 2], axis=0)  # удаление строк
#print("Очищенные данные:", cleaned_data)
cleaned_data.to_csv('cleaned_data.csv',index=False)
# Заменить определенные значения в датасете
#data['Siblings/Spouses Aboard'].fillna(value='замена', inplace=True)  # замена пустых значений
data['Siblings/Spouses Aboard'].replace(to_replace=[0], value='1000', inplace=True)  # замена пустых значений
#print("Данные с заменой значений:", data)
data.to_csv('Siblings_replace.csv',index=False)

# Удалить дубликаты
deduplicated_data = data.drop_duplicates()
#print("Данные без дубликатов:", deduplicated_data)
deduplicated_data.to_csv('deduplicated_data.csv',index=False)

# Провести анализ с помощью функций info
#print("data.info()")
#data.info()

# Провести анализ с помощью функций describe
#print("data.describe()")
#print(data.describe())

# Провести выборку данных по строкам и столбцам с помощью loc
selected_data = data.loc[data['Survived'] == 1, ['Survived', 'Name']]
#print("Выборка данных:", selected_data)
selected_data.to_csv("selected_data.csv",index=False)
exit(0)

# Сохранить новый датасет
data.to_csv('new_file.csv', index=False)
print("Новый датасет сохранен.")