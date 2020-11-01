# flake8: noqa

class STALibValidationError(Exception):
    """
    Algorithm data validation raised Error.

    if the data is not homogenous.
    """

    def __init__(self, _type: str = None) ->None:

        self._type = _type
        super().__init__()

    def __str__(self):
        return "For Algorithms Data should be homogenous"
