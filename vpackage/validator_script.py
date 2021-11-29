class Person(object):
    """
        Класс для одной записи с информацией с полями:
        Attributes
        --------
            telephone : string
                Поле для номера телефона
            weight : str
                Поле веса
            snils: string
                Снилс
            passport_series : str
                Серия паспорта
            occupation : str
                Поле профессии
            political_views : str
                 Политические предпочтения
            worldview : str
                Мировоззрение
            address : str
                Адресс
    """
    telephone: str
    weight: int
    snils: str
    passport_series: str
    occupation: str
    age: int
    political_views: str
    worldview: str
    address: str

    def __init__(
            self,
            telephone: str = '+7-(000)-000-00-00',
            weight: int = 0,
            snils: str = '00000000000',
            passport_series: str = '00 00',
            occupation: str = 'None',
            age: int = 0,
            political_views: str = 'None',
            worldview: str = 'None',
            address: str = 'None') -> None:
        self.telephone = telephone
        self.weight = weight
        self.snils = snils
        self.passport_series = passport_series
        self.occupation = occupation
        self.age = age
        self.political_views = political_views
        self.worldview = worldview
        self.address = address


class Validator(object):
    collection: list
    valid: int
    invalid: int
    ph_error: int
    wt_error: int
    sn_error: int
    ps_error: int
    oc_error: int
    ag_error: int
    pv_error: int
    wv_error: int
    ad_error: int
    """
        Класс-валидатор списка записей,
        который считывает записи из файла и
        проводит их валидацию
        Attributes
        --------
            collection: list
                Контейнер записей типа Person
            valid: int
                Кол-во валидных записей
            invalid: int
                Кол-во невалидных записей
            ph_error: int 
                Кол-во записей с невалидным номером телефона
            wt_error: int
                Кол-во записей с невалидным весом
            sn_error: int
                Кол-во записей с невалидным снилсом
            ps_error: int
                Кол-во записей с невалидной серией паспорта
            oc_error: int
                Кол-во записей с невалидной профессией
            ag_error: int
                Кол-во записей с невалидным возрастом
            pv_error: int
                Кол-во записей с невалидными политическими взглядами
            wv_error: int
                Кол-во записей с невалидным мировоззрением
            ad_error: int
                Кол-во записей с невалидным адресом
                
    """

    def __init__(self, collection: list = None) -> None:
        """
        Конструктор класса-валидатора
        Создает контейнер записей
        """
        if not collection:
            self.collection = []
        else:
            self.collection = collection

    def __len__(self) -> int:
        """
        Функция получения размера списка записей
        :return: int - размер списка записей
        """
        return len(self.collection)

    def load(self, path: str = None) -> None:
        """
        Загружает список записей из файла
        :param path: str - путь к файлу
        :return: None
        """
        import tqdm as tl
        import json

        self.collection = []
        data = json.load(open(path, encoding='windows-1251'))
        progressbar = tl.tqdm(range(len(data)))
        progressbar.set_description('Loading Person\'s data from file')
        for i in progressbar:
            temp = Person(
                data[i]['telephone'],
                data[i]['weight'],
                data[i]['snils'],
                data[i]['passport_series'],
                data[i]['occupation'],
                data[i]['age'],
                data[i]['political_views'],
                data[i]['worldview'],
                data[i]['address'])
            self.collection.append(temp)
        print('Done')

    def validate(self) -> list:
        import tqdm as tv
        import re

        self.ph_error = 0
        self.wt_error = 0
        self.sn_error = 0
        self.ps_error = 0
        self.oc_error = 0
        self.ag_error = 0
        self.pv_error = 0
        self.wv_error = 0
        self.ad_error = 0
        self.invalid = 0
        self.valid = len(self)
        valid_list = []

        progressbar = tv.tqdm(range(len(self)))
        for i in progressbar:
            ph_match = re.match(
                r'\+7-\(9\d{2}\)-\d{3}-\d{2}-\d{2}',
                self.collection[i].telephone)
            if not isinstance(self.collection[i].weight, str):
                correct_weight = (self.collection[i].weight > 0) and (self.collection[i].weight < 200)
            else:
                correct_weight = False
            sn_match = re.match(r'\d{11}', self.collection[i].snils)
            ps_match = re.match(
                r'\d{2} \d{2}',
                self.collection[i].passport_series)
            oc_match = re.match(
                r'([А-Яа-яA-Za-z]+$)',
                self.collection[i].occupation)
            if not isinstance(self.collection[i].age, str):
                correct_age = (self.collection[i].age > 16) and (self.collection[i].age < 100)
            else:
                correct_age = False
            pv_match = re.match(r'^[А-Яа-я]+$', self.collection[i].political_views)
            wv_match = re.match(r'^([А-Яа-я]+$)|(Секулярный гуманизм)', self.collection[i].worldview)
            ad_match = re.match(r'(^ул\. [А-Яа-я, \s]+ \d+$)|(Аллея [А-Яа-я, \s]+ \d+$)', self.collection[i].address)
            if ph_match is None:
                self.ph_error += 1
            if correct_weight is False:
                self.wt_error += 1
            if sn_match is None:
                self.sn_error += 1
            if ps_match is None:
                self.ps_error += 1
            if oc_match is None:
                self.oc_error += 1
            if correct_age is False:
                self.ag_error += 1
            if pv_match is None:
                self.pv_error += 1
            if wv_match is None:
                self.wv_error += 1
            if ad_match is None:
                self.ad_error += 1

            if (
                ph_match is None) or (
                correct_weight is False) or (
                sn_match is None) or (
                ps_match is None) or (
                    oc_match is None) or (
                        correct_age is False) or (
                            pv_match is None) or (
                                wv_match is None) or (
                                    ad_match is None
            ):
                self.invalid += 1
                self.valid -= 1
            else:
                valid_list.append(self.collection[i])

        print('Кол-во невалидных записей: ', self.invalid)
        print('Кол-во валидных записей: ', self.valid)
        print()
        print('Кол-во записей с невалидным номером телефона: ', self.ph_error)
        print('Кол-во записей с невалидным весом: ', self.wt_error)
        print('Кол-во записей с невалидным снилсом: ', self.sn_error)
        print('Кол-во записей с невалидной серией паспорта: ', self.ps_error)
        print('Кол-во записей с невалидной профессией: ', self.oc_error)
        print('Кол-во записей с невалидным возрастом: ', self.ag_error)
        print('Кол-во записей с невалидными политическими взглядами: ', self.pv_error)
        print('Кол-во записей с невалидным мировоззрением: ', self.wv_error)
        print('Кол-во записей с невалидным адресом: ', self.ad_error)
        return valid_list


if __name__ == '__main__':
    import tqdm as t
    import json
    import argparse

    parser = argparse.ArgumentParser(description='Paths to input and output files')
    parser.add_argument('-i', '--input', type=str, help='Path to the input file')
    parser.add_argument('-o', '--output', type=str, help='Path to the output file')

    input_path = '../82.txt'
    output_path = '../valid.txt'
    args = parser.parse_args()
    if args.input is not None:
        input_path = args.input
    if args.output is not None:
        output_path = args.output

    validator = Validator()
    validator.load(input_path)
    valid = validator.validate()
    result_list = []
    result_progressbar = t.tqdm(range(len(valid)))
    result_progressbar.set_description('Сохраняем валидные записи')
    for item in result_progressbar:
        temp_dict = {'telephone': valid[item].telephone,
                     'weight': valid[item].weight,
                     'snils': valid[item].snils,
                     'passport_series': valid[item].passport_series,
                     'occupation': valid[item].occupation,
                     'age': valid[item].age,
                     'political_views': valid[item].political_views,
                     'worldview': valid[item].worldview,
                     'address': valid[item].address}
        result_list.append(temp_dict)

    with open(output_path, 'w') as v_file:
        json.dump(result_list, v_file, ensure_ascii=False)
