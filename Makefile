
gen-tree: __main__.py
	echo "#!/bin/python3" > gen-tree
	zip gen-tree.zip __main__.py
	cat gen-tree.zip >> gen-tree

clean:
	-rm gen-tree.zip
	-rm gen-tree

rebuild:
	make clean
	make