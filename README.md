# grain-deposit-machine
Classify the quality of rice grains by retraining the MobileNetV2 model on a dataset containing three qualities of rice.

## Running the model

* Capture the image
```bash
$./capture_image.sh
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

* Classify the image

```bash
$./quality_check.sh
quality 1 0.9881499
```

* Estimate weights using exchange rates

```bash
./price.sh
```
