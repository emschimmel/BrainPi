
from LongTermMemoryServer import main

import logging
import sys
sys.path.append('../../')
import config

logger = logging.getLogger('LongTermMemory')
logger.setLevel(config.log_level)

fh = logging.FileHandler(config.log_dir+'LongMemory.log', mode='a')
fh.setLevel(config.log_level)

ch = logging.StreamHandler()
ch.setLevel(config.log_level)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
logger.info('creating an instance of Longmemory via main')

main()
