<div align="center">
  <a href="https://nanonets.com/objectdetection/">
    <img src="https://nanonets.com/logo.png" alt="NanoNets Object Detection Python Sample" width="100"/>
    </a>
</div>

<h1 align="center">NanoNets Object Detection Python Sample</h1>

| [Python Sample](https://github.com/NanoNets/multilabel-classifiaction-sample-python)|
| -------------------------- |
| [![](http://kata.coderdojo.com/images/thumb/e/ea/Python_logo.png/100px-Python_logo.png)](https://github.com/NanoNets/multilabel-classifiaction-sample-python) |

** **

## Tracking the Millenium Falcon

Images and annotations taken from - https://www.kaggle.com/neha1703/movie-genre-from-its-poster/home

Images consists of Posters of movies taken from IMBD across different Genre. For Demo, we have cut the number of Genre to 10 and number of images to 970.

Annotations are present for each poster and have the same name as the image name. You can find the example to train a model in python, by updating the api-key and model id in corresponding file. There is also a pre-processed .txt annotations folder that are ready payload for nanonets api.


** **

# Build an Object Detector for the Millenium Falcon
 
### Step 1: Clone the Repo
```bash
git clone https://github.com/NanoNets/multilabel-classifiaction-sample-python.git
cd multilabel-classifiaction-sample-python
```

### Step 2: Get your free API Key
Get your free API Key from http://app.nanonets.com/user/api_key

### Step 3: Set the API key as an Environment Variable
```bash
export NANONETS_API_KEY=YOUR_API_KEY_GOES_HERE
```

### Step 4: Create a New Model
```bash
python ./code/create_model.py
```
 >_**Note:** This generates a MODEL_ID that you need for the next step

### Step 5: Add Model Id as Environment Variable
```bash
export NANONETS_MODEL_ID=YOUR_MODEL_ID
```
 >_**Note:** you will get YOUR_MODEL_ID from the previous step

### Step 6: Upload the Training Data
The training data is found in ```images``` (image files) and ```annotations``` (annotations for the image files)
```bash
python ./code/upload_training.py
```

### Step 7: Train Model
Once the Images have been uploaded, begin training the Model
```bash
python ./code/train_model.py
```

### Step 8: Get Model State
The model takes ~2 hours to train. You will get an email once the model is trained. In the meanwhile you check the state of the model
```bash
python ./code/model_state.py
```

### Step 9: Make Prediction
Once the model is trained. You can make predictions using the model
```bash
python ./code/prediction.py PATH_TO_YOUR_IMAGE.jpg
```

**Sample Usage:**
```bash
python ./code/prediction.py ./multilabel_data/ImageSets/2795.jpg
```
