# bear_classifier
Bear Classifier from Lesson 2 Fast.ai

Simply POST images to this server and it will tell you if the image you've submitted is a Teddy Bear, Grizzly Bear, or a Black Bear.

# Install
`pip install -r requirements.txt`

# Run
`uvicorn bear_classifier:app`

# Instructions

1. POST Request an image to `localhost:8000/predict`
1. Should get a prediction back in the terminal
1. The Response will contain a JSON, use appropriately
```
{
  category: 'yields the bear predicted',
  probs: 'statistics',
  text: 'human friendly text output of the predicted bear',
}
```

# Known Issues
## pillow
* should be 6.2 but had some issues running, so downgraded to 6.1
