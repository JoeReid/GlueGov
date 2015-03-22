extract: download
	cd lib; unzip vis.zip

download: lib
	wget http://visjs.org/download/vis.zip
	mv vis.zip lib
	wget http://code.jquery.com/jquery-2.1.3.min.js
	mv jquery-2.1.3.min.js lib

lib:
	mkdir -p lib
