import sys
def write_in_file(string):
    with open('D:\Programs\PyCharm Community Edition 2021.2.3\Project\PPVIS4\model\data history\history.txt', 'a') as f:
        original_stdout = sys.stdout
        sys.stdout = f
        print(string)
        sys.stdout = original_stdout
