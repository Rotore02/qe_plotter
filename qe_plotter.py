import numpy as np
import matplotlib.pyplot as mp

def read_data(filename):

 k_points = []
 bands = []
 try:
    file = open(filename, 'r')
 except FileNotFoundError:
    print("Input file not found")
    exit()

 k_points_temp = []
 bands_temp = []
 max_val = []
 min_val = []

 for line in file:
    if not line.strip():
        k_points.append(k_points_temp)
        bands.append(bands_temp)
        max_val.append(max(bands_temp))
        min_val.append(min(bands_temp))
        k_points_temp = []
        bands_temp = []
    else:
        k, b, *rest  = line.strip().split()
        try:
           k_points_temp.append(float(k))
           bands_temp.append(float(b))
        except ValueError:
           print("Unable to convert str to float")
           exit()
    
 if k_points_temp and bands_temp:
    k_points.append(k_points_temp)
    bands.append(bands_temp)
    max_val.append(max(bands_temp))
    min_val.append(min(bands_temp))
    k_points_temp = []
    bands_temp = []

 file.close()

 return k_points, bands, max(max_val), min(min_val)

def read_k_points(K_points_filename):
   k_points_labels = []
   coordinates = []
   try:
      file = open(K_points_filename, 'r')
   except FileNotFoundError:
      print("K points file not found")
   for line in file:
      point, coordinate = line.strip().split()
      k_points_labels.append(point)
      coordinates.append(coordinate)
   return k_points_labels, coordinates


def main():
    calc = input("type of calculation: ")
    if calc not in ["bands", "BANDS", "dos", "DOS"]:
       print("Invalid or not supported type of calculation"'\n'"Supported types: dos, DOS, bands, BANDS")
       exit()
    print("Remember to cancel every non data starting line from your input file!"'\n')
    input_file_name = input("Input file name: ")
    output_file_name = input("Output file name: ")
    K_points_filename = input("Input K points file (leave empty if not present): ")
    if not K_points_filename:
       k_points, bands, max_val, min_val = read_data(input_file_name)
       if calc == "bands" or calc == "BANDS":
        for i in np.arange(len(k_points)):
          mp.plot(k_points[i], bands[i], label = f'banda {i+1}')
        mp.ylim(min_val, max_val)
        mp.title("Electronic bands")
        mp.xlabel("K points")
        mp.ylabel("Energy (eV)")
       if calc == "dos" or calc == "DOS":
        for i in np.arange(len(k_points)):
          mp.plot(k_points[i], bands[i])
        mp.ylim(min_val, max_val)
        mp.title("Density of states")
        mp.xlabel("Energy (eV)")
        mp.ylabel("Density of states")

    else:
       k_points, bands, max_val, min_val = read_data(input_file_name)
       if calc == "bands" or calc == "BANDS":
        for i in np.arange(len(k_points)):
          mp.plot(k_points[i], bands[i], label = 'banda {i+1}')
        mp.ylim(min_val, max_val)
        mp.title("Electronic bands")
        mp.xlabel("K points")
        mp.ylabel("Energy (eV)")
        k_points_labels, coordinates = read_k_points(K_points_filename)
        mp.xticks(coordinates, k_points_labels)
       if calc == "dos" or calc == "DOS":
        for i in np.arange(len(k_points)):
          mp.plot(k_points[i], bands[i])
        mp.ylim(min_val, max_val)
        mp.title("Density of states")
        mp.xlabel("Energy (eV)")
        mp.ylabel("Density of states")
       
    

    mp.savefig(output_file_name)
   
if __name__ == "__main__":
   main()