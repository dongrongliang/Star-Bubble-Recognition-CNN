import os, re
import math
from PIL import Image

train_rate=0.8
path=['./raw/nobubble','./raw/bubble']
train_savepath=['./train/nobubble','./train/bubble']
test_savepath=['./validation/nobubble','./validation/bubble']

for i in [0,1]:
    _RAW_DIR = path[i]
    _RE_INDEX = re.compile(u"pic(\d{3})\..+")
    file_cound = len(os.listdir(_RAW_DIR))
    for index in range(1, 1+file_cound):
        this_name = _RAW_DIR+'/pic%03d.png' %index
        with Image.open(this_name) as img:
            _new= img.resize((200, 200), resample=Image.LANCZOS)
            _new=_new.convert('RGB')
            if index<=math.floor(file_cound*train_rate):
                _new.save(train_savepath[i]+"/pic%03d.jpg"%index, format="JPEG")
            else:
                _new.save(test_savepath[i] + "/pic%03d.jpg" % index, format="JPEG")
