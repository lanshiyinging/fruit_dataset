from PIL import Image
import os
import numpy as np
apple_image_path = 'apple/'
tomato_image_path = 'tomato/'

i = 0
for f in os.listdir(apple_image_path):
	img_path = apple_image_path + f
	img = Image.open(img_path)
	# resize
	im = img.resize((224, 224))
	save_path = 'apple_aug/{:0=3}.jpg'.format(i)
	im.save(save_path, 'JPEG')
	i += 1
	# flip
	flipped_img = np.fliplr(im)
	save_path = 'apple_aug/{:0=3}.jpg'.format(i)
	Image.fromarray(flipped_img).save(save_path, 'JPEG')
	i += 1
	# Adding noise
	'''
	noise = np.random.randint(10, size=(224,224,3), dtype='uint8')
	noise_im = np.array(im)
	for w in range(224):
		for h in range(224):
			for k in range(3):
				if(noise_im[w][h][k] < 220):
					noise_im[w][h][k] += noise[w][h][k]
				else:
					noise_im[w][h][k] -= noise[w][h][k]
	save_path = 'apple_aug/{:0=3}.jpg'.format(i)
	Image.fromarray(noise_im).save(save_path, 'JPEG')
	i += 1	
	'''


j = 0
for f in os.listdir(tomato_image_path):
	img_path = tomato_image_path + f
	img = Image.open(img_path)
	im = img.resize((224, 224))
	save_path = 'tomato_aug/{:0=3}.jpg'.format(j)
	im.save(save_path, 'JPEG')
	j += 1

	# flip
	flipped_img = np.fliplr(im)
	save_path = 'tomato_aug/{:0=3}.jpg'.format(j)
	Image.fromarray(flipped_img).save(save_path, 'JPEG')
	j += 1

	# Adding noise
	'''
	noise = np.random.randint(5, size=(224,224,3), dtype='uint8')
	noise_im = np.array(im)
	for w in range(224):
		for h in range(224):
			for k in range(3):
				if(noise_im[w][h][k] <= 220):
					noise_im[w][h][k] += noise[w][h][k]
				else:
					noise_im[w][h][k] -= noise[w][h][k]
	save_path = 'tomato_aug/{:0=3}.jpg'.format(j)
	Image.fromarray(noise_im).save(save_path, 'JPEG')
	j += 1
	'''
