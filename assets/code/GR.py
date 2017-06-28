© Nicholas Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

# SAMPLE CODE

# initialize states
state_11 = {'position':(1,1), 'value': 0}
state_12 = {'position':(1,2), 'value': 0}
state_13 = {'position':(1,3), 'value': 0}
state_21 = {'position':(2,1), 'value': 0}
state_22 = {'position':(2,2), 'value': 0}
state_23 = {'position':(2,3), 'value': 0}
state_31 = {'position':(3,1), 'value': 0}
state_32 = {'position':(3,2), 'value': 0}
state_33 = {'position':(3,3), 'value': 0}
state_41 = {'position':(4,1), 'value': 0}
state_42 = {'position':(4,2), 'value': 0}
state_43 = {'position':(4,3), 'value': 0}

# initialize grid : grid[x-1][y-1] = (x,y)
grid = [[state_11, state_12, state_13],[state_21, state_22, state_23],[state_31, state_32, state_33],[state_41, state_42, state_43]]

# classify states
non_terminal_states = [state_11, state_12, state_13, state_21, state_23, state_31, state_32, state_33, state_41]
terminal_states = [state_42, state_43]
blank_state = [state_22]

# get state information
def getState(x,y):
    return grid[x-1][y-1]

# set value for states
def setState(x, y, v):
    grid[x-1][y-1]['value'] = v

# initial b(s)
def initbs():
    refreshGrid()
    for nt in non_terminal_states:
        x = nt['position'][0]
        y = nt['position'][1]
        setState(x,y,1/9)
    for t in terminal_states:
        x = t['position'][0]
        y = t['position'][1]
        setState(x,y,0)
    state_22['value'] = None
    return grid

def refreshGrid():
    for nt in non_terminal_states:
        x = nt['position'][0]
        y = nt['position'][1]
        setState(x, y, 0)
    for t in terminal_states:
        x = t['position'][0]
        y = t['position'][1]
        setState(x, y, 0)
    state_22['value'] = None
    return grid

# specicialized grid (given)
def initWithDefinedPos(x, y):
    refreshGrid()
    setState(2,2,None)
    setState(x,y, 1)
    for t in terminal_states:
        x = t['position'][0]
        y = t['position'][1]
        setState(x, y, 0)
    for nt in non_terminal_states:
        gx = nt['position'][0]
        gy = nt['position'][1]
        if (x != gx) & (y != gy):
            setState(x, y, 0)
        return grid

# initialize grid : grid[x-1][y-1] = (x,y)
grid = [[state_11, state_12, state_13],[state_21, state_22, state_23],[state_31, state_32, state_33],[state_41, state_42, state_43]]

# group states
non_terminal_states = [state_11, state_12, state_13, state_21, state_23, state_31, state_32, state_33, state_41]
terminal_states = [state_42, state_43]
blank_state = [state_22]

# get state information
def getState(x,y):
    return grid[x-1][y-1]

# set value for states
def setState(x, y, v):
    grid[x-1][y-1]['value'] = v

# initial b(s)
def initbs():
    for nt in non_terminal_states:
        x = nt['position'][0]
        y = nt['position'][1]
        setState(x,y,1/9)
    for t in terminal_states:
        x = t['position'][0]
        y = t['position'][1]
        setState(x,y,0)
    state_22['value'] = None
    return grid

# specified grid (given)
def initWithDefinedPos(x, y):
    setState(2,2,None)
    setState(x,y, 1)
    for t in terminal_states:
        x = t['position'][0]
        y = t['position'][1]
        setState(x, y, 0)
    for nt in non_terminal_states:
        gx = nt['position'][0]
        gy = nt['position'][1]
        if (x != gx) & (y != gy):
            setState(x, y, 0)
        return grid

topRow = [state_13, state_23, state_33, state_43]
bottomRow = [state_11, state_21, state_31, state_41]
leftMostCol = [state_11, state_12, state_13]
rightMostCol = [state_41, state_42, state_43]

# Actions are one of the following : UP, LEFT, RIGHT, DOWNN

def action_Up(state):
    x = state['position'][0]
    y = state['position'][1]
    value = []
    if state != state_22:
        # up with 0.8, check non_terminal
        if state != state_21:
            if state not in topRow:
                    if getState(x,y+1) in non_terminal_states:
                        value.append(0.8*getState(x,y+1)['value'])
        # up and hits wall 0.8
        if state == state_21:
                value.append(0.8*getState(x,y)['value'])
        if state in topRow:
                value.append(0.8*getState(x,y)['value'])
        # left 0.1, check non_terminal
        if state != state_32:
            if state not in leftMostCol:
                if getState(x-1,y) in non_terminal_states:
                    value.append(0.1*getState(x-1,y)['value'])
        # left and hits wall 0.1
        if state == state_32:
            value.append(0.1*getState(x,y)['value'])
        if state in leftMostCol:
            value.append(0.1*getState(x,y)['value'])
        # right 0.1, check non_terminal
        if state != state_12:
            if state not in rightMostCol:
                if getState(x+1, y) in non_terminal_states:
                    value.append(0.1*getState(x+1,y)['value'])
        # right and hits wall 0.1
        if state in rightMostCol:
            value.append(0.1*getState(x,y)['value'])
        if state == state_12:
            value.append(0.1*getState(x,y)['value'])
    print(value)
    value = sum(value)
    return value

def action_Down(state):
    x = state['position'][0]
    y = state['position'][1]
    value = []
    if state != state_22:
        # down with 0.8, check non_terminal
        if state != state_23:
            if state not in bottomRow:
                    if getState(x,y-1) in non_terminal_states:
                        value.append(0.8*getState(x,y-1)['value'])
        # down and hits wall 0.8
        if state == state_23:
                value.append(0.8*getState(x,y)['value'])
        if state in bottomRow:
                value.append(0.8*getState(x,y)['value'])
        # left 0.1, check non_terminal
        if state != state_32:
            if state not in leftMostCol:
                if getState(x-1,y) in non_terminal_states:
                    value.append(0.1*getState(x-1,y)['value'])
        # left and hits wall 0.1
        if state == state_32:
            value.append(0.1*getState(x,y)['value'])
        if state in leftMostCol:
            value.append(0.1*getState(x,y)['value'])
        # right 0.1, check non_terminal
        if state != state_12:
            if state not in rightMostCol:
                if getState(x+1, y) in non_terminal_states:
                    value.append(0.1*getState(x+1,y)['value'])
        # right and hits wall 0.1
        if state in rightMostCol:
            value.append(0.1*getState(x,y)['value'])
        if state == state_12:
            value.append(0.1*getState(x,y)['value'])
    print(value)
    value = sum(value)
    return value

def action_Right(state):
    x = state['position'][0]
    y = state['position'][1]
    value = []
    if state != state_22:
        # right with 0.8, check non_terminal
        if state != state_12:
            if state not in rightMostCol:
                if getState(x+1,y) in non_terminal_states:
                    value.append(0.8*getState(x+1,y)['value'])
        # right and hits wall 0.8
        if state == state_12:
            value.append(0.8*getState(x,y)['value'])
        if state in rightMostCol:
            value.append(0.8*getState(x,y)['value'])
        # up 0.1, check non_terminal
        if state != state_21:
            if state not in topRow:
                if getState(x,y+1) in non_terminal_states:
                    value.append(0.1*getState(x,y+1)['value'])
        # up and hits wall 0.1
        if state == state_21:
            value.append(0.1*getState(x,y)['value'])
        if state in topRow:
            value.append(0.1*getState(x,y)['value'])
        # down 0.1, check non_terminal
        if state != state_23:
            if state not in bottomRow:
                if getState(x, y-1) in non_terminal_states:
                    value.append(0.1*getState(x,y-1)['value'])
        # down and hits wall 0.1
        if state in bottomRow:
            value.append(0.1*getState(x,y)['value'])
        if state == state_23:
            value.append(0.1*getState(x,y)['value'])
    print(value)
    value = sum(value)
    return value

def action_Left(state):
    x = state['position'][0]
    y = state['position'][1]
    value = []
    if state != state_22:
        # left with 0.8, check non_terminal
        if state != state_32:
            if state not in leftMostCol:
                if getState(x-1,y) in non_terminal_states:
                    value.append(0.8*getState(x-1,y)['value'])
        # left and hits wall 0.8
        if state == state_12:
            value.append(0.8*getState(x,y)['value'])
        if state in leftMostCol:
            value.append(0.8*getState(x,y)['value'])
        # up 0.1, check non_terminal
        if state != state_12:
            if state not in topRow:
                if getState(x,y+1) in non_terminal_states:
                    value.append(0.1*getState(x,y+1)['value'])
        # up and hits wall 0.1
        if state == state_12:
            value.append(0.1*getState(x,y)['value'])
        if state in topRow:
            value.append(0.1*getState(x,y)['value'])
        # down 0.1, check non_terminal
        if state != state_23:
            if state not in bottomRow:
                if getState(x, y-1) in non_terminal_states:
                    value.append(0.1*getState(x,y-1)['value'])
        # down and hits wall 0.1
        if state in bottomRow:
            value.append(0.1*getState(x,y)['value'])
        if state == state_23:
            value.append(0.1*getState(x,y)['value'])
    print(value)
    value = sum(value)
    return value

def act(action, state):
    if action == 'up':
        return action_Up(state)
    if action == 'down':
        return action_Down(state)
    if action == 'left':
        return action_Left(state)
    if action == 'right':
        return action_Right(state)

# all states excluding state_22
allStates = [state_11, state_12, state_13, state_21, state_23, state_31, state_32, state_33, state_41, state_42, state_43]

def update2(action, observation):
    observation_Values = []
    update_Values = []
    i = 0
    for s1 in allStates:
        update_Values.append(act(action, s1))
    for s2 in allStates:
        s2['value'] = update_Values[i]
        i+=1
    action_Values = update_Values
    # observation = 1
    if observation == 1:
        for j in range(len(allStates)):
            if (j == 9) or (j == 10):
                observation_Values.append(0)
            elif (j == 5) or (j == 6) or (j == 7):
                observation_Values.append(0.9)
            else:
                observation_Values.append(0.1)
    # observation = 2
    if observation == 2:
        for j in range(len(allStates)):
            if (j == 9) or (j == 10):
                observation_Values.append(0)
            elif (j == 5) or (j == 6) or (j == 7):
                observation_Values.append(0.1)
            else:
                observation_Values.append(0.9)
    # observation = end
    if observation == 'end':
        for j in range(len(allStates)):
            if (j == 9) or (j == 10):
                observation_Values.append(1)
            else:
                observation_Values.append(0)
    new_Values = []
    for k in range(len(allStates)):
        new_Value = observation_Values[k] * action_Values[k]
        new_Values.append(new_Value)
    print(new_Values)
    print(sum(new_Values))

def update(action, observation):
    observation_Values = []
    update_Values = []
    i = 0
    for s1 in allStates:
        update_Values.append(act(action, s1))
    for s2 in allStates:
        s2['value'] = update_Values[i]
        i+=1
    action_Values = update_Values
    # observation = 1
    if observation == 1:
        for j in range(len(allStates)):
            if (j == 9) or (j == 10):
                observation_Values.append(0)
            elif (j == 5) or (j == 6) or (j == 7):
                observation_Values.append(0.9)
            else:
                observation_Values.append(0.1)
    # observation = 2
    if observation == 2:
        for j in range(len(allStates)):
            if (j == 9) or (j == 10):
                observation_Values.append(0)
            elif (j == 5) or (j == 6) or (j == 7):
                observation_Values.append(0.1)
            else:
                observation_Values.append(0.9)
    # observation = end
    if observation == 'end':
        for j in range(len(allStates)):
            if (j == 9) or (j == 10):
                observation_Values.append(1)
            else:
                observation_Values.append(0)
    new_Values = []
    for k in range(len(allStates)):
        new_Value = observation_Values[k] * action_Values[k]
        new_Values.append(new_Value)
    z = 0
    normalizingF = 0
    sumState = 0
    p = 0
    for st in allStates:
        st['value'] = new_Values[z]
        z += 1
    for i in allStates:
        sumState += i['value']
    normalizingF = 1/sumState
    for k in allStates:
        k['value'] = normalizingF*new_Values[p]
        p += 1  

def gridSum():
    sumState = 0
    for i in allStates:
        sumState += i['value']
    return sumState

def bsUpdate(initBS, actions, observations):
    refreshGrid()
    for p in range(len(actions)):
        update(actions[p], observations[p])
    print('RESULTS')
    for i in allStates:
        print(i)
    print(gridSum())

#tests
##bsUpdate(initbs(),['up','up','up'],[2,2,2])
##bsUpdate(initbs(),['up','up','up'],[1,1,1])
##bsUpdate(initWithDefinedPos(2,3),['right','right','up'],[1,1,'end'])
##bsUpdate(initWithDefinedPos(1,1),['up','right','right','right'],[2,2,1,1])
