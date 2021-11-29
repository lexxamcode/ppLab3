from vpackage.validator_script import Person


def load(path: str = None) -> list:
    import tqdm as t
    import json

    collection = []
    data = json.load(open(path, encoding='windows-1251'))
    progressbar = t.tqdm(range(len(data)))
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
        collection.append(temp)
    print('Done')
    return collection


def write(path: str, sorted_list: list) -> None:
    import tqdm as t
    import json

    result_list = []
    result_progressbar = t.tqdm(range(len(sorted_list)))
    result_progressbar.set_description('Сохраняем отсортированные записи')
    for i in result_progressbar:
        temp_dict = {'telephone': sorted_list[i].telephone,
                     'weight': sorted_list[i].weight,
                     'snils': sorted_list[i].snils,
                     'passport_series': sorted_list[i].passport_series,
                     'occupation': sorted_list[i].occupation,
                     'age': sorted_list[i].age,
                     'political_views': sorted_list[i].political_views,
                     'worldview': sorted_list[i].worldview,
                     'address': sorted_list[i].address}
        result_list.append(temp_dict)

    with open(path, 'w') as v_file:
        json.dump(result_list, v_file, ensure_ascii=False)


def quick_sort(list_of_persons: list) -> list:
    import sys

    sys.setrecursionlimit(100000)
    if len(list_of_persons) < 2:
        return list_of_persons
    else:
        pivot = list_of_persons[0]
        less = [i for i in list_of_persons[1:] if i.age <= pivot.age]

        greater = [i for i in list_of_persons[1:] if i.age > pivot.age]

        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    input_path = '../valid.txt'
    output_path = '../svalid.txt'
    persons = load(input_path)

    sorted_result_list = quick_sort(persons)
    write(output_path, sorted_result_list)

    sorted_persons = load('../svalid.txt')
    for item in sorted_persons:
        print(item.age)
