# Installation

1.  If you didn't install Lerobot, install it. Example of installation with Feetech support:

```
git clone -b user/rcadene/2024_09_04_feetech https://github.com/huggingface/lerobot.git
cd lerobot
pip install -e .
```

2 Install Simple Automation scripts in another folder

```
git clone https://github.com/1g0rrr/SimpleAutomation.git
cd SimpleAutomation
```

3 Setup ports for your so100 robot in "core/configs/robot/so100.yaml". If you use Koch arm create corresponding file.

# Run

### Run teleoperation:

Use it for testing if all is working.

```
python core/models_chain.py teleoperate \
 --robot-path core/configs/robot/so100.yaml \
 --robot-overrides '~cameras'
```

### Run recording

Difference with Lerobot is added warming up between episodes, so you can set robot to position other than "rest". This is usefull to be able to switch between models in this position.

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

Fill episodes chain by changing example "core/configs/chains/lamp_testing.yaml"

```
python core/models_chain.py evaluate \
  --robot-path core/configs/robot/so100.yaml \
  --chain-path core/configs/chains/lamp_testing.yaml
```

# Training

### Train model in google colab:

Feel free to use this simple script for model training in Google Colab.
Choose A100 as a GPU.
It will take about 2.5 hours and $1.5 to train typical 80K steps.
Don't disconnect colab and don't close browser as all data will be deleted.
https://colab.research.google.com/github/1g0rrr/SimpleAutomation/blob/main/colab/SimpleAutomationTrainModel.ipynb

# Tips for chaining models
