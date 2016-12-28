import math

from PIL import Image, ImageDraw, ImageFont

def drawpoint(img,x_y,radius=10,circle_color=(255,0,0)):
	x,y=x_y
	draw = ImageDraw.Draw(img)
	draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=circle_color)
	return img

# Display coords given a dataset
def display_coords(df,cols=["x","y"],radius=10,color=(0,255,0),screenWidth=100,screenHeight=100,\
					font_family="arial.ttf",font_size=20,font_color=(0,0,0),background_color="gray",display_num=True):
	img = Image.new("RGB", (screenWidth, screenHeight), background_color)
	draw = ImageDraw.Draw(img)

	i = 0
	for row in df.iterrows():
		img = Toolbox.graphics.drawpoint(img,(row[1][cols[0]],row[1][cols[0]]),radius=radius,circle_color=color)

		if(display_num):
			draw.text((row[1][cols[0]],row[1][cols[0]]), str(i+1), fill=font_color,\
				font=ImageFont.truetype(font_family, font_size))

		i=i+1

	return img

def drawline(img,coords_start,coords_end,color=(255,0,0),width=5):
	draw = ImageDraw.Draw(img)
	draw.line((coords_start,coords_end), fill=color,width=width)
	return img

def generateAroundArea(x,y,offset):
	return {"x_start":x-offset,"y_start":y-offset,"x_end":x+offset,"y_end":y+offset}

# Determine if the coordinates are in a given area
def is_in_area(points=(5,5),area={'x_start':0,'y_start':0,'x_end':10,'y_end':10}):
	x,y = points

	if(x >= area['x_start'] and x < area['x_end'] and y >= area['y_start'] and y < area['y_end']):
		return True
	else:
		return False

# Alias with the goal to replace drawlineAround
def drawbox(img,center,border=None,offset=10,color=(0,0,255),width=5):
	return drawlineAround(img,center,border,offset,color,width)

def drawlineAround(img,center,border=None,offset=10,color=(0,0,255),width=5):
	if(border == None):
		border = generateAroundArea(center[0],center[1],offset)

	draw = ImageDraw.Draw(img)
	img = drawline(img,(border["x_start"],border["y_start"]),(border["x_end"],border["y_start"]), color=color,width=width)
	img = drawline(img,(border["x_end"],border["y_start"]),(border["x_end"],border["y_end"]), color=color,width=width)
	img = drawline(img,(border["x_start"],border["y_end"]),(border["x_end"],border["y_end"]), color=color,width=width)
	img = drawline(img,(border["x_start"],border["y_start"]),(border["x_start"],border["y_end"]), color=color,width=width)
	return img

# Compute euclidian distance between two points
def distance(x1,y1,x2,y2):
	return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
