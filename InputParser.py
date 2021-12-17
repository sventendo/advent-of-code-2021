class InputParser:
    @staticmethod
    def parse(file_path):
        with open(file_path) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            return lines

    @staticmethod
    def parse_int(file_path):
        with open(file_path) as file:
            lines = file.readlines()
            lines = [int(line.rstrip()) for line in lines]
            return lines
