# Which car is that ?
Android app containing an Image classifier based on transfer learning CNN using Tensorflow 1.4.1 on Stanford's Imagenet cars dataset.  

![Android app icon](https://i.imgur.com/xxomPOZ.png)

## Project details
* This application is a demonstration of an image classifier built using convolutional neural network.  
* The model is trained on Stanford's imagenet dataset of 196 cars. Dataset can be accessed here: http://ai.stanford.edu/~jkrause/cars/car_dataset.html  
* The Cars dataset contains 16,185 images of 196 classes of cars. Full list of cars is present here: https://paste.ubuntu.com/26311458/  
* This project is published as an Android app available on Play Store. [LINK](https://play.google.com/store/apps/details?id=com.reachsumit.whichcaristhat&hl=en)  

## Screenshots
App on Play store  
![App on Play store](https://i.imgur.com/0iCyds8.png)

### Test 1 
![Test 1](https://i.imgur.com/EhfFxCq.jpg)

### Test 2  
![Test 2](https://i.imgur.com/YuGf4s3.jpg)

### Test 3  
![Test 3](https://i.imgur.com/xX2veJ9.jpg)

### Test 4  
![Test 4](https://i.imgur.com/h7INKZg.jpg)

### Test 5  
![Test 5](https://i.imgur.com/yh29bd9.jpg)

## Other commands

IMAGE_SIZE=224
ARCHITECTURE="mobilenet_0.75_${IMAGE_SIZE}"

python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=5000 \
  --model_dir=tf_files/models/"${ARCHITECTURE}" \
  --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture="${ARCHITECTURE}" \
  --image_dir=tf_files/dataset

python -m scripts.retrain \
    --image_dir=tf_files/dataset \
    --learning_rate=0.0001 \
    --testing_percentage=20 \
    --validation_percentage=20 \
    --train_batch_size=32 \
    --validation_batch_size=-1 \
    --flip_left_right True \
    --random_scale=30 \
    --random_brightness=30 \
    --eval_step_interval=100 \
    --how_many_training_steps=600 \
    --architecture mobilenet_1.0_224
