def conversion_from_coord_to_index(coord) -> int:
    """
    Conversion from coordinate to index
    :param coord: (row, col)
    :return: index
    """
    return coord[1] + 3*coord[0]


def conversion_from_index_to_coord(index) -> tuple:
    """
    Conversion from index to coordinate
    :param index: index
    :return: coordinate
    """
    return index // 3, round(index % 3)


def connection_of_elements_place(indices: tuple, place: list) -> str:
    """

    :param indices: indexes to be concatenated into a string
    :param place: place from which values are taken
    :return: string
    """
    result_string = ''
    for index in indices:
        coord = conversion_from_index_to_coord(index)
        result_string += str(place[coord[0]][coord[1]])
    return result_string


def remove_duplicate_characters(string) -> str:
    """
    :param string: string to remove duplicate characters from
    :return:
    """
    return "".join(set(string))