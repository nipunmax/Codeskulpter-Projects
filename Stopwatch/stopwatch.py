# template for "Stopwatch: The Game"
import simplegui
# define global variables
interval = 100
time = 0
stop_count = 0
winner_count = 0
states = False

#define functions
def converter(value,status):
    if value < 10 and status == True:
        return "0"+str(value)
    else:
        return str(value)

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format_time(time):
    
    seconds = (time/1000)%60
    tens_of_seconds = (time//100)%10
    minits = ((time/1000)//60)%60
    str_seconds = converter(seconds,True)
    str_tos = converter(tens_of_seconds,False)
    str_minits = converter(minits,True)
    return str_minits+ ":" + str_seconds+ "." +str_tos





def tot_stop(state):
    '''
    (boolean) -> String
    this function increase the winner_count , stop_count
    and change to String according to given condition.
    '''
    
    global winner_count , stop_count
    if state == True:
        stop_count = stop_count + 1
        winner_count = winner_count + 1
    else:
        stop_count = stop_count + 1
    s_winner = str(winner_count)
    s_count = str(stop_count)
    return s_winner+"/"+s_count

def attempts(states):
    '''
    (boolean) -> String
    this function find and return strings the
    success/attempts rate of the game
    '''
    global winner_count , stop_count
    if states == True and (time//100)%10 == 0:
        points = tot_stop(True)
        return points
    elif states == True and (time//100)%10 != 0:
        points = tot_stop(False)
        return points
    else:
        return str(winner_count)+"/"+str(stop_count)
    
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_handler1():
    timer.start()
        
def button_handler2():
    timer.stop()
    states = True
    attempts(states)

def button_handler3():
    global time ,winner_count , stop_count
    timer.stop()
    time = 0
    stop_count = 0
    winner_count = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global time,interval
    time = time + interval
     
# define draw handler
def draw(canvas):
    canvas.draw_text(format_time(time), [150,100], 40, 'Green')
    canvas.draw_text(attempts(states), [340,20], 25, 'White')    
    
# create frame
frame = simplegui.create_frame("stopwatch" , 400,200)

# register event handlers
button1 = frame.add_button('Start', button_handler1, 50)
button2 = frame.add_button('Stop', button_handler2, 50)
button3 = frame.add_button('Reset', button_handler3, 50)
timer = simplegui.create_timer(interval , tick)
frame.set_draw_handler(draw)

# start frame
frame.start()


