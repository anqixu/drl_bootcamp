#!/usr/bin/env python3
import gym
import time

import gym
env = gym.make('CartPole-v0')

for i_episode in range(3):
    observation = env.reset()

    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        time.sleep(0.01)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            time.sleep(1.)
            break
