for layer in model.encoder.layer[:-2]:
    layer.trainable = False