from gurobipy import *



images = ["image1", "image2", "image3", "image4", "image5"]
intervals = ["inter1", "inter2", "inter3"]

image_length = {"image1": 4.23, "image2": 2, "image3": 5.6, "image4": 9.12, "image5": 4.5}
interval_length = {"inter1": 2.5, "inter2": 1.6, "inter3": 9}
interval_index = {"inter1": 3, "inter2": 2, "inter3": 1}

"""
images = ["image1", "image2", "image3", "image4", "image5", "image6", "image7", "image8", "image9", "image10"]
intervals = ["inter1", "inter2", "inter3", "inter4", "inter5", "inter6"]

image_length = {"image1": 1.4, "image2": 2, "image3": 3.1, "image4": 3.6, "image5": 5.4, "image6": 7.3, "image7": 8.9, "image8": 9.7, "image9": 12.1, "image10": 13}
interval_length = {"inter1": 2.4, "inter2": 1.5, "inter3": 0.3, "inter4": 1.2, "inter5": 5.4, "inter6": 4.5}
interval_index = {"inter1": 6, "inter2": 5, "inter3": 4, "inter4": 3, "inter5": 2, "inter6": 1}
"""


model = Model("Image Scheduling")

x = model.addVars(images, intervals, vtype = GRB.BINARY, name = "if inside")

c1 = model.addConstrs((quicksum(image_length[image]*x[image, interval] for image in images) <= interval_length[interval]) 
	for interval in intervals)
c2 = model.addConstrs((quicksum(x[image, interval] for interval in intervals) <= 1) for image in images)


obj_function = quicksum(interval_index[interval]*x[image, interval]*image_length[image] for interval in intervals for image in images)
model.setObjective(obj_function, GRB.MAXIMIZE)

model.optimize()
model.printAttr('X')

