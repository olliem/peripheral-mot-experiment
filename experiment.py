#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.79.01), Thu Feb 20 15:58:25 2014
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui, monitors
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
import random
import os  # handy system and path functions

# Utility methods
# Divdes list into N chunks
def chunk(xs, n):
    ys = list(xs)
    random.shuffle(ys)
    ylen = len(ys)
    size = int(ylen / n)
    chunks = [ys[0+size*i : size*(i+1)] for i in xrange(n)]
    leftover = ylen - size*n
    edge = size*n
    for i in xrange(leftover):
        chunks[i%n].append(ys[edge+i])
    return chunks

# Store info about the experiment session
expName = u'experiment'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Start Code - component code to be run before the window creation

# Setup variables
width = 1440
height = 900

mon = monitors.Monitor('testMonitor')
primary = visual.Window(size=[width, height], fullscr=False, screen=0, allowGUI=True, units='pix', monitor=mon)

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=primary.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instrText = visual.TextStim(primary, ori=0, name='instrText',
    text=u'Press any key to start test',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=primary, screenHz=expInfo['frameRate'], name='ISI')
mouse = event.Mouse()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(instrText)
instructionsComponents.append(key_resp_2)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if t >= 0.0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t  # underestimates by a little under one frame
        instrText.frameNStart = frameN  # exact frame index
        instrText.setAutoDraw(True)
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents()
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        primary.flip()
        
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'conditions.xlsx'),
    seed=None, name='trials')

thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

screenRec = visual.Rect(primary, width=width/2, height=height/2)
screenRec.fillColor = 'black'
#screenRec.fillColor = 'grey'
#screenRec.lineWidth = 10
screenRec.lineColor = 'black'

nDots = 1000
dotSize = 5
nCircles = 10
circleSize = 30
speed = 1.5
maxRotSpeed = .2
timeTargetVisible = 3
timeMoving = 10

for thisTrial in trials:
    circles = []
    circleAngles = []
    for i in range(nCircles):
        circle = visual.Polygon(primary, name='circle',
            edges = 90, size=circleSize, units = 'pix',
            ori=0, pos=[random.randint((-width/4)+15, (width/4)-15), random.randint((-height/4)+15, (height/4)-15)],
            lineWidth=1, lineColor=[1,1,1], lineColorSpace=u'rgb',
            fillColor=[1,1,1], fillColorSpace=u'rgb',
            opacity=1,interpolate=True)
        circleAngles.append(random.random() * 2*np.pi)
        circles.append(circle)
    
    # Randomly place dots bounded around the primary screen
    coords = []
    while(len(coords) < nDots):
        randx = random.randint(-width/2, width/2)
        randy = random.randint(-height/2, height/2)
        
        if randy in range(int(-height/4), int(height/4)):
            if randx not in range(int(-width/4), int(width/4)):
                coords.append([randx, randy])
        else:
            coords.append([randx, randy])
    
    dots = visual.ElementArrayStim(primary, elementTex=None, elementMask='circle', nElements=nDots, 
                                   sizes=dotSize, units = 'pix', xys = coords)
    
    percentConnectedVar = thisTrial['percentConnected']
    numOfTargetsVar = thisTrial['numOfTargets']
    inclSecondScreenVar = thisTrial['inclSecondScreen']
    
    # Randomly select some circles subject must track
    print "percent connected:" + str(percentConnectedVar)
    print "num of targets:" +str(numOfTargetsVar)
    print "include second screen:" +str(inclSecondScreenVar)
    
    targetsNum = int(numOfTargetsVar)
    targetsSelectedKeys = random.sample(circles, targetsNum)
    
    if (percentConnectedVar >= 100):
        connectedDotsIndexs = range(0, nDots)
    else:
        connectedDotsIndexs = random.sample(range(0, nDots),  int(nDots * percentConnectedVar))
    
    print "number of connected dots:" + str(len(connectedDotsIndexs))
    
    connectedDotsChunkedEvenly = chunk(connectedDotsIndexs, targetsNum)
    
    # Creates dictionary of targets mapped to its connected dots
    targets = dict(zip(targetsSelectedKeys, connectedDotsChunkedEvenly))
    
    flattened = [x for sublist in connectedDotsChunkedEvenly for x in sublist]
    
    notConnectedDotIndexs = [i for i in range(0, nDots) if i not in flattened]
    
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    # update component parameters for each repeat
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    for circle in circles:
        trialComponents.append(circle)
    trialComponents.append(mouse)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    clickCount = 0
    clickedCircles = []
    
    lastPressClock = core.Clock()
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        #frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *circle* updates
        if t >= 0.0 and t <= timeTargetVisible:
            if int(inclSecondScreenVar) > 0:
                dots.draw()
            screenRec.draw()
            for circle in circles:
                if circle in targets: circle.fillColor = 'red'
                circle.draw()
                
        elif t >= timeTargetVisible and t <= timeMoving + timeTargetVisible :
            dotXys = dots.xys
            
            # the draw is here so drawing is in correct order and draws rec over the top of dots
            if int(inclSecondScreenVar) > 0:
                dots.draw()
            screenRec.draw()
            
            for index, circle in enumerate(circles):
                # Reset targets back to white
                circle.fillColor = 'white'
                
                a = circleAngles[index]
                x = speed * np.cos(a)
                y = speed * np.sin(a) 
                
                circle.pos[0] += x
                circle.pos[1] += y
                
                circle.draw()
                
                if circle in targets:
                    for dotIdx in targets[circle]:
                        if dotXys[dotIdx][0] <= -width/2 +20 or dotXys[dotIdx][0] >= width/2 +20 or dotXys[dotIdx][1] <= -height/2 +20 or dotXys[dotIdx][1] >= height/2 +20:
                            dotXys[dotIdx][0] = dotXys[dotIdx][0] * -1
                            dotXys[dotIdx][1] = dotXys[dotIdx][1] * -1
                        else:
                            dotXys[dotIdx][0] += x
                            dotXys[dotIdx][1] += y
                
                if circle.pos[0] <= (-width/4)+15 or circle.pos[0] >= (width/4)-15 or circle.pos[1] <= (-height/4)+15 or circle.pos[1] >= (height/4)-15:
                    a = a + np.pi
                else:
                    # else randomly rotate the stimulus a bit
                    a += (random.random()-.5) * maxRotSpeed
                
                circleAngles[index] = a
            
            for dotInx in notConnectedDotIndexs:
                if dotXys[dotInx][0] <= -width/2 +2 or dotXys[dotInx][0] >= width/2 +2 or dotXys[dotInx][1] <= -height/2 +2 or dotXys[dotInx][1] >= height/2 +2:
                    dotXys[dotInx][0] = dotXys[dotInx][0] * -1
                    dotXys[dotInx][1] = dotXys[dotInx][1] * -1
                else:
                    dotXys[dotInx][0] += (random.random()-.5) * 2
                    dotXys[dotInx][1] += (random.random()-.5) * 2
            
            dots.setXYs(dotXys)
            
        # *mouse* updates
        if t >= timeMoving + timeTargetVisible and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t  # underestimates by a little under one frame
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouse.status == STARTED:  # only update if started and not stopped!
            if int(inclSecondScreenVar) > 0:
                dots.draw()
            screenRec.draw()
            for circle in circles:
                circle.draw()
            
            if mouse.getPressed()[0] and lastPressClock.getTime() > 0.2:
                lastPressClock.reset()
                for circle in circles:
                    if circle.contains(mouse) and circle not in clickedCircles:
                        clickedCircles.append(circle)
                        clickCount += 1
                
                print clickCount
                print targetsNum
                print clickedCircles
            if clickCount >= targetsNum:  # ie if any button is pressed
                # abort routine on response
                continueRoutine = False
                
        # *ISI* period
        #if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            #ISI.tStart = t  # underestimates by a little under one frame
            #ISI.frameNStart = frameN  # exact frame index
            #ISI.start(2)
        #elif ISI.status == STARTED: #one frame should pass before updating params and completing
            #ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        primary.flip()
        # refresh the screen
        #if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            #primary.flip()
        #else:  # this Routine was not non-slip safe so reset non-slip timer
        #    routineTimer.reset()
    

    #core.wait(2)
        
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
    # store data for trials (TrialHandler)
    targetsCorrectlyIdentified = list(set(clickedCircles).intersection(targets))
    trials.addData('targetsCorrectlyIdentified', len(targetsCorrectlyIdentified))
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'
primary.close()
core.quit()