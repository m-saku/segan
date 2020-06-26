#
# Settings for SEGAN
#

class settings:

    def __init__(self):

        # General Settings
        self.len                = 2 ** 14           # Input Size (len = 16384)
        self.device_id          = 0                 # GPU ID (init:0)
        self.random_seed        = 0
        self.halfprec           = True              # 16Bit or not

        # Parameters
        self.batch_size 	    = 150               # Batch size
        self.epoch              = 200               # Epoch
        self.learning_rate_gen  = 0.0001            # Learning Rate (Generator)
        self.learning_rate_dis  = 0.00001          # Learning Rate (Discriminator)
        self.weight_decay_rate 	= 0.0001              # Regularization rate (weight decay = learning_rate * weight_decay_rate)

        # Retrain
        self.epoch_from         = 0                 # Epoch No. from that Retraining starts (init:0)

        # Save path
        self.model_save_path    = 'params'          # Network model path
        self.model_save_cycle   = 20                      # Epoch cycle for saving model (init:1)

        # Save wav path
        self.wav_save_path      = 'pred'


        self.clean_train_path = 'D:\data/clean_trainset_wav_16k'  # 学習用クリーンwavのパス
        self.noisy_train_path = 'D:\data/noisy_trainset_wav_16k'  # 学習用ノイジィwavのパス
        self.clean_test_path = 'D:\data/clean_testset_wav_16k'
        self.noisy_test_path = 'D:\data/noisy_testset_wav_16k'

        self.train_pkl_path = 'pkl'             # 学習用クリーンpklのパス
        self.train_pkl_clean = 'train_clean.pkl'             # 学習用ノイジィpklのパス
        self.train_pkl_noisy = 'train_noisy.pkl'

        # Pkl files for test
        self.test_pkl_path      = 'pkl'             # Folder of pkl files for test
        self.test_pkl_clean     = 'test_clean.pkl'  # File name of "Clean" pkl for test
        self.test_pkl_noisy     = 'test_noisy.pkl'  # File name of "Noisy" pkl for test

