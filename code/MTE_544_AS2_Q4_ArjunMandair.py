"""
Student Name & Last Name: Arjun Mandair
Origianl Author : Pi Thanacha Choopojcharoen
You must change the name of your file to MTE_544_AS2_Q4_(your full name).py
Do not use jupyter notebook.

*You may want to install the following libraries if you haven't done so.*

pip install numpy matplotlib pandas scipy

"""

import numpy as np

def decode_measurement(measurements):
    readings = []
    for measurement in measurements:
        readings.append(int(np.argmax(measurement)) + 1)  # +1 for 1-based indexing
    return readings

def moodeng_behavior_update(state, A):
    # Given the current state, and the transition matrix A, 
    # randomly return the next state of Moo-Deng based on A
    ##### ADD your code here : #####
    # Column (state-1) of A = probabilities of the next zone given the current zone.
    # States are 1-based (1=F, 2=R, 3=P), numpy indices are 0-based.
    next_state = int(np.random.choice([1, 2, 3], p=A[:, state - 1]))
    ##### END #####
    return next_state
def sensor_measurement(state, C):
    # Given a state, and the matrix C, 
    # randomly return the encoded measurement based on C
    # Note that : 
    # F -> np.array([1,0,0])
    # R -> np.array([0,1,0])
    # P -> np.array([0,0,1])
    ##### ADD your code here : #####
    # Column (state-1) of C = probabilities of each displayed zone given the true zone.
    reading = np.random.choice([0, 1, 2], p=C[:, state - 1])
    measurement = np.eye(3, dtype=int)[reading]      # one-hot: F, R or P
    ##### END #####
    return measurement

def sim_moodeng(initial_state=1,iteration = 20):
    # Given an initial state of Moo-Deng's whereabout and number of iteration,
    # simulate Moo-Deng's behavior and the designed state estimator
    
    belief = np.array([1/3, 1/3, 1/3])  # Initial belief for the Bayesian filter
    
    ##### ADD your code here : #####
    # A[i, j] = p(next = i+1 | current = j+1)   (columns sum to 1)
    A = np.array([[0.6, 0.2, 0.2],
                  [0.4, 0.4, 0.1],
                  [0.0, 0.4, 0.7]])
    # C[i, j] = p(display i+1 | true zone j+1)   (columns sum to 1)
    C = np.array([[0.80, 0.20, 0.05],
                  [0.10, 0.70, 0.10],
                  [0.10, 0.10, 0.85]])
    ##### END #####

    states = []
    measurements = []
    estimated_states = []
    beliefs = []
    state = initial_state
    for i in range(iteration):
               
        ##### ADD your code here : #####
        # Simulate the true world
        next_state = moodeng_behavior_update(state, A)      # Moo-Deng moves
        measurement = sensor_measurement(next_state, C)     # noisy sensor reading
        # Bayes filter
        predicted = A @ belief                              # prediction: x_bar = A x_{k-1}
        unnormalized = (C.T @ measurement) * predicted      # correction: likelihood * prediction
        updated_belief = unnormalized / unnormalized.sum()  # normalise (eta)
        estimated_state = int(np.argmax(updated_belief)) + 1  # most likely zone, 1-based
        # carry forward to the next step
        belief = updated_belief
        state = next_state

        ##### END #####
        states.append(next_state)
        measurements.append(measurement)
        beliefs.append(updated_belief)
        estimated_states.append(estimated_state)
        
    return states, measurements, estimated_states, beliefs

    
# Run the simulation

states, measurements, estimated, beliefs = sim_moodeng(initial_state=1, iteration=20)

readings = decode_measurement(measurements)
# Print results
print("True states:          ", states)
print("Sensor measurements:  ", readings)
print("Estimated states:     ", estimated)
print("Belief sequence:      ", np.array(beliefs))
