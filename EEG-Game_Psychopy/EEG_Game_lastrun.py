#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on April 05, 2024, at 12:41
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
#Set number of repetitions  for each test
global_rep_num = 1
rep_num1 = global_rep_num
rep_num2 = global_rep_num
rep_num3 = global_rep_num
rep_num4 = global_rep_num

#Set number of trials for each test
global_trial_num = 2
trial_num1 = global_trial_num
trial_num2 = global_trial_num
trial_num3 = global_trial_num
trial_num4 = global_trial_num

#Set duration of repetitions for each test
global_dur_test = 5
dur_test1 = global_dur_test
dur_test2 = global_dur_test
dur_test3 = global_dur_test
dur_test4 = global_dur_test

#Size/position of display objects including ship, target boxes and backgrounds
ship_size = (0.15, 0.15)
box_size = (0.15, 0.075)
game_back_size = (1.75, 1)
game_back_pos = (-0.1, 0)
home_back_size = (1.5, 1.2)
warning_back_size = (1.5, 1) #Current window size
gameDet_back_size = (1.5, 1)
pickTest_back_size = (1.5, 1)
about_back_size = (1.5, 1)

#Duration after a repetition
dur_blank = 2

#Duration of win/lose screens
dur_end = 3

#Intialize all buttons to False
return_home = True
about_exp_button = False
start_exp_button = False
buttont1 = False
buttont2 = False
buttont3 = False
buttont4 = False
lose = False

#Update display to show target object
def selectTarget(objects, target):
    for i in range(len(objects)):
        if i == (target - 1):
            objects[i].lineColor = 'red'
        else:
            objects[i].lineColor = 'white'

# Update opacities based on current frame number for each stimulus
def flickerObjects(objects, freqs, frameN):
    for i in range(len(objects)): #loop through all objects
        frames_per_cycle = 60 // freqs[i]
        objects[i].opacity = (((frameN) % frames_per_cycle) < (frames_per_cycle / 2))
        
#Check if frequency is correct range     
def compareFreq(EEGdata, freq):
    DELTA = 0
    THETA = 1
    ALPHA = 2
    BETA = 3
    GAMMA = 4
    
    freq_band = EEGdata.index(max(EEGdata))
    
    if (freq_band == DELTA) and (0 <= freq < 4):
        return True 
    elif (freq_band == THETA) and (4 <= freq < 8):
        return True 
    elif (freq_band == ALPHA) and (8 <= freq < 12):
        return True 
    elif (freq_band == BETA) and (12 <= freq < 30):
        return True
    elif (freq_band == GAMMA) and (freq >= 30):
        return True
    else:
        return False
     
# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'Test1'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\evanl\\Downloads\\SYP-GambitGameDev-main (2)\\SYP-GambitGameDev-main\\EEG-Game_Psychopy\\EEG_Game_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[900, 600], fullscr=False, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0.0000, 0.0000, 0.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0.0000, 0.0000, 0.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = True
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "GlobalFunctions" ---
    
    # --- Initialize components for Routine "WelcomeScreen" ---
    homepage_image = visual.ImageStim(
        win=win,
        name='homepage_image', 
        image='homepage_1.webp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=home_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    about_button = visual.ButtonStim(win, 
        text='Click here to learn more ', font='Arvo',
        pos=(-0.5, -0.4),
        letterHeight=0.03,
        size=(0.5, 0.09), borderWidth=0.0,
        fillColor=[-1.0000, -1.0000, -1.0000], borderColor=None,
        color=[1.0000, -0.4588, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='about_button',
        depth=-1
    )
    about_button.buttonClock = core.Clock()
    start_button = visual.ButtonStim(win, 
        text='Click here to start game', font='Arvo',
        pos=(0.5, -0.4),
        letterHeight=0.03,
        size=(0.5, 0.08), borderWidth=0.0,
        fillColor=[-1.0000, -1.0000, -1.0000], borderColor=None,
        color=[1.0000, -0.4588, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='start_button',
        depth=-2
    )
    start_button.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "instructionprep" ---
    # Run 'Begin Experiment' code from code_2
    cur_row = 0
    button_pressed = "none"
    show_instructions = 1
    max_slides = 6
    
    # --- Initialize components for Routine "AboutExpScreen" ---
    image_instruction = visual.ImageStim(
        win=win,
        name='image_instruction', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=about_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    next_button = visual.ButtonStim(win, 
        text='Next >>', font='Arvo',
        pos=(0.5, -0.4),
        letterHeight=0.03,
        size=(0.2, 0.08), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='next_button',
        depth=-1
    )
    next_button.buttonClock = core.Clock()
    back_button = visual.ButtonStim(win, 
        text='<< Back', font='Arvo',
        pos=(-0.5, -0.4),
        letterHeight=0.03,
        size=(0.2, 0.08), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='back_button',
        depth=-2
    )
    back_button.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "WarningScreen" ---
    white_background = visual.ImageStim(
        win=win,
        name='white_background', 
        image='white_background.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=warning_back_size,
        color=[0.6549, 0.6549, 0.6549], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    welcome_message = visual.TextStim(win=win, name='welcome_message',
        text='',
        font='Garamond',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    caution_sign = visual.ImageStim(
        win=win,
        name='caution_sign', 
        image='warning_sign.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0.4), size=(0.3, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    button = visual.ButtonStim(win, 
        text='Click here to proceed', font='Arvo',
        pos=(0, -0.30),
        letterHeight=0.03,
        size=(0.25, 0.125), borderWidth=2.0,
        fillColor=[1.0000, 0.9500, -1.0000], borderColor=[-1.0000, -1.0000, -1.0000],
        color='black', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button',
        depth=-3
    )
    button.buttonClock = core.Clock()
    warning_heading = visual.TextStim(win=win, name='warning_heading',
        text='WARNING',
        font='Open Sans',
        pos=(0, 0.3), height=0.09, wrapWidth=None, ori=0.0, 
        color=[0.0902, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "GameDet" ---
    MindBattle = visual.ImageStim(
        win=win,
        name='MindBattle', 
        image='alien_invasion.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=gameDet_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    explanation = visual.TextStim(win=win, name='explanation',
        text="Aliens are attacking Earth and it's up to you to stop them. Using the power of your mind focus on the RED outlined spaceship to stop its attack. Fail to focus on the target and the aliens will win.",
        font='Open Sans',
        pos=(0, 0.33), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Skip = visual.ButtonStim(win, 
        text='Skip', font='Arvo',
        pos=(0, -0.3),
        letterHeight=0.04,
        size=(0.2, 0.1), borderWidth=2.0,
        fillColor=[-1.0000, -1.0000, -1.0000], borderColor=[1.0000, 1.0000, 1.0000],
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='Skip',
        depth=-2
    )
    Skip.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "PickTest" ---
    brain_animation = visual.MovieStim(
        win, name='brain_animation',
        filename='brain_animation.mp4', movieLib='ffpyplayer',
        loop=True, volume=1.0, noAudio=False,
        pos=(0, 0), size=pickTest_back_size, units=win.units,
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=0
    )
    button_t1 = visual.ButtonStim(win, 
        text='Level 1', font='Arvo',
        pos=(-0.25, 0.25),
        letterHeight=0.04,
        size=(0.2, 0.2), borderWidth=2.0,
        fillColor=[-0.1686, -0.2941, 0.6078], borderColor=[0.0902, -1.0000, 0.0902],
        color='black', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_t1',
        depth=-1
    )
    button_t1.buttonClock = core.Clock()
    button_t2 = visual.ButtonStim(win, 
        text='Level 2', font='Arvo',
        pos=(0.25, 0.25),
        letterHeight=0.04,
        size=(0.2, 0.2), borderWidth=2.0,
        fillColor=[-0.1686, -0.2941, 0.6078], borderColor=[0.0902, -1.0000, 0.0902],
        color='black', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_t2',
        depth=-2
    )
    button_t2.buttonClock = core.Clock()
    button_t3 = visual.ButtonStim(win, 
        text='Level 3', font='Arvo',
        pos=(-0.25, -0.25),
        letterHeight=0.04,
        size=(0.2, 0.2), borderWidth=2.0,
        fillColor=[-0.1686, -0.2941, 0.6078], borderColor=[0.0902, -1.0000, 0.0902],
        color='black', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_t3',
        depth=-3
    )
    button_t3.buttonClock = core.Clock()
    button_t4 = visual.ButtonStim(win, 
        text='Level 4', font='Arvo',
        pos=(0.25, -0.25),
        letterHeight=0.04,
        size=(0.2, 0.2), borderWidth=2.0,
        fillColor=[-0.1686, -0.2941, 0.6078], borderColor=[0.0902, -1.0000, 0.0902],
        color='black', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_t4',
        depth=-4
    )
    button_t4.buttonClock = core.Clock()
    button_all = visual.ButtonStim(win, 
        text='All', font='Arvo',
        pos=(0, 0),
        letterHeight=0.038,
        size=(0.2, 0.2), borderWidth=2.0,
        fillColor=[0.0902, -1.0000, 0.0902], borderColor=[-0.1686, -0.2941, 0.6078],
        color='black', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_all',
        depth=-5
    )
    button_all.buttonClock = core.Clock()
    text = visual.TextStim(win=win, name='text',
        text='Choose a level',
        font='Open Sans ',
        pos=(0, 0.43), height=0.06, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    
    # --- Initialize components for Routine "test_1" ---
    earth1 = visual.ImageStim(
        win=win,
        name='earth1', 
        image='earth.jpeg', mask=None, anchor='center',
        ori=0.0, pos=game_back_pos, size=game_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    boxL1_1 = visual.Rect(
        win=win, name='boxL1_1',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.35, 0), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-1.0, interpolate=True)
    shipL1_1 = visual.ImageStim(
        win=win,
        name='shipL1_1', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.35, 0), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Attack_message = visual.TextStim(win=win, name='Attack_message',
        text='Focus on the attacking RED alien ship to stop it!!!',
        font='Open Sans',
        pos=(0, 0.45), height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    test_1_mess = visual.TextStim(win=win, name='test_1_mess',
        text=None,
        font='Open Sans',
        pos=(0, 0.4), height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "earth_pause_1" ---
    earth_blank_4 = visual.ImageStim(
        win=win,
        name='earth_blank_4', 
        image='earth.jpeg', mask=None, anchor='center',
        ori=0.0, pos=game_back_pos, size=game_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    continue_playing_message_4 = visual.TextStim(win=win, name='continue_playing_message_4',
        text='Good job but another wave of aliens are coming!',
        font='Open Sans',
        pos=(0, 0.45), height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "before_test2" ---
    earth_blank_5 = visual.ImageStim(
        win=win,
        name='earth_blank_5', 
        image='earth.jpeg', mask=None, anchor='center',
        ori=0.0, pos=game_back_pos, size=game_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    continue_playing_message_5 = visual.TextStim(win=win, name='continue_playing_message_5',
        text='3 more spaceships are coming get ready!',
        font='Open Sans',
        pos=(0, 0.45), height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "test_2" ---
    earth2 = visual.ImageStim(
        win=win,
        name='earth2', 
        image='earth.jpeg', mask=None, anchor='center',
        ori=0.0, pos=game_back_pos, size=game_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    boxL2_1 = visual.Rect(
        win=win, name='boxL2_1',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.1, 0), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-1.0, interpolate=True)
    shipL2_1 = visual.ImageStim(
        win=win,
        name='shipL2_1', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.1, 0), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    boxL2_2 = visual.Rect(
        win=win, name='boxL2_2',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.35, 0), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-3.0, interpolate=True)
    shipL2_2 = visual.ImageStim(
        win=win,
        name='shipL2_2', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.35, 0), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    boxL2_3 = visual.Rect(
        win=win, name='boxL2_3',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.6, 0), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-5.0, interpolate=True)
    shipL2_3 = visual.ImageStim(
        win=win,
        name='shipL2_3', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    Attack_message2 = visual.TextStim(win=win, name='Attack_message2',
        text='Focus on the attacking RED alien ship to stop it!!!',
        font='Open Sans',
        pos=(0, 0.45), height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    test_2_mess = visual.TextStim(win=win, name='test_2_mess',
        text=None,
        font='Open Sans',
        pos=(0, 0.4), height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    
    # --- Initialize components for Routine "earth_pause_2" ---
    earth_blank_3 = visual.ImageStim(
        win=win,
        name='earth_blank_3', 
        image='earth.jpeg', mask=None, anchor='center',
        ori=0.0, pos=game_back_pos, size=game_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    continue_playing_message_3 = visual.TextStim(win=win, name='continue_playing_message_3',
        text='Good job but another wave of aliens are coming!',
        font='Open Sans',
        pos=(0, 0.45), height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "before_test3" ---
    earth_blank_6 = visual.ImageStim(
        win=win,
        name='earth_blank_6', 
        image='earth.jpeg', mask=None, anchor='center',
        ori=0.0, pos=game_back_pos, size=game_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    continue_playing_message_6 = visual.TextStim(win=win, name='continue_playing_message_6',
        text='4 more spaceships are coming get ready!',
        font='Open Sans',
        pos=(0, 0.45), height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "test_3" ---
    earth3 = visual.ImageStim(
        win=win,
        name='earth3', 
        image='earth.jpeg', mask=None, anchor='center',
        ori=0.0, pos=game_back_pos, size=game_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    boxL3_1 = visual.Rect(
        win=win, name='boxL3_1',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.1, 0.25), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-1.0, interpolate=True)
    shipL3_1 = visual.ImageStim(
        win=win,
        name='shipL3_1', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.1, 0.25), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    boxL3_2 = visual.Rect(
        win=win, name='boxL3_2',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.6, 0.25), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-3.0, interpolate=True)
    shipL3_2 = visual.ImageStim(
        win=win,
        name='shipL3_2', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0.25), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    boxL3_3 = visual.Rect(
        win=win, name='boxL3_3',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.1, -0.25), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-5.0, interpolate=True)
    shipL3_3 = visual.ImageStim(
        win=win,
        name='shipL3_3', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.1, -0.25), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    boxL3_4 = visual.Rect(
        win=win, name='boxL3_4',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.6, -0.25), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-7.0, interpolate=True)
    shipL3_4 = visual.ImageStim(
        win=win,
        name='shipL3_4', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.6, -0.25), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    Attack_message3 = visual.TextStim(win=win, name='Attack_message3',
        text='Focus on the attacking RED alien ship to stop it!!!',
        font='Open Sans',
        pos=(0, 0.45), height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    test_3_mess = visual.TextStim(win=win, name='test_3_mess',
        text=None,
        font='Open Sans',
        pos=(0, 0.4), height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-10.0);
    
    # --- Initialize components for Routine "earth_pause_3" ---
    earth_blank_2 = visual.ImageStim(
        win=win,
        name='earth_blank_2', 
        image='earth.jpeg', mask=None, anchor='center',
        ori=0.0, pos=game_back_pos, size=game_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    continue_playing_message_2 = visual.TextStim(win=win, name='continue_playing_message_2',
        text='Good job but another wave of aliens are coming!',
        font='Open Sans',
        pos=(0, 0.45), height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "before_test4" ---
    earth_blank_7 = visual.ImageStim(
        win=win,
        name='earth_blank_7', 
        image='earth.jpeg', mask=None, anchor='center',
        ori=0.0, pos=game_back_pos, size=game_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    continue_playing_message_7 = visual.TextStim(win=win, name='continue_playing_message_7',
        text='ALL the remaining spaceships are coming get ready!',
        font='Open Sans',
        pos=(0, 0.45), height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "test_4" ---
    earth4 = visual.ImageStim(
        win=win,
        name='earth4', 
        image='earth.jpeg', mask=None, anchor='center',
        ori=0.0, pos=game_back_pos, size=game_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    boxL4_1 = visual.Rect(
        win=win, name='boxL4_1',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.1, 0.25), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-1.0, interpolate=True)
    shipL4_1 = visual.ImageStim(
        win=win,
        name='shipL4_1', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.1, 0.25), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    boxL4_2 = visual.Rect(
        win=win, name='boxL4_2',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.35, 0.25), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-3.0, interpolate=True)
    shipL4_2 = visual.ImageStim(
        win=win,
        name='shipL4_2', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.35, 0.25), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    boxL4_3 = visual.Rect(
        win=win, name='boxL4_3',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.6, 0.25), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-5.0, interpolate=True)
    shipL4_3 = visual.ImageStim(
        win=win,
        name='shipL4_3', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0.25), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    boxL4_4 = visual.Rect(
        win=win, name='boxL4_4',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.1, 0), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-7.0, interpolate=True)
    shipL4_4 = visual.ImageStim(
        win=win,
        name='shipL4_4', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.1, 0), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    boxL4_5 = visual.Rect(
        win=win, name='boxL4_5',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.35, 0), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-9.0, interpolate=True)
    shipL4_5 = visual.ImageStim(
        win=win,
        name='shipL4_5', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.35, 0), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-10.0)
    boxL4_6 = visual.Rect(
        win=win, name='boxL4_6',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.6, 0), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-11.0, interpolate=True)
    shipL4_6 = visual.ImageStim(
        win=win,
        name='shipL4_6', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-12.0)
    boxL4_7 = visual.Rect(
        win=win, name='boxL4_7',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.1, -0.25), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-13.0, interpolate=True)
    shipL4_7 = visual.ImageStim(
        win=win,
        name='shipL4_7', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.1, -0.25), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-14.0)
    boxL4_8 = visual.Rect(
        win=win, name='boxL4_8',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.35, -0.25), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-15.0, interpolate=True)
    shipL4_8 = visual.ImageStim(
        win=win,
        name='shipL4_8', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.35, -0.25), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-16.0)
    boxL4_9 = visual.Rect(
        win=win, name='boxL4_9',
        width=box_size[0], height=box_size[1],
        ori=0.0, pos=(0.6, -0.25), anchor='center',
        lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=None,
        opacity=None, depth=-17.0, interpolate=True)
    shipL4_9 = visual.ImageStim(
        win=win,
        name='shipL4_9', 
        image='spaceship.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.6, -0.25), size=ship_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-18.0)
    Attack_message4 = visual.TextStim(win=win, name='Attack_message4',
        text='Focus on the attacking RED alien ship to stop it!!!',
        font='Open Sans',
        pos=(0, 0.45), height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-19.0);
    test_4_mess = visual.TextStim(win=win, name='test_4_mess',
        text=None,
        font='Open Sans',
        pos=(0, 0.4), height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-20.0);
    
    # --- Initialize components for Routine "earth_pause_4" ---
    earth_blank = visual.ImageStim(
        win=win,
        name='earth_blank', 
        image='earth.jpeg', mask=None, anchor='center',
        ori=0.0, pos=game_back_pos, size=game_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    continue_playing_message = visual.TextStim(win=win, name='continue_playing_message',
        text='Good job but another wave of aliens are coming!',
        font='Open Sans',
        pos=(0, 0.45), height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "earth_win" ---
    earth_win_2 = visual.ImageStim(
        win=win,
        name='earth_win_2', 
        image='earth_win.jpeg', mask=None, anchor='center',
        ori=0.0, pos=game_back_pos, size=game_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    win_message = visual.TextStim(win=win, name='win_message',
        text='YOU WIN!!! You saved Earth from aliens!!!',
        font='Open Sans',
        pos=(0, 0.45), height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "earth_lose" ---
    earth_lose_2 = visual.ImageStim(
        win=win,
        name='earth_lose_2', 
        image='Earth_lost.jpeg', mask=None, anchor='center',
        ori=0.0, pos=game_back_pos, size=game_back_size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    lose_message = visual.TextStim(win=win, name='lose_message',
        text='YOU LOSE!!! Aliens destroyed Earth!!!\nYou did not focus on the correct spaceship',
        font='Open Sans',
        pos=(0, 0.45), height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "reset_buttons" ---
    
    # --- Initialize components for Routine "GoodBye" ---
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "GlobalFunctions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('GlobalFunctions.started', globalClock.getTime())
    # keep track of which components have finished
    GlobalFunctionsComponents = []
    for thisComponent in GlobalFunctionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "GlobalFunctions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GlobalFunctionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "GlobalFunctions" ---
    for thisComponent in GlobalFunctionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('GlobalFunctions.stopped', globalClock.getTime())
    # the Routine "GlobalFunctions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "WelcomeScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('WelcomeScreen.started', globalClock.getTime())
    # reset about_button to account for continued clicks & clear times on/off
    about_button.reset()
    # reset start_button to account for continued clicks & clear times on/off
    start_button.reset()
    # keep track of which components have finished
    WelcomeScreenComponents = [homepage_image, about_button, start_button]
    for thisComponent in WelcomeScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "WelcomeScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *homepage_image* updates
        
        # if homepage_image is starting this frame...
        if homepage_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            homepage_image.frameNStart = frameN  # exact frame index
            homepage_image.tStart = t  # local t and not account for scr refresh
            homepage_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(homepage_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'homepage_image.started')
            # update status
            homepage_image.status = STARTED
            homepage_image.setAutoDraw(True)
        
        # if homepage_image is active this frame...
        if homepage_image.status == STARTED:
            # update params
            pass
        # *about_button* updates
        
        # if about_button is starting this frame...
        if about_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            about_button.frameNStart = frameN  # exact frame index
            about_button.tStart = t  # local t and not account for scr refresh
            about_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(about_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'about_button.started')
            # update status
            about_button.status = STARTED
            about_button.setAutoDraw(True)
        
        # if about_button is active this frame...
        if about_button.status == STARTED:
            # update params
            pass
            # check whether about_button has been pressed
            if about_button.isClicked:
                if not about_button.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    about_button.timesOn.append(about_button.buttonClock.getTime())
                    about_button.timesOff.append(about_button.buttonClock.getTime())
                elif len(about_button.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    about_button.timesOff[-1] = about_button.buttonClock.getTime()
                if not about_button.wasClicked:
                    # end routine when about_button is clicked
                    continueRoutine = False
                if not about_button.wasClicked:
                    # run callback code when about_button is clicked
                    global about_exp_button
                    about_exp_button = True
        # take note of whether about_button was clicked, so that next frame we know if clicks are new
        about_button.wasClicked = about_button.isClicked and about_button.status == STARTED
        # *start_button* updates
        
        # if start_button is starting this frame...
        if start_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            start_button.frameNStart = frameN  # exact frame index
            start_button.tStart = t  # local t and not account for scr refresh
            start_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'start_button.started')
            # update status
            start_button.status = STARTED
            start_button.setAutoDraw(True)
        
        # if start_button is active this frame...
        if start_button.status == STARTED:
            # update params
            pass
            # check whether start_button has been pressed
            if start_button.isClicked:
                if not start_button.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    start_button.timesOn.append(start_button.buttonClock.getTime())
                    start_button.timesOff.append(start_button.buttonClock.getTime())
                elif len(start_button.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    start_button.timesOff[-1] = start_button.buttonClock.getTime()
                if not start_button.wasClicked:
                    # end routine when start_button is clicked
                    continueRoutine = False
                if not start_button.wasClicked:
                    # run callback code when start_button is clicked
                    global start_exp_button
                    start_exp_button = True
        # take note of whether start_button was clicked, so that next frame we know if clicks are new
        start_button.wasClicked = start_button.isClicked and start_button.status == STARTED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WelcomeScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "WelcomeScreen" ---
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('WelcomeScreen.stopped', globalClock.getTime())
    thisExp.addData('about_button.numClicks', about_button.numClicks)
    if about_button.numClicks:
       thisExp.addData('about_button.timesOn', about_button.timesOn)
       thisExp.addData('about_button.timesOff', about_button.timesOff)
    else:
       thisExp.addData('about_button.timesOn', "")
       thisExp.addData('about_button.timesOff', "")
    thisExp.addData('start_button.numClicks', start_button.numClicks)
    if start_button.numClicks:
       thisExp.addData('start_button.timesOn', start_button.timesOn)
       thisExp.addData('start_button.timesOff', start_button.timesOff)
    else:
       thisExp.addData('start_button.timesOn', "")
       thisExp.addData('start_button.timesOff', "")
    # the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    instructions_controller = data.TrialHandler(nReps=9999.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='instructions_controller')
    thisExp.addLoop(instructions_controller)  # add the loop to the experiment
    thisInstructions_controller = instructions_controller.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstructions_controller.rgb)
    if thisInstructions_controller != None:
        for paramName in thisInstructions_controller:
            globals()[paramName] = thisInstructions_controller[paramName]
    
    for thisInstructions_controller in instructions_controller:
        currentLoop = instructions_controller
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisInstructions_controller.rgb)
        if thisInstructions_controller != None:
            for paramName in thisInstructions_controller:
                globals()[paramName] = thisInstructions_controller[paramName]
        
        # --- Prepare to start Routine "instructionprep" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('instructionprep.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_2
        if (about_exp_button == False) :
            instructions_controller.finished = 1
            show_instructions = 0
            cur_row = max_slides
        if(button_pressed == "next"):
            cur_row += 1 
         
        elif (button_pressed == "back"):
            cur_row -= 1 
        button_pressed = "none"
        
        if (cur_row < 0) :
            cur_row = 0 
         
        if (cur_row > max_slides) :
            instructions_controller.finished = 1
            show_instructions = 0
            cur_row = max_slides
            
                
        # keep track of which components have finished
        instructionprepComponents = []
        for thisComponent in instructionprepComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "instructionprep" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instructionprepComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "instructionprep" ---
        for thisComponent in instructionprepComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('instructionprep.stopped', globalClock.getTime())
        # the Routine "instructionprep" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        about_slide_loop = data.TrialHandler(nReps=show_instructions, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('slide_order.xlsx', selection=str(cur_row)),
            seed=None, name='about_slide_loop')
        thisExp.addLoop(about_slide_loop)  # add the loop to the experiment
        thisAbout_slide_loop = about_slide_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAbout_slide_loop.rgb)
        if thisAbout_slide_loop != None:
            for paramName in thisAbout_slide_loop:
                globals()[paramName] = thisAbout_slide_loop[paramName]
        
        for thisAbout_slide_loop in about_slide_loop:
            currentLoop = about_slide_loop
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisAbout_slide_loop.rgb)
            if thisAbout_slide_loop != None:
                for paramName in thisAbout_slide_loop:
                    globals()[paramName] = thisAbout_slide_loop[paramName]
            
            # --- Prepare to start Routine "AboutExpScreen" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('AboutExpScreen.started', globalClock.getTime())
            image_instruction.setImage(about_slide)
            # reset next_button to account for continued clicks & clear times on/off
            next_button.reset()
            # reset back_button to account for continued clicks & clear times on/off
            back_button.reset()
            # keep track of which components have finished
            AboutExpScreenComponents = [image_instruction, next_button, back_button]
            for thisComponent in AboutExpScreenComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "AboutExpScreen" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_instruction* updates
                
                # if image_instruction is starting this frame...
                if image_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_instruction.frameNStart = frameN  # exact frame index
                    image_instruction.tStart = t  # local t and not account for scr refresh
                    image_instruction.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_instruction, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_instruction.started')
                    # update status
                    image_instruction.status = STARTED
                    image_instruction.setAutoDraw(True)
                
                # if image_instruction is active this frame...
                if image_instruction.status == STARTED:
                    # update params
                    pass
                # *next_button* updates
                
                # if next_button is starting this frame...
                if next_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    next_button.frameNStart = frameN  # exact frame index
                    next_button.tStart = t  # local t and not account for scr refresh
                    next_button.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(next_button, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'next_button.started')
                    # update status
                    next_button.status = STARTED
                    next_button.setAutoDraw(True)
                
                # if next_button is active this frame...
                if next_button.status == STARTED:
                    # update params
                    pass
                    # check whether next_button has been pressed
                    if next_button.isClicked:
                        if not next_button.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            next_button.timesOn.append(next_button.buttonClock.getTime())
                            next_button.timesOff.append(next_button.buttonClock.getTime())
                        elif len(next_button.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            next_button.timesOff[-1] = next_button.buttonClock.getTime()
                        if not next_button.wasClicked:
                            # end routine when next_button is clicked
                            continueRoutine = False
                        if not next_button.wasClicked:
                            # run callback code when next_button is clicked
                            button_pressed = "next"
                # take note of whether next_button was clicked, so that next frame we know if clicks are new
                next_button.wasClicked = next_button.isClicked and next_button.status == STARTED
                # *back_button* updates
                
                # if back_button is starting this frame...
                if back_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    back_button.frameNStart = frameN  # exact frame index
                    back_button.tStart = t  # local t and not account for scr refresh
                    back_button.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(back_button, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'back_button.started')
                    # update status
                    back_button.status = STARTED
                    back_button.setAutoDraw(True)
                
                # if back_button is active this frame...
                if back_button.status == STARTED:
                    # update params
                    pass
                    # check whether back_button has been pressed
                    if back_button.isClicked:
                        if not back_button.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            back_button.timesOn.append(back_button.buttonClock.getTime())
                            back_button.timesOff.append(back_button.buttonClock.getTime())
                        elif len(back_button.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            back_button.timesOff[-1] = back_button.buttonClock.getTime()
                        if not back_button.wasClicked:
                            # end routine when back_button is clicked
                            continueRoutine = False
                        if not back_button.wasClicked:
                            # run callback code when back_button is clicked
                            button_pressed = "back"
                # take note of whether back_button was clicked, so that next frame we know if clicks are new
                back_button.wasClicked = back_button.isClicked and back_button.status == STARTED
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AboutExpScreenComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "AboutExpScreen" ---
            for thisComponent in AboutExpScreenComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('AboutExpScreen.stopped', globalClock.getTime())
            about_slide_loop.addData('next_button.numClicks', next_button.numClicks)
            if next_button.numClicks:
               about_slide_loop.addData('next_button.timesOn', next_button.timesOn)
               about_slide_loop.addData('next_button.timesOff', next_button.timesOff)
            else:
               about_slide_loop.addData('next_button.timesOn', "")
               about_slide_loop.addData('next_button.timesOff', "")
            about_slide_loop.addData('back_button.numClicks', back_button.numClicks)
            if back_button.numClicks:
               about_slide_loop.addData('back_button.timesOn', back_button.timesOn)
               about_slide_loop.addData('back_button.timesOff', back_button.timesOff)
            else:
               about_slide_loop.addData('back_button.timesOn', "")
               about_slide_loop.addData('back_button.timesOff', "")
            # the Routine "AboutExpScreen" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed show_instructions repeats of 'about_slide_loop'
        
    # completed 9999.0 repeats of 'instructions_controller'
    
    
    # --- Prepare to start Routine "WarningScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('WarningScreen.started', globalClock.getTime())
    # reset button to account for continued clicks & clear times on/off
    button.reset()
    # Run 'Begin Routine' code from code_6
    warning_heading.bold = True
    # keep track of which components have finished
    WarningScreenComponents = [white_background, welcome_message, caution_sign, button, warning_heading]
    for thisComponent in WarningScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "WarningScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *white_background* updates
        
        # if white_background is starting this frame...
        if white_background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            white_background.frameNStart = frameN  # exact frame index
            white_background.tStart = t  # local t and not account for scr refresh
            white_background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(white_background, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'white_background.started')
            # update status
            white_background.status = STARTED
            white_background.setAutoDraw(True)
        
        # if white_background is active this frame...
        if white_background.status == STARTED:
            # update params
            pass
        
        # *welcome_message* updates
        
        # if welcome_message is starting this frame...
        if welcome_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_message.frameNStart = frameN  # exact frame index
            welcome_message.tStart = t  # local t and not account for scr refresh
            welcome_message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_message, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_message.started')
            # update status
            welcome_message.status = STARTED
            welcome_message.setAutoDraw(True)
        
        # if welcome_message is active this frame...
        if welcome_message.status == STARTED:
            # update params
            welcome_message.setText('\n\nThis experiment entails the observation of flickering objects. Individuals with a predisposition to epilepsy or other visual sensitivities are advised to exercise caution or to abstain from participation. We cannot assume liability for any discomfort or complications that may ensue.\n\n\n', log=False)
        
        # *caution_sign* updates
        
        # if caution_sign is starting this frame...
        if caution_sign.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            caution_sign.frameNStart = frameN  # exact frame index
            caution_sign.tStart = t  # local t and not account for scr refresh
            caution_sign.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(caution_sign, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'caution_sign.started')
            # update status
            caution_sign.status = STARTED
            caution_sign.setAutoDraw(True)
        
        # if caution_sign is active this frame...
        if caution_sign.status == STARTED:
            # update params
            pass
        # *button* updates
        
        # if button is starting this frame...
        if button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button.frameNStart = frameN  # exact frame index
            button.tStart = t  # local t and not account for scr refresh
            button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button.started')
            # update status
            button.status = STARTED
            button.setAutoDraw(True)
        
        # if button is active this frame...
        if button.status == STARTED:
            # update params
            pass
            # check whether button has been pressed
            if button.isClicked:
                if not button.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    button.timesOn.append(button.buttonClock.getTime())
                    button.timesOff.append(button.buttonClock.getTime())
                elif len(button.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    button.timesOff[-1] = button.buttonClock.getTime()
                if not button.wasClicked:
                    # end routine when button is clicked
                    continueRoutine = False
                if not button.wasClicked:
                    # run callback code when button is clicked
                    pass
        # take note of whether button was clicked, so that next frame we know if clicks are new
        button.wasClicked = button.isClicked and button.status == STARTED
        
        # *warning_heading* updates
        
        # if warning_heading is starting this frame...
        if warning_heading.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            warning_heading.frameNStart = frameN  # exact frame index
            warning_heading.tStart = t  # local t and not account for scr refresh
            warning_heading.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(warning_heading, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'warning_heading.started')
            # update status
            warning_heading.status = STARTED
            warning_heading.setAutoDraw(True)
        
        # if warning_heading is active this frame...
        if warning_heading.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WarningScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "WarningScreen" ---
    for thisComponent in WarningScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('WarningScreen.stopped', globalClock.getTime())
    thisExp.addData('button.numClicks', button.numClicks)
    if button.numClicks:
       thisExp.addData('button.timesOn', button.timesOn)
       thisExp.addData('button.timesOff', button.timesOff)
    else:
       thisExp.addData('button.timesOn', "")
       thisExp.addData('button.timesOff', "")
    # Run 'End Routine' code from code_6
    skip = False
    # the Routine "WarningScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "GameDet" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('GameDet.started', globalClock.getTime())
    # skip this Routine if its 'Skip if' condition is True
    continueRoutine = continueRoutine and not (skip == True)
    # reset Skip to account for continued clicks & clear times on/off
    Skip.reset()
    # keep track of which components have finished
    GameDetComponents = [MindBattle, explanation, Skip]
    for thisComponent in GameDetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "GameDet" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *MindBattle* updates
        
        # if MindBattle is starting this frame...
        if MindBattle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MindBattle.frameNStart = frameN  # exact frame index
            MindBattle.tStart = t  # local t and not account for scr refresh
            MindBattle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MindBattle, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'MindBattle.started')
            # update status
            MindBattle.status = STARTED
            MindBattle.setAutoDraw(True)
        
        # if MindBattle is active this frame...
        if MindBattle.status == STARTED:
            # update params
            pass
        
        # *explanation* updates
        
        # if explanation is starting this frame...
        if explanation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            explanation.frameNStart = frameN  # exact frame index
            explanation.tStart = t  # local t and not account for scr refresh
            explanation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(explanation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'explanation.started')
            # update status
            explanation.status = STARTED
            explanation.setAutoDraw(True)
        
        # if explanation is active this frame...
        if explanation.status == STARTED:
            # update params
            pass
        # *Skip* updates
        
        # if Skip is starting this frame...
        if Skip.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Skip.frameNStart = frameN  # exact frame index
            Skip.tStart = t  # local t and not account for scr refresh
            Skip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Skip, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Skip.started')
            # update status
            Skip.status = STARTED
            Skip.setAutoDraw(True)
        
        # if Skip is active this frame...
        if Skip.status == STARTED:
            # update params
            pass
            # check whether Skip has been pressed
            if Skip.isClicked:
                if not Skip.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    Skip.timesOn.append(Skip.buttonClock.getTime())
                    Skip.timesOff.append(Skip.buttonClock.getTime())
                elif len(Skip.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    Skip.timesOff[-1] = Skip.buttonClock.getTime()
                if not Skip.wasClicked:
                    # end routine when Skip is clicked
                    continueRoutine = False
                if not Skip.wasClicked:
                    # run callback code when Skip is clicked
                    skip = True
        # take note of whether Skip was clicked, so that next frame we know if clicks are new
        Skip.wasClicked = Skip.isClicked and Skip.status == STARTED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GameDetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "GameDet" ---
    for thisComponent in GameDetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('GameDet.stopped', globalClock.getTime())
    thisExp.addData('Skip.numClicks', Skip.numClicks)
    if Skip.numClicks:
       thisExp.addData('Skip.timesOn', Skip.timesOn)
       thisExp.addData('Skip.timesOff', Skip.timesOff)
    else:
       thisExp.addData('Skip.timesOn', "")
       thisExp.addData('Skip.timesOff', "")
    # the Routine "GameDet" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    return_to_homepage = data.TrialHandler(nReps=10.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='return_to_homepage')
    thisExp.addLoop(return_to_homepage)  # add the loop to the experiment
    thisReturn_to_homepage = return_to_homepage.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisReturn_to_homepage.rgb)
    if thisReturn_to_homepage != None:
        for paramName in thisReturn_to_homepage:
            globals()[paramName] = thisReturn_to_homepage[paramName]
    
    for thisReturn_to_homepage in return_to_homepage:
        currentLoop = return_to_homepage
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisReturn_to_homepage.rgb)
        if thisReturn_to_homepage != None:
            for paramName in thisReturn_to_homepage:
                globals()[paramName] = thisReturn_to_homepage[paramName]
        
        # --- Prepare to start Routine "PickTest" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('PickTest.started', globalClock.getTime())
        # reset button_t1 to account for continued clicks & clear times on/off
        button_t1.reset()
        # reset button_t2 to account for continued clicks & clear times on/off
        button_t2.reset()
        # reset button_t3 to account for continued clicks & clear times on/off
        button_t3.reset()
        # reset button_t4 to account for continued clicks & clear times on/off
        button_t4.reset()
        # reset button_all to account for continued clicks & clear times on/off
        button_all.reset()
        # Run 'Begin Routine' code from code_5
        text.bold = True
        lose = False
        # keep track of which components have finished
        PickTestComponents = [brain_animation, button_t1, button_t2, button_t3, button_t4, button_all, text]
        for thisComponent in PickTestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PickTest" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *brain_animation* updates
            
            # if brain_animation is starting this frame...
            if brain_animation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                brain_animation.frameNStart = frameN  # exact frame index
                brain_animation.tStart = t  # local t and not account for scr refresh
                brain_animation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(brain_animation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'brain_animation.started')
                # update status
                brain_animation.status = STARTED
                brain_animation.setAutoDraw(True)
                brain_animation.play()
            # *button_t1* updates
            
            # if button_t1 is starting this frame...
            if button_t1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_t1.frameNStart = frameN  # exact frame index
                button_t1.tStart = t  # local t and not account for scr refresh
                button_t1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_t1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_t1.started')
                # update status
                button_t1.status = STARTED
                button_t1.setAutoDraw(True)
            
            # if button_t1 is active this frame...
            if button_t1.status == STARTED:
                # update params
                pass
                # check whether button_t1 has been pressed
                if button_t1.isClicked:
                    if not button_t1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_t1.timesOn.append(button_t1.buttonClock.getTime())
                        button_t1.timesOff.append(button_t1.buttonClock.getTime())
                    elif len(button_t1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_t1.timesOff[-1] = button_t1.buttonClock.getTime()
                    if not button_t1.wasClicked:
                        # end routine when button_t1 is clicked
                        continueRoutine = False
                    if not button_t1.wasClicked:
                        # run callback code when button_t1 is clicked
                        global buttont1 
                        buttont1 = True
            # take note of whether button_t1 was clicked, so that next frame we know if clicks are new
            button_t1.wasClicked = button_t1.isClicked and button_t1.status == STARTED
            # *button_t2* updates
            
            # if button_t2 is starting this frame...
            if button_t2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_t2.frameNStart = frameN  # exact frame index
                button_t2.tStart = t  # local t and not account for scr refresh
                button_t2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_t2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_t2.started')
                # update status
                button_t2.status = STARTED
                button_t2.setAutoDraw(True)
            
            # if button_t2 is active this frame...
            if button_t2.status == STARTED:
                # update params
                pass
                # check whether button_t2 has been pressed
                if button_t2.isClicked:
                    if not button_t2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_t2.timesOn.append(button_t2.buttonClock.getTime())
                        button_t2.timesOff.append(button_t2.buttonClock.getTime())
                    elif len(button_t2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_t2.timesOff[-1] = button_t2.buttonClock.getTime()
                    if not button_t2.wasClicked:
                        # end routine when button_t2 is clicked
                        continueRoutine = False
                    if not button_t2.wasClicked:
                        # run callback code when button_t2 is clicked
                        global buttont2
                        buttont2 = True
            # take note of whether button_t2 was clicked, so that next frame we know if clicks are new
            button_t2.wasClicked = button_t2.isClicked and button_t2.status == STARTED
            # *button_t3* updates
            
            # if button_t3 is starting this frame...
            if button_t3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_t3.frameNStart = frameN  # exact frame index
                button_t3.tStart = t  # local t and not account for scr refresh
                button_t3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_t3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_t3.started')
                # update status
                button_t3.status = STARTED
                button_t3.setAutoDraw(True)
            
            # if button_t3 is active this frame...
            if button_t3.status == STARTED:
                # update params
                pass
                # check whether button_t3 has been pressed
                if button_t3.isClicked:
                    if not button_t3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_t3.timesOn.append(button_t3.buttonClock.getTime())
                        button_t3.timesOff.append(button_t3.buttonClock.getTime())
                    elif len(button_t3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_t3.timesOff[-1] = button_t3.buttonClock.getTime()
                    if not button_t3.wasClicked:
                        # end routine when button_t3 is clicked
                        continueRoutine = False
                    if not button_t3.wasClicked:
                        # run callback code when button_t3 is clicked
                        global buttont3
                        buttont3 = True
            # take note of whether button_t3 was clicked, so that next frame we know if clicks are new
            button_t3.wasClicked = button_t3.isClicked and button_t3.status == STARTED
            # *button_t4* updates
            
            # if button_t4 is starting this frame...
            if button_t4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_t4.frameNStart = frameN  # exact frame index
                button_t4.tStart = t  # local t and not account for scr refresh
                button_t4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_t4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_t4.started')
                # update status
                button_t4.status = STARTED
                button_t4.setAutoDraw(True)
            
            # if button_t4 is active this frame...
            if button_t4.status == STARTED:
                # update params
                pass
                # check whether button_t4 has been pressed
                if button_t4.isClicked:
                    if not button_t4.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_t4.timesOn.append(button_t4.buttonClock.getTime())
                        button_t4.timesOff.append(button_t4.buttonClock.getTime())
                    elif len(button_t4.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_t4.timesOff[-1] = button_t4.buttonClock.getTime()
                    if not button_t4.wasClicked:
                        # end routine when button_t4 is clicked
                        continueRoutine = False
                    if not button_t4.wasClicked:
                        # run callback code when button_t4 is clicked
                        global buttont4
                        buttont4= True
            # take note of whether button_t4 was clicked, so that next frame we know if clicks are new
            button_t4.wasClicked = button_t4.isClicked and button_t4.status == STARTED
            # *button_all* updates
            
            # if button_all is starting this frame...
            if button_all.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_all.frameNStart = frameN  # exact frame index
                button_all.tStart = t  # local t and not account for scr refresh
                button_all.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_all, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_all.started')
                # update status
                button_all.status = STARTED
                button_all.setAutoDraw(True)
            
            # if button_all is active this frame...
            if button_all.status == STARTED:
                # update params
                pass
                # check whether button_all has been pressed
                if button_all.isClicked:
                    if not button_all.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_all.timesOn.append(button_all.buttonClock.getTime())
                        button_all.timesOff.append(button_all.buttonClock.getTime())
                    elif len(button_all.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_all.timesOff[-1] = button_all.buttonClock.getTime()
                    if not button_all.wasClicked:
                        # end routine when button_all is clicked
                        continueRoutine = False
                    if not button_all.wasClicked:
                        # run callback code when button_all is clicked
                        buttont1 = True
                        buttont2= True
                        buttont3= True
                        buttont4= True
            # take note of whether button_all was clicked, so that next frame we know if clicks are new
            button_all.wasClicked = button_all.isClicked and button_all.status == STARTED
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PickTestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PickTest" ---
        for thisComponent in PickTestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('PickTest.stopped', globalClock.getTime())
        brain_animation.stop()  # ensure movie has stopped at end of Routine
        return_to_homepage.addData('button_t1.numClicks', button_t1.numClicks)
        if button_t1.numClicks:
           return_to_homepage.addData('button_t1.timesOn', button_t1.timesOn)
           return_to_homepage.addData('button_t1.timesOff', button_t1.timesOff)
        else:
           return_to_homepage.addData('button_t1.timesOn', "")
           return_to_homepage.addData('button_t1.timesOff', "")
        return_to_homepage.addData('button_t2.numClicks', button_t2.numClicks)
        if button_t2.numClicks:
           return_to_homepage.addData('button_t2.timesOn', button_t2.timesOn)
           return_to_homepage.addData('button_t2.timesOff', button_t2.timesOff)
        else:
           return_to_homepage.addData('button_t2.timesOn', "")
           return_to_homepage.addData('button_t2.timesOff', "")
        return_to_homepage.addData('button_t3.numClicks', button_t3.numClicks)
        if button_t3.numClicks:
           return_to_homepage.addData('button_t3.timesOn', button_t3.timesOn)
           return_to_homepage.addData('button_t3.timesOff', button_t3.timesOff)
        else:
           return_to_homepage.addData('button_t3.timesOn', "")
           return_to_homepage.addData('button_t3.timesOff', "")
        return_to_homepage.addData('button_t4.numClicks', button_t4.numClicks)
        if button_t4.numClicks:
           return_to_homepage.addData('button_t4.timesOn', button_t4.timesOn)
           return_to_homepage.addData('button_t4.timesOff', button_t4.timesOff)
        else:
           return_to_homepage.addData('button_t4.timesOn', "")
           return_to_homepage.addData('button_t4.timesOff', "")
        return_to_homepage.addData('button_all.numClicks', button_all.numClicks)
        if button_all.numClicks:
           return_to_homepage.addData('button_all.timesOn', button_all.timesOn)
           return_to_homepage.addData('button_all.timesOff', button_all.timesOff)
        else:
           return_to_homepage.addData('button_all.timesOn', "")
           return_to_homepage.addData('button_all.timesOff', "")
        # the Routine "PickTest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_1 = data.TrialHandler(nReps=trial_num1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_1')
        thisExp.addLoop(trials_1)  # add the loop to the experiment
        thisTrial_1 = trials_1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
        if thisTrial_1 != None:
            for paramName in thisTrial_1:
                globals()[paramName] = thisTrial_1[paramName]
        
        for thisTrial_1 in trials_1:
            currentLoop = trials_1
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
            if thisTrial_1 != None:
                for paramName in thisTrial_1:
                    globals()[paramName] = thisTrial_1[paramName]
            
            # set up handler to look after randomisation of conditions etc
            repetition_1 = data.TrialHandler(nReps=rep_num1, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='repetition_1')
            thisExp.addLoop(repetition_1)  # add the loop to the experiment
            thisRepetition_1 = repetition_1.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisRepetition_1.rgb)
            if thisRepetition_1 != None:
                for paramName in thisRepetition_1:
                    globals()[paramName] = thisRepetition_1[paramName]
            
            for thisRepetition_1 in repetition_1:
                currentLoop = repetition_1
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisRepetition_1.rgb)
                if thisRepetition_1 != None:
                    for paramName in thisRepetition_1:
                        globals()[paramName] = thisRepetition_1[paramName]
                
                # --- Prepare to start Routine "test_1" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('test_1.started', globalClock.getTime())
                # skip this Routine if its 'Skip if' condition is True
                continueRoutine = continueRoutine and not ((buttont1 == False) or (lose == True))
                # Run 'Begin Routine' code from test_1_code
                #Start aquiring data
                #startTest(dur_test1)
                
                home_button = False
                
                # Frequencies for each trial
                freq_trials = [[15], #Trial 1 frequency
                            [16],   #Trial 2 frequency
                            [1],  #Trial 3 frequency
                            [15],  #Trial 4 frequency
                            [15],  #Trial 5 frequency
                            [15],  #Trial 6 frequency
                            [15],  #Trial 7 frequency
                            [15],  #Trial 8 frequency
                            [15],  #Trial 9 frequency
                            [15]]  #Trial 10 frequency
                
                loop_num = trials_1.thisN
                #Select frequencies for current trial
                freq_curr_trial = freq_trials[loop_num]
                
                #Target object for user to look at for each trial
                targets = [1, 1, 1, 1, 1,
                           1, 1, 1, 1, 1]
                
                
                #All objects
                objects = [boxL1_1]
                
                #Select target object for user to look at
                selectTarget(objects, targets[loop_num]) 
                
                test_1_mess.text = 'Level 1, Round ' + str(loop_num + 1)
                # keep track of which components have finished
                test_1Components = [earth1, boxL1_1, shipL1_1, Attack_message, test_1_mess]
                for thisComponent in test_1Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test_1" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *earth1* updates
                    
                    # if earth1 is starting this frame...
                    if earth1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        earth1.frameNStart = frameN  # exact frame index
                        earth1.tStart = t  # local t and not account for scr refresh
                        earth1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(earth1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'earth1.started')
                        # update status
                        earth1.status = STARTED
                        earth1.setAutoDraw(True)
                    
                    # if earth1 is active this frame...
                    if earth1.status == STARTED:
                        # update params
                        pass
                    
                    # if earth1 is stopping this frame...
                    if earth1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > earth1.tStartRefresh + dur_test1-frameTolerance:
                            # keep track of stop time/frame for later
                            earth1.tStop = t  # not accounting for scr refresh
                            earth1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'earth1.stopped')
                            # update status
                            earth1.status = FINISHED
                            earth1.setAutoDraw(False)
                    
                    # *boxL1_1* updates
                    
                    # if boxL1_1 is starting this frame...
                    if boxL1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL1_1.frameNStart = frameN  # exact frame index
                        boxL1_1.tStart = t  # local t and not account for scr refresh
                        boxL1_1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL1_1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL1_1.started')
                        # update status
                        boxL1_1.status = STARTED
                        boxL1_1.setAutoDraw(True)
                    
                    # if boxL1_1 is active this frame...
                    if boxL1_1.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL1_1 is stopping this frame...
                    if boxL1_1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL1_1.tStartRefresh + dur_test1-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL1_1.tStop = t  # not accounting for scr refresh
                            boxL1_1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL1_1.stopped')
                            # update status
                            boxL1_1.status = FINISHED
                            boxL1_1.setAutoDraw(False)
                    
                    # *shipL1_1* updates
                    
                    # if shipL1_1 is starting this frame...
                    if shipL1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL1_1.frameNStart = frameN  # exact frame index
                        shipL1_1.tStart = t  # local t and not account for scr refresh
                        shipL1_1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL1_1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL1_1.started')
                        # update status
                        shipL1_1.status = STARTED
                        shipL1_1.setAutoDraw(True)
                    
                    # if shipL1_1 is active this frame...
                    if shipL1_1.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL1_1 is stopping this frame...
                    if shipL1_1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL1_1.tStartRefresh + dur_test1-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL1_1.tStop = t  # not accounting for scr refresh
                            shipL1_1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL1_1.stopped')
                            # update status
                            shipL1_1.status = FINISHED
                            shipL1_1.setAutoDraw(False)
                    
                    # *Attack_message* updates
                    
                    # if Attack_message is starting this frame...
                    if Attack_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        Attack_message.frameNStart = frameN  # exact frame index
                        Attack_message.tStart = t  # local t and not account for scr refresh
                        Attack_message.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Attack_message, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Attack_message.started')
                        # update status
                        Attack_message.status = STARTED
                        Attack_message.setAutoDraw(True)
                    
                    # if Attack_message is active this frame...
                    if Attack_message.status == STARTED:
                        # update params
                        pass
                    
                    # if Attack_message is stopping this frame...
                    if Attack_message.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Attack_message.tStartRefresh + dur_test1-frameTolerance:
                            # keep track of stop time/frame for later
                            Attack_message.tStop = t  # not accounting for scr refresh
                            Attack_message.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Attack_message.stopped')
                            # update status
                            Attack_message.status = FINISHED
                            Attack_message.setAutoDraw(False)
                    
                    # *test_1_mess* updates
                    
                    # if test_1_mess is starting this frame...
                    if test_1_mess.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        test_1_mess.frameNStart = frameN  # exact frame index
                        test_1_mess.tStart = t  # local t and not account for scr refresh
                        test_1_mess.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(test_1_mess, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'test_1_mess.started')
                        # update status
                        test_1_mess.status = STARTED
                        test_1_mess.setAutoDraw(True)
                    
                    # if test_1_mess is active this frame...
                    if test_1_mess.status == STARTED:
                        # update params
                        pass
                    
                    # if test_1_mess is stopping this frame...
                    if test_1_mess.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > test_1_mess.tStartRefresh + dur_test1-frameTolerance:
                            # keep track of stop time/frame for later
                            test_1_mess.tStop = t  # not accounting for scr refresh
                            test_1_mess.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'test_1_mess.stopped')
                            # update status
                            test_1_mess.status = FINISHED
                            test_1_mess.setAutoDraw(False)
                    # Run 'Each Frame' code from test_1_code
                    #Flicker objects are set frequencies
                    flickerObjects(objects, freq_curr_trial, frameN)
                    
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test_1Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test_1" ---
                for thisComponent in test_1Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('test_1.stopped', globalClock.getTime())
                # Run 'End Routine' code from test_1_code
                if buttont1 == True and lose == False:
                    #EEGdata = getEEGData()
                    EEGdata = [6, 2, 3, 8, 0.25]
                    lose = not compareFreq(EEGdata, freq_curr_trial[targets[trials_1.thisN] - 1])
                # the Routine "test_1" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "earth_pause_1" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('earth_pause_1.started', globalClock.getTime())
                # skip this Routine if its 'Skip if' condition is True
                continueRoutine = continueRoutine and not ((buttont1 == False) or (lose == True) or (trials_1.thisN == (trials_1.nReps - 1)))
                # keep track of which components have finished
                earth_pause_1Components = [earth_blank_4, continue_playing_message_4]
                for thisComponent in earth_pause_1Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "earth_pause_1" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *earth_blank_4* updates
                    
                    # if earth_blank_4 is starting this frame...
                    if earth_blank_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        earth_blank_4.frameNStart = frameN  # exact frame index
                        earth_blank_4.tStart = t  # local t and not account for scr refresh
                        earth_blank_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(earth_blank_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'earth_blank_4.started')
                        # update status
                        earth_blank_4.status = STARTED
                        earth_blank_4.setAutoDraw(True)
                    
                    # if earth_blank_4 is active this frame...
                    if earth_blank_4.status == STARTED:
                        # update params
                        pass
                    
                    # if earth_blank_4 is stopping this frame...
                    if earth_blank_4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > earth_blank_4.tStartRefresh + dur_blank-frameTolerance:
                            # keep track of stop time/frame for later
                            earth_blank_4.tStop = t  # not accounting for scr refresh
                            earth_blank_4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'earth_blank_4.stopped')
                            # update status
                            earth_blank_4.status = FINISHED
                            earth_blank_4.setAutoDraw(False)
                    
                    # *continue_playing_message_4* updates
                    
                    # if continue_playing_message_4 is starting this frame...
                    if continue_playing_message_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        continue_playing_message_4.frameNStart = frameN  # exact frame index
                        continue_playing_message_4.tStart = t  # local t and not account for scr refresh
                        continue_playing_message_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(continue_playing_message_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'continue_playing_message_4.started')
                        # update status
                        continue_playing_message_4.status = STARTED
                        continue_playing_message_4.setAutoDraw(True)
                    
                    # if continue_playing_message_4 is active this frame...
                    if continue_playing_message_4.status == STARTED:
                        # update params
                        pass
                    
                    # if continue_playing_message_4 is stopping this frame...
                    if continue_playing_message_4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > continue_playing_message_4.tStartRefresh + dur_blank-frameTolerance:
                            # keep track of stop time/frame for later
                            continue_playing_message_4.tStop = t  # not accounting for scr refresh
                            continue_playing_message_4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'continue_playing_message_4.stopped')
                            # update status
                            continue_playing_message_4.status = FINISHED
                            continue_playing_message_4.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in earth_pause_1Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "earth_pause_1" ---
                for thisComponent in earth_pause_1Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('earth_pause_1.stopped', globalClock.getTime())
                # the Routine "earth_pause_1" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed rep_num1 repeats of 'repetition_1'
            
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed trial_num1 repeats of 'trials_1'
        
        
        # --- Prepare to start Routine "before_test2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('before_test2.started', globalClock.getTime())
        # skip this Routine if its 'Skip if' condition is True
        continueRoutine = continueRoutine and not ((buttont1 == False) or (lose == True) or (buttont2 == False))
        # keep track of which components have finished
        before_test2Components = [earth_blank_5, continue_playing_message_5]
        for thisComponent in before_test2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "before_test2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *earth_blank_5* updates
            
            # if earth_blank_5 is starting this frame...
            if earth_blank_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                earth_blank_5.frameNStart = frameN  # exact frame index
                earth_blank_5.tStart = t  # local t and not account for scr refresh
                earth_blank_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(earth_blank_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'earth_blank_5.started')
                # update status
                earth_blank_5.status = STARTED
                earth_blank_5.setAutoDraw(True)
            
            # if earth_blank_5 is active this frame...
            if earth_blank_5.status == STARTED:
                # update params
                pass
            
            # if earth_blank_5 is stopping this frame...
            if earth_blank_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > earth_blank_5.tStartRefresh + dur_blank-frameTolerance:
                    # keep track of stop time/frame for later
                    earth_blank_5.tStop = t  # not accounting for scr refresh
                    earth_blank_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'earth_blank_5.stopped')
                    # update status
                    earth_blank_5.status = FINISHED
                    earth_blank_5.setAutoDraw(False)
            
            # *continue_playing_message_5* updates
            
            # if continue_playing_message_5 is starting this frame...
            if continue_playing_message_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                continue_playing_message_5.frameNStart = frameN  # exact frame index
                continue_playing_message_5.tStart = t  # local t and not account for scr refresh
                continue_playing_message_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continue_playing_message_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_playing_message_5.started')
                # update status
                continue_playing_message_5.status = STARTED
                continue_playing_message_5.setAutoDraw(True)
            
            # if continue_playing_message_5 is active this frame...
            if continue_playing_message_5.status == STARTED:
                # update params
                pass
            
            # if continue_playing_message_5 is stopping this frame...
            if continue_playing_message_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > continue_playing_message_5.tStartRefresh + dur_blank-frameTolerance:
                    # keep track of stop time/frame for later
                    continue_playing_message_5.tStop = t  # not accounting for scr refresh
                    continue_playing_message_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'continue_playing_message_5.stopped')
                    # update status
                    continue_playing_message_5.status = FINISHED
                    continue_playing_message_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in before_test2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "before_test2" ---
        for thisComponent in before_test2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('before_test2.stopped', globalClock.getTime())
        # the Routine "before_test2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler(nReps=trial_num2, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_2')
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    globals()[paramName] = thisTrial_2[paramName]
            
            # set up handler to look after randomisation of conditions etc
            repetition_2 = data.TrialHandler(nReps=rep_num2, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='repetition_2')
            thisExp.addLoop(repetition_2)  # add the loop to the experiment
            thisRepetition_2 = repetition_2.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisRepetition_2.rgb)
            if thisRepetition_2 != None:
                for paramName in thisRepetition_2:
                    globals()[paramName] = thisRepetition_2[paramName]
            
            for thisRepetition_2 in repetition_2:
                currentLoop = repetition_2
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisRepetition_2.rgb)
                if thisRepetition_2 != None:
                    for paramName in thisRepetition_2:
                        globals()[paramName] = thisRepetition_2[paramName]
                
                # --- Prepare to start Routine "test_2" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('test_2.started', globalClock.getTime())
                # skip this Routine if its 'Skip if' condition is True
                continueRoutine = continueRoutine and not ((buttont2 == False) or (lose == True))
                # Run 'Begin Routine' code from test_2_code
                #Start aquiring data
                #startTest(dur_test2)
                
                #Target object for user to look at for each trial
                targets = [1, 2, 3, 1, 1,
                           1, 1, 1, 1, 1]
                
                # Frequencies for each object for every trial
                freq_trials = [[2, 10 , 15 ], #Trial 1 frequencies
                               [10 , 5 , 2 ], #Trial 2 frequencies
                               [2 , 5 , 2 ], #Trial 3 frequencies
                               [6 , 4 , 30], #Trial 4 frequencies
                               [8 , 6 , 7 ], #Trial 5 frequencies
                               [10, 20, 30], #Trial 6 frequencies
                               [1 , 2 , 30], #Trial 7 frequencies
                               [1 , 20, 3 ], #Trial 8 frequencies
                               [10, 2 , 3 ], #Trial 9 frequencies
                               [10 ,10 ,10 ]] #Trial 10 frequencies
                
                #Select frequencies for current trial
                freq_curr_trial = freq_trials[trials_2.thisN]
                
                #All objects
                objects = [boxL2_1, boxL2_2, boxL2_3]
                
                #Select target object for user to look at
                selectTarget(objects, targets[trials_2.thisN]) 
                
                test_2_mess.text = 'Level 2, Round ' + str(trials_2.thisN + 1)
                # keep track of which components have finished
                test_2Components = [earth2, boxL2_1, shipL2_1, boxL2_2, shipL2_2, boxL2_3, shipL2_3, Attack_message2, test_2_mess]
                for thisComponent in test_2Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test_2" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *earth2* updates
                    
                    # if earth2 is starting this frame...
                    if earth2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        earth2.frameNStart = frameN  # exact frame index
                        earth2.tStart = t  # local t and not account for scr refresh
                        earth2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(earth2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'earth2.started')
                        # update status
                        earth2.status = STARTED
                        earth2.setAutoDraw(True)
                    
                    # if earth2 is active this frame...
                    if earth2.status == STARTED:
                        # update params
                        pass
                    
                    # if earth2 is stopping this frame...
                    if earth2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > earth2.tStartRefresh + dur_test1-frameTolerance:
                            # keep track of stop time/frame for later
                            earth2.tStop = t  # not accounting for scr refresh
                            earth2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'earth2.stopped')
                            # update status
                            earth2.status = FINISHED
                            earth2.setAutoDraw(False)
                    
                    # *boxL2_1* updates
                    
                    # if boxL2_1 is starting this frame...
                    if boxL2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL2_1.frameNStart = frameN  # exact frame index
                        boxL2_1.tStart = t  # local t and not account for scr refresh
                        boxL2_1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL2_1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL2_1.started')
                        # update status
                        boxL2_1.status = STARTED
                        boxL2_1.setAutoDraw(True)
                    
                    # if boxL2_1 is active this frame...
                    if boxL2_1.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL2_1 is stopping this frame...
                    if boxL2_1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL2_1.tStartRefresh + dur_test2-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL2_1.tStop = t  # not accounting for scr refresh
                            boxL2_1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL2_1.stopped')
                            # update status
                            boxL2_1.status = FINISHED
                            boxL2_1.setAutoDraw(False)
                    
                    # *shipL2_1* updates
                    
                    # if shipL2_1 is starting this frame...
                    if shipL2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL2_1.frameNStart = frameN  # exact frame index
                        shipL2_1.tStart = t  # local t and not account for scr refresh
                        shipL2_1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL2_1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL2_1.started')
                        # update status
                        shipL2_1.status = STARTED
                        shipL2_1.setAutoDraw(True)
                    
                    # if shipL2_1 is active this frame...
                    if shipL2_1.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL2_1 is stopping this frame...
                    if shipL2_1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL2_1.tStartRefresh + dur_test2-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL2_1.tStop = t  # not accounting for scr refresh
                            shipL2_1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL2_1.stopped')
                            # update status
                            shipL2_1.status = FINISHED
                            shipL2_1.setAutoDraw(False)
                    
                    # *boxL2_2* updates
                    
                    # if boxL2_2 is starting this frame...
                    if boxL2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL2_2.frameNStart = frameN  # exact frame index
                        boxL2_2.tStart = t  # local t and not account for scr refresh
                        boxL2_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL2_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL2_2.started')
                        # update status
                        boxL2_2.status = STARTED
                        boxL2_2.setAutoDraw(True)
                    
                    # if boxL2_2 is active this frame...
                    if boxL2_2.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL2_2 is stopping this frame...
                    if boxL2_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL2_2.tStartRefresh + dur_test2-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL2_2.tStop = t  # not accounting for scr refresh
                            boxL2_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL2_2.stopped')
                            # update status
                            boxL2_2.status = FINISHED
                            boxL2_2.setAutoDraw(False)
                    
                    # *shipL2_2* updates
                    
                    # if shipL2_2 is starting this frame...
                    if shipL2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL2_2.frameNStart = frameN  # exact frame index
                        shipL2_2.tStart = t  # local t and not account for scr refresh
                        shipL2_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL2_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL2_2.started')
                        # update status
                        shipL2_2.status = STARTED
                        shipL2_2.setAutoDraw(True)
                    
                    # if shipL2_2 is active this frame...
                    if shipL2_2.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL2_2 is stopping this frame...
                    if shipL2_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL2_2.tStartRefresh + dur_test2-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL2_2.tStop = t  # not accounting for scr refresh
                            shipL2_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL2_2.stopped')
                            # update status
                            shipL2_2.status = FINISHED
                            shipL2_2.setAutoDraw(False)
                    
                    # *boxL2_3* updates
                    
                    # if boxL2_3 is starting this frame...
                    if boxL2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL2_3.frameNStart = frameN  # exact frame index
                        boxL2_3.tStart = t  # local t and not account for scr refresh
                        boxL2_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL2_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL2_3.started')
                        # update status
                        boxL2_3.status = STARTED
                        boxL2_3.setAutoDraw(True)
                    
                    # if boxL2_3 is active this frame...
                    if boxL2_3.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL2_3 is stopping this frame...
                    if boxL2_3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL2_3.tStartRefresh + dur_test2-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL2_3.tStop = t  # not accounting for scr refresh
                            boxL2_3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL2_3.stopped')
                            # update status
                            boxL2_3.status = FINISHED
                            boxL2_3.setAutoDraw(False)
                    
                    # *shipL2_3* updates
                    
                    # if shipL2_3 is starting this frame...
                    if shipL2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL2_3.frameNStart = frameN  # exact frame index
                        shipL2_3.tStart = t  # local t and not account for scr refresh
                        shipL2_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL2_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL2_3.started')
                        # update status
                        shipL2_3.status = STARTED
                        shipL2_3.setAutoDraw(True)
                    
                    # if shipL2_3 is active this frame...
                    if shipL2_3.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL2_3 is stopping this frame...
                    if shipL2_3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL2_3.tStartRefresh + dur_test2-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL2_3.tStop = t  # not accounting for scr refresh
                            shipL2_3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL2_3.stopped')
                            # update status
                            shipL2_3.status = FINISHED
                            shipL2_3.setAutoDraw(False)
                    
                    # *Attack_message2* updates
                    
                    # if Attack_message2 is starting this frame...
                    if Attack_message2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        Attack_message2.frameNStart = frameN  # exact frame index
                        Attack_message2.tStart = t  # local t and not account for scr refresh
                        Attack_message2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Attack_message2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Attack_message2.started')
                        # update status
                        Attack_message2.status = STARTED
                        Attack_message2.setAutoDraw(True)
                    
                    # if Attack_message2 is active this frame...
                    if Attack_message2.status == STARTED:
                        # update params
                        pass
                    
                    # if Attack_message2 is stopping this frame...
                    if Attack_message2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Attack_message2.tStartRefresh + dur_test1-frameTolerance:
                            # keep track of stop time/frame for later
                            Attack_message2.tStop = t  # not accounting for scr refresh
                            Attack_message2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Attack_message2.stopped')
                            # update status
                            Attack_message2.status = FINISHED
                            Attack_message2.setAutoDraw(False)
                    
                    # *test_2_mess* updates
                    
                    # if test_2_mess is starting this frame...
                    if test_2_mess.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        test_2_mess.frameNStart = frameN  # exact frame index
                        test_2_mess.tStart = t  # local t and not account for scr refresh
                        test_2_mess.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(test_2_mess, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'test_2_mess.started')
                        # update status
                        test_2_mess.status = STARTED
                        test_2_mess.setAutoDraw(True)
                    
                    # if test_2_mess is active this frame...
                    if test_2_mess.status == STARTED:
                        # update params
                        pass
                    
                    # if test_2_mess is stopping this frame...
                    if test_2_mess.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > test_2_mess.tStartRefresh + dur_test2-frameTolerance:
                            # keep track of stop time/frame for later
                            test_2_mess.tStop = t  # not accounting for scr refresh
                            test_2_mess.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'test_2_mess.stopped')
                            # update status
                            test_2_mess.status = FINISHED
                            test_2_mess.setAutoDraw(False)
                    # Run 'Each Frame' code from test_2_code
                    #Flicker objects are set frequencies
                    flickerObjects(objects, freq_curr_trial, frameN)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test_2Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test_2" ---
                for thisComponent in test_2Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('test_2.stopped', globalClock.getTime())
                # Run 'End Routine' code from test_2_code
                if buttont2 == True and lose == False:
                    #EEGdata = getEEGData()
                    EEGdata = [6, 2, 3, 4, 3]
                
                    lose = not compareFreq(EEGdata, freq_curr_trial[targets[trials_2.thisN] - 1])
                
                # the Routine "test_2" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "earth_pause_2" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('earth_pause_2.started', globalClock.getTime())
                # skip this Routine if its 'Skip if' condition is True
                continueRoutine = continueRoutine and not ((buttont2 == False) or (lose == True) or (trials_2.thisN == (trials_2.nReps - 1)))
                # keep track of which components have finished
                earth_pause_2Components = [earth_blank_3, continue_playing_message_3]
                for thisComponent in earth_pause_2Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "earth_pause_2" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *earth_blank_3* updates
                    
                    # if earth_blank_3 is starting this frame...
                    if earth_blank_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        earth_blank_3.frameNStart = frameN  # exact frame index
                        earth_blank_3.tStart = t  # local t and not account for scr refresh
                        earth_blank_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(earth_blank_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'earth_blank_3.started')
                        # update status
                        earth_blank_3.status = STARTED
                        earth_blank_3.setAutoDraw(True)
                    
                    # if earth_blank_3 is active this frame...
                    if earth_blank_3.status == STARTED:
                        # update params
                        pass
                    
                    # if earth_blank_3 is stopping this frame...
                    if earth_blank_3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > earth_blank_3.tStartRefresh + dur_blank-frameTolerance:
                            # keep track of stop time/frame for later
                            earth_blank_3.tStop = t  # not accounting for scr refresh
                            earth_blank_3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'earth_blank_3.stopped')
                            # update status
                            earth_blank_3.status = FINISHED
                            earth_blank_3.setAutoDraw(False)
                    
                    # *continue_playing_message_3* updates
                    
                    # if continue_playing_message_3 is starting this frame...
                    if continue_playing_message_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        continue_playing_message_3.frameNStart = frameN  # exact frame index
                        continue_playing_message_3.tStart = t  # local t and not account for scr refresh
                        continue_playing_message_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(continue_playing_message_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'continue_playing_message_3.started')
                        # update status
                        continue_playing_message_3.status = STARTED
                        continue_playing_message_3.setAutoDraw(True)
                    
                    # if continue_playing_message_3 is active this frame...
                    if continue_playing_message_3.status == STARTED:
                        # update params
                        pass
                    
                    # if continue_playing_message_3 is stopping this frame...
                    if continue_playing_message_3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > continue_playing_message_3.tStartRefresh + dur_blank-frameTolerance:
                            # keep track of stop time/frame for later
                            continue_playing_message_3.tStop = t  # not accounting for scr refresh
                            continue_playing_message_3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'continue_playing_message_3.stopped')
                            # update status
                            continue_playing_message_3.status = FINISHED
                            continue_playing_message_3.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in earth_pause_2Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "earth_pause_2" ---
                for thisComponent in earth_pause_2Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('earth_pause_2.stopped', globalClock.getTime())
                # the Routine "earth_pause_2" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed rep_num2 repeats of 'repetition_2'
            
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed trial_num2 repeats of 'trials_2'
        
        
        # --- Prepare to start Routine "before_test3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('before_test3.started', globalClock.getTime())
        # skip this Routine if its 'Skip if' condition is True
        continueRoutine = continueRoutine and not ((buttont1 == False) or (lose == True) or (buttont3 == False))
        # keep track of which components have finished
        before_test3Components = [earth_blank_6, continue_playing_message_6]
        for thisComponent in before_test3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "before_test3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *earth_blank_6* updates
            
            # if earth_blank_6 is starting this frame...
            if earth_blank_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                earth_blank_6.frameNStart = frameN  # exact frame index
                earth_blank_6.tStart = t  # local t and not account for scr refresh
                earth_blank_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(earth_blank_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'earth_blank_6.started')
                # update status
                earth_blank_6.status = STARTED
                earth_blank_6.setAutoDraw(True)
            
            # if earth_blank_6 is active this frame...
            if earth_blank_6.status == STARTED:
                # update params
                pass
            
            # if earth_blank_6 is stopping this frame...
            if earth_blank_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > earth_blank_6.tStartRefresh + dur_blank-frameTolerance:
                    # keep track of stop time/frame for later
                    earth_blank_6.tStop = t  # not accounting for scr refresh
                    earth_blank_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'earth_blank_6.stopped')
                    # update status
                    earth_blank_6.status = FINISHED
                    earth_blank_6.setAutoDraw(False)
            
            # *continue_playing_message_6* updates
            
            # if continue_playing_message_6 is starting this frame...
            if continue_playing_message_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                continue_playing_message_6.frameNStart = frameN  # exact frame index
                continue_playing_message_6.tStart = t  # local t and not account for scr refresh
                continue_playing_message_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continue_playing_message_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_playing_message_6.started')
                # update status
                continue_playing_message_6.status = STARTED
                continue_playing_message_6.setAutoDraw(True)
            
            # if continue_playing_message_6 is active this frame...
            if continue_playing_message_6.status == STARTED:
                # update params
                pass
            
            # if continue_playing_message_6 is stopping this frame...
            if continue_playing_message_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > continue_playing_message_6.tStartRefresh + dur_blank-frameTolerance:
                    # keep track of stop time/frame for later
                    continue_playing_message_6.tStop = t  # not accounting for scr refresh
                    continue_playing_message_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'continue_playing_message_6.stopped')
                    # update status
                    continue_playing_message_6.status = FINISHED
                    continue_playing_message_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in before_test3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "before_test3" ---
        for thisComponent in before_test3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('before_test3.stopped', globalClock.getTime())
        # the Routine "before_test3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_3 = data.TrialHandler(nReps=trial_num3, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_3')
        thisExp.addLoop(trials_3)  # add the loop to the experiment
        thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                globals()[paramName] = thisTrial_3[paramName]
        
        for thisTrial_3 in trials_3:
            currentLoop = trials_3
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
            if thisTrial_3 != None:
                for paramName in thisTrial_3:
                    globals()[paramName] = thisTrial_3[paramName]
            
            # set up handler to look after randomisation of conditions etc
            repetition_3 = data.TrialHandler(nReps=rep_num3, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='repetition_3')
            thisExp.addLoop(repetition_3)  # add the loop to the experiment
            thisRepetition_3 = repetition_3.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisRepetition_3.rgb)
            if thisRepetition_3 != None:
                for paramName in thisRepetition_3:
                    globals()[paramName] = thisRepetition_3[paramName]
            
            for thisRepetition_3 in repetition_3:
                currentLoop = repetition_3
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisRepetition_3.rgb)
                if thisRepetition_3 != None:
                    for paramName in thisRepetition_3:
                        globals()[paramName] = thisRepetition_3[paramName]
                
                # --- Prepare to start Routine "test_3" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('test_3.started', globalClock.getTime())
                # skip this Routine if its 'Skip if' condition is True
                continueRoutine = continueRoutine and not ((buttont3 == False) or (lose == True))
                # Run 'Begin Routine' code from test_3_code
                #Start aquiring data
                #startTest(dur_test3)
                
                #Target object for user to look at for each trial
                targets = [4, 2, 3, 4, 1,
                           1, 1, 1, 1, 1]
                           
                # Frequencies for each object for every trial
                freq_trials = [[10, 5,
                                2, 15], #Trial 1 frequencies
                               [10, 5,
                                2, 15], #Trial 2 frequencies
                               [10, 5,
                                2, 15], #Trial 3 frequencies
                               [10, 5,
                                2, 15], #Trial 4 frequencies
                               [10, 5,
                                2, 15], #Trial 5 frequencies
                               [10, 5,
                               2, 15], #Trial 6 frequencies
                               [10, 5,
                                2, 15], #Trial 7 frequencies
                               [10, 5,
                                2, 15], #Trial 8 frequencies
                               [10, 5,
                                2, 15], #Trial 9 frequencies
                               [10, 5,
                                2, 15]] #Trial 10 frequencies
                
                #Select frequencies for current trial
                freq_curr_trial = freq_trials[trials_3.thisN]
                
                #All objects
                objects = [boxL3_1, boxL3_2, boxL3_3, boxL3_4]
                
                #Select target object for user to look at
                selectTarget(objects, targets[trials_3.thisN])
                
                test_3_mess.text = 'Level 3, Round ' + str(trials_3.thisN + 1)
                # keep track of which components have finished
                test_3Components = [earth3, boxL3_1, shipL3_1, boxL3_2, shipL3_2, boxL3_3, shipL3_3, boxL3_4, shipL3_4, Attack_message3, test_3_mess]
                for thisComponent in test_3Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test_3" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *earth3* updates
                    
                    # if earth3 is starting this frame...
                    if earth3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        earth3.frameNStart = frameN  # exact frame index
                        earth3.tStart = t  # local t and not account for scr refresh
                        earth3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(earth3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'earth3.started')
                        # update status
                        earth3.status = STARTED
                        earth3.setAutoDraw(True)
                    
                    # if earth3 is active this frame...
                    if earth3.status == STARTED:
                        # update params
                        pass
                    
                    # if earth3 is stopping this frame...
                    if earth3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > earth3.tStartRefresh + dur_test1-frameTolerance:
                            # keep track of stop time/frame for later
                            earth3.tStop = t  # not accounting for scr refresh
                            earth3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'earth3.stopped')
                            # update status
                            earth3.status = FINISHED
                            earth3.setAutoDraw(False)
                    
                    # *boxL3_1* updates
                    
                    # if boxL3_1 is starting this frame...
                    if boxL3_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL3_1.frameNStart = frameN  # exact frame index
                        boxL3_1.tStart = t  # local t and not account for scr refresh
                        boxL3_1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL3_1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL3_1.started')
                        # update status
                        boxL3_1.status = STARTED
                        boxL3_1.setAutoDraw(True)
                    
                    # if boxL3_1 is active this frame...
                    if boxL3_1.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL3_1 is stopping this frame...
                    if boxL3_1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL3_1.tStartRefresh + dur_test3-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL3_1.tStop = t  # not accounting for scr refresh
                            boxL3_1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL3_1.stopped')
                            # update status
                            boxL3_1.status = FINISHED
                            boxL3_1.setAutoDraw(False)
                    
                    # *shipL3_1* updates
                    
                    # if shipL3_1 is starting this frame...
                    if shipL3_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL3_1.frameNStart = frameN  # exact frame index
                        shipL3_1.tStart = t  # local t and not account for scr refresh
                        shipL3_1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL3_1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL3_1.started')
                        # update status
                        shipL3_1.status = STARTED
                        shipL3_1.setAutoDraw(True)
                    
                    # if shipL3_1 is active this frame...
                    if shipL3_1.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL3_1 is stopping this frame...
                    if shipL3_1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL3_1.tStartRefresh + dur_test3-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL3_1.tStop = t  # not accounting for scr refresh
                            shipL3_1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL3_1.stopped')
                            # update status
                            shipL3_1.status = FINISHED
                            shipL3_1.setAutoDraw(False)
                    
                    # *boxL3_2* updates
                    
                    # if boxL3_2 is starting this frame...
                    if boxL3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL3_2.frameNStart = frameN  # exact frame index
                        boxL3_2.tStart = t  # local t and not account for scr refresh
                        boxL3_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL3_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL3_2.started')
                        # update status
                        boxL3_2.status = STARTED
                        boxL3_2.setAutoDraw(True)
                    
                    # if boxL3_2 is active this frame...
                    if boxL3_2.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL3_2 is stopping this frame...
                    if boxL3_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL3_2.tStartRefresh + dur_test3-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL3_2.tStop = t  # not accounting for scr refresh
                            boxL3_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL3_2.stopped')
                            # update status
                            boxL3_2.status = FINISHED
                            boxL3_2.setAutoDraw(False)
                    
                    # *shipL3_2* updates
                    
                    # if shipL3_2 is starting this frame...
                    if shipL3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL3_2.frameNStart = frameN  # exact frame index
                        shipL3_2.tStart = t  # local t and not account for scr refresh
                        shipL3_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL3_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL3_2.started')
                        # update status
                        shipL3_2.status = STARTED
                        shipL3_2.setAutoDraw(True)
                    
                    # if shipL3_2 is active this frame...
                    if shipL3_2.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL3_2 is stopping this frame...
                    if shipL3_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL3_2.tStartRefresh + dur_test3-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL3_2.tStop = t  # not accounting for scr refresh
                            shipL3_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL3_2.stopped')
                            # update status
                            shipL3_2.status = FINISHED
                            shipL3_2.setAutoDraw(False)
                    
                    # *boxL3_3* updates
                    
                    # if boxL3_3 is starting this frame...
                    if boxL3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL3_3.frameNStart = frameN  # exact frame index
                        boxL3_3.tStart = t  # local t and not account for scr refresh
                        boxL3_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL3_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL3_3.started')
                        # update status
                        boxL3_3.status = STARTED
                        boxL3_3.setAutoDraw(True)
                    
                    # if boxL3_3 is active this frame...
                    if boxL3_3.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL3_3 is stopping this frame...
                    if boxL3_3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL3_3.tStartRefresh + dur_test3-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL3_3.tStop = t  # not accounting for scr refresh
                            boxL3_3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL3_3.stopped')
                            # update status
                            boxL3_3.status = FINISHED
                            boxL3_3.setAutoDraw(False)
                    
                    # *shipL3_3* updates
                    
                    # if shipL3_3 is starting this frame...
                    if shipL3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL3_3.frameNStart = frameN  # exact frame index
                        shipL3_3.tStart = t  # local t and not account for scr refresh
                        shipL3_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL3_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL3_3.started')
                        # update status
                        shipL3_3.status = STARTED
                        shipL3_3.setAutoDraw(True)
                    
                    # if shipL3_3 is active this frame...
                    if shipL3_3.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL3_3 is stopping this frame...
                    if shipL3_3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL3_3.tStartRefresh + dur_test3-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL3_3.tStop = t  # not accounting for scr refresh
                            shipL3_3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL3_3.stopped')
                            # update status
                            shipL3_3.status = FINISHED
                            shipL3_3.setAutoDraw(False)
                    
                    # *boxL3_4* updates
                    
                    # if boxL3_4 is starting this frame...
                    if boxL3_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL3_4.frameNStart = frameN  # exact frame index
                        boxL3_4.tStart = t  # local t and not account for scr refresh
                        boxL3_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL3_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL3_4.started')
                        # update status
                        boxL3_4.status = STARTED
                        boxL3_4.setAutoDraw(True)
                    
                    # if boxL3_4 is active this frame...
                    if boxL3_4.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL3_4 is stopping this frame...
                    if boxL3_4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL3_4.tStartRefresh + dur_test3-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL3_4.tStop = t  # not accounting for scr refresh
                            boxL3_4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL3_4.stopped')
                            # update status
                            boxL3_4.status = FINISHED
                            boxL3_4.setAutoDraw(False)
                    
                    # *shipL3_4* updates
                    
                    # if shipL3_4 is starting this frame...
                    if shipL3_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL3_4.frameNStart = frameN  # exact frame index
                        shipL3_4.tStart = t  # local t and not account for scr refresh
                        shipL3_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL3_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL3_4.started')
                        # update status
                        shipL3_4.status = STARTED
                        shipL3_4.setAutoDraw(True)
                    
                    # if shipL3_4 is active this frame...
                    if shipL3_4.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL3_4 is stopping this frame...
                    if shipL3_4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL3_4.tStartRefresh + dur_test3-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL3_4.tStop = t  # not accounting for scr refresh
                            shipL3_4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL3_4.stopped')
                            # update status
                            shipL3_4.status = FINISHED
                            shipL3_4.setAutoDraw(False)
                    
                    # *Attack_message3* updates
                    
                    # if Attack_message3 is starting this frame...
                    if Attack_message3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        Attack_message3.frameNStart = frameN  # exact frame index
                        Attack_message3.tStart = t  # local t and not account for scr refresh
                        Attack_message3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Attack_message3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Attack_message3.started')
                        # update status
                        Attack_message3.status = STARTED
                        Attack_message3.setAutoDraw(True)
                    
                    # if Attack_message3 is active this frame...
                    if Attack_message3.status == STARTED:
                        # update params
                        pass
                    
                    # if Attack_message3 is stopping this frame...
                    if Attack_message3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Attack_message3.tStartRefresh + dur_test1-frameTolerance:
                            # keep track of stop time/frame for later
                            Attack_message3.tStop = t  # not accounting for scr refresh
                            Attack_message3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Attack_message3.stopped')
                            # update status
                            Attack_message3.status = FINISHED
                            Attack_message3.setAutoDraw(False)
                    
                    # *test_3_mess* updates
                    
                    # if test_3_mess is starting this frame...
                    if test_3_mess.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        test_3_mess.frameNStart = frameN  # exact frame index
                        test_3_mess.tStart = t  # local t and not account for scr refresh
                        test_3_mess.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(test_3_mess, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'test_3_mess.started')
                        # update status
                        test_3_mess.status = STARTED
                        test_3_mess.setAutoDraw(True)
                    
                    # if test_3_mess is active this frame...
                    if test_3_mess.status == STARTED:
                        # update params
                        pass
                    
                    # if test_3_mess is stopping this frame...
                    if test_3_mess.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > test_3_mess.tStartRefresh + dur_test3-frameTolerance:
                            # keep track of stop time/frame for later
                            test_3_mess.tStop = t  # not accounting for scr refresh
                            test_3_mess.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'test_3_mess.stopped')
                            # update status
                            test_3_mess.status = FINISHED
                            test_3_mess.setAutoDraw(False)
                    # Run 'Each Frame' code from test_3_code
                    #Flicker objects are set frequencies
                    flickerObjects(objects, freq_curr_trial, frameN)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test_3Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test_3" ---
                for thisComponent in test_3Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('test_3.stopped', globalClock.getTime())
                # Run 'End Routine' code from test_3_code
                if buttont3 == True and lose == False:
                    #EEGdata = getEEGData()
                    EEGdata = [6, 2, 3, 4, 3]
                    lose = not compareFreq(EEGdata, freq_curr_trial[targets[trials_3.thisN] - 1])
                # the Routine "test_3" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "earth_pause_3" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('earth_pause_3.started', globalClock.getTime())
                # skip this Routine if its 'Skip if' condition is True
                continueRoutine = continueRoutine and not ((buttont3 == False) or (lose == True) or (trials_3.thisN == (trials_3.nReps - 1)))
                # keep track of which components have finished
                earth_pause_3Components = [earth_blank_2, continue_playing_message_2]
                for thisComponent in earth_pause_3Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "earth_pause_3" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *earth_blank_2* updates
                    
                    # if earth_blank_2 is starting this frame...
                    if earth_blank_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        earth_blank_2.frameNStart = frameN  # exact frame index
                        earth_blank_2.tStart = t  # local t and not account for scr refresh
                        earth_blank_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(earth_blank_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'earth_blank_2.started')
                        # update status
                        earth_blank_2.status = STARTED
                        earth_blank_2.setAutoDraw(True)
                    
                    # if earth_blank_2 is active this frame...
                    if earth_blank_2.status == STARTED:
                        # update params
                        pass
                    
                    # if earth_blank_2 is stopping this frame...
                    if earth_blank_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > earth_blank_2.tStartRefresh + dur_blank-frameTolerance:
                            # keep track of stop time/frame for later
                            earth_blank_2.tStop = t  # not accounting for scr refresh
                            earth_blank_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'earth_blank_2.stopped')
                            # update status
                            earth_blank_2.status = FINISHED
                            earth_blank_2.setAutoDraw(False)
                    
                    # *continue_playing_message_2* updates
                    
                    # if continue_playing_message_2 is starting this frame...
                    if continue_playing_message_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        continue_playing_message_2.frameNStart = frameN  # exact frame index
                        continue_playing_message_2.tStart = t  # local t and not account for scr refresh
                        continue_playing_message_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(continue_playing_message_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'continue_playing_message_2.started')
                        # update status
                        continue_playing_message_2.status = STARTED
                        continue_playing_message_2.setAutoDraw(True)
                    
                    # if continue_playing_message_2 is active this frame...
                    if continue_playing_message_2.status == STARTED:
                        # update params
                        pass
                    
                    # if continue_playing_message_2 is stopping this frame...
                    if continue_playing_message_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > continue_playing_message_2.tStartRefresh + dur_blank-frameTolerance:
                            # keep track of stop time/frame for later
                            continue_playing_message_2.tStop = t  # not accounting for scr refresh
                            continue_playing_message_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'continue_playing_message_2.stopped')
                            # update status
                            continue_playing_message_2.status = FINISHED
                            continue_playing_message_2.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in earth_pause_3Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "earth_pause_3" ---
                for thisComponent in earth_pause_3Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('earth_pause_3.stopped', globalClock.getTime())
                # the Routine "earth_pause_3" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed rep_num3 repeats of 'repetition_3'
            
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed trial_num3 repeats of 'trials_3'
        
        
        # --- Prepare to start Routine "before_test4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('before_test4.started', globalClock.getTime())
        # skip this Routine if its 'Skip if' condition is True
        continueRoutine = continueRoutine and not ((buttont1 == False) or (lose == True) or (buttont4 == False))
        # keep track of which components have finished
        before_test4Components = [earth_blank_7, continue_playing_message_7]
        for thisComponent in before_test4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "before_test4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *earth_blank_7* updates
            
            # if earth_blank_7 is starting this frame...
            if earth_blank_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                earth_blank_7.frameNStart = frameN  # exact frame index
                earth_blank_7.tStart = t  # local t and not account for scr refresh
                earth_blank_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(earth_blank_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'earth_blank_7.started')
                # update status
                earth_blank_7.status = STARTED
                earth_blank_7.setAutoDraw(True)
            
            # if earth_blank_7 is active this frame...
            if earth_blank_7.status == STARTED:
                # update params
                pass
            
            # if earth_blank_7 is stopping this frame...
            if earth_blank_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > earth_blank_7.tStartRefresh + dur_blank-frameTolerance:
                    # keep track of stop time/frame for later
                    earth_blank_7.tStop = t  # not accounting for scr refresh
                    earth_blank_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'earth_blank_7.stopped')
                    # update status
                    earth_blank_7.status = FINISHED
                    earth_blank_7.setAutoDraw(False)
            
            # *continue_playing_message_7* updates
            
            # if continue_playing_message_7 is starting this frame...
            if continue_playing_message_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                continue_playing_message_7.frameNStart = frameN  # exact frame index
                continue_playing_message_7.tStart = t  # local t and not account for scr refresh
                continue_playing_message_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continue_playing_message_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_playing_message_7.started')
                # update status
                continue_playing_message_7.status = STARTED
                continue_playing_message_7.setAutoDraw(True)
            
            # if continue_playing_message_7 is active this frame...
            if continue_playing_message_7.status == STARTED:
                # update params
                pass
            
            # if continue_playing_message_7 is stopping this frame...
            if continue_playing_message_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > continue_playing_message_7.tStartRefresh + dur_blank-frameTolerance:
                    # keep track of stop time/frame for later
                    continue_playing_message_7.tStop = t  # not accounting for scr refresh
                    continue_playing_message_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'continue_playing_message_7.stopped')
                    # update status
                    continue_playing_message_7.status = FINISHED
                    continue_playing_message_7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in before_test4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "before_test4" ---
        for thisComponent in before_test4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('before_test4.stopped', globalClock.getTime())
        # the Routine "before_test4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_4 = data.TrialHandler(nReps=trial_num4, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_4')
        thisExp.addLoop(trials_4)  # add the loop to the experiment
        thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                globals()[paramName] = thisTrial_4[paramName]
        
        for thisTrial_4 in trials_4:
            currentLoop = trials_4
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
            if thisTrial_4 != None:
                for paramName in thisTrial_4:
                    globals()[paramName] = thisTrial_4[paramName]
            
            # set up handler to look after randomisation of conditions etc
            repetition_4 = data.TrialHandler(nReps=rep_num4, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='repetition_4')
            thisExp.addLoop(repetition_4)  # add the loop to the experiment
            thisRepetition_4 = repetition_4.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisRepetition_4.rgb)
            if thisRepetition_4 != None:
                for paramName in thisRepetition_4:
                    globals()[paramName] = thisRepetition_4[paramName]
            
            for thisRepetition_4 in repetition_4:
                currentLoop = repetition_4
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisRepetition_4.rgb)
                if thisRepetition_4 != None:
                    for paramName in thisRepetition_4:
                        globals()[paramName] = thisRepetition_4[paramName]
                
                # --- Prepare to start Routine "test_4" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('test_4.started', globalClock.getTime())
                # skip this Routine if its 'Skip if' condition is True
                continueRoutine = continueRoutine and not ((buttont4 == False) or (lose == True))
                # Run 'Begin Routine' code from test_4_code
                #Start aquiring data
                #startTest(dur_test4)
                
                #Target object for user to look at for each trial
                targets = [2, 2, 3, 4, 5,
                           6, 7, 8, 9, 1]
                
                # Frequencies for each object
                freq_trials = [[10, 5, 2,
                                1, 8, 12,
                                20, 25, 30],#Trial 1 frequencies
                                [10, 5, 2,
                                1, 8, 12,
                                20, 25, 30], #Trial 2 frequencies
                                [10, 5, 2,
                                1, 8, 12,
                                20, 25, 30], #Trial 3 frequencies
                                [10, 5, 2,
                                1, 8, 12,
                                20, 25, 30], #Trial 4 frequencies
                                [10, 5, 2,
                                1, 8, 12,
                                20, 25, 30], #Trial 5 frequencies
                                [10, 5, 2,
                                1, 8, 12,
                                20, 25, 30], #Trial 6 frequencies
                                [10, 5, 2,
                                1, 8, 12,
                                20, 25, 30], #Trial 7 frequencies
                                [10, 5, 2,
                                1, 8, 12,
                                20, 25, 30], #Trial 8 frequencies
                                [10, 5, 2,
                                1, 8, 12,
                                20, 25, 30], #Trial 9 frequencies
                               [10, 5, 2,
                                1, 8, 12,
                                20, 25, 30]] #Trial 10 frequencies
                                
                #All objects
                objects = [boxL4_1, boxL4_2, boxL4_3,
                           boxL4_4, boxL4_5, boxL4_6,
                           boxL4_7, boxL4_8, boxL4_9]
                
                #Select frequencies for current trial
                freq_curr_trial = freq_trials[trials_4.thisN]
                
                #Select target object for user to look at
                selectTarget(objects, targets[trials_4.thisN])
                
                test_4_mess.text = 'Level 4, Round ' + str(trials_4.thisN + 1)
                # keep track of which components have finished
                test_4Components = [earth4, boxL4_1, shipL4_1, boxL4_2, shipL4_2, boxL4_3, shipL4_3, boxL4_4, shipL4_4, boxL4_5, shipL4_5, boxL4_6, shipL4_6, boxL4_7, shipL4_7, boxL4_8, shipL4_8, boxL4_9, shipL4_9, Attack_message4, test_4_mess]
                for thisComponent in test_4Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test_4" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *earth4* updates
                    
                    # if earth4 is starting this frame...
                    if earth4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        earth4.frameNStart = frameN  # exact frame index
                        earth4.tStart = t  # local t and not account for scr refresh
                        earth4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(earth4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'earth4.started')
                        # update status
                        earth4.status = STARTED
                        earth4.setAutoDraw(True)
                    
                    # if earth4 is active this frame...
                    if earth4.status == STARTED:
                        # update params
                        pass
                    
                    # if earth4 is stopping this frame...
                    if earth4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > earth4.tStartRefresh + dur_test1-frameTolerance:
                            # keep track of stop time/frame for later
                            earth4.tStop = t  # not accounting for scr refresh
                            earth4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'earth4.stopped')
                            # update status
                            earth4.status = FINISHED
                            earth4.setAutoDraw(False)
                    
                    # *boxL4_1* updates
                    
                    # if boxL4_1 is starting this frame...
                    if boxL4_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL4_1.frameNStart = frameN  # exact frame index
                        boxL4_1.tStart = t  # local t and not account for scr refresh
                        boxL4_1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL4_1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL4_1.started')
                        # update status
                        boxL4_1.status = STARTED
                        boxL4_1.setAutoDraw(True)
                    
                    # if boxL4_1 is active this frame...
                    if boxL4_1.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL4_1 is stopping this frame...
                    if boxL4_1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL4_1.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL4_1.tStop = t  # not accounting for scr refresh
                            boxL4_1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL4_1.stopped')
                            # update status
                            boxL4_1.status = FINISHED
                            boxL4_1.setAutoDraw(False)
                    
                    # *shipL4_1* updates
                    
                    # if shipL4_1 is starting this frame...
                    if shipL4_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL4_1.frameNStart = frameN  # exact frame index
                        shipL4_1.tStart = t  # local t and not account for scr refresh
                        shipL4_1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL4_1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL4_1.started')
                        # update status
                        shipL4_1.status = STARTED
                        shipL4_1.setAutoDraw(True)
                    
                    # if shipL4_1 is active this frame...
                    if shipL4_1.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL4_1 is stopping this frame...
                    if shipL4_1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL4_1.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL4_1.tStop = t  # not accounting for scr refresh
                            shipL4_1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL4_1.stopped')
                            # update status
                            shipL4_1.status = FINISHED
                            shipL4_1.setAutoDraw(False)
                    
                    # *boxL4_2* updates
                    
                    # if boxL4_2 is starting this frame...
                    if boxL4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL4_2.frameNStart = frameN  # exact frame index
                        boxL4_2.tStart = t  # local t and not account for scr refresh
                        boxL4_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL4_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL4_2.started')
                        # update status
                        boxL4_2.status = STARTED
                        boxL4_2.setAutoDraw(True)
                    
                    # if boxL4_2 is active this frame...
                    if boxL4_2.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL4_2 is stopping this frame...
                    if boxL4_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL4_2.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL4_2.tStop = t  # not accounting for scr refresh
                            boxL4_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL4_2.stopped')
                            # update status
                            boxL4_2.status = FINISHED
                            boxL4_2.setAutoDraw(False)
                    
                    # *shipL4_2* updates
                    
                    # if shipL4_2 is starting this frame...
                    if shipL4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL4_2.frameNStart = frameN  # exact frame index
                        shipL4_2.tStart = t  # local t and not account for scr refresh
                        shipL4_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL4_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL4_2.started')
                        # update status
                        shipL4_2.status = STARTED
                        shipL4_2.setAutoDraw(True)
                    
                    # if shipL4_2 is active this frame...
                    if shipL4_2.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL4_2 is stopping this frame...
                    if shipL4_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL4_2.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL4_2.tStop = t  # not accounting for scr refresh
                            shipL4_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL4_2.stopped')
                            # update status
                            shipL4_2.status = FINISHED
                            shipL4_2.setAutoDraw(False)
                    
                    # *boxL4_3* updates
                    
                    # if boxL4_3 is starting this frame...
                    if boxL4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL4_3.frameNStart = frameN  # exact frame index
                        boxL4_3.tStart = t  # local t and not account for scr refresh
                        boxL4_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL4_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL4_3.started')
                        # update status
                        boxL4_3.status = STARTED
                        boxL4_3.setAutoDraw(True)
                    
                    # if boxL4_3 is active this frame...
                    if boxL4_3.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL4_3 is stopping this frame...
                    if boxL4_3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL4_3.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL4_3.tStop = t  # not accounting for scr refresh
                            boxL4_3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL4_3.stopped')
                            # update status
                            boxL4_3.status = FINISHED
                            boxL4_3.setAutoDraw(False)
                    
                    # *shipL4_3* updates
                    
                    # if shipL4_3 is starting this frame...
                    if shipL4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL4_3.frameNStart = frameN  # exact frame index
                        shipL4_3.tStart = t  # local t and not account for scr refresh
                        shipL4_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL4_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL4_3.started')
                        # update status
                        shipL4_3.status = STARTED
                        shipL4_3.setAutoDraw(True)
                    
                    # if shipL4_3 is active this frame...
                    if shipL4_3.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL4_3 is stopping this frame...
                    if shipL4_3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL4_3.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL4_3.tStop = t  # not accounting for scr refresh
                            shipL4_3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL4_3.stopped')
                            # update status
                            shipL4_3.status = FINISHED
                            shipL4_3.setAutoDraw(False)
                    
                    # *boxL4_4* updates
                    
                    # if boxL4_4 is starting this frame...
                    if boxL4_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL4_4.frameNStart = frameN  # exact frame index
                        boxL4_4.tStart = t  # local t and not account for scr refresh
                        boxL4_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL4_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL4_4.started')
                        # update status
                        boxL4_4.status = STARTED
                        boxL4_4.setAutoDraw(True)
                    
                    # if boxL4_4 is active this frame...
                    if boxL4_4.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL4_4 is stopping this frame...
                    if boxL4_4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL4_4.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL4_4.tStop = t  # not accounting for scr refresh
                            boxL4_4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL4_4.stopped')
                            # update status
                            boxL4_4.status = FINISHED
                            boxL4_4.setAutoDraw(False)
                    
                    # *shipL4_4* updates
                    
                    # if shipL4_4 is starting this frame...
                    if shipL4_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL4_4.frameNStart = frameN  # exact frame index
                        shipL4_4.tStart = t  # local t and not account for scr refresh
                        shipL4_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL4_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL4_4.started')
                        # update status
                        shipL4_4.status = STARTED
                        shipL4_4.setAutoDraw(True)
                    
                    # if shipL4_4 is active this frame...
                    if shipL4_4.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL4_4 is stopping this frame...
                    if shipL4_4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL4_4.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL4_4.tStop = t  # not accounting for scr refresh
                            shipL4_4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL4_4.stopped')
                            # update status
                            shipL4_4.status = FINISHED
                            shipL4_4.setAutoDraw(False)
                    
                    # *boxL4_5* updates
                    
                    # if boxL4_5 is starting this frame...
                    if boxL4_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL4_5.frameNStart = frameN  # exact frame index
                        boxL4_5.tStart = t  # local t and not account for scr refresh
                        boxL4_5.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL4_5, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL4_5.started')
                        # update status
                        boxL4_5.status = STARTED
                        boxL4_5.setAutoDraw(True)
                    
                    # if boxL4_5 is active this frame...
                    if boxL4_5.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL4_5 is stopping this frame...
                    if boxL4_5.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL4_5.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL4_5.tStop = t  # not accounting for scr refresh
                            boxL4_5.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL4_5.stopped')
                            # update status
                            boxL4_5.status = FINISHED
                            boxL4_5.setAutoDraw(False)
                    
                    # *shipL4_5* updates
                    
                    # if shipL4_5 is starting this frame...
                    if shipL4_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL4_5.frameNStart = frameN  # exact frame index
                        shipL4_5.tStart = t  # local t and not account for scr refresh
                        shipL4_5.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL4_5, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL4_5.started')
                        # update status
                        shipL4_5.status = STARTED
                        shipL4_5.setAutoDraw(True)
                    
                    # if shipL4_5 is active this frame...
                    if shipL4_5.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL4_5 is stopping this frame...
                    if shipL4_5.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL4_5.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL4_5.tStop = t  # not accounting for scr refresh
                            shipL4_5.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL4_5.stopped')
                            # update status
                            shipL4_5.status = FINISHED
                            shipL4_5.setAutoDraw(False)
                    
                    # *boxL4_6* updates
                    
                    # if boxL4_6 is starting this frame...
                    if boxL4_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL4_6.frameNStart = frameN  # exact frame index
                        boxL4_6.tStart = t  # local t and not account for scr refresh
                        boxL4_6.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL4_6, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL4_6.started')
                        # update status
                        boxL4_6.status = STARTED
                        boxL4_6.setAutoDraw(True)
                    
                    # if boxL4_6 is active this frame...
                    if boxL4_6.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL4_6 is stopping this frame...
                    if boxL4_6.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL4_6.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL4_6.tStop = t  # not accounting for scr refresh
                            boxL4_6.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL4_6.stopped')
                            # update status
                            boxL4_6.status = FINISHED
                            boxL4_6.setAutoDraw(False)
                    
                    # *shipL4_6* updates
                    
                    # if shipL4_6 is starting this frame...
                    if shipL4_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL4_6.frameNStart = frameN  # exact frame index
                        shipL4_6.tStart = t  # local t and not account for scr refresh
                        shipL4_6.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL4_6, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL4_6.started')
                        # update status
                        shipL4_6.status = STARTED
                        shipL4_6.setAutoDraw(True)
                    
                    # if shipL4_6 is active this frame...
                    if shipL4_6.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL4_6 is stopping this frame...
                    if shipL4_6.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL4_6.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL4_6.tStop = t  # not accounting for scr refresh
                            shipL4_6.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL4_6.stopped')
                            # update status
                            shipL4_6.status = FINISHED
                            shipL4_6.setAutoDraw(False)
                    
                    # *boxL4_7* updates
                    
                    # if boxL4_7 is starting this frame...
                    if boxL4_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL4_7.frameNStart = frameN  # exact frame index
                        boxL4_7.tStart = t  # local t and not account for scr refresh
                        boxL4_7.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL4_7, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL4_7.started')
                        # update status
                        boxL4_7.status = STARTED
                        boxL4_7.setAutoDraw(True)
                    
                    # if boxL4_7 is active this frame...
                    if boxL4_7.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL4_7 is stopping this frame...
                    if boxL4_7.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL4_7.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL4_7.tStop = t  # not accounting for scr refresh
                            boxL4_7.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL4_7.stopped')
                            # update status
                            boxL4_7.status = FINISHED
                            boxL4_7.setAutoDraw(False)
                    
                    # *shipL4_7* updates
                    
                    # if shipL4_7 is starting this frame...
                    if shipL4_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL4_7.frameNStart = frameN  # exact frame index
                        shipL4_7.tStart = t  # local t and not account for scr refresh
                        shipL4_7.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL4_7, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL4_7.started')
                        # update status
                        shipL4_7.status = STARTED
                        shipL4_7.setAutoDraw(True)
                    
                    # if shipL4_7 is active this frame...
                    if shipL4_7.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL4_7 is stopping this frame...
                    if shipL4_7.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL4_7.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL4_7.tStop = t  # not accounting for scr refresh
                            shipL4_7.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL4_7.stopped')
                            # update status
                            shipL4_7.status = FINISHED
                            shipL4_7.setAutoDraw(False)
                    
                    # *boxL4_8* updates
                    
                    # if boxL4_8 is starting this frame...
                    if boxL4_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL4_8.frameNStart = frameN  # exact frame index
                        boxL4_8.tStart = t  # local t and not account for scr refresh
                        boxL4_8.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL4_8, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL4_8.started')
                        # update status
                        boxL4_8.status = STARTED
                        boxL4_8.setAutoDraw(True)
                    
                    # if boxL4_8 is active this frame...
                    if boxL4_8.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL4_8 is stopping this frame...
                    if boxL4_8.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL4_8.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL4_8.tStop = t  # not accounting for scr refresh
                            boxL4_8.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL4_8.stopped')
                            # update status
                            boxL4_8.status = FINISHED
                            boxL4_8.setAutoDraw(False)
                    
                    # *shipL4_8* updates
                    
                    # if shipL4_8 is starting this frame...
                    if shipL4_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL4_8.frameNStart = frameN  # exact frame index
                        shipL4_8.tStart = t  # local t and not account for scr refresh
                        shipL4_8.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL4_8, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL4_8.started')
                        # update status
                        shipL4_8.status = STARTED
                        shipL4_8.setAutoDraw(True)
                    
                    # if shipL4_8 is active this frame...
                    if shipL4_8.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL4_8 is stopping this frame...
                    if shipL4_8.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL4_8.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL4_8.tStop = t  # not accounting for scr refresh
                            shipL4_8.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL4_8.stopped')
                            # update status
                            shipL4_8.status = FINISHED
                            shipL4_8.setAutoDraw(False)
                    
                    # *boxL4_9* updates
                    
                    # if boxL4_9 is starting this frame...
                    if boxL4_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        boxL4_9.frameNStart = frameN  # exact frame index
                        boxL4_9.tStart = t  # local t and not account for scr refresh
                        boxL4_9.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(boxL4_9, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'boxL4_9.started')
                        # update status
                        boxL4_9.status = STARTED
                        boxL4_9.setAutoDraw(True)
                    
                    # if boxL4_9 is active this frame...
                    if boxL4_9.status == STARTED:
                        # update params
                        pass
                    
                    # if boxL4_9 is stopping this frame...
                    if boxL4_9.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > boxL4_9.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            boxL4_9.tStop = t  # not accounting for scr refresh
                            boxL4_9.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'boxL4_9.stopped')
                            # update status
                            boxL4_9.status = FINISHED
                            boxL4_9.setAutoDraw(False)
                    
                    # *shipL4_9* updates
                    
                    # if shipL4_9 is starting this frame...
                    if shipL4_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        shipL4_9.frameNStart = frameN  # exact frame index
                        shipL4_9.tStart = t  # local t and not account for scr refresh
                        shipL4_9.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(shipL4_9, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'shipL4_9.started')
                        # update status
                        shipL4_9.status = STARTED
                        shipL4_9.setAutoDraw(True)
                    
                    # if shipL4_9 is active this frame...
                    if shipL4_9.status == STARTED:
                        # update params
                        pass
                    
                    # if shipL4_9 is stopping this frame...
                    if shipL4_9.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > shipL4_9.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            shipL4_9.tStop = t  # not accounting for scr refresh
                            shipL4_9.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'shipL4_9.stopped')
                            # update status
                            shipL4_9.status = FINISHED
                            shipL4_9.setAutoDraw(False)
                    
                    # *Attack_message4* updates
                    
                    # if Attack_message4 is starting this frame...
                    if Attack_message4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        Attack_message4.frameNStart = frameN  # exact frame index
                        Attack_message4.tStart = t  # local t and not account for scr refresh
                        Attack_message4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Attack_message4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Attack_message4.started')
                        # update status
                        Attack_message4.status = STARTED
                        Attack_message4.setAutoDraw(True)
                    
                    # if Attack_message4 is active this frame...
                    if Attack_message4.status == STARTED:
                        # update params
                        pass
                    
                    # if Attack_message4 is stopping this frame...
                    if Attack_message4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Attack_message4.tStartRefresh + dur_test1-frameTolerance:
                            # keep track of stop time/frame for later
                            Attack_message4.tStop = t  # not accounting for scr refresh
                            Attack_message4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Attack_message4.stopped')
                            # update status
                            Attack_message4.status = FINISHED
                            Attack_message4.setAutoDraw(False)
                    
                    # *test_4_mess* updates
                    
                    # if test_4_mess is starting this frame...
                    if test_4_mess.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        test_4_mess.frameNStart = frameN  # exact frame index
                        test_4_mess.tStart = t  # local t and not account for scr refresh
                        test_4_mess.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(test_4_mess, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'test_4_mess.started')
                        # update status
                        test_4_mess.status = STARTED
                        test_4_mess.setAutoDraw(True)
                    
                    # if test_4_mess is active this frame...
                    if test_4_mess.status == STARTED:
                        # update params
                        pass
                    
                    # if test_4_mess is stopping this frame...
                    if test_4_mess.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > test_4_mess.tStartRefresh + dur_test4-frameTolerance:
                            # keep track of stop time/frame for later
                            test_4_mess.tStop = t  # not accounting for scr refresh
                            test_4_mess.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'test_4_mess.stopped')
                            # update status
                            test_4_mess.status = FINISHED
                            test_4_mess.setAutoDraw(False)
                    # Run 'Each Frame' code from test_4_code
                    #Flicker objects are set frequencies
                    flickerObjects(objects, freq_curr_trial, frameN)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test_4Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test_4" ---
                for thisComponent in test_4Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('test_4.stopped', globalClock.getTime())
                # Run 'End Routine' code from test_4_code
                if buttont4 == True and lose == False:
                    #EEGdata = getEEGData()
                    EEGdata = [6, 10, 3, 8, 3]
                    lose = not compareFreq(EEGdata, freq_curr_trial[targets[trials_4.thisN] - 1])
                    #lose = not compareFreq(EEGdata, 5)
                # the Routine "test_4" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "earth_pause_4" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('earth_pause_4.started', globalClock.getTime())
                # skip this Routine if its 'Skip if' condition is True
                continueRoutine = continueRoutine and not ((buttont4 == False) or (lose == True) or (trials_4.thisN == (trials_4.nReps - 1)))
                # keep track of which components have finished
                earth_pause_4Components = [earth_blank, continue_playing_message]
                for thisComponent in earth_pause_4Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "earth_pause_4" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *earth_blank* updates
                    
                    # if earth_blank is starting this frame...
                    if earth_blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        earth_blank.frameNStart = frameN  # exact frame index
                        earth_blank.tStart = t  # local t and not account for scr refresh
                        earth_blank.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(earth_blank, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'earth_blank.started')
                        # update status
                        earth_blank.status = STARTED
                        earth_blank.setAutoDraw(True)
                    
                    # if earth_blank is active this frame...
                    if earth_blank.status == STARTED:
                        # update params
                        pass
                    
                    # if earth_blank is stopping this frame...
                    if earth_blank.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > earth_blank.tStartRefresh + dur_blank-frameTolerance:
                            # keep track of stop time/frame for later
                            earth_blank.tStop = t  # not accounting for scr refresh
                            earth_blank.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'earth_blank.stopped')
                            # update status
                            earth_blank.status = FINISHED
                            earth_blank.setAutoDraw(False)
                    
                    # *continue_playing_message* updates
                    
                    # if continue_playing_message is starting this frame...
                    if continue_playing_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        continue_playing_message.frameNStart = frameN  # exact frame index
                        continue_playing_message.tStart = t  # local t and not account for scr refresh
                        continue_playing_message.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(continue_playing_message, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'continue_playing_message.started')
                        # update status
                        continue_playing_message.status = STARTED
                        continue_playing_message.setAutoDraw(True)
                    
                    # if continue_playing_message is active this frame...
                    if continue_playing_message.status == STARTED:
                        # update params
                        pass
                    
                    # if continue_playing_message is stopping this frame...
                    if continue_playing_message.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > continue_playing_message.tStartRefresh + dur_blank-frameTolerance:
                            # keep track of stop time/frame for later
                            continue_playing_message.tStop = t  # not accounting for scr refresh
                            continue_playing_message.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'continue_playing_message.stopped')
                            # update status
                            continue_playing_message.status = FINISHED
                            continue_playing_message.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in earth_pause_4Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "earth_pause_4" ---
                for thisComponent in earth_pause_4Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('earth_pause_4.stopped', globalClock.getTime())
                # the Routine "earth_pause_4" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed rep_num4 repeats of 'repetition_4'
            
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed trial_num4 repeats of 'trials_4'
        
        
        # --- Prepare to start Routine "earth_win" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('earth_win.started', globalClock.getTime())
        # skip this Routine if its 'Skip if' condition is True
        continueRoutine = continueRoutine and not (lose == True)
        # keep track of which components have finished
        earth_winComponents = [earth_win_2, win_message]
        for thisComponent in earth_winComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "earth_win" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *earth_win_2* updates
            
            # if earth_win_2 is starting this frame...
            if earth_win_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                earth_win_2.frameNStart = frameN  # exact frame index
                earth_win_2.tStart = t  # local t and not account for scr refresh
                earth_win_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(earth_win_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'earth_win_2.started')
                # update status
                earth_win_2.status = STARTED
                earth_win_2.setAutoDraw(True)
            
            # if earth_win_2 is active this frame...
            if earth_win_2.status == STARTED:
                # update params
                pass
            
            # if earth_win_2 is stopping this frame...
            if earth_win_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > earth_win_2.tStartRefresh + dur_end-frameTolerance:
                    # keep track of stop time/frame for later
                    earth_win_2.tStop = t  # not accounting for scr refresh
                    earth_win_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'earth_win_2.stopped')
                    # update status
                    earth_win_2.status = FINISHED
                    earth_win_2.setAutoDraw(False)
            
            # *win_message* updates
            
            # if win_message is starting this frame...
            if win_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                win_message.frameNStart = frameN  # exact frame index
                win_message.tStart = t  # local t and not account for scr refresh
                win_message.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(win_message, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'win_message.started')
                # update status
                win_message.status = STARTED
                win_message.setAutoDraw(True)
            
            # if win_message is active this frame...
            if win_message.status == STARTED:
                # update params
                pass
            
            # if win_message is stopping this frame...
            if win_message.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > win_message.tStartRefresh + dur_end-frameTolerance:
                    # keep track of stop time/frame for later
                    win_message.tStop = t  # not accounting for scr refresh
                    win_message.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'win_message.stopped')
                    # update status
                    win_message.status = FINISHED
                    win_message.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in earth_winComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "earth_win" ---
        for thisComponent in earth_winComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('earth_win.stopped', globalClock.getTime())
        # the Routine "earth_win" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "earth_lose" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('earth_lose.started', globalClock.getTime())
        # skip this Routine if its 'Skip if' condition is True
        continueRoutine = continueRoutine and not (lose == False)
        # keep track of which components have finished
        earth_loseComponents = [earth_lose_2, lose_message]
        for thisComponent in earth_loseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "earth_lose" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *earth_lose_2* updates
            
            # if earth_lose_2 is starting this frame...
            if earth_lose_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                earth_lose_2.frameNStart = frameN  # exact frame index
                earth_lose_2.tStart = t  # local t and not account for scr refresh
                earth_lose_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(earth_lose_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'earth_lose_2.started')
                # update status
                earth_lose_2.status = STARTED
                earth_lose_2.setAutoDraw(True)
            
            # if earth_lose_2 is active this frame...
            if earth_lose_2.status == STARTED:
                # update params
                pass
            
            # if earth_lose_2 is stopping this frame...
            if earth_lose_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > earth_lose_2.tStartRefresh + dur_end-frameTolerance:
                    # keep track of stop time/frame for later
                    earth_lose_2.tStop = t  # not accounting for scr refresh
                    earth_lose_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'earth_lose_2.stopped')
                    # update status
                    earth_lose_2.status = FINISHED
                    earth_lose_2.setAutoDraw(False)
            
            # *lose_message* updates
            
            # if lose_message is starting this frame...
            if lose_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                lose_message.frameNStart = frameN  # exact frame index
                lose_message.tStart = t  # local t and not account for scr refresh
                lose_message.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(lose_message, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'lose_message.started')
                # update status
                lose_message.status = STARTED
                lose_message.setAutoDraw(True)
            
            # if lose_message is active this frame...
            if lose_message.status == STARTED:
                # update params
                pass
            
            # if lose_message is stopping this frame...
            if lose_message.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > lose_message.tStartRefresh + dur_end-frameTolerance:
                    # keep track of stop time/frame for later
                    lose_message.tStop = t  # not accounting for scr refresh
                    lose_message.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'lose_message.stopped')
                    # update status
                    lose_message.status = FINISHED
                    lose_message.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in earth_loseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "earth_lose" ---
        for thisComponent in earth_loseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('earth_lose.stopped', globalClock.getTime())
        # the Routine "earth_lose" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "reset_buttons" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('reset_buttons.started', globalClock.getTime())
        # Run 'Begin Routine' code from reset_button_bool
        buttont1 = False
        buttont2 = False
        buttont3 = False
        buttont4 = False
        start_exp_button = False
        # keep track of which components have finished
        reset_buttonsComponents = []
        for thisComponent in reset_buttonsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reset_buttons" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reset_buttonsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reset_buttons" ---
        for thisComponent in reset_buttonsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('reset_buttons.stopped', globalClock.getTime())
        # the Routine "reset_buttons" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 10.0 repeats of 'return_to_homepage'
    
    
    # --- Prepare to start Routine "GoodBye" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('GoodBye.started', globalClock.getTime())
    # keep track of which components have finished
    GoodByeComponents = []
    for thisComponent in GoodByeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "GoodBye" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GoodByeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "GoodBye" ---
    for thisComponent in GoodByeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('GoodBye.stopped', globalClock.getTime())
    # the Routine "GoodBye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
