def simple_file_reading():
    fd = open('file.txt')
    print(fd.readline())
    fd.close()


def file_reading_with_try():
    fd = open('file.txt')
    try:
        result = fd.readline()
        raise Exception()
        print(result)
    except:
        print('Exception occurred')
    finally:
        fd.close()


def file_reading_with_context_manager():
    with open('file.txt') as fd:
        result = fd.readline()
        raise Exception()
        print(result)


class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.fd = None

    def __enter__(self):
        self.fd = open(self.filename)
        return self.fd

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        self.fd.close()


def file_reading_with_custom_manager():
    with FileManager('file.txt') as fd:
        result = fd.readline()
        raise Exception()
        print(result)


if __name__ == '__main__':
    simple_file_reading()
    # file_reading_with_try()
    # file_reading_with_context_manager()
    # file_reading_with_custom_manager()
