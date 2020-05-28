unittest:
	python3 test/test_roundtrip.py

install:
	python3 setup.py install

clean:
	-rm -r build
	-rm -r dist
	-rm -r simplerosbag.egg-info
	-rm -r /usr/local/lib/python3.8/site-packages/simplerosbag-0.1-py3.8.egg
