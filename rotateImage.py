def rotate_image(img):
    rotated_image = [[]for x in range(len(img))] # Creates an array of len(img) elements with value []
    for i in range(len(img)):
        for j in range(len(img[i])):
          rotated_image[len(img) - j - 1].append(img[i][j])
    return rotated_image

image = [
  [1, 1, 5, 9, 9],
  [2, 2, 6, 0, 0],
  [3, 3, 7, 1, 1],
  [4, 4, 8, 2, 2],
  [5, 5, 9, 3, 3]
]

rotated_img = rotate_image(image)
for i in rotated_img:
    print(i)