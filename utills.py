def filter_query(param: str, data: list[str]) -> list[str]:
    """Поиск по фильтру параметров в данных"""
    # def search(data, param):
    #     result = []
    #     for row in data:
    #         if param in row:
    #             result.append(row)
    #     return result
    return list(filter(lambda row: param in row, data))


def map_query(param: str, data: list[str]) -> list[str]:
    col_numb = int(param)
    return list(map(lambda row: row.split(' ')[col_numb], data))


def unique_query(data: list[str], *args, **kwargs) -> list[str]:
    result = []
    seen = set()
    for row in data:
        if row in seen:
            continue
        else:
            result.append(row)
            seen.add(row)
    return result


def sort_query(param: str, data: list[str]) -> list[str]:
    reverse = False if param == "asc" else True
    return sorted(data, reverse=reverse)


def limit_query(param: str, data: list[str]) -> list[str]:
    limit = int(param)
    return data[:limit]


dict_of_utils = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
}


def build_query(cmd, param, filename, data=None):
    if not data:
        with open(f'data/{filename}') as file:
            data = list(map(lambda row: row.strip(), file))
    return dict_of_utils[cmd](param=param, data=data)
