import sys
if list(sys.version)[0]!="3":
    sys.stdout.write("ERREUR DE VERSION : LA VERSION DE PYTHON DOIT ETRE 3.X , Il est recommande d'installer python 3.8")
    exit()

import startMenuLib, main
import termios
import tty

#redimmensionne l'ecran
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=38, cols=44))

#interaction clavier
old_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())

#effacer la console
sys.stdout.write("\033[1;1H")
sys.stdout.write("\033[2J")

startMenuLib.init()
startMenuLib.run(old_settings)
startMenuLib.close()

main.init()
main.run()
