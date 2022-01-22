import safety_gym
import gym

import torch

env = gym.make('Safexp-PointGoal1-v0')
dim_action = env.action_space.shape[0]

import pdb; pdb.set_trace()


env.reset()

for i in range(100):
    env.reset()
    while True:
        # action = torch.Tensor(1,dim_action).uniform_(-1,1).cpu().numpy().flatten()
        action = env.action_space.sample()
        next_observation, reward, done, info = env.step(action)


        # print(next_observation, next_observation.shape)
        print(info)

        env.render()
        if done:
            break

