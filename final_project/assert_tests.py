from json_dict_processing import extract_nested_value, process_dictionary_with_config


# тест: извлечение вложенного значения
test_dict = {'a': {'b': {'c': 42}}}
assert extract_nested_value(test_dict, ['a', 'b', 'c']) == 42
print("тест 1 пройден успешно")


# тест: несуществующий путь возвращает None
assert extract_nested_value(test_dict, ['a', 'x', 'y']) is None
print("тест 2 пройден успешно")


# тест: обработка с функцией
config = {'year': (['date'], lambda x: int(x[:4]))}
test_date_dict = {'date': '1999-12-31'}
result = process_dictionary_with_config(test_date_dict, config)
assert result == {'year': 1999}
print("тест 3 пройден успешно")


# тест: проверка конфига config_person на реальном лауреате
test_laureate = {
    'id': '745',
    'knownName': {'en': 'A. Michael Spence'},
    'gender': 'male',
    'birth': {
        'date': '1943-05-14',
        'place': {
            'country': {'en': 'USA'},
            'countryNow': {'en': 'USA'}
        }
    },
    'nobelPrizes': []
}

from laureates_configs import person_processor
processor = person_processor()
result = processor(test_laureate)

assert result['id'] == 745
assert result['name'] == 'A. Michael Spence'
assert result['birth_year'] == 1943
assert result['country_birth'] == 'USA'
print("тест 4 пройден успешно")