from classes import Lz77_compress, Lzw_compress

math_text = '11213409172489889898121341345134511617171167'
weird_text = 'abacabadabacacacd'
short_text = 'I love discrete math without any discussions.'
big_text = 'Доброго дня, пані Світлано!\nЯ – … студентка Українського католицького \
університету. Представниця організаторів інтелектуальної гри «Monty Quiz». Звертаюся \
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

print('Nice work =^w^=')
