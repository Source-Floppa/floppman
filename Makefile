all: install

install:
	chmod 755 floppman
	cp floppman /usr/local/bin
	ln -sf /usr/local/bin/floppman /usr/local/bin/flp
