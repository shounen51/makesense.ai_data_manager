import json
import os
import shutil
import re

from configs import dataDir, pic_dir, del_dir
from utils.utils import save_json

def load_json(path):
    _dict={}
    with open(path,encoding="utf-8") as file:
        _dict = json.load(file)
    return _dict

class data_loader():
    def __init__(self, srcDir):
        self.srcDir = srcDir
        txtPath = "classes.txt"
        with open(txtPath, 'r', encoding="utf-8") as txt:
            classes = txt.readlines()
        self.classesNames = [c.rstrip() for c in classes]
        self.classNum = len(self.classesNames)
        self.data_dict = {}
        self.classesPics = {}
        self.region_num = 0
        for cl in self.classesNames:
            self.classesPics[cl] = []
        self.zhPattern = re.compile(u'[\u4e00-\u9fff]+')
        self._load_json()

    def _load_json(self):
        os.makedirs(pic_dir, exist_ok = True)
        pic_dir_0 = os.path.join(pic_dir, '0')
        os.makedirs(pic_dir_0, exist_ok = True)
        for d in [pic_dir, self.srcDir]:
            for _file in os.listdir(d):
                _dir = os.path.join(d, _file)
                if os.path.isdir(_dir):
                    for path in os.listdir(_dir):
                        if path.split('.')[-1]=='json' or path.split('.')[-1]=='txt':
                            jsonPath = os.path.join(_dir, path)
                            _json = load_json(jsonPath)
                            for pic in _json:
                                if self.zhPattern.search(pic):
                                    continue
                                pic_dict = _json[pic]
                                pic_path = os.path.join(_dir, pic)
                                shutil.move(os.path.join(_dir, pic), os.path.join(pic_dir_0, pic))
                                _json[pic]['filename'] = os.path.join(pic_dir_0, pic)
                                regions = pic_dict['regions']
                                for region in regions.values():
                                    self.region_num += 1
                                    label = region['region_attributes']['label']
                                    if not pic in self.classesPics[label]:
                                        self.classesPics[label].append(pic)
                            self.data_dict.update(_json)
                            os.remove(jsonPath)
        self.save_json()

    def save_json(self):
        pic_dir_0 = os.path.join(pic_dir, '0')
        save_json(os.path.join(pic_dir_0,'ann.json'), self.data_dict)

    def del_json(self, pic_name):
        os.makedirs(del_dir, exist_ok = True)
        shutil.move(self.data_dict[pic_name]['filename'], os.path.join(del_dir, pic_name))
        self.data_dict.pop(pic_name)

    def get_classes_pics(self, className):
        return self.classesPics[className]

    def get_pic_dict(self, picName):
        return self.data_dict[picName]

    def get_class_names(self):
        return self.classesNames

    def get_pics_num(self):
        return len(self.data_dict)

    def get_region_num(self):
        return self.region_num
