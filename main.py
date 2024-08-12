import types

def flat_generator(list_of_lists):
    """генератор для списков с одним уровнем вложенности"""
    for sublist in list_of_lists:
        for item in sublist:
            print(f"FG item: {item}") 
            yield item

def deep_flat_generator(list_of_list):
    """генератор для списков с любым уровнем вложенности"""
    for item in list_of_list:
        if isinstance(item, list):
            print(f"DFG: {item}")  
            yield from deep_flat_generator(item)  
        else:
            print(f"DFG item: {item}") 
            yield item

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            deep_flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(deep_flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(deep_flat_generator(list_of_lists_2), types.GeneratorType)

if __name__ == '__main__':
    test_2()
    test_4()
