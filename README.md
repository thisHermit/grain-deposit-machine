# grain-deposit-machine
Classify the quality of rice grains by retraining the MobileNetV2 model on a dataset containing three qualities of rice.

## Running the model

* Capture the image
```bash
./capture_image.sh
```

* Classify the image

```bash
./quality_check.sh
```

* Estimate weights using exchange rates

```bash
./price.sh
```
