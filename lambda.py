# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# -- LAMBDA++ --                                                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class flist(list):
    """ @brief augmented builtin list: supports call operation """
    def __call__(self, *args, **kwargs):
        """ @brief call each element of the list and return list of results """
        return [f(*args, **kwargs) for f in self]

class fdict(dict):
    """ @brief augmented builtin dict: supports call operation """
    def __call__(self, *args, **kwargs):
        """ @brief call each element of the dict and return a dict:
             key -> result function call """
        return dict((k, v(*args, **kwargs)) for k, v in self.items())
