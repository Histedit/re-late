import subprocess
from time import sleep
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
def animate(i):
    subprocess.call("copy C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.events C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.3",shell=True)
    subprocess.call("TYPE C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\e.nd >> C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.3",shell=True)
    tree = ET.parse('C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.3')
    root = tree.getroot()
    _nowLen = int(len(root))
    
    data = []
    for i in range(7):
        data.append(float(root[_nowLen-1][i].get('value')))
    performance = data

    objects = ('anger', 'boredom', 'disgust', 'fear', 'happiness', 'neutral','sadness')
    y_pos = np.arange(len(objects))
    fig.clear()
    plt.ylim(0.0, 1.0)
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Value')
    plt.title('Speech Emotion Recognition')

ani = animation.FuncAnimation(fig,animate,interval=750) 
plt.show()
    