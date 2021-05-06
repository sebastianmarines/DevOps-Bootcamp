# Compression

## Tar
Tar is an archiving tool, it collects files and their metadata together and produces one file.

It does not provide compression.

### Commands:
- `tar -cvf archive.tar [FILES]`: Archive files
- `tar -xvf archive.tar`: Extract files from archive

## GZip
GZip is a compression algorith that works by searching the file for duplicated chains of characters. If GZip finds duplicated bytes it replaces them for a reference to the first occurrence.

GZip can only compress individual files, this is why it is commonly combined with the _tar_ archiver to create tarballs _(.tar.gz or .tgz)_

### Commands:
- `tar -czvf archive.tar.gz [FILES]`: Crate a tarball.
- `tar -xzvf archive.tgz`: Decompress tarball

## BZip2
bzip2 is another compression program that uses the Burrows-Wheeler and Huffman algorithms.

The commpression ratio can be higher than most other compression programs but it uses more memory and it is slower.

### Commands:
- `bzip2 file`: Compress a file
- `bunzip2 file.bz2`: Decompress

## Zip
Zip uses a very simple method to compress files, it compresses each file separately, which allows to extract individual files without reading the whole compressed file.
 
This is veri efficient when you want to extract specific files, but the size of the archive is bigger because it stores individual files instead of grouping and then compressing them.

### Commands
- `zip archive.zip [FILES]`: Compress files
- `unzip archive.zip`: Decompress
