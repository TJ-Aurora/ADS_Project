from gurobipy import *




images = ["image1", "image2", "image3"]
intervals = ["inter1", "inter2", "inter3"]
#blocks = ["block1", "block2"]

image_length = {"image1": 4, "image2": 2.5, "image3": 2}
interval_length = {"inter1": 2.5, "inter2": 1.6, "inter3": 9}
#block_length = {"block1": 0.9, "block2": 3}
interval_index = {"inter1": 3, "inter2": 2, "inter3": 1}



model = Model("Image Scheduling")

x = model.addVars(images, intervals, vtype = GRB.BINARY, name = "if inside")
#y = model.addVars(blocks, vtype = GRB.BINARY, name = "if include")

c1 = model.addConstrs((quicksum(image_length[image]*x[image, interval] for image in images) <= interval_length[interval]) 
	for interval in intervals)
c2 = model.addConstrs((quicksum(x[image, interval] for interval in intervals) <= 1) for image in images)

c3 = model.addConstrs((quicksum(x[image, interval] for interval in intervals) >= 1) for image in images)
"""
c4 = model.addConstrs((int((quicksum(x[image, interval] for image in images for interval in intervals[blocks.index(block)+1:]) >= 1) == True) 
	== y[block]) for block in blocks)
"""



#obj_function = quicksum(image_length[image]*x[image, interval] for image in images for interval in intervals) + quicksum(y[block]*block_length[block] for block in blocks)
obj_function = quicksum(interval_index[interval]*x[image, interval]*image_length[image] for interval in intervals for image in images)
model.setObjective(obj_function, GRB.MAXIMIZE)

model.optimize()
model.printAttr('X')

