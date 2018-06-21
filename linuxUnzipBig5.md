
For windows user: download [putty](https://www.putty.org/)

Reference: http://samwhelp.github.io/book-ubuntu-qna/read/case/file-archiving-and-compression/zip/unzip-big5

```
cd /data
```
```
LANG=C 7z x Flu_raw_data/part1.zip
```
```
LANG=C 7z x Flu_raw_data/part2.zip
```
```
convmv -f BIG5 -t UTF-8 -r Flu_raw_data --notest
```

