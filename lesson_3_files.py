# чтение файла
# !!! Можно открыть только существующий файл !!!

# открытие файла
myfile = open("myfile.txt", "r", encoding="utf-8")
text = myfile.read()
myfile.close()  # закрытие файла
                # чтение файла
# print(text)
# print(len(text))
# print(text.splitlines())
# print(len(text.splitlines()))

# # открытие файла в режиме записи (перезаписи)
# new_file = open("new_file.txt", "w", encoding="utf-8")
# text = "I Love Python!"
# new_file.write(text+'\n')
# new_file.write("Python forever!!!\n")
#
# names = ["Masha", "Sasha", "Ivan"]
# # for word in names:
# #     new_file.write(word+'\n')
#
# names_string = "\n".join(names)
# new_file.write(names_string+'\n')
#
# new_file.close()

new_file = open("new_file.txt", "a", encoding="utf-8")
new_file.write("\nNEW TEXT")
new_file.close()
