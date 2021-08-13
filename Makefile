package_name = custom_lib

install: ${package_name}.o ${package_name}_wrap.o
	gcc -shared ${package_name}.o ${package_name}_wrap.o -o _${package_name}.so

${package_name}_wrap.o: ${package_name}_wrap.c ${package_name}.o
	gcc -O2 -fPIC -c ${package_name}_wrap.c -I/usr/include/python3.9

${package_name}.o: ${package_name}.c
	gcc -O2 -fPIC -c ${package_name}.c

${package_name}_wrap.c ${package_name}.py: ${package_name}.i ${package_name}.c ${package_name}.h
	swig -python ${package_name}.i

clean:
	rm -rf *.o __pycache__/

delete:
	rm -rf *.o ${package_name}.py ${package_name}_wrap.c _${package_name}.so __pycache__/
