# GPL License
# Copyright (C) 2021 , UESTC
# All Rights Reserved 
#
# @Time    : 2022/4/25 0:17
# @Author  : Xiao Wu
# @reference:
import sys
sys.path.append('../..')
from UDL.AutoDL import TaskDispatcher
from UDL.AutoDL.trainer import main

if __name__ == '__main__':
    # cfg = TaskDispatcher.new(task='pansharpening', mode='entrypoint', arch='BDPN')
    cfg = TaskDispatcher.new(task='pansharpening', mode='entrypoint', arch='FusionNet')
    print(TaskDispatcher._task.keys())
    # main(cfg)    # 进行训练


# arch='BDPN', and configs/option_bdpn.py has:
# __cfg.eval__ = False,
# __cfg.workflow__ = [('train', 50), ('val', 1)],
# __cfg.dataset__ = {'train': 'wv3', 'val': 'wv3_multiExm.h5'}