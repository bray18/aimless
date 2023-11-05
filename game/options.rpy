## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("aimless")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.1"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""

*********** CREDITS ***********

Developed By:

    - Brady Walters and 1000mg of caffiene
            (Programmer)

    - Casey Bach and peace and love
            (Programmer, Writer)

    - Sun Anderson and an illegal amount of milk duds
            (Illustrator - Sprites/Assets/Logo/Backgrounds, Writer, Programmer)

    - Hailey Donald and pure spite and sleep deprivation <3
            (Illustrator - Backgrounds/Misc, Editor/Assistant)



GitHub Copilot used for code repitition and logic assistance

Music by Steven Bach used under royalty free CC liscense (https://www.youtube.com/watch?v=YcWhrIWyjZE)



Stock images from Adobe Stock:
    - Two cows on a rainy day By Ruud Morijn
    - Golden Retriever dog enjoying outdoors at a large grass field at sunset, beautiful golden light By Tanya
    - Modern laptop By blackday
    - House surrounded by green spaces and plants. Apartment building with many windows for pixel game. Panorama architecture. Layout of mobile app, computer pixelated game. Old architectural construction By robu_s
    - bearded man looks around in the city street. By APHOTOSTUDIO
    - Young hispanic man smiling happy standing at the city. By Krakenimages.com
    


AI cows from The Wall Street Journal (https://www.wsj.com/articles/attempting-to-code-the-human-brain-1391473543)

DALL·E mini by craiyon.com

DALL·E 2 by OpenAI

Bing Image Creator by Microsoft powered by DALL·E 3 by OpenAI

ChatGPT by OpenAI

Bing AI chat for coding timer. "I spent so damn long on this stupid QTE timer" -Brady




*********** TESTIMONIALS ***********

Creating this game was a journey but it was a fun and rewarding experience that I am *sure* I can say we all experienced.
I personally enjoyed working with such an amazing team that I have had so much fun working with to make a game, not only now but
previously as well.  It was also so fun to be able to bounce from illustration, to programming, to editing and so much more.  It surely is
an experience that cannot be replicated in many other situations.  I hold my teammembers in such high regard as they are truly some
of the most hardworking, kind, silly, and determined people I could have ever hoped to have worked with.  No matter if it is Brady
trudging through code trying to trouble shoot an idea that this language will not support, or Casey and how they are always finding
all of the peices that have been left behind and fixinT them up to make a truly beautiful and fun experience, or Sun who always had
such an energetic personality annd was always excited for the next step.  hough this experience was draining and I have not slept
for 48 hours as of when I'm writing this, I truly enjoyed this and have absolutely no regrets for being a part of this.  10/10 will
call in sick to work again.

Also honorable mention to my Bluey pillowpet.  10/10 emotional support.

    - Hailey Donald


I always thought my dream of being a game developer would be unreachable. But this team always seems to prove me wrong.
I would only be able to make half the stuff I do today with the help of the people who have been trapped with me for the last 38 hours.
Doing something this quickly and under this much pressure is always draining. But since we focused more on the joy our project gave us it help us push through.
I know the people on my team are going to do great things no matter where they are in the world. 10/10 would work with these weirdos again.

    - Sun Anderson

""")

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "aimless"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 100


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "aimless-1699069014"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

define config.layers = [ 'master', 'transient', 'new_overlay', 'screens' ]
define config.rollback_enabled = False