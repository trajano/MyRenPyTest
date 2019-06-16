screen gallery_sword():

    default cg_page_sword = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"
        
        ## Our buttons for the pages of Character A's Gallery section.
        textbutton _("1") action SetLocalVariable("cg_page_sword", 1)
        textbutton _("2") action SetLocalVariable("cg_page_sword", 2)

    showif cg_page_sword == 1:
        grid 2 2:
            style_prefix "gallery_stuff"
            
            ## Replace one null with one button created according to this structure:
            ## add g.make_button("CG_Button_Name", "path/Unlocked_Thumbnail.png", "path/Locked_Thumbnail.png")
            add g.make_button("sword", "sword thumbnail")
            add g.make_button("sword", "sword thumbnail")
            null
            null

    elif cg_page_sword == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            ## Replace one null with one button created according to this structure:
            ## add g.make_button("CG_Button_Name", "path/Unlocked_Thumbnail.png", "path/Locked_Thumbnail.png")
            null
            null
            null
            null
