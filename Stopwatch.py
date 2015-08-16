# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100
B_interval = 500
minutes,tenth_seconds,seconds = 0,0,0
time_total = 0
stop_total, wins = 0, 0
blinker = ":"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time_total):
    
    global tenth_seconds
   
    
    tenth_seconds = time_total%10
    seconds = (time_total/10)%60
    minutes = (time_total/10)/60
    
    if(seconds<10):
        string_seconds = "0" + str(seconds)
    else:
        string_seconds = str(seconds)
        
    return str(minutes) +  " " + string_seconds + "." + str(tenth_seconds)
    

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    blink_timer.start()
    timer.start()
    

def Stop():
    global wins, stop_total,blinker
    
    if(timer.is_running()):
        
        blinker = ":"
        blink_timer.stop()
        timer.stop()
        
        if(tenth_seconds == 0):
            wins, stop_total = wins + 1, stop_total + 1
        else:
        
            stop_total += 1
    
    
def Reset():
    global tenth_seconds,minutes,seconds,time_total,wins,stop_total,blinker
    
    tenth_seconds,minutes,seconds,wins,stop_total = 0,0,0,0,0
    
    if(timer.is_running() or timer.is_running() == False):
        time_total = "0:00.0"
    
    blinker = ":"
    blink_timer.stop()
    timer.stop()


# define event handler for timer with 0.1 sec interval
def tick():
    global time_total
 
    time_total += 1 

def blink():
    global blinker 
    
    blinker = not blinker 
    
         

# define draw handler

def draw(canvas):
    global time_total

    if(time_total == "0:00.0"):
        canvas.draw_text(str(time_total), (90,115), 50, "White")
        time_total = 0
        return 
           
    if blinker:
        canvas.draw_text(":", (102,115), 60, "White" , "sans-serif")
    
    
    canvas.draw_text(format(time_total),(70,115), 60, "White", "sans-serif")
    canvas.draw_text(str(wins) + "/" + str(stop_total), (235,30) , 25 , "Lime", "sans-serif")
    canvas.draw_line((1,140),(300,140),3, "White")
    canvas.draw_line((1,50),(300,50),3, "White")
    canvas.draw_text("STOP THE TIMER AT A WHOLE SECOND TO WIN!", (15,180) , 12 , "White", "sans-serif")
    
# Frame,Timer and Colon Blinker 

frame = simplegui.create_frame("StopWatch",300,200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval,tick) 
blink_timer = simplegui.create_timer(B_interval,blink)


# register event handlers
frame.add_button("Start", Start, 200)
frame.add_label("")
frame.add_button("Stop", Stop, 200)
frame.add_label("")
frame.add_button("Reset", Reset, 200)

# start frame
frame.start()

