import os
import shutil
import glob


idir = os.listdir('/home/dev/NanoJet/Generating_Handwritten/Data/IAM/iam-handwritten-forms-dataset/data/')
isave = '/home/dev/NanoJet/Generating_Handwritten/Data/IAM/iam-handwritten-forms-dataset/totals/'

def _check_exits():
    total_img = glob.glob(isave + '*.*')
    return total_img

for kli in idir:
    print('KLI: \t', kli)
    tt_img = _check_exits()
    print('tt_img: \t', len(tt_img))
    
    for i in glob.glob(f'/home/dev/NanoJet/Generating_Handwritten/Data/IAM/iam-handwritten-forms-dataset/data/{kli}/*.*'):
        name = os.path.basename(i)
        if i in tt_img:
            print('EXITED: \t', i)
        else:
            shutil.copyfile(i, isave+name)