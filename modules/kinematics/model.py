class Model:
    """
    Model class for kinematics module.
    model defines a kinematic data set and provides methods to manipulate it. and current frame of the model
    """

    def __init__(self, data) -> None:
        self.kinematic = data.kinematic
        self.emg = data.emg

    def kinematic_frame(self, frame):
        return self.kinematic[frame]

    def kinematic_frames(self):
        return self.kinematic.length

    def kinematic_frame_rate(self):
        return self.kinematic.data.fs

    def total_time(self):
        return self.kinematic.length / self.kinematic.data.fs
