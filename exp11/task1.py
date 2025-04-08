from docx import Document
from docx.shared import RGBColor

boldText = []
redText = []
# 修正引号
doc = Document('test.docx')

for p in doc.paragraphs:
    for r in p.runs:
        # 加粗字体
        # 修正变量名大小写
        if r.bold:
            boldText.append(r.text)
        # 红色字体
        # 修正变量名大小写
        if r.font.color.rgb == RGBColor(255, 0, 0):
            redText.append(r.text)

# 修正引号
result = {'red text': redText,
          "bold text": boldText,
          'both': set(redText) & set(boldText)}

# 输出结果
for title in result.keys():
    # 修正逗号
    print(title.center(30, "="))
    for text in result[title]:
        print(text)
