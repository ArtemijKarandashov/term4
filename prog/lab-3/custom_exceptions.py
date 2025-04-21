class JsonDecoratorNonValidPath(BaseException):
    def __str__(self):
        return "Can not open .json log file! Wrong directory indicated?"