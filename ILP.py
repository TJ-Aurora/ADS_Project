from gurobipy import *




images = ["image1", "image2", "image3", "image4", "image5"]
intervals = ["inter1", "inter2", "inter3"]

image_length = {"image1": 4.23, "image2": 2, "image3": 5.6, "image4": 9.12, "image5": 4.5}
interval_length = {"inter1": 2.5, "inter2": 1.6, "inter3": 9}

model = Model("Image Scheduling")

x = model.addVars(images, intervals, vtype = GRB.BINARY, name = "if inside")

c1 = model.addConstrs((quicksum(image_length[image]*x[image, interval] for image in images) <= interval_length[interval]) for interval in intervals)
c2 = model.addConstrs((quicksum(x[image, interval] for interval in intervals) <= 1) for image in images)

obj_function = quicksum(image_length[image]*x[image, interval] for image in images for interval in intervals)
model.setObjective(obj_function, GRB.MAXIMIZE)

model.optimize()
model.printAttr('x')

