import enum
import logging
import math
import time
import traceback
from copy import deepcopy
from pathlib import Path

import numpy as np
import tqdm
import mujoco


from lerobot.common.robot_devices.utils import RobotDeviceAlreadyConnectedError, RobotDeviceNotConnectedError
from lerobot.common.utils.utils import capture_timestamp_utc

class SimulatedFollower:

    def __init__(
        self,
        port: str,
        # configuration,
        motors: dict[str, tuple[int, str]],
        extra_model_control_table: dict[str, list[tuple]] | None = None,
        extra_model_resolution: dict[str, int] | None = None,
        mock=False,
    ):
        # self.configuration = configuration
        self.old_pos = np.zeros(12)
        self.port = port
        self.motors = {
                    # name: (index, model)
                    "shoulder_pan": (1, "xl330-m077"),
                    "shoulder_lift": (2, "xl330-m077"),
                    "elbow_flex": (3, "xl330-m077"),
                    "wrist_flex": (4, "xl330-m077"),
                    "wrist_roll": (5, "xl330-m077"),
                    "gripper": (6, "xl330-m077"),
                }
        pass
    
    @property
    def motor_names(self) -> list[str]:
        return list(self.motors.keys())
    
    def connect(self):
        self.is_connected = True
        # self.data = self.configuration.data
        # self.model = self.configuration.model

        # init_pos_rad = [-1.5708, -1.5708, 1.5708, -1.5708, -1.5708, 0]
        # self.data.qpos[-6:] = init_pos_rad
        # self.old_pos = deepcopy(self.data.qpos[-6:])
        # deep copy
        # mujoco.mj_forward(self.model, self.data)

        pass

    def read(self, data_name, motor_names: str | list[str] | None = None):
        values = np.zeros(6)
        values = values.astype(np.int32)
        return values

    def set_calibration(self, calibration: dict[str, tuple[int, bool]]):
        self.calibration = calibration

    def write(self, data_name, values: int | float | np.ndarray, motor_names: str | list[str] | None = None):

        if data_name in ["Torque_Enable", "Operating_Mode", "Homing_Offset", "Drive_Mode", "Position_P_Gain", "Position_I_Gain", "Position_D_Gain"]:
            return np.array(None)

        pass

    def disconnect(self):
        self.is_connected = False

    def __del__(self):
        if getattr(self, "is_connected", False):
            self.disconnect()

if __name__ == "__main__":
    pass
