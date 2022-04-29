import time
import sys

indent = 0    # How many spaces to indent
indentIncreasing = True    # Whether the indentation is increasing or not.

try:
    while True:    # The man program loop
        print('  ' * indent, end='')
        print('********')
        time.sleep(0.1)    # Pause for 1/10 of a second

        if indentIncreasing:
            # Increase the number for spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction
                indentIncreasing = False
        else:
            # Decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
