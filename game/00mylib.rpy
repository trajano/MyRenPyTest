init -1 python in speakers:
    from renpy.text.textsupport import TAG, TEXT
    import renpy.text.textsupport as textsupport
    import os.path
    import re
    import wave

    speakers = set()

    """
    The sound file containing the blip sound.
    """
    blip_sound = "audio/sfx-blipfemale.stereo.wav"

    blipwave = wave.open(os.path.normpath(renpy.loader.get_path(blip_sound)), "rb")
    blip_framerate = blipwave.getframerate()
    blip_frame_length = blipwave.getnframes()
    blip_channels = blipwave.getnchannels()
    blip_sample_width = blipwave.getsampwidth()
    blip_frames = blipwave.readframes(blipwave.getnframes())
    blipwave.close()

    """
    The length of the blip
    """
    blip_length = 1.0 * blip_frame_length / blip_framerate


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
                    renpy.restart_interaction()
            return the_callback

        def queue_blips(who, what, cps):
            """
            Queue the blips.  This creates a blip every other character and resets the blip when a comma or space is detected.
            If the CPS is higher frequency than the blip length, it switches to Wendy Oldbag mode where it just beeps as fast
            as it can.
            """

            def test_writable(fn):
                try:
                    open(fn, "w").close()
                    open(fn, "r").close()
                    unlink(fn)
                    return True
                except:
                    return False

            def blip_paths():
                computed_blip_file = "cache/%d.wav" % ( hash( (who, what, cps) ) )
                computed_blip_path = os.path.normpath(renpy.loader.get_path(computed_blip_file)).replace("\\", "/")
                if test_writable(computed_blip_path):
                    return (computed_blip_file, computed_blip_path)

                computed_blip_file = "%s/%d.wav" % ( renpy.config.savedir.replace("\\", "/"), hash( (who, what, cps) ) )
                computed_blip_path = os.path.normpath(renpy.loader.get_path(computed_blip_file)).replace("\\", "/")
                return (computed_blip_file, computed_blip_path)

            (computed_blip_file, computed_blip_path) = blip_paths()

            if os.path.isfile(computed_blip_path):
                renpy.sound.play(computed_blip_file)
                return

            tokens = textsupport.tokenize(unicode(what))
            odd = False

            blipout = wave.open(computed_blip_path, "wb")
            blipout.setframerate(blip_framerate)
            blipout.setsampwidth(blip_sample_width)
            blipout.setnchannels(blip_channels)

            cps_stack = []
            # initial character gap

            def silence(seconds):
                silence_byte_length = seconds *  blip_framerate * 2 * 2
                return b'\0' * int(silence_byte_length)

            def blip(seconds):
                silence_byte_length = ((seconds - blip_length) *  blip_framerate ) * 2
                return blip_frames + b'\0' * int(silence_byte_length)

            # queue.append("<silence %0.2f>" % (1.0/cps))
            blipout.writeframes(silence(1.0/cps))

            for token_type, token_text in tokens:
                if token_type == TEXT:
                    if cps > (1.0 / blip_length):
                        # Wendy Oldbag Speed at this point assume 0.05 seconds and just keep on playing until it reaches the end of the segment.
                        beeps_needed = int(len(token_text) / cps / blip_length)
                        for i in xrange(beeps_needed):
                            # queue.append("<from 0 to %0.3f>%s" % (blip_length, blip_sound))
                            blipout.writeframes(blip_frames)
                    elif cps == 0:
                        pass
                    else:
                        speed = 1.0/cps
                        for letter in token_text:
                            odd = not odd
                            if letter in ', ':
                                # queue.append("<silence %0.3f>" % speed)
                                blipout.writeframes(silence(speed))
                                odd = False
                            else:
                                if odd:
                                    # queue.append("<from 0 to %0.3f>%s" % (speed, blip_sound))
                                    blipout.writeframes(blip(speed))
                                else:
                                    # queue.append("<silence %0.3f>" % speed)
                                    blipout.writeframes(silence(speed))

                if token_type == TAG:
                    match_cps_multiplier = re.match( r'cps=\*([0-9\.]+)', token_text)
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
            blipout.close()
            renpy.log(computed_blip_path)
            renpy.sound.play(computed_blip_file)
            # renpy.sound.queue(queue, clear_queue=True, tight=True)

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
        """
        This function can be used in a ConditionSwitch to check if a character is speaking or not.
        """
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
