# grain-deposit-machine
A hello world project using raspberry pi 3 B plus and Tensorflow in order to learn Transfer Learning.

Here I classify the quality of rice grains by retraining the MobileNetV2 model on a dataset containing three qualities of rice.

## Running the model

* Capture the image
```bash
$ ./capture_image.sh
--- Opening /dev/video0...
Trying source module v4l2...
/dev/video0 opened.
No input was specified, using the first.
Adjusting resolution from 384x288 to 424x240.
--- Capturing frame...
Captured frame in 0.00 seconds.
--- Processing captured image...
Setting output format to PNG, quality 0
Writing PNG image to 'image.png'.
```

* Classify the image (Output format "quality id-of-quality confidence-in-classification")

```bash
$ ./quality_check.sh
quality 1 0.9881499
```

* Estimate weights using exchange rates (providing the quality as the parameter)

```bash
$ ./price.sh 1
Weight: 114g
Price: Rs. 10.26
```
