'''Module with classes to compress information in different ways.'''

class Lzw_compress:
    '''Use LZW algorithm to encode and decode information.'''
    def encode(text: str) -> tuple[list[int], dict]:
        '''
        Encode text.

        Return a tuple with list of coded information and default dictionary to decode.
        '''
        chrs_dict = {idx: chr for idx, chr in enumerate(sorted(list(set(text))))}
        code = []

        i = 0
        while i < len(text): # go through the text
            current_chr = text[i]
            if i == len(text) - 1:
                code.append(list(chrs_dict.keys())[list(chrs_dict.values()).index(current_chr)]) # get the code
                break
            while current_chr in chrs_dict.values():
                i += 1
                current_chr = current_chr + text[i]
            current_chr = current_chr[0:-1]
            code.append(list(chrs_dict.keys())[list(chrs_dict.values()).index(current_chr)]) # get the code
            next_chr = text[i]
            chrs_dict[len(chrs_dict)] = current_chr + next_chr
        
        return code, chrs_dict

    def decode(code: list[int], default_dict: dict) -> str:
        '''
        Decode information encoded with LZW algorithm.
        
        Return text.
        '''
        text = []
        i = 0
        while i < len(code):
            if i < len(code) - 1 and code[i+1] in default_dict.keys():
                default_dict[len(default_dict)] = default_dict[code[i]] + default_dict[code[i+1]][:1]
            else:
                default_dict[len(default_dict)] = default_dict[code[i]] + default_dict[code[i]][:1]
            text.append(default_dict[code[i]])
            i += 1
        
        return ''.join(text)


class Lz77_compress:
    '''Use LZ-77 algorithm to encode and decode information.'''
    def encode(text: str, buffer_size: int) -> list[tuple[int, int, str]]:
        '''
        Encode text.

        Return a list with tuples of coded information.
        '''
        code = []
        buffer = ['']
        i = 0 # idx of current letter
        while i < len(text):
            for idx, chr in enumerate(buffer):
                if idx == len(buffer) - 1:
                    code.append((0, 0, text[i]))
                    i += 1
                    buffer = text[max(0, i - buffer_size): i]
                    break

                if chr == text[i]:
                    start = idx
                    num_chr = 1
                    if i == len(text) - 1:
                        code.append((len(buffer) - start, num_chr, ''))
                        return code
                    while idx + 1 < len(buffer) and buffer[idx + 1] == text[i + 1]:
                        num_chr += 1
                        i += 1
                        idx += 1
                    code.append((len(buffer) - start, num_chr, text[i + 1]))
                    i += 1
                    buffer = text[max(0, i - buffer_size + 1) : i + 1]
                    i += 1
                    break

        return code

    def decode(code: list[tuple[int, int, str]]) -> str:
        '''
        Decode information encoded with LZ-77 algorithm.
        
        Return text.
        '''
        decode = ''
        for back, number, last in code:
            decode = decode + decode[len(decode) - back : len(decode) - back + number] + last
        
        return decode
