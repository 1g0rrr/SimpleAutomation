# Make robots do something useful!

Our goal is to make robots affordable so more people can try them out, discover useful applications, and eventually make money using them to do work.

Currently, it's a set of helper scripts on top of LeRobot, plus a $300 robot arm compatible with π₀ and other foundational robotics models.

<img src="https://github.com/user-attachments/assets/4c30e970-5d89-48ea-86db-72ae8d1ab47a" width=450/>

# Intro

<table>
  <tr>
    <td><video src="https://github.com/user-attachments/assets/62472ce6-3084-41ec-8245-32a3c10f4b79" width=200/></td>
    <td></td>
  </tr>
</table>



# Installation

1.  If you didn't install LeRobot, install it:

```
git clone https://github.com/huggingface/lerobot.git
cd lerobot
pip install -e .
```

2 Clone Simple Automation scripts to another folder

```
git clone https://github.com/1g0rrr/SimpleAutomation.git
cd SimpleAutomation
```

3 Setup ports for your robot in "core/configs/robot/so100.yaml".

# Run

### Use multiple ACT models to solve complex robotics tasks.

For example, in the lamp testing demo, we combined 3 models:

1. For getting the lamp from a random position
2. For precise insertion into the tester
3. For sorting working/not working bulbs

![unnamed](https://github.com/user-attachments/assets/d105cf69-1b82-4581-90b7-9a9cd0a4f595)

### Run evaluation

-   Change the config file for using your models "core/configs/chains/lamp_testing.yaml"
-   While evaluating press "right" key to move to the next model

```
python core/models_chain.py evaluate \
  --robot-path core/configs/robot/so100.yaml \
  --chain-path core/configs/chains/lamp_testing.yaml
```

### Use LLM agent to run models
```
python core/models_chain.py llm_agent \
  --robot-path core/configs/robot/so100.yaml
```

### Run recording

-   The difference from Lerobot's recording is added teleoperation between episodes. This is usefull to be able to switch between models in not "resting" position.

```
python core/models_chain.py record \
  --robot-path core/configs/robot/so100.yaml \
  --fps 30 \
  --root data \
  --repo-id 1g0rrr/koch_test21 \
  --tags tutorial \
  --warmup-time-s 5 \
  --episode-time-s 5 \
  --reset-time-s 5 \
  --num-episodes 2
```

### Run teleoperation:

Use it for testing if all is working.

```
python core/models_chain.py teleoperate \
 --robot-path core/configs/robot/so100.yaml \
 --robot-overrides '~cameras'
```



# Tips

-   Make sure you have all inintial positions in the following model to prevent robot from sudden movements.
-   "Pick and place" task is hard for the model and gripper can grab object not precisely at the center. To solve this re-grab object at the beginning of next model.

# Training

### Train model in Google Colab:

You can model in Google Colab to save time.
https://colab.research.google.com/github/1g0rrr/SimpleAutomation/blob/main/colab/SimpleAutomationTrainModel.ipynb

-   It will take about 2.5 hours and $1.5 to train typical 80K steps.
-   Choose A100 as the fastest GPU.
-   Don't disconnect colab and don't close browser as all data will be deleted.

# Hardware
### S.A.M.01

![arm2](https://github.com/user-attachments/assets/35113d53-93b1-4678-af15-463d563cd238)

Join https://discord.gg/NFsqq4CVhs to get recent information.

### SO-100

Follow [SO-100](https://github.com/TheRobotStudio/SO-ARM100) to build your arm.

<img src="./media/so-100.png" width=500/>


# Join the community

Say 👋 in our [public discord channel](https://discord.gg/NFsqq4CVhs). We help each other with assembling, training models, and making the robot do something useful. 

Thank you for contributing to SimpleAutomation!

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=1g0rrr/simpleautomation&type=Timeline)](https://star-history.com/#1g0rrr/simpleautomation&Timeline)
