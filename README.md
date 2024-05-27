# Bencode decoder
This is a very simple bencode decoder i have written as a learning excersize
It can decode a torrent file and neatly parse the contents

## usage:
```
decoded_dict = bdecoder.decode("./example.torrent")
```
that should return the contents of the dictionary encoded in to the torrent file

can be installed by cloning, and calling `pip3 install .` from within the root folder.
to uninstall, use `pip3 remove bencode-decoder`. 
