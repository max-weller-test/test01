import framework
from time import sleep

# test 2

if __name__ == '__main__':
	framework.start()
	framework.record("a", framework.param('a'))
	sleep(2)
	framework.record("b", framework.param('b'))
	framework.stop()

