# The MIT License
#
#  Copyright (c) 2017, lswang2
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

FROM        lswang2/base:latest
MAINTAINER  wang@picocel.com

USER        root
ENV         VERSION=1.3.4
ENV         FILE=or1k_tool_chain_wang_bionic_v${VERSION}.txz
ENV         URL=https://github.com/lswang2/binutils-gdb/releases/download/${VERSION}/${FILE}

ENV         PATH="/usr/local/or1k/bin:${PATH}"

WORKDIR     /tmp
RUN         wget ${URL}

WORKDIR     /usr/local
RUN         tar Jxvf /tmp/${FILE}

RUN         rm -f /tmp/${FILE}

WORKDIR     /root

VOLUME      /work

WORKDIR     /work

RUN         echo "alias list=\"or1k-elf-gcc -Wa,-adhln -g\"" >> /root/.bashrc
RUN         echo "export PATH=$PATH:/usr/local/or1k/bin" >> /root/.bashrc

#ENTRYPOINT ["/bin/bash"]
