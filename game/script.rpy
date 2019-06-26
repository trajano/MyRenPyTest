init python:
    def character_callback(character):
        def callback(event, interact=True, **kwargs):
            renpy.log(event + " " + character)
            # Attributes that are not talking
            current_attributes = [ x for x in renpy.get_attributes(character) if x != "talking" ]
            
            if event == "show":
                current = [character] + current_attributes + ["talking"]
                image = " ".join(current)
                renpy.log(image)
                renpy.show(image)
    
            elif event == "show_done":
                pass
                # renpy.show("sword aim")
            elif event == "slow_done":
                current = [character] + current_attributes
                image = " ".join(current)
                renpy.log(image)
                renpy.show(image)
                renpy.restart_interaction()
        return callback
            
define b = Character("Bo-Bo-Bo", callback=character_callback("bo"))
define d = Character("Don", callback=character_callback("don"))
define config.log = "D:\\r\\log.log"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg field
    show don with dissolve
    d "You've created a new Ren'Py game. Once you add a story, pictures, and music, you can release it to the world! You've created a new Ren'Py game. Once you add a story, pictures, and music, you can release it to the world!"
    
    show bo at left with dissolve
    b "You've created a new Ren'Py game. Once you add a story, pictures, and music, you can release it to the world! You've created a new Ren'Py game. Once you add a story, pictures, and music, you can release it to the world!"

    # These display lines of dialogue.

#    e "You've created a new Ren'Py game. Once you add a story, pictures, and music, you can release it to the world! You've created a new Ren'Py game. Once you add a story, pictures, and music, you can release it to the world!"
    pause
    # This ends the game.

    return
