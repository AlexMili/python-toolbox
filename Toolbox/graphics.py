import math
from typing import List, Tuple, Union

import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def drawpoint(img: Image,
              x_y: Union[Tuple, List],
              radius: int = 10,
              circle_color: Tuple = (255, 0, 0)) -> Image:
    x, y = x_y
    draw = ImageDraw.Draw(img)
    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=circle_color)
    return img


# Display coords given a dataset
def display_coords(df: pd.DataFrame,
                   cols: List = ["x","y"],
                   radius: int = 10,
                   color: Tuple = (0, 255, 0),
                   screenWidth: int = 100,
                   screenHeight: int = 100,
                   font_family: str = "arial.ttf",
                   font_size: int = 20,
                   font_color: Tuple = (0, 0, 0),
                   background_color: str = "gray",
                   display_num: bool = True) -> Image:
    img = Image.new("RGB", (screenWidth, screenHeight), background_color)
    draw = ImageDraw.Draw(img)

    i = 0
    for row in df.iterrows():
        img = drawpoint(img, (row[1][cols[0]],row[1][cols[0]]),
                        radius=radius, circle_color=color)

        if (display_num):
            draw.text((row[1][cols[0]], row[1][cols[0]]), str(i+1), fill=font_color,
                      font=ImageFont.truetype(font_family, font_size))

        i=i+1

    return img


def drawline(img: Image,
             coords_start: Union[Tuple, List],
             coords_end: Union[Tuple, List],
             color: Tuple = (255, 0, 0),
             width: int = 5) -> Image:
    draw = ImageDraw.Draw(img)
    draw.line((coords_start, coords_end), fill=color,width=width)
    return img


def generateAroundArea(x: int, y: int, offset: int) -> dict:
    return {
        "x_start": x - offset,
        "y_start": y - offset,
        "x_end": x + offset,
        "y_end": y + offset
    }


# Determine if the coordinates are in a given area
def is_in_area(points: Union[Tuple, List] = (5,5),
               area: dict = {'x_start': 0, 'y_start': 0, 'x_end':10, 'y_end': 10}) -> bool:
    x,y = points

    if (x >= area['x_start'] and x < area['x_end'] and
        y >= area['y_start'] and y < area['y_end']):
        return True
    else:
        return False


# Alias with the goal to replace drawlineAround
def drawbox(img: Image,
            center: List,
            border: dict = None,
            offset: int = 10,
            color: Tuple = (0, 0, 255),
            width: int = 5) -> Image:
    return drawlineAround(img, center, border, offset, color, width)


def drawlineAround(img: np.ndarray,
                   center: List,
                   border: dict = None,
                   offset: int = 10,
                   color: Tuple = (0, 0, 255),
                   width: int = 5) -> Image:

    if (border is None):
        border = generateAroundArea(center[0], center[1], offset)

    img = drawline(img, (border["x_start"],border["y_start"]), (border["x_end"], border["y_start"]), color=color, width=width)
    img = drawline(img, (border["x_end"], border["y_start"]), (border["x_end"], border["y_end"]), color=color, width=width)
    img = drawline(img, (border["x_start"], border["y_end"]), (border["x_end"], border["y_end"]), color=color, width=width)
    img = drawline(img, (border["x_start"], border["y_start"]), (border["x_start"], border["y_end"]), color=color, width=width)

    return img


# Compute euclidian distance between two points
def distance(x1: Union[int, float],
             y1: Union[int, float],
             x2: Union[int, float],
             y2: Union[int, float]) -> Union[int, float]:
    return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))


def imshow(path: Union[str, np.ndarray],
           coords: Union[List[int], Tuple, List[List[int]]] = None,
           marker_size: int = None,
           marker_color: Tuple = (255, 0, 0),
           figsize: Tuple = (20, 50)) -> None:

    if (type(path) is str):
        img = cv2.imread(path, cv2.COLOR_BGR2RGB)
    else:
        img = path.copy()
    
    if (len(img.shape) > 2):
        # If image is already in RGB, the next line will raise an error
        try:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        except:
            pass
    else:
        img = cv2.normalize(img, None, 0, 255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F).astype(np.uint8)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    
    plt.figure(figsize=figsize)
    
    if (not coords is None):
        if (marker_size is None):
            marker_size = img.shape[0]/40
        
        # Convert to numpy for data manipulation
        coords = np.array(coords)
        
        # If there is only one coord
        if (len(coords.shape) == 1):
            coords = np.array([coords])

        for coord in coords:
            cv2.circle(img,(coord[0], coord[1]), int(marker_size), marker_color, -1)
            #plt.plot(coord[0], coord[1], marker='o', markersize=marker_size, color="red")
    
    plt.imshow(img)
    plt.show()


def pixels_to_pts(pixels: Union[int, float]):
    # Based on W3C standard:
    # https://www.w3.org/TR/css3-values/#absolute-lengths
    return pixels * 72 / 96


def pts_to_pixels(pts: Union[int, float]):
    # Based on W3C standard:
    # https://www.w3.org/TR/css3-values/#absolute-lengths
    return pts * 96 / 72
