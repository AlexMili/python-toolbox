import math

from PIL import Image, ImageDraw, ImageFont

def drawpoint(img,(x,y),radius=10,circle_color=(255,0,0)):
	draw = ImageDraw.Draw(img)
	draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=circle_color)
	return img

def drawline(img,coords_start,coords_end,color=(255,0,0),width=5):
	draw = ImageDraw.Draw(img)
	draw.line((coords_start,coords_end), fill=color,width=width)
	return img

def generateAroundArea(x,y,offset):
	return {"x_start":x-offset,"y_start":y-offset,"x_end":x+offset,"y_end":y+offset}

def drawlineAround(img,center,offset=10,color=(0,0,255),width=5):
	border = generateAroundArea(center[0],center[1],offset)
	draw = ImageDraw.Draw(img)
	drawline(((border["x_start"],border["y_start"]),(border["x_end"],border["y_start"])), color=color,width=width)
	drawline(((border["x_end"],border["y_start"]),(border["x_end"],border["y_end"])), color=color,width=width)
	drawline(((border["x_start"],border["y_end"]),(border["x_end"],border["y_end"])), color=color,width=width)
	drawline(((border["x_start"],border["y_start"]),(border["x_start"],border["y_end"])), color=color,width=width)
	return img

# Compute euclidian distance between two points
def distance(x1,y1,x2,y2):
	return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))