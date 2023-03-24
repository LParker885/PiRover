#import ros2
#import good physics engine

class track:
    def __init__ (self, difficultyStep):
        #init environment based on difficulty step with walls, floor friction, target position, starting position

        #init physics engine

        #init set of agents with position/velocity/acceleration, collision detection, distance to target, lidar data, requested wheel speed, entity in phyics engnie

        #init trainer linked to each agent

        #init score tracking system

        self.simtime = 0

        pass

    def step(self, timestep):
        #have each actor make a decision
        #step simtime by timestep - possibly physics engine?
        #have each actor get trained on previous decision
        pass

    def saveBestActor(self,actornumber):
        #every such and so time, save the best actor if it is better than the previous actor
        pass


