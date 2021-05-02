"""This file is used to find pictures that are closest to the given color."""


def match_image_by_color(image, color, threshold = 60, number_of_colors = 5):

    image_colors = get_colors(image, number_of_colors, False)
    selected_color = rgb2lab(np.uint8(np.asarray([[color]])))

    select_image = False
    for i in range(number_of_colors):
        curr_color = rgb2lab(np.uint8(np.asarray([[image_colors[i]]])))
        diff = deltaE_cie76(selected_color, curr_color)
        if (diff < threshold):
            select_image = True

    return select_image



def show_selected_images(images, color, threshold, colors_to_match):
    index = 1

    for i in range(len(images)):
        selected = match_image_by_color(images[i], color, threshold, colors_to_match)
        if (selected):
            plt.subplot(1, 8, index)
            plt.imshow(images[i])
            index += 1
