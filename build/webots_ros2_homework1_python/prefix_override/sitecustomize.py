import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ggkarabas/cooper/f24_robotics/install/webots_ros2_homework1_python'
