from UDL.AutoDL import TaskDispatcher
from UDL.AutoDL.trainer import main

if __name__ == '__main__':
    # cfg = parser_args()
    cfg = TaskDispatcher.new(task='pansharpening', mode='entrypoint', arch='BDPN')
    cfg.eval = True  # perform test on the dataset of wv3_multiExm.h5.
    # cfg.dataset = {'train': 'wv3', 'valid': 'wv3_multiExm.h5'} #'wv3_OrigScale_multiExm1.h5'
    print(TaskDispatcher._task.keys())
    main(cfg)


    # A test example:
    # __cfg.eval__ = True
    # or __cfg.workflow__ = [('val', 1)]