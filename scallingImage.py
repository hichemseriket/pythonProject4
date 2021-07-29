import cv2
img = cv2.imread('hichem_modified.jpg', cv2.IMREAD_UNCHANGED)
print('taille origine', img.shape)


scale_percent = 220
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

print('image amélioré : ', resized.shape)
cv2.imshow("hichem", img)
cv2.imshow("amelioré", resized)
# print(img)
# print(resized)
# image = image.open(resized)
# cv2.putText(resized, "hichem le boss", (70, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
cv2.waitKey(0)
cv2.imwrite("hichem_contrast_pixel.png", resized)

cv2.destroyAllWindows()
