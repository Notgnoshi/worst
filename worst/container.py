from worst.number_theory import is_prime


class Worst(object):
    """
        The worst container class.
    """

    def __init__(self):
        """
            Instantiates a Worst object, optionally from
            a given iterable of finite length.
        """
        # Wrap a dict() so we don't provide all the handy methods
        self.__items = dict()

    def __setitem__(self, key, item):
        """
            Inserts an item at the given key.
        """
        if not isinstance(key, int):
            raise TypeError(f'Unsupported key type: {type(key)}')

        if is_prime(key):
            self.__items[key] = item
        else:
            raise NotImplementedError('Composite commands not implemented yet...')

    def __getitem__(self, key):
        """
            Gets an item stored at the given key.
        """
        if not isinstance(key, int):
            raise TypeError(f'Unsupported key type : {type(key)}')
        if is_prime(key):
            return self.__items[key]
        else:
            raise NotImplementedError('Composite commands not implemented yet...')
