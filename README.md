# Bencode decoder
This is a very simple bencode decoder i have written as a learning excersize
It can decode a torrent file and neatly parse the contents

## usage:
```
from bencode_decoder import bencode_decoder
decoded_dict = bencode_decoder.bdecoder.decode("./example.torrent")
```
that should return the contents of the dictionary encoded in to the torrent file

# installation

can be installed with `pip3 install git+https://github.com/vancha/bencode_decoder.git`

to uninstall, use `pip3 remove bencode-decoder`. 
