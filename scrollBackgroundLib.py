import sys

def init(filename):

    scrollBackgroundList = dict()

    myFile = open(filename, 'r')
    fileContent = myFile.read()

    scrollBackground_separated = fileContent.split("\nscrollBackground\n")

    for scrollBackground_raw in scrollBackground_separated:
        scrollBackground_lines = scrollBackground_raw.split("\n")
        scrollBackground_name = scrollBackground_lines[0]
        del scrollBackground_lines[0]
        scrollBackgroundList[scrollBackground_name]=[]
        for scrollBackground_line in scrollBackground_lines:
            scrollBackgroundList[scrollBackground_name].append(scrollBackground_line)

    return scrollBackgroundList

def show(scrollBackground,level_length,scrollLine):

    #couleur fond noire
    sys.stdout.write("\033[40m")
    b=1
    scrollSpeed = 0.4

    txt="\033[3"+str(4)+"m"
    sys.stdout.write(txt)

    for i in range(int(level_length)-int(scrollLine*scrollSpeed),int(level_length)-int(scrollLine*scrollSpeed)+33):
        txt="\033["+str(b+1)+";"+str(2)+"H"
        sys.stdout.write(txt)

        sys.stdout.write(scrollBackground[i])
        b=b+1
