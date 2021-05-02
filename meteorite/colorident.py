"""This file includes relevant function for color identification."""



def RGB2HEX(color):
    # function returning hex values of colour as string we want to identify
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_colors(image, number_of_colors, show_chart):
    # function extracting top colors from an image and display as pie chart

    # KMeans expects flattened array as input during its fit method, thus reshape the image using numpy
    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA) # reduce size to lessen pixels to reduce time to extract color from images
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3) # reshape image data to 2 dimensions

    # apply KMeans to first fit and then predict on the image to get the results
    clf = KMeans(n_clusters = number_of_colors) # apply clusters based on supplied count of clusters
    labels = clf.fit_predict(modified_image) # extract prediction in to variable labels

    counts = Counter(labels)

    center_colors = clf.cluster_centers_
    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i]/255 for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]*255) for i in counts.keys()]
    rgb_colors = [ordered_colors[i]*255 for i in counts.keys()]
    # plot the colors as a pie chart
    if (show_chart):
        plt.figure(figsize = (8, 6))
        plt.pie(counts.values(), labels = hex_colors, colors = ordered_colors)

    return rgb_colors

    # from model above we can extractt major colors
