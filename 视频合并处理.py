import os, shutil
from natsort import natsorted

fl = open(os.path.join('3','list.txt'),'w+')

# 访问指定文件夹(假设视频都放在这里面)
for root, dirs, files in os.walk("./3"):
    # 按文件名排序
    files = natsorted(files)
    # 遍历所有文件
    for file in files:
        # 如果后缀名为 .mp4
        if os.path.splitext(file)[1] == '.mp4':
            # 拼接成路径写入
            var = 'file '+'3/'+file
            fl.writelines(var)
            fl.write('\n')


fl.close()
# 生成目标视频文件
list_txt = os.path.join('3',"list")
finishcode2 = "ffmpeg -f concat -i "+list_txt+".txt"+" -c copy "+"output.mp4"
os.system(finishcode2)
#shutil.rmtree("./3")删除不删除大家看着来，一定要慎重，建议不要启用
#os.makedirs('3')
