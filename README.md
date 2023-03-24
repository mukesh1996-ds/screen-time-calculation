# Screen Time Calculation

In this project I have tried to create folders and files using OS module and the only reason is that 
"TIME PASS"

Created Folders name:
1. Data: It will contain my video clip
2. Data Frames: Here we need to process the video and convert it into frames which will be stored in this folder.
3. SCR: It will contain all the CODE needed to perfrom.
4. requirements file: It contains all the requirements that are required

## Stage 1:

Install all the requirements using **requirements.txt**

If you get error saying version mismatch then manuall goto the official release documentation and try again the installation using pip command.

### Stage 2: 

Read the video, extract frames from it and save them as images

Now we will load the video and convert it into frames. You can download the video used for this example from this link. We will first capture the video from the given directory using the VideoCapture() function, and then we’ll extract frames from the video and save them as an image using the imwrite() function. 

let's read the image from the video

> img = plt.imread("/content/sample_data/xvz/frame0.jpg")   # reading image using its name
> plt.imshow(img)


Our task is to identify which image has TOM, and which image has JERRY. If our extracted images would have been similar to the ones present in the popular Imagenet dataset, this challenge could have been a breeze. How? We could simply have used models pre-trained on that Imagenet data and achieved a high accuracy score! But then where’s the fun in that?

We have cartoon images so it’ll be very difficult (if not impossible) for any pre-trained model to identify TOM and JERRY in a given video.

### Stage 3: Label a few images for training the model

So how do we go about handling this? A possible solution is to manually give labels to a few of the images and train the model on them. Once the model has learned the patterns, we can use it to make predictions on a previously unseen set of images.

Keep in mind that there could be frames when neither TOM nor JERRY are present. So, we will treat it as a multi-class classification problem. The classes which I have defined are:

* 0 – neither JERRY nor TOM
* 1 – for JERRY
* 2 – for TOM

I have annoted every frame and stored inside the excel.

The frame.csv file contains two columns:

* Image_ID: Contains the name of each image
* Class: Contains corresponding class for each image

Our next step is to read the images which we will do based on their names, aka, the Image_ID column.

We will be using a VGG16 pretrained model which takes an input image of shape (224 X 224 X 3). Since our images are in a different size, we need to reshape all of them. We will use the resize() function of skimage.transform to do this.

All the images have been reshaped to 224 X 224 X 3. But before passing any input to the model, we must preprocess it as per the model’s requirement. Otherwise, the model will not perform well enough. Use the preprocess_input() function of keras.applications.vgg16 to perform this step.