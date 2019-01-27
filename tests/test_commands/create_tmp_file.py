import os


class CreateTmpFile(object):
    def __init__(self, file_name, text):
        self.file_name = file_name
        self.text = text

    def __call__(self, original_func):
        def wrappee(*args, **kwargs):
            with open(self.file_name, 'w') as f:
                f.write(self.text)
            original_func(*args, **kwargs)
            os.remove(self.file_name)

        return wrappee
