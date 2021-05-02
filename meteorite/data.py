"""This file is used to import initial database and to create dataframe with vector representation
of each painting image"""


def get_image(image_path):
    # get image into python in the RBG space
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # change color space
    return image
