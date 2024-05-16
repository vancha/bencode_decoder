from more_itertools import peekable

'''
A python class that can decode a torrent file
'''
class bdecoder:

    def decode_byte_string(byte_iterator):
        #byte strings are prefixed with a length
        length = ''
        
        while chr(byte_iterator.peek()).isnumeric():
            length += chr(next(byte_iterator))
        
        #also skip the double colon that's present after every string length
        next(byte_iterator)
        value = ""
        for _ in range(int(length)):
            value += chr(next(byte_iterator))
        return value

    def decode_integer(byte_iterator):
        #skip over the 'i'
        next(byte_iterator)
        values = ''
         
        while not chr(byte_iterator.peek()) == 'e':#.isnumeric():
            values += chr(next(byte_iterator))
        
        #skip over the 'e'
        next(byte_iterator)
        return int(values)

    def decode_list( byte_iterator):
        #skip over the 'l'
        next(byte_iterator)

        result = []
        while not chr(byte_iterator.peek()) == 'e':
            result.append(bdecoder.decode_next(byte_iterator))

        #skip over the 'e'
        next(byte_iterator)
        return result

    def decode_next(byte_iterator):
        val = chr(byte_iterator.peek())

        if val == 'd':
            return bdecoder.decode_dict(byte_iterator)
        elif val == 'l':
            return bdecoder.decode_list(byte_iterator)
        elif val == 'i':
            return bdecoder.decode_integer(byte_iterator)
        else:
            return bdecoder.decode_byte_string(byte_iterator)

    def decode_dict(byte_iterator):
        #skip over the initial 'd'
        next(byte_iterator)

        result  = {}
        while not chr(byte_iterator.peek()) == "e":
            field_name =  bdecoder.decode_byte_string(byte_iterator)
            field_value = bdecoder.decode_next(byte_iterator)
            result[field_name] = field_value

        #skip over the 'e'
        next(byte_iterator)
        return result

    #returns the decoded torrent file
    def decode(torrent_file):
        file  = open(torrent_file, "rb").read()
        byte_iterator  = peekable(file)
        return bdecoder.decode_next(byte_iterator)


decoded_dict = bdecoder.decode("./ubuntu.torrent")
for key in decoded_dict.keys():
    print(f'key: {key}')

print(decoded_dict["info"])
