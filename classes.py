'''Module with classes to compress information in different ways.'''

import csv

class Lzw_compress:
    '''Use LZW algorithm to encode and decode information.'''
    def encode(text: str) -> tuple[list[int], dict]:
        '''
        Encode text.

        Return a tuple with list of coded information and default dictionary to decode.
        '''
        chrs_dict = {idx: chr for idx, chr in enumerate(sorted(list(set(text))))}
        chrs_default = {key: chr for key, chr in chrs_dict.items()}
        code = []

        i = 0
        while i < len(text): # go through the text
            current_chr = text[i]
            if i == len(text) - 1:
                code.append(list(chrs_dict.keys())[list(chrs_dict.values()).index(current_chr)]) # get the code
                break
            end = False
            while current_chr in chrs_dict.values():
                i += 1
                if i == len(text):
                    code.append(list(chrs_dict.keys())[list(chrs_dict.values()).index(current_chr)]) # get the code
                    end = True
                    break
                current_chr = current_chr + text[i]
            if end:
                break
            current_chr = current_chr[0:-1] if len(current_chr) > 1 else current_chr
            code.append(list(chrs_dict.keys())[list(chrs_dict.values()).index(current_chr)]) # get the code
            next_chr = text[i]
            chrs_dict[len(chrs_dict)] = current_chr + next_chr
        
        return code, chrs_default

    def decode(code: list[int], default_dict: dict) -> str:
        '''
        Decode information encoded with LZW algorithm.
        
        Return text.
        '''
        text = []
        i = 0
        while i < len(code):
            if i < len(code) - 1 and code[i+1] in default_dict:
                default_dict[len(default_dict)] = default_dict[code[i]] + default_dict[code[i+1]][:1]
            else:
                default_dict[len(default_dict)] = default_dict[code[i]] + default_dict[code[i]][:1]
            text.append(default_dict[code[i]])
            i += 1
        
        return ''.join(text)

    def write_encoded(code: list[int], def_dict: dict[int], file_name: str) -> None:
        '''Write encoded text to a file.'''
        with open(file_name, 'w') as file:
            file.write(','.join([str(num) for num in code]))
            file.write(str(def_dict))


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

    def write_encoded(code: list[int], file_name: str) -> None:
        '''Write encoded text to a file.'''
        with open(file_name, 'w') as file:
            file.write(','.join([str(num) for num in code]))
            

from collections import Counter, defaultdict
class Huffman:
    """
    Reduce size file.
    """

    def count_frequency(self, message: str) -> list[tuple]:
        """
        Count frequency for all unique elements in message

        Args:
            Message: 'random string'

        Returns:
            List with probability

        """
        return [(key, freq/len(message)) for key, freq in Counter(message).items()]

    def build_code(self, probability: list[tuple]) -> dict:
        """
        Build tree and create dictionary with code for all letters

        Args:
            Probability: [("A", 0.1), ("B", 0.1), ("C", 0.1), ("E", 0.7)])

        Returns:
            Dictionary of code: {'A': '101', 'B': '001', 'C': '11', 'E': '0'}
        """
        dict_code = defaultdict(str)
        sort_probability = sorted(probability, key=lambda x: x[1])
        while len(sort_probability) != 1:
            left_node, right_node = sort_probability[0], sort_probability[1]
            parent_node = (left_node[0] + right_node[0], left_node[1] + right_node[1])

            for name in left_node[0]:
                dict_code[name] += '1' 
            for name in right_node[0]:
                dict_code[name] += '0'

            sort_probability.append(parent_node)
            sort_probability.pop(0)
            sort_probability.pop(0)

        return dict_code

    def encode(self, message: str) -> list[float]:
        """
        Encode by Huffman algorithm

        Args:
            Message: 'random string'

        Returns:
            list: encoded message
        """
        probability = self.count_frequency(message)
        dict_code = self.build_code(probability)
        code_message = []
        for letter in message:
            code_message.append(dict_code.get(letter))
        return code_message, dict_code
    
    def decode(self, code: list[float], tree: dict) -> str:
        """
        Decode message by Huffman algorithm
        
        Args:
            Code: encoded message
            Tree: dictionary, key - number or letter and value - binary code 

        Returns:
            str: decoded message
        """
        decode_code = []
        for item in code:
            for key, value in tree.items():
                if item == value:
                    decode_code.append(key)
        return ''.join(decode_code)
        

def read_file(input_file: str):
   """
   Read file

   Args:
        Name file: 'chorna_rada.txt'
   """
    with open(input_file, 'r', encoding='utf-8') as file:
        return file.read()
  
