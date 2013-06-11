# InteractiveMinecraft for Minecraft: Pi Edition
# Graham Laming, www.grahamlaming.co.uk

from minecraft import Minecraft
from vec3 import Vec3

def copy():
    """Copies and places a structure based on right clicks with the sword.
       Terminal interaction guides the user through this process.

       Copying works by the user selecting the extremities of a structure,
       thereby creating a bounding box; the contents of which is then copied -
       including the 'air' blocks.
    """
    
    mc.events.clearAll() # Clear all hit-events before starting
    raw_input("Right click the extremities of the object you wish to copy in " +
        "the Minecraft world with your sword, then press ENTER.")
    hits = mc.events.pollBlockHits()
    if len(hits) < 2:
        print("More than 1 block needs to be selected!")
        return

    # Work out the bounding box from the right-clicks. Initialise the minimum
    # and maximum values of the bounding box to be one of the clicks for
    # comparison purposes.
    
    hit = hits.pop()
    v = hit.pos # A vector of (x,y,z) co-ords for the clicked block
    minx = v.x
    maxx = v.x
    miny = v.y
    maxy = v.y
    minz = v.z
    maxz = v.z
    
    while len(hits) > 0:
        hit = hits.pop()
        v = hit.pos
        minx = min(minx, v.x)
        maxx = max(maxx, v.x)
        miny = min(miny, v.y)
        maxy = max(maxy, v.y)
        minz = min(minz, v.z)
        maxz = max(maxz, v.z)

    # Get the contents of the bounding box and store as a list of tuples; the
    # first element of a tuple being a postion vector, the second being the
    # block ID number.

    structure = []
    for x in range(minx, maxx+1):
        for y in range(miny, maxy+1):
            for z in range(minz, maxz+1):
               structure.append((Vec3(x,y,z),mc.getBlock(x,y,z)))

    # Count the number of non-air blocks copied.

    count = 0
    for block in structure:
        if block[1] != 0:
            count += 1

    # Have the user chose where to place the copied structure.

    mc.events.clearAll()
    raw_input("Structure with " + repr(count) + " non-air blocks has been " +
        "copied. Right click the block on which to place the copied" +
        "structure with your sword and then press ENTER.")
    hits = mc.events.pollBlockHits()
    if len(hits) == 0:
        print("A location needs to be selected")
        return
    hit = hits.pop()
    v = hit.pos

    # Place the structure at the chosen location. The position is calculated by
    # taking a block's orginal location, subtracting the minimum position
    # vector of the bounding box and adding the position vector of the chosen
    # location.

    for block in structure:
        pos = block[0] - Vec3(minx, miny, minz) + Vec3(v.x, v.y+1, v.z)
        mc.setBlock(pos, block[1])
    
              
if __name__ == "__main__":
    mc = Minecraft.create()
    mc.postToChat("InteractiveMinecraft working!")
    
    flag = True
    while flag:
        x = raw_input("Enter your command or type 'help' " + 
            "to see a list of available commands.\n:> ")
        if x.lower() == "copy":
            copy()
        elif x.lower() == "quit":
            flag = False
        elif x.lower() == "help":
            print "Todo!"


