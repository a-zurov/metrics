import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from matplotlib.colors import Normalize

def draw_3d_histogram():
    # Data from previous analysis
    query_execution_durations = [0.5131089687347412, 0.3452739715576172, 0.154191255569458, 0.05582284927368164, 0.27645230293273926, 0.21557831764221191, 0.16778159141540527, 0.45563435554504395, 0.40924072265625, 0.5481777191162109, 0.294708251953125, 0.21262311935424805, 0.3470020294189453, 0.21551942825317383, 0.19594764709472656, 0.31882786750793457, 0.2350447177886963, 0.3012046813964844, 0.24967479705810547, 0.18256664276123047, 0.17208433151245117, 0.17142724990844727, 0.20713472366333008, 0.23127150535583496, 0.17861294746398926]
    read_latencies =  [0.4765031337738037, 0.2297372817993164, 0.14148759841918945, 0.045487403869628906, 0.27388954162597656, 0.1633617877960205, 0.12872838973999023, 0.33054518699645996, 0.2510843276977539, 0.2610199451446533, 0.22614622116088867, 0.15712237358093262, 0.2531602382659912, 0.14961719512939453, 0.13094472885131836, 0.26723361015319824, 0.18885183334350586, 0.3664565086364746, 0.20654559135437012, 0.15381360054016113, 0.13079166412353516, 0.1570594310760498, 0.2561986446380615, 0.22499370574951172, 0.1565237045288086]
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
