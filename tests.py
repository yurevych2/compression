from classes import Lz77_compress, Lzw_compress

text = 'I love discrete math without any discussions.'
code, def_dic = Lzw_compress.encode(text)
assert(text == Lzw_compress.decode(code, def_dic))
assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 4)))
assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 5)))
assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 6)))
assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 7)))
assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 8)))
assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 9)))

text = 'abacabadabacacacd'
code, def_dic = Lzw_compress.encode(text)
assert(text == Lzw_compress.decode(code, def_dic))
assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 4)))
assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 5)))
assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 6)))
assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 7)))
assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 8)))
assert(text == Lz77_compress.decode(Lz77_compress.encode(text, 9)))

if __name__ == '__main__':
    print('All is nice =^w^=')
