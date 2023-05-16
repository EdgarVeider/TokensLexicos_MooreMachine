import sys

class FileOpen:

    @staticmethod
    def read_file(file):
        arq = None
        with open(file, "r") as arquivo:
            arq = arquivo.read()

        buffer = arq.split('\n')

        str_p = ""
        for b in buffer:
            str_p = str_p + b

        return str_p
    
