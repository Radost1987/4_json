import json
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open (filepath) as input_datas:
        loaded_data=json.load(input_datas)
        return loaded_data

        
def pretty_print_json(data):
    if data is not None:
        formatted_data=json.dumps(data, ensure_ascii = False, sort_keys=True, indent=4)
        print('JSON файл в удобном формате:',formatted_data)
    else:
        print('Неправильно введен путь до файла или имя файла')

if __name__ == '__main__':
    filepath=input('Введите путь до файла ')
    pretty_print_json(load_data(filepath))     
     
