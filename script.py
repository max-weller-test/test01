import framework
from time import sleep

if __name__ == '__main__':
	framework.start()
	framework.record("a", framework.param('a'))
	sleep(2)
	framework.record("b", framework.param('b'))
	framework.stop()

    