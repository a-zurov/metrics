import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from matplotlib.colors import Normalize

def draw_3d_histogram():
    # Data from previous analysis
    query_execution_durations =  [0.31578707695007324, 0.1733379364013672, 0.11465978622436523, 0.038672685623168945, 0.15253949165344238, 0.11572408676147461, 0.10745596885681152, 0.2843639850616455, 0.22206783294677734, 0.20615577697753906, 0.1659088134765625, 0.13867568969726562, 0.21921849250793457, 0.13065409660339355, 0.12177205085754395, 0.21158194541931152, 0.15075945854187012, 0.1658954620361328, 0.12460637092590332, 0.13865327835083008, 0.10924482345581055, 0.11766600608825684, 0.12574458122253418, 0.11546993255615234, 0.1140446662902832]
    read_latencies =   [0.24005532264709473, 0.15590333938598633, 0.0996406078338623, 0.03750729560852051, 0.13541769981384277, 0.10248947143554688, 0.09839129447937012, 0.23510313034057617, 0.19327425956726074, 0.18544650077819824, 0.1666247844696045, 0.13736248016357422, 0.21811270713806152, 0.12962627410888672, 0.10993480682373047, 0.1892843246459961, 0.15209245681762695, 0.17849040031433105, 0.12835407257080078, 0.10121607780456543, 0.10571408271789551, 0.10302996635437012, 0.10997915267944336, 0.10561418533325195, 0.11203122138977051]
    ids = [286100, 179617, 98371, 20922, 157043, 111643, 98202, 299869, 230403, 189797, 178272, 133881, 228845, 132765, 111253, 220436, 159779, 150050, 113765, 110674, 110849, 108786, 122897, 113861, 102722]
    
    num_bboxes = 5
    x = np.tile(np.arange(num_bboxes), num_bboxes)
    y = np.repeat(np.arange(num_bboxes), num_bboxes)
    z = np.zeros(len(read_latencies))
    dx = dy = np.ones(len(read_latencies))
    dz = read_latencies

    # Normalize the values to map to a colormap
    norm = Normalize(vmin=min(dz), vmax=max(dz))
    colors = cm.viridis(norm(dz))

    # Create figure
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plotting the 3D histogram with colors
    ax.bar3d(x, y, z, dx, dy, dz, shade=True, color=colors)
    
    # Adding labels
    ax.set_xlabel('X (bbox index)')
    ax.set_ylabel('Y (bbox index)')
    ax.set_zlabel('Read Latency (s)')
    ax.set_title('3D Histogram of Query Performance Metrics')

    # Adding IDs on top of each column
    for i in range(len(ids)):
        ax.text(x[i]+dx[i]/2, y[i]+dy[i]/2, dz[i], '%d' % ids[i], ha='center', va='bottom', fontsize=10, color='red')

    # Display the 3D histogram
    plt.tight_layout()
    plt.show()

# Draw the 3D histogram
draw_3d_histogram()
