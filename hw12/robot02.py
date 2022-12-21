import turtle as t

def RobotBattle():
    # robotList stores the list of robots in the battle
    robotList = []
    
    while True:
        # Clear the screen and draw the robots
        t.clear()
        for robot in robotList:
            robot.draw()
        
        # Display the status of each robot
        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(i, " : ")
            robot.displayStatus()
            i += 1
        print("================")
        
        # Ask user which robot to command or to create a new robot
        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit: ")
        if choice == 'q':
            break
        elif choice == 'c':
            print("Enter which type of robots to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot: ")
            if robotType == 'r':
                newRobot = Robot()
            elif robotType == 'm':
                newRobot = MedicBot()
            elif robotType == 's':
                newRobot = StrikerBot()
            robotList = robotList + [newRobot]
        else:
            n = int(choice)
            robotList[n].command(robotList)
            
        # Delete all the robots with health <= 0 from the list
        i = 0
        for robot in robotList:
            if (robot.health <= 0):
                del robotList[i]
            i += 1
            
class Robot(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.health = 100
        self.energy = 100
        
    def move(self, x, y):
        if self.energy > 0:
            self.x = x
            self.y = y
            self.energy -= 10
            t.pu()
            t.goto(self.x, self.y)
            t.pd()
            
    def draw(self):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        t.circle(50)

    def displayStatus(self):
        print(f"x = {self.x}, y = {self.y}, health = {self.health}, energy = {self.energy}")
    
    def command(self, robotList):
        print("Possible actions: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX, newY)
        
class MedicBot(Robot):
    def __init__(self):
        super().__init__()
    
    def heal(self, r):
        self.distance = (((self.x - r.x) ** 2) + ((self.y - r.y) ** 2)) ** (1/2)
        if self.energy >= 20 and self.distance <= 10:
            self.energy -= 20
            r.health += 10

    def command(self, robotList):
        print("Possible actions: move, heal")
        action = input("Enter action: ")
        if action == "move":
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX, newY)
        
        elif action == "heal":
            heal_robot = int(input("Choose robot to heal: "))
            self.heal(robotList[heal_robot])

    def draw(self):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        t.circle(50)

        t.pu()
        t.goto(self.x - 30, self.y + 65)
        t.seth(0)
        t.pd()
        for i in range(4):
            t.fd(20)
            t.lt(90)
            t.fd(20)
            t.rt(90)
            t.fd(20)
            t.rt(90)

        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        t.seth(0)


class StrikerBot(Robot):
    def __init__(self, missle = 5):
        super().__init__()

        self.missle = missle

    def strike(self, r):
        self.distance = (((self.x - r.x) ** 2) + ((self.y - r.y) ** 2)) ** (1/2)
        if self.energy >= 20 and self.distance <= 10 and self.missle > 0:
            self.energy -= 20
            self.missle -= 1
            r.health -= 50

    def displayStatus(self):
        print(f"x = {self.x}, y = {self.y}, health = {self.health}, energy = {self.energy}, missle = {self.missle}")

    def command(self, robotList):
        print("Possible actions: move, strike")
        action = input("Enter action: ")
        if action == "move":
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX, newY)
        
        elif action == "strike":
            strike_robot = int(input("Choose robot to strike: "))
            self.strike(robotList[strike_robot])

    def draw(self):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        t.circle(50)

        t.pu()
        t.goto(self.x, self.y + 80)
        t.seth(0)
        t.pd()

        t.lt(45)
        for i in range(4):
            t.rt(90)
            t.fd(40)

        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        t.seth(0)


RobotBattle()