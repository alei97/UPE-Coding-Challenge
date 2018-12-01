import requests

#initial post call
Session_ENDPOINT =  "http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/session"
UID = { "uid" : "804613563"}
r = requests.post(Session_ENDPOINT, UID)
r = r.json()
x = r["token"]

#dictionaries used for later post calls

up = { "action" : "UP" }
down = { "action" : "DOWN"}
left = { "action" : "LEFT"}
right = { "action" : "RIGHT"}
        

#dfs helper fucntion
def dfs(currentSpot, maze):
    Session_Get = "http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=x"
    g = requests.get("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",params=r) 
    g = g.json()
    maxY = g["maze_size"][0]
    maxX = g["maze_size"][1]
    x= currentSpot[1]
    y = currentSpot[0]
    #= "v" # mark as visited
    maze[x][y] = "v"
    #up
    if(x > 0 and (maze[x-1][y] != "w" and maze[x-1][y]  != "o" and maze[x-1][y] != "v")):
        move_up = requests.post("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",up, params=r)
        move_up = move_up.json()
        result = move_up["result"]
        print("move up is", result)
        if result == "END":
            return True
        elif (result == "SUCCESS"):
            currentSpot[1] = currentSpot[1] - 1
            maze[x-1][y] = "v" # mark as visited
            booleanResult = dfs(currentSpot, maze)
            if(booleanResult):
                return True
            else:
                move_down = requests.post("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",down, params=r)
                move_down = move_down.json()
                maze[x-1][y] = "v"
                currentSpot[1] = currentSpot[1] + 1
#                return dfs(currentSpot, maze)
        elif(result == "WALL"):
            maze[x-1][y] = "w" #mark as wall
            return dfs(currentSpot, maze)
 #           return False
        elif(result == "OUT_OF_BOUNDS"):
            maze[x-1][y] = "o" # mark as out of bounds
            return dfs(currentSpot, maze)
#            return False
    #left
    elif(y > 0 and (maze[x][y-1] != "w" and maze[x][y-1] != "o" and maze[x][y-1] != "v")):
        move_left = requests.post("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",left, params=r)
        move_left = move_left.json()
        move_left = move_left["result"]
        print("move left is ", move_left)
        if move_left == "END":
             return True
        elif (move_left == "SUCCESS"):
            currentSpot[0] = currentSpot[0] -1
            maze[x][y-1] = "v" # mark as visited
            booleanResult = dfs(currentSpot, maze)
            if(booleanResult):
                return True
            else:
                move_right = requests.post("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",right, params=r)
                move_right = move_right.json()
                maze[x][y-1] = "v"
                currentSpot[0] = currentSpot[0] + 1
#                return dfs(currentSpot, maze)
        elif(move_left == "WALL"):
            maze[x][y-1] = "w" #mark as wall
            return dfs(currentSpot, maze)
 #           return False
        elif(move_left == "OUT_OF_BOUNDS"):
            maze[x][y-1] = "o" # mark as out of bounds
            return dfs(currentSpot, maze)
 #           return False
    #right
    elif(y < maxY-1  and (maze[x][y+1] != "w" and maze[x][y+1] != "o" and maze[x][y+1] != "v")):
        move_right = requests.post("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",right, params=r)
        move_right = move_right.json()
        move_right = move_right["result"]
        print("move right is", move_right)
        if move_right == "END":
             return True
        elif (move_right == "SUCCESS"):
            currentSpot[0] = currentSpot[0]+1
            maze[x][y+1] = "v" # mark as visited
            booleanResult = dfs(currentSpot, maze)
            if(booleanResult):
                return True
            else:
                move_left = requests.post("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",left, params=r)
                move_left = move_left.json()
                currentSpot[0] = currentSpot[0] - 1
                maze[x][y+1] = "v"
#                return dfs(currentSpot, maze)
        elif(move_right == "WALL"):
            maze[x][y+1] = "w" #mark as wall
            return dfs(currentSpot, maze)
            #return False
        elif(move_right == "OUT_OF_BOUNDS"):
            maze[x][y+1] = "o" # mark as out of bounds
            return dfs(currentSpot, maze)
#            return False
    #down
    elif(x < maxX-1 and (maze[x+1][y] != "w" and maze[x+1][y]  != "o" and maze[x+1][y] != "v")):
        move_down = requests.post("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",down, params=r)
        move_down = move_down.json()
        move_down = move_down["result"]
        print("move down is ", move_down)
        if move_down == "END":
            return True
        elif (move_down == "SUCCESS"):
            currentSpot[1] = currentSpot[1] + 1
            maze[x+1][y] = "v" # mark as visited
            booleanResult = dfs(currentSpot, maze)
            if(booleanResult):
                return True
            else:
                move_up = requests.post("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",up, params=r)
                move_up = move_up.json()
                maze[x+1][y] = "v"
                currentSpot[1] = currentSpot[1] - 1
 #               return dfs(currentSpot, maze)
        elif(move_down == "WALL"):
            maze[x+1][y] = "w" #mark as wall
            return dfs(currentSpot, maze)
            #return False
        elif(move_down == "OUT_OF_BOUNDS"):
            maze[x+1][y] = "o" # mark as out of bounds
            return dfs(currentSpot, maze)
#            return False
    else:
        #you have to to backtrack and go up
        if((maze[x+1][y] != "v" and maze[x+1][y] != " ") and (maze[x][y-1] != "v" and
                                                              maze[x][y-1] != " ") and (maze[x][y+1] != "v" and maze[x][y+1] != " " ) and (maze[x-1][y] == "v")): #(maze[x-1][y] == "v") and 
             print("up if statement back entered")
             move = requests.post("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",up, params=r)
             move = move.json()
             move = move["result"]
             print(move)
             if(move == "SUCCESS"):
                 currentSpot[1] = currentSpot[1] - 1
                 maze[x-1][y] = " "
                 return dfs(currentSpot,maze)
 #            return False
#             return dfs(currentSpot,maze)
        elif((maze[x+1][y] != "v" and maze[x+1][y] != " ") and (maze[x][y-1] =="v") and (maze[x][y+1] != "v" and maze[x][y+1] != " " ) and (maze[x-1][y] != "v" and maze[x-1][y] != " ")): #backtrack left #and maze[x][y-1] == "v"
             print("left if statement back entered")
             move_left = requests.post("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",right, params=r)
             move_left = move_left.json()
             move_left = move_left["result"]
             if(move_left == "SUCCESS"):
                 currentSpot[0] = currentSpot[0] -1
                 maze[x][y-1] = " "
                 return dfs(currentSpot,maze)            
#             return False
#             return dfs(currentSpot,maze)
        elif((maze[x+1][y] != "v" and maze[x+1][y] != " ") and (maze[x][y-1] != "v" and maze[x][y-1] != " ") and (maze[x][y+1] == "v") and (maze[x-1][y] != "v" and maze[x-1][y] != " ")): #right
             print("right if statement back entered")
             move_right = requests.post("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",left, params=r)
             move_right = move_right.json()
             move_right = move_right["result"]
             if(move_right == "SUCCESS"):
                 currentSpot[0] = currentSpot[0]+1
                 maze[x][y+1] = " "
                 return dfs(currentSpot,maze)
 #            return False
#             return dfs(currentSpot,maze)
        elif((maze[x+1][y] == "v") and (maze[x][y-1] != "v" and maze[x][y-1] != " ") and (maze[x][y+1] != "v" and maze[x][y+1] != " ") and (maze[x-1][y] != "v" and maze[x-1][y] != " ")):#down #and (maze[x+1][y] == "v") 
             print("down if statement back entered")
             move_down = requests.post("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",up, params=r)
             move_down = move_down.json()
             move_down = move_down["result"]
             if(move_down == "SUCCESS"):
                 currentSpot[1] = currentSpot[1] + 1
                 maze[x+1][y] = " "
                 return dfs(currentSpot,maze)
    return False
#             return dfs(currentSpot,maze)
# dont need to pass in status

#
 #   if(status == "FINISHED":
  #     return "done"
  #  else if (status == "GAME_OVER"):
  #     return "gg"
  #  else:
 #   move_right = requests.post("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",right, params=r)
 #   move_right = move_right.json()
 #   if(move_right == "END"):
  #      return "END"

        
   # print(action)
    

#maze helper function
#def make2dList(rows, cols):
#    a=[]
#    for row in range(rows): a += [' '*cols]
#    return a


total_levels = 5
levels_completed = 0
while levels_completed < total_levels:
    #first get call for the first maze
    
    Session_Get = "http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=x"
    g = requests.get("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",params=r) 
    g = g.json()
 #   print(g)

    
 #   postTest = requests.post("http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=%5BACCESS_TOKEN%5D",right, params=r)
#    postTest = postTest.json()
#    print(postTest)
    #constructing the maze
    width = g["maze_size"][0]
    height = g["maze_size"][1]
 #   print(g["maze_size"])
    
#    print(width)
    gameStats = g["status"]
    #maze = make2dList(width,height)
    maze = [[" " for x in range(width)]for y in range(height)]
    
    mazeStart = g["current_location"]
#    for y in maze:
#        print(y)
    #print(mazeStart[0])
    # start dfs
    dfs(mazeStart, maze)

   # print(maze[0][0])
    done = g["levels_completed"]
    print(done)
    
    levels_completed += 1



# solving the maze






#while levels_completed < total_levels:
    #print(levels_completed)
#    levels_completed += 1
#access_token = r["token"]
# if this dones't work, look into converting JSON into a dictionary
#json is an object that works liek a dictionary but is not an actual dictionary

#requests.get(....)

# this returns a json object, requests has a built in function to convert the json object
# after I get r, do something like r = r.json (). This will make r equal the token:str

# the access token needs to be the value of the token later on
# posting starts the timer
# get gives you information about the maze in the form of a json object

# x = requests.get(link,
#size = mazeInfo["maze+_size"]

#POST /session the session part is ready to accept post requests


# Expected Response Body:
#{
#    “token”: str # token encoded with uid
#}
# the str returned to the token is a unique identifier to me, basically an encryption key


# i have to construct once I get the coordinates
#everytime I want to move, I do a post call, and then do a get call to see where I am
# after I solve the first maze, (when result == end) you do another get request to get the next maze

#every maze sstart off with a get request
# while levels_completed < total_levels:
    # construct the maze
    # run a DFS
    # if at the end,
#          levels_completed++
#         get request for new maze


#maze info you get
  #     Expected Response Body:
#{
#	“maze_size”: [int, int], <- [width, height], null if status is NONE or FINISHED
#	“current_location”: [int, int], <- [xcol, ycol], null if status is NONE or FINISHED
#	“status”: str, <- can be “PLAYING”, “GAME_OVER”, “NONE”, “FINISHED”
#	“levels_completed”: int <- 0 indexed, 0-L, null if status is NONE or FINISHED
#	“total_levels”: int <- L, null if status is NONE or FINISHED
#}
