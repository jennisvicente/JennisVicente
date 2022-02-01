# Import routines

import numpy as np
import math
import random

# Defining hyperparameters
m = 5 # number of cities, ranges from 1 ..... m
t = 24 # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5 # Per hour fuel and other costs
R = 9 # per hour revenue from a passenger


class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        self.action_space = [(p,q) for p in range(m) for q in range(m) if p != q or p==0]
        self.state_space = [(X,T,D) for X in range(m) for T in range(t) for D in range(d)]
        self.state_init = random.choice(self.state_space)

        # Start the first round
        self.reset()


    ## Encoding state (or state-action) for NN input

    def state_encod_arch2(self, state):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""
        state_encod = np.zeros(m+t+d).astype(int)
        state_encod[state[0]] = 1;
        state_encod[state[1] + m] = 1;
        state_encod[state[2] + m + t] = 1;
        #print("state_encod",state_encod)
        return state_encod


    # Use this function if you are using architecture-2 
    # def state_encod_arch2(self, state, action):
    #     """convert the (state-action) into a vector so that it can be fed to the NN. This method converts a given state-action pair into a vector format. Hint: The vector is of size m + t + d + m + m."""

        
    #     return state_encod


    ## Getting number of requests

    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        location = state[0]
        if location == 0:
            requests = np.random.poisson(2)
        if location == 1:
            requests = np.random.poisson(12)
        if location == 2:
            requests = np.random.poisson(4)
        if location == 3:
            requests = np.random.poisson(7)
        if location == 4:
            requests = np.random.poisson(8)

        if requests >15:
            requests =15

        possible_actions_idx = random.sample(range(1, (m-1)*m +1), requests) # (0,0) is not considered as customer request
        actions = [self.action_space[i] for i in possible_actions_idx]

        possible_actions_idx.append(0)
        actions.append((0,0))

        return possible_actions_idx,actions   



    def reward_func(self, state, action, Time_matrix):
        """Takes in state, action and Time-matrix and returns the reward"""
        wait_time, ride_time, transit_time = self.getDuration(state, action, Time_matrix)
        passenger_time = ride_time
        idle_time      = wait_time + transit_time
        
        reward = (R * passenger_time) - (C * (passenger_time + idle_time))

        return reward




    def next_state_func(self, state, action, Time_matrix, total_time_driven):
        """Takes state and action as input and returns next state"""
        #print("next_state_func state", state)
        #print("next_state_func action", action)
        wait_time, ride_time, transit_time = self.getDuration(state, action, Time_matrix)
        curr_time = state[1]
        curr_day = state[2]
        next_state = list(state)

        time_spent_during_ride = curr_time + wait_time + ride_time + transit_time # only wait_time will be added when action is (0,0)
        next_time = int(time_spent_during_ride % 24)
        num_days = int(time_spent_during_ride / 24)
        next_day = int((curr_day + num_days) % 7)
        if action != (0,0):
          next_state[0] = action[1]

        next_state[1] = next_time
        next_state[2] = next_day
        total_time_driven = total_time_driven + time_spent_during_ride
        return tuple(next_state), total_time_driven

    def getDuration(self, state, action, Time_matrix):
        #print("next_state_func state", state)
        #print("next_state_func action", action)
        curr_loc = state[0]
        pickup_loc = action[0]
        drop_loc = action[1]
        wait_time = 0 # time to wait for the next requests without accepting the current requests
        ride_time = 0 # time from pick up to drop loc
        transit_time = 0 # time to reach pickup loc from current loc
        if action == (0,0):
          wait_time = 1
        else:
          if curr_loc == pickup_loc:
              ride_time = Time_matrix[pickup_loc][drop_loc][state[1]][state[2]]
          else:
              transit_time = Time_matrix[curr_loc][pickup_loc][state[1]][state[2]]
              new_time = int((state[1] + transit_time) % 24)
              num_days = int((state[1] + transit_time) / 24)
              new_day = int((state[2] + num_days) % 7)
              ride_time = Time_matrix[pickup_loc][drop_loc][new_time][new_day]
        
        return wait_time, ride_time, transit_time


    def reset(self):
        return self.action_space, self.state_space, self.state_init
