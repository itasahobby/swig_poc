# Swig PoC
PoC to showcase C integration with Python as well as some benchmarks

# Setup

Compile the package:
```
make
gcc -O2 -fPIC -c custom_lib.c
swig -python custom_lib.i
gcc -O2 -fPIC -c custom_lib_wrap.c -I/usr/include/python3.9
gcc -shared custom_lib.o custom_lib_wrap.o -o _custom_lib.so
```

Run the benchmarks:
```
python3 benchmark.py 
Factorial benchmark:
c_time=9.265873008000199
py_time=10.641659813998558
Anagram benchmark:
c_time=9.163944766001805
py_time=141.76448946099845
```
