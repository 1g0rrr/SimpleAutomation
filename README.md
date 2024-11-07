# Set of helper scripts on top of LeRobot
<img src="https://github.com/user-attachments/assets/6e96531c-bf3d-4d5e-98c8-183fa3e10d17" width=400/>

# Multiple models

### Use multiple ACT models to solve more complex robotics tasks.

For example, in the lamp testing demo, we combined 3 models:

1. For getting the lamp from a random position
2. For precise insertion into the tester
3. For sorting working/not working bulbs

![unnamed](https://github.com/user-attachments/assets/d105cf69-1b82-4581-90b7-9a9cd0a4f595)

# Intro

<table>
  <tr>
    <td><video src="https://github.com/user-attachments/assets/62472ce6-3084-41ec-8245-32a3c10f4b79" width=200/></td>
    <td></td>
  </tr>
</table>

# Hardware

Follow [SO-100](https://github.com/TheRobotStudio/SO-ARM100) to build your arm.

![Leader_And_Follower](./media/so-100.png)

### Buy assembled in US:

There are additional costs of assembling

-   BOM price: $241
-   Shipping: $30-$80 depending on speed (5-20 days)
-   Printing: 30-50 hours, $10 plastic
-   Assembly and calibration: 1-2 days

We can offer properly assembled and calibrated robot in the US for $400

DM me if interested:

https://x.com/ihorbeaver

# Installation

1.  If you didn't install Lerobot, install it:

```
git clone -b user/rcadene/2024_09_04_feetech https://github.com/huggingface/lerobot.git
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

### Run evaluation

-   Change config file for using your models "core/configs/chains/lamp_testing.yaml"
-   While evaluating press "right" key to move to the next model

```
python core/models_chain.py evaluate \
  --robot-path core/configs/robot/so100.yaml \
  --chain-path core/configs/chains/lamp_testing.yaml
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
-   Choose A100 as fastest GPU.
-   Don't disconnect colab and don't close browser as all data will be deleted.
