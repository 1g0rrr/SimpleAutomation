# Chain of models

Use multiple ACT models to solve more complex robotics task.

https://github.com/user-attachments/assets/c1692a7c-a353-49f0-8119-c8c6e14c9a89

For example in lamp testing demo we combined 3 models:

1. For getting lamp from random position
2. For precise insertion into the tester
3. For sorting working/not working bulbs

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
