from PIL import Image
import time
from mazes import Maze
from factory import SolverFactory
Image.MAX_IMAGE_PIXELS = None
import glob,os


def solve(factory, method, method2, input_file):
    # Load Image
    print ("Loading Image")
    im = Image.open(input_file)
    im1 = Image.open(input_file)


    # Create the maze (and time it) - for many mazes this is more time consuming than solving the maze
    print ("Creating Maze")
    t0 = time.time()
    maze = Maze(im)
    t1 = time.time()
    print ("Node Count:", maze.count)
    total = t1-t0
    print ("Time elapsed:", total, "\n")

    # Create and run solver astar
    [title, solver] = factory.createsolver(method)
    print ("Starting Solve:", title)

    t0 = time.time()
    [result, stats] = solver(maze)
    t1 = time.time()

    total = t1-t0

    # Print solve stats
    print ("Nodes explored: ", stats[0])
    if (stats[2]):
        print ("Path found, length", stats[1])
    else:
        print ("No Path Found")
    print ("Time elapsed: ", total, "\n")

    """
    Create and save the output image.
    This is simple drawing code that travels between each node in turn, drawing either
    a horizontal or vertical line as required. Line colour is roughly interpolated between
    blue and red depending on how far down the path this section is.
    """

    print ("Saving Image")
    im = im.convert('RGB')
    impixels = im.load()

    resultpath = [n.Position for n in result]

    length = len(resultpath)

    # print("length is ", length)
    # print("resultpath is ", resultpath[0])

    for i in range(0, length - 1):
        a = resultpath[i]
        b = resultpath[i+1]

        # Blue - red
        r = int((i / length) * 255)  #'r' value changes from 0 to 255 by path length
        px = (r, 0, 255 - r)

        if a[0] == b[0]:
            # Ys equal - horizontal line
            for x in range(min(a[1],b[1]), max(a[1],b[1])):
                impixels[x,a[0]] = px
        elif a[1] == b[1]:
            # Xs equal - vertical line
            for y in range(min(a[0],b[0]), max(a[0],b[0]) + 1):
                impixels[a[1],y] = px

    # im.save(output_file.split('.')[0]+'_astar.'+output_file.split('.')[1])
    im.save('astar/'+input_file.split('\\')[1])

    # Create and run solver breadthfirst search
    [title, solver] = factory.createsolver(method2)
    print("Starting Solve:", title)

    t0 = time.time()
    [result, stats] = solver(maze)
    t1 = time.time()

    total = t1 - t0

    # Print solve stats
    print("Nodes explored: ", stats[0])
    if (stats[2]):
        print("Path found, length", stats[1])
    else:
        print("No Path Found")
    print("Time elapsed: ", total, "\n")

    """
    Create and save the output image.
    This is simple drawing code that travels between each node in turn, drawing either
    a horizontal or vertical line as required. Line colour is roughly interpolated between
    blue and red depending on how far down the path this section is.
    """

    print("Saving Image")
    im = im1.convert('RGB')
    impixels = im.load()

    resultpath = [n.Position for n in result]

    length = len(resultpath)

    for i in range(0, length - 1):
        a = resultpath[i]
        b = resultpath[i + 1]

        # Blue - red
        r = int((i / length) * 255)
        px = (r, 0, 255 - r)

        if a[0] == b[0]:
            # Ys equal - horizontal line
            for x in range(min(a[1], b[1]), max(a[1], b[1])):
                impixels[x, a[0]] = px
        elif a[1] == b[1]:
            # Xs equal - vertical line
            for y in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                impixels[a[1], y] = px

    # im.save(output_file.split('.')[0]+'_breadthfirst.'+output_file.split('.')[1])
    im.save('breadthfirst/'+input_file.split('\\')[1])


def main():
    sf = SolverFactory()
    all_files = glob.glob('examples/*.png')
    if not os.path.exists('astar'):
        os.mkdir('astar')
    if not os.path.exists('breadthfirst'):
        os.mkdir('breadthfirst')
    for input_file in all_files:
        solve(sf, 'astar','breadthfirst', input_file)

if __name__ == "__main__":
    main()

