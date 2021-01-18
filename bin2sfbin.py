#!/usr/bin/env python3

################################################################################
# commands
################################################################################
# or1k-elf-gcc -nostdlib filename.S -o filename.elf
# or1k-elf-objcopy -O binary filename.elf filename.bin
# bin2sfbin.py filename.bin start_addr sf_filename.bin
################################################################################

################################################################################
# SF file format (Big Endian)
################################################################################
# header
#    12B : dummy data ( maybe signature,versions )
#    4B  : code size in bytes
#    4B  : internal memory location to be copied
#    4B  : reset vector address
#    40B : dummy data
#    ~~~ : firmware body
################################################################################


import re,os,sys

if len(sys.argv)<3:
	print('Usage:')
	print('{} inputfile.bin start_address [outputfile.bin]'.format(sys.argv[0]))
	print('')
	quit()
elif len(sys.argv)>3:
	output_file = sys.argv[3]
	outfile = open(output_file,'wb')
else:
	print('Error')
	quit()

input_file = sys.argv[1]
if '0x' in sys.argv[2]:
	start_addr = int(sys.argv[2],16)
else:
	start_addr = int(sys.argv[2])

with open(input_file,'rb') as f:
	data = f.read()

size = len(data)
size_0 = ((size+4))%256
size_1 = ((size+4)//256)%256
size_2 = ((size+4)//256//256)%256
size_3 = ((size+4)//256//256//256)%256

addr_0 = ((start_addr))%256
addr_1 = ((start_addr)//256)%256
addr_2 = ((start_addr)//256//256)%256
addr_3 = ((start_addr)//256//256//256)%256

comment = None

def set_comment(s):
	pass
#	global comment
#	if comment is not None:
#		comment = comment + s
#	else:
#		comment = s

def write(l):
	outfile.write(bytes(l))


#write('')
set_comment('\t\\\\ Serial Flash memory image')
set_comment('\t\\\\ Header')
for i in range(3):
	write([0x00,0x00,0x00,0x00])
set_comment('\t\\\\ Firmware size')
write([size_3,size_2,size_1,size_0])
set_comment('\t\\\\ Firmware address')
write([0x00,0x00,0x00,0x00])
set_comment('\t\\\\ Firmware reset address')
write([addr_3,addr_2,addr_1,addr_0])
set_comment('\t\\\\ dummy header bytes')
for i in range(10):
	write([0x00,0x00,0x00,0x00])

set_comment('\t\\\\ firmware body')
for i in range(0,size,4):
	write([data[i],data[i+1],data[i+2],data[i+3]])
	
set_comment('\t\\\\ just padding')
for i in range(10):
	write([0x00,0x00,0x00,0x00])







