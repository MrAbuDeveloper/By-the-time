# str_1 = 'config ichidagi str_1'
# str_2 = 'config ichidagi str_2'

def create_txt(name, text):
    with open(f"{name}.txt", mode='w', encoding='utf-8') as file:
        file.write(text)






