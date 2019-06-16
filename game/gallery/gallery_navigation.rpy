# from https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=55597#p512937

screen gallery_navigation():
     
    ## Change with your image
    add "images/bg holodeck.png"

    vbox:
        style_prefix "gallery_nav"

        ## Gallery Navigation to Character A, Character B and Character C gallery.
        textbutton _("Sword") action Show("gallery_sword")

    textbutton _("Return") action [Return(), Hide("gallery_navigation")] xalign 0.97 yalign 0.95

## The position of the vertical box containing the gallery navigation buttons
style gallery_nav_vbox:
    xalign 0.03
    yalign 0.5
    spacing 40

## The position of our gallery images.
style gallery_stuff_grid:
    xalign 0.5
    yalign 0.5
    xspacing 20
    yspacing 20

## The position of the page-buttons.
style gallery_stuff_hbox:
    xalign 0.5
    yanchor 0.9
    ypos 0.95
    xspacing 10
