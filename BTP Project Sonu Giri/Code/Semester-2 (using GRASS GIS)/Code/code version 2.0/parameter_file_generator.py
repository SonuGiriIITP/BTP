import main
import os
import sys
import time

time0 = time.time()
time1 = time.time()
#with single H value without erosion
H = [[0.95],[0.85],[0.8],[0.75],[0.65],[0.55],[0.5],[0.4],[0.3],[0.2]]
seed = [[3],[5],[7],[11],[13],[17],[23],[29],[31],[37]]
pathname = os.path.dirname(sys.argv[0])
fullpath = os.path.abspath(pathname)
filename = fullpath + "/" + "Output_single_H_no_erosion"
if not os.path.exists(filename):
	os.makedirs(filename)          # create output directory if it doesn't exist 

for i in range(1,11):
	filename = "parameter_1_H_no_erosion"+str(i)+".yaml"
	print filename
	fo = open(filename,"w")
	fo.write('---'+'\n')
	fo.write('resolution: 50'+'\n')
	fo.write('H: '+str(H[i-1])+'\n')
	fo.write('H_wt: [1]'+'\n')
	fo.write('seed: '+str(seed[i-1])+'\n')
	fo.write('sigma: 1.0'+'\n')
	fo.write('elev_range: [200, 1400]'+'\n')
	fo.write('max_level: 11'+'\n')
	fo.write('DEMcreator_option: fm2D'+'\n')
	fo.write('output_dir: Output_single_H_no_erosion/H_'+str(int(H[i-1][0]*100))+'\n')
	fo.write('river_drop: 15'+'\n')
	fo.write('Erosion_permission: False'+'\n')
	fo.write('counter: 1'+'\n')
	if i == 1:
		fo.write('decision_tree: True'+'\n')
	else:
		fo.write('decision_tree: False'+'\n')
	fo.write('no_of_veg_class: 10'+'\n')
	fo.write('training_elev_filename: new_elev.asc'+'\n')
	fo.write('training_landcover_filename: new_land.asc'+'\n')
	fo.write('training_river_filename: new_rivers.asc'+'\n')
	fo.write('...'+'\n')
	fo.close()
	main.main(filename)

time2 = time.time()
print "time taken", time2-time1
time1 = time2
print " Output_single_H_no_erosion completed"

#with single H value and erosion 10 times
H = [[0.95],[0.85],[0.8],[0.75],[0.65],[0.55],[0.5],[0.4],[0.3],[0.2]]
seed = [[3],[5],[7],[11],[13],[17],[23],[29],[31],[37]]
pathname = os.path.dirname(sys.argv[0])
fullpath = os.path.abspath(pathname)
filename = fullpath + "/" + "Output_single_H_with_erosion"
if not os.path.exists(filename):
	os.makedirs(filename)          # create output directory if it doesn't exist 
for i in range(1,11):
	filename = "parameter_1_H_erosion"+str(i)+".yaml"
	print filename
	fo = open(filename,"w")
	fo.write('---'+'\n')
	fo.write('resolution: 50'+'\n')
	fo.write('H: '+str(H[i-1])+'\n')
	fo.write('H_wt: [1]'+'\n')
	fo.write('seed: '+str(seed[i-1])+'\n')
	fo.write('sigma: 1.0'+'\n')
	fo.write('elev_range: [200, 1400]'+'\n')
	fo.write('max_level: 11'+'\n')
	fo.write('DEMcreator_option: fm2D'+'\n')
	fo.write('output_dir: Output_single_H_with_erosion/H_'+str(int(H[i-1][0]*100))+'\n')
	fo.write('river_drop: 15'+'\n')
	fo.write('Erosion_permission: True'+'\n')
	fo.write('counter: 10'+'\n')
	fo.write('decision_tree: False'+'\n')
	fo.write('no_of_veg_class: 10'+'\n')
	fo.write('training_elev_filename: new_elev.asc'+'\n')
	fo.write('training_landcover_filename: new_land.asc'+'\n')
	fo.write('training_river_filename: new_rivers.asc'+'\n')
	fo.write('...'+'\n')
	fo.close()
	main.main(filename)

time2 = time.time()
print "time taken", time2-time1
time1 = time2
print " Output_single_H_with_erosion completed"

#with double H value and no erosion
H = [[0.95, 0.6],[0.95, 0.4],[0.95, 0.2],[0.75,0.5],[0.65,0.3],[0.55,0.4],[0.5, 0.2],[0.4, 0.1],[0.3,0.9],[0.2,0.75]]
H_wt = [[0.8,0.2],[0.8,0.2],[0.85,0.2],[0.7,0.3],[0.85,0.15],[0.7,0.3],[0.8,0.2],[0.8,0.2],[0.2,0.8],[0.15,0.85]]
seed = [[3,7],[5,61],[31,7],[11,97],[13,53],[17,2],[23,31],[29,100],[31,76],[37,59]]
pathname = os.path.dirname(sys.argv[0])
fullpath = os.path.abspath(pathname)
filename = fullpath + "/" + "Output_double_H_no_erosion"
if not os.path.exists(filename):
	os.makedirs(filename)          # create output directory if it doesn't exist 
for i in range(1,11):
	filename = "parameter_2_H_no_erosion"+str(i)+".yaml"
	print filename
	fo = open(filename,"w")
	fo.write('---'+'\n')
	fo.write('resolution: 50'+'\n')
	fo.write('H: '+str(H[i-1])+'\n')
	fo.write('H_wt: '+str(H_wt[i-1])+'\n')
	fo.write('seed: '+str(seed[i-1])+'\n')
	fo.write('sigma: 1.0'+'\n')
	fo.write('elev_range: [200, 1400]'+'\n')
	fo.write('max_level: 11'+'\n')
	fo.write('DEMcreator_option: fm2D'+'\n')
	fo.write('output_dir: Output_double_H_no_erosion/H_'+str(int(H[i-1][0]*100))+'H_wt_'+str(int(H_wt[i-1][0]*100))+'H_'+str(int(H[i-1][1]*100))+'H_wt_'+str(int(H_wt[i-1][1]*100))+'\n')
	fo.write('river_drop: 15'+'\n')
	fo.write('Erosion_permission: False'+'\n')
	fo.write('counter: 10'+'\n')
	fo.write('decision_tree: False'+'\n')
	fo.write('no_of_veg_class: 10'+'\n')
	fo.write('training_elev_filename: new_elev.asc'+'\n')
	fo.write('training_landcover_filename: new_land.asc'+'\n')
	fo.write('training_river_filename: new_rivers.asc'+'\n')
	fo.write('...'+'\n')
	fo.close()
	main.main(filename)

time2 = time.time()
print "time taken", time2-time1
time1 = time2
print "Output_double_H_no_erosion done"

#with double H value and erosion
H = [[0.95, 0.6],[0.95, 0.4],[0.95, 0.2],[0.75,0.5],[0.65,0.3],[0.55,0.4],[0.5, 0.2],[0.4, 0.1],[0.3,0.9],[0.2,0.75]]
H_wt = [[0.8,0.2],[0.8,0.2],[0.85,0.2],[0.7,0.3],[0.85,0.15],[0.7,0.3],[0.8,0.2],[0.8,0.2],[0.2,0.8],[0.15,0.85]]
seed = [[3,7],[5,61],[31,7],[11,97],[13,53],[17,2],[23,31],[29,100],[31,76],[37,59]]
pathname = os.path.dirname(sys.argv[0])
fullpath = os.path.abspath(pathname)
filename = fullpath + "/" + "Output_double_H_with_erosion"
if not os.path.exists(filename):
	os.makedirs(filename)          # create output directory if it doesn't exist 
for i in range(1,11):
	filename = "parameter_2_H_erosion"+str(i)+".yaml"
	print filename
	fo = open(filename,"w")
	fo.write('---'+'\n')
	fo.write('resolution: 50'+'\n')
	fo.write('H: '+str(H[i-1])+'\n')
	fo.write('H_wt: '+str(H_wt[i-1])+'\n')
	fo.write('seed: '+str(seed[i-1])+'\n')
	fo.write('sigma: 1.0'+'\n')
	fo.write('elev_range: [200, 1400]'+'\n')
	fo.write('max_level: 11'+'\n')
	fo.write('DEMcreator_option: fm2D'+'\n')
	fo.write('output_dir: Output_double_H_with_erosion/H_'+str(int(H[i-1][0]*100))+'H_wt_'+str(int(H_wt[i-1][0]*100))+'H_'+str(int(H[i-1][1]*100))+'H_wt_'+str(int(H_wt[i-1][1]*100))+'\n')
	fo.write('river_drop: 15'+'\n')
	fo.write('Erosion_permission: True'+'\n')
	fo.write('counter: 10'+'\n')
	fo.write('decision_tree: False'+'\n')
	fo.write('no_of_veg_class: 10'+'\n')
	fo.write('training_elev_filename: new_elev.asc'+'\n')
	fo.write('training_landcover_filename: new_land.asc'+'\n')
	fo.write('training_river_filename: new_rivers.asc'+'\n')
	fo.write('...'+'\n')
	fo.close()
	main.main(filename)

time2 = time.time()
print "time taken", time2-time1
time1 = time2
print "Output_double_H_with_erosion done"

#with Triple H value and no erosion
H = [[0.95, 0.8,0.6],[0.95,0.6,0.4],[0.95,0.7,0.2],[0.75,0.6,0.5],[0.65,0.5,0.3],[0.55,0.45,0.4],[0.5,0.3,0.2],[0.4,0.3,0.1],[0.3,0.6,0.9],[0.2,0.5,0.75]]
H_wt = [[0.7,0.15,0.15],[0.75,0.15,0.1],[0.85,0.1,0.05],[0.65,0.2,0.15],[0.8,0.15,0.05],[0.6,0.3,0.1],[0.7,0.2,0.1],[0.6,0.3,0.1],[0.1,0.3,0.6],[0.15,0.35,0.5]]
seed = [[3,7,31],[5,61,1],[31,7,17],[11,97,47],[13,53,7],[17,2,41],[23,31,5],[29,100,3],[31,76,13],[37,59,29]]
pathname = os.path.dirname(sys.argv[0])
fullpath = os.path.abspath(pathname)
filename = fullpath + "/" + "Output_Triple_H_no_erosion"
if not os.path.exists(filename):
	os.makedirs(filename)          # create output directory if it doesn't exist 
for i in range(1,11):
	filename = "parameter_3_H_no_erosion"+str(i)+".yaml"
	print filename
	fo = open(filename,"w")
	fo.write('---'+'\n')
	fo.write('resolution: 50'+'\n')
	fo.write('H: '+str(H[i-1])+'\n')
	fo.write('H_wt: '+str(H_wt[i-1])+'\n')
	fo.write('seed: '+str(seed[i-1])+'\n')
	fo.write('sigma: 1.0'+'\n')
	fo.write('elev_range: [200, 1400]'+'\n')
	fo.write('max_level: 11'+'\n')
	fo.write('DEMcreator_option: fm2D'+'\n')
	fo.write('output_dir: Output_Triple_H_no_erosion/H_'+str(int(H[i-1][0]*100))+'H_wt_'+str(int(H_wt[i-1][0]*100))+'H_'+str(int(H[i-1][1]*100))+'H_wt_'+str(int(H_wt[i-1][1]*100))+'H_'+str(int(H[i-1][2]*100))+'H_wt_'+str(int(H_wt[i-1][2]*100))+'\n')
	fo.write('river_drop: 15'+'\n')
	fo.write('Erosion_permission: False'+'\n')
	fo.write('counter: 10'+'\n')
	fo.write('decision_tree: False'+'\n')
	fo.write('no_of_veg_class: 10'+'\n')
	fo.write('training_elev_filename: new_elev.asc'+'\n')
	fo.write('training_landcover_filename: new_land.asc'+'\n')
	fo.write('training_river_filename: new_rivers.asc'+'\n')
	fo.write('...'+'\n')
	fo.close()
	main.main(filename)

time2 = time.time()
print "time taken", time2-time1
time1 = time2
print "Output_Triple_H_no_erosion done"



#with Triple H value and erosion
H = [[0.95, 0.8,0.6],[0.95,0.6,0.4],[0.95,0.7,0.2],[0.75,0.6,0.5],[0.65,0.5,0.3],[0.55,0.45,0.4],[0.5,0.3,0.2],[0.4,0.3,0.1],[0.3,0.6,0.9],[0.2,0.5,0.75]]
H_wt = [[0.7,0.15,0.15],[0.75,0.15,0.1],[0.85,0.1,0.05],[0.65,0.2,0.15],[0.8,0.15,0.05],[0.6,0.3,0.1],[0.7,0.2,0.1],[0.6,0.3,0.1],[0.1,0.3,0.6],[0.15,0.35,0.5]]
seed = [[3,7,31],[5,61,1],[31,7,17],[11,97,47],[13,53,7],[17,2,41],[23,31,5],[29,100,3],[31,76,13],[37,59,29]]
pathname = os.path.dirname(sys.argv[0])
fullpath = os.path.abspath(pathname)
filename = fullpath + "/" + "Output_Triple_H_erosion"
if not os.path.exists(filename):
	os.makedirs(filename)          # create output directory if it doesn't exist 
for i in range(1,11):
	filename = "parameter_3_H_erosion"+str(i)+".yaml"
	print filename
	fo = open(filename,"w")
	fo.write('---'+'\n')
	fo.write('resolution: 50'+'\n')
	fo.write('H: '+str(H[i-1])+'\n')
	fo.write('H_wt: '+str(H_wt[i-1])+'\n')
	fo.write('seed: '+str(seed[i-1])+'\n')
	fo.write('sigma: 1.0'+'\n')
	fo.write('elev_range: [200, 1400]'+'\n')
	fo.write('max_level: 11'+'\n')
	fo.write('DEMcreator_option: fm2D'+'\n')
	fo.write('output_dir: Output_Triple_H_erosion/H_'+str(int(H[i-1][0]*100))+'H_wt_'+str(int(H_wt[i-1][0]*100))+'H_'+str(int(H[i-1][1]*100))+'H_wt_'+str(int(H_wt[i-1][1]*100))+'H_'+str(int(H[i-1][2]*100))+'H_wt_'+str(int(H_wt[i-1][2]*100))+'\n')
	fo.write('river_drop: 15'+'\n')
	fo.write('Erosion_permission: True'+'\n')
	fo.write('counter: 10'+'\n')
	fo.write('decision_tree: False'+'\n')
	fo.write('no_of_veg_class: 10'+'\n')
	fo.write('training_elev_filename: new_elev.asc'+'\n')
	fo.write('training_landcover_filename: new_land.asc'+'\n')
	fo.write('training_river_filename: new_rivers.asc'+'\n')
	fo.write('...'+'\n')
	fo.close()
	main.main(filename)

time2 = time.time()
print "time taken", time2-time1
time1 = time2
time3 = time.time()
print "Output_Triple_H_erosion done"
print "Total time taken", time3-time0
