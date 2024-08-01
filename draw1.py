import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def draw_3d_histogram():
    # Data from previous analysis
    query_execution_durations = [0.4695591926574707, 0.22533345222473145, 0.13015174865722656, 0.03989672660827637, 0.19720697402954102, 0.22051334381103516, 0.12401342391967773, 0.35902929306030273, 0.27614545822143555, 0.269528865814209, 0.2185976505279541, 0.17514610290527344, 0.2766439914703369, 0.16667699813842773, 0.14165377616882324, 0.2590913772583008, 0.19258618354797363, 0.18382883071899414, 0.14954781532287598, 0.14006757736206055, 0.14096522331237793, 0.13477134704589844, 0.15429472923278809, 0.14032244682312012, 0.1273336410522461]
    read_latencies = [0.3095676898956299, 0.19873976707458496, 0.11423468589782715, 0.03549480438232422, 0.17312335968017578, 0.1318531036376953, 0.11600899696350098, 0.31893062591552734, 0.25846195220947266, 0.25026416778564453, 0.20276165008544922, 0.15565013885498047, 0.24782776832580566, 0.1492459774017334, 0.12613821029663086, 0.25355076789855957, 0.17456364631652832, 0.1681685447692871, 0.13210606575012207, 0.1250171661376953, 0.12603092193603516, 0.12501120567321777, 0.1389307975769043, 0.15549373626708984, 0.1323552131652832]
    ids = [286100, 179617, 98371, 20922, 157043, 111643, 98202, 299869, 230403, 189797, 178272, 133881, 228845, 132765, 111253, 220436, 159779, 150050, 113765, 110674, 110849, 108786, 122897, 113861, 102722]
    
    num_bboxes = 5
    x = np.tile(np.arange(num_bboxes), num_bboxes)
    y = np.repeat(np.arange(num_bboxes), num_bboxes)
    z = np.zeros(len(read_latencies))
    dx = dy = np.ones(len(read_latencies))
    dz = read_latencies

    # Create figure
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plotting the 3D histogram
    ax.bar3d(x, y, z, dx, dy, dz, shade=True)
    
    # Adding labels
    ax.set_xlabel('X (bbox index)')
    ax.set_ylabel('Y (bbox index)')
    ax.set_zlabel('Read Latency (s)')
    ax.set_title('3D Histogram of Query Performance Metrics')

    # Adding IDs on top of each column
    for i in range(len(ids)):
        ax.text(x[i], y[i], dz[i] + 0.05, '%d' % ids[i], ha='center', va='bottom', fontsize=10, color='red')

    # Display the 3D histogram
    plt.tight_layout()
    plt.show()

# Draw the 3D histogram
draw_3d_histogram()
