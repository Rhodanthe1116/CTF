https://codebeautify.org/hex-string-converter
- github.com/lijiejie/ds_store_exp

## pwntools

```
apt-get update
apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pwntools
```
## dump data

```
objcopy -O binary --only-section=.data ./gift data2
od -An -t x1 data2 > data22
```

## ida

- strings: shift + f12

### remote 

```
ip add | grep '172'
```

## gdb

```sh
sudo apt-get update
sudo apt-get install gdb
```

```
vmmap
p/x 0xa - 0xb
```
### gef

```
sh -c "$(curl -fsSL http://gef.blah.cat/sh)"
```

for docker

```
apt-get install curl
apt-get install wget
```

### readelf

```
apt-get install binutils
```

如果想快速從libc找某個function的offset，可以用readelf -s | grep

```

readelf -a /lib64/libc-2.32.so | grep 'system'
readelf -a /lib/x86_64-linux-gnu/libc-2.29.so | grep 'system'

readelf -s <libc binary> | grep <symbol(function) name>
```

### patch

```
python3 ../../LD_CHANGER.py ld-2.31.so babynote 
```