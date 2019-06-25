init python:
     def callback(event, interact=True, **kwargs):
        renpy.log(event)
        
        if event == "show":
            renpy.show("sword fire")
 
        elif event == "show_done":
            pass
            # renpy.show("sword aim")
        elif event == "slow_done":
            renpy.show("sword aim")
            renpy.restart_interaction()
            
define e = Character("Sword", callback=callback)
# define config.log = "D:\\r\\log.log"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg field
    show sword aim

    # These display lines of dialogue.

    e "You've created a new Ren'Py game. Once you add a story, pictures, and music, you can release it to the world! You've created a new Ren'Py game. Once you add a story, pictures, and music, you can release it to the world!"
    pause
    # This ends the game.

    return
