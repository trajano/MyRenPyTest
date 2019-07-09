define e = speakers.Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg field

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!  For now I'm going to start talking like Wendy Oldbag"

    e """
    {cps=50}So just call me \"grandma.\" It's practically my name! So even when I was young I was an Oldbag, but not really that was just my name dearie. Still how the other children would make fun of me and just because of my name can you believe it?{/cps}{nw}

    {cps=50}But there was this boy, the captain of the chess club in junior high, and whene called me an old bag well I just cried and cried because I had a crush on him you see--{/cps}
    """

    e "Objection!! {cps=*0.3}I object to this{/cps} long testimony {cps=0}(^_^;;{/cps}"

    # This ends the game.

    return
