import numpy as np
import pandas as pd
import imageio
import matplotlib.pyplot as plt
import math
import os.path
import os
import csv
import glob
import h5py as h5py
import imageio
import imutils
import matplotlib.pyplot as plt
import matplotlib.image as img
import playsound
import dlib
import shutil
import cv2
from mlxtend.image import extract_face_landmarks
from imutils import face_utils
from threading import Thread
from scipy.spatial import distance 
from sklearn.metrics import roc_curve, roc_auc_score, f1_score, accuracy_score, confusion_matrix
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from IPython.display import clear_output
from PIL import Image