from classes import Lz77_compress, Lzw_compress

math_text = '11213409172489889898121341345134511617171167'
weird_text = 'abacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacd\
abacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacd\
abacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacd\
abacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacd\
abacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacd\
abacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacd\
abacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacd\
abacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacd\
abacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacd\
abacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacdabacabadabacacacd'
short_text = 'I love discrete math without any discussions.'
big_text = 'Доброго дня, пані Світлано!\nЯ – … студентка Українського католицького \
університету. Представниця організаторів інтелектуальної гри «Monty Quiz». Звертаюся \
до компанії «Sigma Software» з пропозицією стати партнерами нашого заходу.\nПишу вам, \
бо наша команда цінує значний вклад «Sigma Software» в розвиток ІТ-освіти, надійність і \
високу якість наданих послуг.\n«Monty Quiz» – тематичний квіз для любителів Python. \
Ділимося з вами нашим першим досвідом проведення гри серед студентів та викладачів \
УКУ й додаємо правила, фотозвіт та посилання на пост.\
до компанії «Sigma Software» з пропозицією стати партнерами нашого заходу.\nПишу вам, \
бо наша команда цінує значний вклад «Sigma Software» в розвиток ІТ-освіти, надійність і \
високу якість наданих послуг.\n«Monty Quiz» – тематичний квіз для любителів Python. \
Ділимося з вами нашим першим досвідом проведення гри серед студентів та викладачів \
УКУ й додаємо правила, фотозвіт та посилання на пост.\
до компанії «Sigma Software» з пропозицією стати партнерами нашого заходу.\nПишу вам, \
бо наша команда цінує значний вклад «Sigma Software» в розвиток ІТ-освіти, надійність і \
високу якість наданих послуг.\n«Monty Quiz» – тематичний квіз для любителів Python. \
Ділимося з вами нашим першим досвідом проведення гри серед студентів та викладачів \
УКУ й додаємо правила, фотозвіт та посилання на пост.'

text_list = [math_text, weird_text, short_text, big_text]

for text in text_list:
    code, def_dic = Lzw_compress.encode(text)
    assert(text == Lzw_compress.decode(code, def_dic))
    assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 4)))
    assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 5)))
    assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 6)))
    assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 7)))
    assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 8)))
    assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 9)))

# save text that is different
with open('different_text.txt', 'r', encoding='utf-8') as file:
    different_text = '\n'.join(file.readlines())

# write encoded by LZW different text
code, def_dict = Lzw_compress.encode(different_text)
Lzw_compress.write_encoded(code, def_dict, 'different_encoded_lzw.txt')

# write encoded by LZ-77 (buffer 7) different text
code = Lz77_compress.encode(different_text, 7)
Lz77_compress.write_encoded(code, 'different_encoded_lz77_7.txt')

# write encoded by LZ-77 (buffer 17) different text
code = Lz77_compress.encode(different_text, 17)
Lz77_compress.write_encoded(code, 'different_encoded_lz77_17.txt')

# write encoded by LZ-77 (buffer 27) different text
code = Lz77_compress.encode(different_text, 27)
Lz77_compress.write_encoded(code, 'different_encoded_lz77_27.txt')

# save text that is similar
with open('similar_text.txt', 'w') as file:
    file.write(weird_text)

# write encoded by LZW similar text
code, def_dict = Lzw_compress.encode(weird_text)
Lzw_compress.write_encoded(code, def_dict, 'similar_encoded_lzw.txt')

# write encoded by LZ-77 (buffer 7) different text
code = Lz77_compress.encode(weird_text, 7)
Lz77_compress.write_encoded(code, 'similar_encoded_lz77_7.txt')

# write encoded by LZ-77 (buffer 17) different text
code = Lz77_compress.encode(weird_text, 17)
Lz77_compress.write_encoded(code, 'similar_encoded_lz77_17.txt')

# write encoded by LZ-77 (buffer 27) different text
code = Lz77_compress.encode(weird_text, 27)
Lz77_compress.write_encoded(code, 'similar_encoded_lz77_27.txt')

# LZW
# SIMILAR TEXT 833bytes before encoding and 456bytes after ~ 1,8
# DIFFERENT TEXT 7,93KB before encoding and 11,5KB after ~ 0,68

# LZ-77
# SIMILAR TEXT with buffer 7 833bytes before encoding and 4,6KB after ~ 0,18
# SIMILAR TEXT with buffer 17 833bytes before encoding and 714bytes after ~ 1,2
# SIMILAR TEXT with buffer 27 833bytes before encoding and 2,51KB after ~ 0,33
# DIFFERENT TEXT with buffer 7 7,93KB before encoding and 71,6 after ~ 0,12
# DIFFERENT TEXT with buffer 17  7,93KB before encoding and 60,5KB after ~ 0,13
# DIFFERENT TEXT with buffer 27  7,93KB before encoding and 55,4KB after ~ 0,14

print('Nice work =^w^=')
