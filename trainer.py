from imageai.Classification.Custom import ClassificationModelTrainer

model_trainer = ClassificationModelTrainer()
model_trainer.setModelTypeAsDenseNet121()
model_trainer.setDataDirectory(r"<path/to/folder/with/dataset/")
model_trainer.trainModel(num_experiments=100, batch_size=32)