import json
import os
import shutil

def load_json(path):
    _dict={}
    with open(path,encoding="utf-8") as file:
        _dict = json.load(file)
    return _dict

class data_loader():
    def __init__(self, rootDir):
        self.rootDir = rootDir
        txtPath = os.path.join(rootDir,"classes.txt")
        with open(txtPath, 'r', encoding="utf-8") as txt:
            classes = txt.readlines()
        self.classesNames = [c.rstrip() for c in classes]
        self.classNum = len(self.classesNames)
        self.data_dict = {}
        self.classesPics = {}
        for cl in self.classesNames:
            self.classesPics[cl] = []
        self._load_json()

    def _load_json(self):
        for _file in os.listdir(self.rootDir):
            _dir = os.path.join(self.rootDir,_file)
            if os.path.isdir(_dir):
                for path in os.listdir(_dir):
                    if path.split('.')[-1]=='json':
                        jsonPath = os.path.join(_dir, path)
                        _json = load_json(jsonPath)
                        for pic in _json:
                            pic_dict = _json[pic]
                            _json[pic]['filename'] = os.path.join(_dir, pic)
                            regions = pic_dict['regions']
                            for region in regions.values():
                                label = region['region_attributes']['label']
                                if not pic in self.classesPics[label]:
                                    self.classesPics[label].append(pic)
                        self.data_dict.update(_json)

    def get_classes_pics(self, className):
        return self.classesPics[className]

    def get_pic_dict(self, picName):
        return self.data_dict[picName]

    def get_class_names(self):
        return self.classesNames

    def get_pics_num(self):
        return len(self.data_dict)

