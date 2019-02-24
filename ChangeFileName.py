import os
import re
class BatchRename():
    '''
    批量重命名文件夹中的图片文件

    '''
    def __init__(self):
        self.path = 'I:\Joymii.com_14.06.16.Josephine.A.Quick.Romp.XXX.IMAGESET-GAGBALL[rarbg]'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 0

        for item in filelist:
            #print(item)
            if item.endswith('.jpg'):
                a = re.sub("\\[.*?]", "", item)
                #a=item.replace('r_4297','')
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), a)
                #dst=os.rename("/\[.*\]/", '', item)
                os.rename(src, dst)

                #dst = os.path.join(os.path.abspath(self.path), str(i) + '.jpg')
'''
                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...')% (src, dst)

                except:
                    continue
                    print('')
'''

        #print('total %d to rename & converted %d jpgs')%(total_num, i)


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
