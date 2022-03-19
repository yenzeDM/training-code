import os

FOUND_FILE_PATH = []


def file_traversal(path, name, level=1):
    # print('Level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if str(i) == name:
            global FOUND_FILE_PATH
            FOUND_FILE_PATH.append(path + '\\' + i)
        if os.path.isdir(path + '\\' + i):
            # print('Going down', path + '\\' + i)
            file_traversal(path + '\\' + i, name)
            # print('Back to', path)


name = 'adobe_creative_cloud.png'
path = 'C:\\D'
file_traversal(path, name)
print(*FOUND_FILE_PATH)



# через class
#
#
# class FileSearch:
#     FOUND_FILE_PATH = []
#
#     def file_traversal(self, path, name):
#         for i in os.listdir(path):
#             if str(i) == name:
#                 FileSearch.FOUND_FILE_PATH.append(path + '\\' + i)
#             if os.path.isdir(path + '\\' + i):
#                 FileSearch.file_traversal(self, path + '\\' + i, name)
#
#
# file = 'adobe_creative_cloud.png'
# directory = 'C:\\D'
# f = FileSearch()
# f.file_traversal(directory, file)
# print(*f.FOUND_FILE_PATH)