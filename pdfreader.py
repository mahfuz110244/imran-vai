# -*- coding: utf-8 -*-
import textract
# text = textract.process("invoice.pdf")
text = textract.process("invo.pdf")
text_list = text.splitlines()
# print text_list
# text_list.remove('')
# print text_list
# for l in range(len(text_list)):
#     print text_list[l]
#     if text_list[l]:
#         print text_list[l]
# print text_list
# [x for x in text_list if x]
# print text_list
text_list = filter(None, text_list)
print text_list
for t in text_list:
    print t