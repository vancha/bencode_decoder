# Bencode decoder
This is a very simple bencode decoder i have written as a learning excersize
It can decode a torrent file and neatly parse the contents

## usage:
```
decoded_dict = bdecoder.decode("./example.torrent")
```
that should return the contents of the dictionary encoded in to the torrent file
