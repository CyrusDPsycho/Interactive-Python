# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2,HEIGHT/2]
ball_radius = 20
ball_vel = [0,0]
direction = "left"
paddle1_pos1,paddle1_pos2 = [0,150],[0,250]
paddle2_pos1,paddle2_pos2 = [WIDTH,150],[WIDTH,250]
paddle2_pos = [WIDTH,250]
paddle1_vel,paddle2_vel = 0,0
score1,score2 = 0,0
accelerate = 1
count_down, animation = 3, False
count_sizer = [150,350]
count_inc = 500
splash_Screen = "Press The SpaceBar To Start"

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH/2,HEIGHT/2]   
    
    if direction == "right":
        
        ball_vel = [(random.randrange(3,6)), -(random.randrange(3,6))]
        
    elif direction =="left":
       
        ball_vel = [-(random.randrange(3,6)), -(random.randrange(3,6))]
       
        
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1,score2 = 0,0
    paddle1_pos, paddle2_pos = [0,150],[0,250] , [WIDTH,150],[WIDTH,250]
    paddle1_vel, paddle2_vel = 0,0
    
    spawn_ball("left") 

def draw(canvas):
    global score1, score2, paddle1_pos1,paddle1_pos2, paddle2_pos1,paddle2_pos2, ball_pos
    global ball_vel,paddle1_vel,accelerate,count_down,animation,count_inc,count_sizer,splash_Screen
        
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #Reflection(Top and Bottom) 
    
    if ball_pos[1] <= ball_radius:
        ball_vel[1] = -ball_vel[1]
        
    elif ball_pos[1] >= HEIGHT - ball_radius:   
        ball_vel[1] = -ball_vel[1] 
       
    #GutterToucher
    
    if ball_pos[0] <= PAD_WIDTH:
        score2 += 1
        spawn_ball("right")
        
    elif ball_pos[0] >= WIDTH - PAD_WIDTH:
        score1 += 1
        spawn_ball("left")
        
    # draw ball
    canvas.draw_circle(ball_pos, ball_radius, 2, "Blue","White")
    
    
    #Paddle to remain in the canvas
        
    if paddle1_pos2 >= [0,400]: 
        
        paddle1_pos1 = [0,300]
        paddle1_pos2 = [0,400]
        
    if paddle1_pos1 <= [0,0]:
        
        paddle1_pos1 = [0,0]
        paddle1_pos2 = [0,100]
        
    if paddle2_pos2 >= [WIDTH,400]:
        
        paddle2_pos1 = [WIDTH,300]
        paddle2_pos2 = [WIDTH,400]
        
    if paddle2_pos1 <= [WIDTH,0]:
        
        paddle2_pos1 = [WIDTH,0]
        paddle2_pos2 = [WIDTH,100]
        
    # update paddle's vertical position, keep paddle on the screen
        
        
    paddle1_pos1[1] += paddle1_vel
    paddle1_pos2[1] += paddle1_vel
       

    paddle2_pos1[1] += paddle2_vel
    paddle2_pos2[1] += paddle2_vel
    
    # draw paddles
    canvas.draw_line(paddle1_pos1, paddle1_pos2,16, "White")
    canvas.draw_line(paddle2_pos1 ,paddle2_pos2,16,"White")
    
    
    # determine whether paddle and ball collide    
    
    if ball_pos[0] <= ball_radius:
        
        if ball_pos[1] >= paddle1_pos1[1] and ball_pos[1] <= paddle1_pos2[1]:
            
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] += accelerate

    if ball_pos[0] >= WIDTH - ball_radius:
        
        if ball_pos[1] >= paddle2_pos1[1] and ball_pos[1] <= paddle2_pos2[1]:
            
            ball_vel[0] += accelerate
            ball_vel[0] = -ball_vel[0]

    # draw scores
    canvas.draw_text(str(score1),(125,100),50, "Lime","sans-serif")
    canvas.draw_text(str(score2),(450,100),50, "Lime","sans-serif")
    
    #draw countdown animation
    if count_down>0 and animation == True:
        canvas.draw_text(str(count_down), count_sizer, count_inc, 'White',"monospace")
        
    
    if 	count_down == 0:
        
        animation = False
        count_down -= 1
        timer.stop()
        new_game()
        
    #draw splash screen animation 
    if(splash_timer.is_running()):
        canvas.draw_text("PONG!", [225,80], 50, "White")
        if splash_Screen:
            canvas.draw_text("Press Spacebar To Start" ,[160,300], 30, "Lime")
          
        
def keydown(key):
    global paddle1_vel, paddle2_vel,paddle1_pos
    global animation

    if key == simplegui.KEY_MAP["space"]:
        splash_timer.stop()
        timer.start()
        animation = True
        return
    
    if key == simplegui.KEY_MAP["w"]:
     
        paddle1_vel = -4      
        return
    
    if key == simplegui.KEY_MAP["s"]:
        
        paddle1_vel = 4
        return

    if key == simplegui.KEY_MAP["up"]:
    
        paddle2_vel = -4
        return
    
    if key == simplegui.KEY_MAP["down"]:
        
        paddle2_vel = 4
        return
                             

def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"] :
        paddle1_vel = 0
        print paddle1_pos1,paddle1_pos2
        return
    
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"] :
        paddle2_vel = 0
        return 

def Restart():
    
    new_game()

def Countdown():
    
    global count_down,count_sizer,count_inc
    
    count_down -= 1


        
def splashScreenAnimation():
    global splash_Screen
    
    splash_Screen = not splash_Screen
    
    
# create frame,timer and game starter
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)



frame.add_label("")
frame.add_label("")
frame.add_label("")
frame.add_label("")

frame.add_button("RESTART",Restart,125)


timer = simplegui.create_timer(1000, Countdown)
splash_timer = simplegui.create_timer(500,splashScreenAnimation)


#start frame and splash timer on opening of frame
splash_timer.start()
frame.start()
