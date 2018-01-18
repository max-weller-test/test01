### CFG int test_parameter [ms] "write description here..."
### CFG string str_param "write description here..."
### ENV float float_param "write description here..."
### CFG int foo "write description here..."
### CFG int bar "write description here..."
import framework
from time import sleep

# test 2

if __name__ == '__main__':
	framework.start()
	framework.record("a", framework.param('a'))
	sleep(2)
	framework.record("b", framework.param('b'))
	framework.stop()

