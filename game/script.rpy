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

    "{cps=0}mr narrator should not blip{/cps}"

    "{cps=0}Going to play an mp3 file{/cps}"

    play sound "audio/sfx-blipfemale.mp3"

    "{cps=0}Works for me.  Going to play an mono wav file{/cps}"

    play sound "audio/sfx-blipfemale.wav"

    "{cps=0}Didn't work for me.  Going to play a stereo wav file{/cps}"

    play sound "audio/sfx-blipfemale.stereo.wav"
    
    "{cps=0}Works for me.  Going to play a stereo wav file using renpysound{/cps}"
    $ renpy.audio.renpysound.play( renpy.audio.audio.get_channel("music").number, renpy.file("audio/sfx-blipfemale.stereo.wav"), "audio/sfx-blipfemale.stereo.wav", tight=True, end=-1)

    "{cps=0}Works for me on the PC.  Going to play an OGG file{/cps}"

    play sound "audio/sfx-blipfemale.ogg"

    "{cps=0}Works for me{/cps}"

    show eileen

    e "testing again"

    e "{cps=2}TeStInG.{/cps}"
    e "{cps=2}TeStInG{/cps}"
    e '{cps=50}renpy.audio.renpysound.play( renpy.audio.audio.get_channel("music").number, renpy.file("audio/sfx-blipfemale.stereo.wav"), "audio/sfx-blipfemale.stereo.wav", tight=True, end=-1){/cps}'

    e "TeStInG AgAiN"

    return
