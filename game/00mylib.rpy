init -1 python in speakers:
    from renpy.text.textsupport import TAG, TEXT
    import renpy.text.textsupport as textsupport
    import re

    speakers = set()

    """
    The length of the blip
    """
    blip_length = 0.05

    """
    The sound file containing the blip sound.
    """
    blip_sound = "audio/sfx-blipfemale.ogg"

    def Character(name, image=None, **kwargs):
        if image == None:
            image = name.lower()

        def character_callback(character):
            global speakers
            def the_callback(event, interact=True, **kwargs):
                if not interact:
                    return
                if event == "show":
                    speakers.add(character)
                elif event == "show_done":
                    pass
                elif event == "slow_done":
                    speakers.discard(character)
                    renpy.sound.stop()
            return the_callback

        def queue_blips(who, what, cps):
            """
            Queue the blips.  This creates a blip every other character and resets the blip when a comma or space is detected.
            If the CPS is higher frequency than the blip length, it switches to Wendy Oldbag mode where it just beeps as fast
            as it can.
            """
            tokens = textsupport.tokenize(unicode(what))
            odd = False
            queue = []
            cps_stack = []
            queue.append("<silence %0.2f>" % (1.0/cps))
            for token_type, token_text in tokens:
                if token_type == TEXT:
                    if cps > (1.0 / blip_length):
                        # Wendy Oldbag Speed at this point assume 0.05 seconds and just keep on playing until it reaches the end of the segment.
                        beeps_needed = int(len(token_text) / cps / blip_length)
                        for i in xrange(beeps_needed):
                            queue.append("<from 0 to %0.3f>%s" % (blip_length, blip_sound))

                    else:
                        speed = 1.0/cps
                        for letter in token_text:
                            odd = not odd
                            if letter in ', ':
                                queue.append("<silence %0.3f>" % speed)
                                odd = False
                            else:
                                if odd:
                                    queue.append("<from 0 to %0.3f>%s" % (speed, blip_sound))
                                else:
                                    queue.append("<silence %0.3f>" % speed)

                if token_type == TAG:
                    match_cps_multiplier = re.match( r'cps\*=([0-9\.]+)', token_text)
                    match_cps = re.match( r'cps=([0-9\.]+)', token_text)
                    match_close_cps = re.match( r'/cps', token_text)
                    if match_cps_multiplier:
                        cps_stack.append(cps)
                        cps *= float(match_cps_multiplier.group(1))
                    elif match_cps:
                        cps_stack.append(cps)
                        cps = float(match_cps.group(1))
                    elif match_close_cps:
                        cps = cps_stack.pop()
                    odd = False
            renpy.sound.queue(queue, clear_queue=True, tight=True)

        def blip_show_function(who, what, **kwargs):
            cps = renpy.game.preferences.text_cps
            if (cps > 0):
                queue_blips(who, what, cps)

            return renpy.character.show_display_say(
                who,
                what,
                **kwargs)

        return renpy.character.Character(name,
            image=image,
            callback=character_callback(image),
            show_function=blip_show_function,
            **kwargs
        )

    def MouthSwitch(character, talking_displayable, quiet_displayable):
        """
        This function creates a ConditionSwitch displayable that switches between talking and quiet characters.
        """
        return renpy.display.layout.ConditionSwitch(
            "speakers.IsSpeaking('%s')" % character, talking_displayable,
            "True",  quiet_displayable
        )

    def IsSpeaking(character):
        return character in speakers

init -1 python in animate:
    from renpy.display.layout import DynamicDisplayable

    def ImageSequence(path, start, end, pause=1.0/30.0, reverse=False, loop=True, **properties):
        frames = ["{:s}/{:04d}.png".format(path, x) for x in xrange(start, end + 1)]
        if (reverse):
            frames += ["{:s}/{:04d}.png".format(path, x) for x in reversed(xrange(start+1, end))]

        def seq(st, at, **kwargs):
            """
            This determines which frame from frames.
            :param st: The amount of time the displayable has been shown for (in seconds)
            :param at: The amount of time any displayable with the same tag has been shown for.
            :param kwargs: Any positional or keyword arguments supplied to DynamicDisplayable.
            :return: Displayable, pause
            """
            index = int(st / pause) % len(frames)
            d = frames[index]
            if index == len(frames) and not repeat:
                return d, None
            else:
                return d, pause
        return DynamicDisplayable(seq)
