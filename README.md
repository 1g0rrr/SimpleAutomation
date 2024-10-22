# Chain of models

Use multiple ACT models to solve more complex robotics task.

https://github.com/user-attachments/assets/76f47c09-cc9e-40e7-b401-da85258b3f98

For example in lamp testing demo we combined 3 models:

1. For getting lamp from random position
2. For precise insertion into the tester
3. For sorting working/not working bulbs

# Tips

-   Pick and place from random position is hard and gripper can grab object not precisely at the center. Re-grab object at the beginning of next model
-   Make sure you have all inintial positions in the following model to prevent robot from sudden movements.

# Installation

1.  If you didn't install Lerobot, install:

```
git clone -b user/rcadene/2024_09_04_feetech https://github.com/huggingface/lerobot.git
cd lerobot
pip install -e .
```

2 Clone Simple Automation scripts in another folder

```
git clone https://github.com/1g0rrr/SimpleAutomation.git
cd SimpleAutomation
```

3 Setup ports for your robot in "core/configs/robot/so100.yaml". If you use Koch arm create corresponding file.

# Run

### Run teleoperation:

Use it for testing if all is working.

```
python core/models_chain.py teleoperate \
 --robot-path core/configs/robot/so100.yaml \
 --robot-overrides '~cameras'
```

### Run recording

-   The difference from Lerobot is added teleoperation between episodes. You can set robot to position other than "rest" befre recording. This is usefull to be able to switch between models in this position.

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

### Run evaluation

-   Edit config file with your models "core/configs/chains/lamp_testing.yaml"
-   Tip: Press "right" to move to the next model

```
python core/models_chain.py evaluate \
  --robot-path core/configs/robot/so100.yaml \
  --chain-path core/configs/chains/lamp_testing.yaml
```

# Training

### Train model in Google Colab:

Train model with Lerobot in Google Colab.
https://colab.research.google.com/github/1g0rrr/SimpleAutomation/blob/main/colab/SimpleAutomationTrainModel.ipynb

-   It will take about 2.5 hours and $1.5 to train typical 80K steps.
-   Choose A100 as fastest GPU.
-   Don't disconnect colab and don't close browser as all data will be deleted.
