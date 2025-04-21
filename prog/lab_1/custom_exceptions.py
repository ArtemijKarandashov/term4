class NegativeHeightException(Exception):
    def __str__(self):
        return 'Cannot build binary tree. Height value is negative!'