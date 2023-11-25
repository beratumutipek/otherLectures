from keras.models import Sequential, Model
from keras.layers import Conv2D
from keras.preprocessing.image import load_img, img_to_array
import matplotlib.pyplot as plt

image = load_img("into to ai/picture1.jpg", target_size=(224, 224))
input_image = img_to_array(image)

model = Sequential()

model.add(Conv2D(filters=16, kernel_size=(16,16), input_shape = (224, 224, 3), activation='relu' ))
model.add(Conv2D(filters=8, kernel_size=(8,8), input_shape = (224, 224, 3), activation='relu' ))
model.add(Conv2D(filters=4, kernel_size=(4,4), input_shape = (224, 224, 3), activation='relu' ))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
plt.figure(figsize=(5,5))
plt.imshow(input_image / 255.0)

plt.title('original')



layer_outputs = [layer.output for layer in model.layers]
activation_model = Model(inputs= model.input, outputs = layer_outputs)

acvtivations = activation_model.predict(input_image.reshape(1, 224, 224, 3))

num_layers = len(acvtivations)
plt.figure(figsize=(15,5*num_layers))

for layer_idx, layer_activation in enumerate(acvtivations):
    num_channels = layer_activation.shape[-1]
    for channel_idx in range(num_channels):
        plt.subplot(num_layers, num_channels, layer_idx*num_channels + channel_idx +1)
        plt.imshow(layer_activation[0,:,:,channel_idx], cmap='gray')
        plt.title(f"L{layer_idx}, C{channel_idx+1}")

plt.show()

