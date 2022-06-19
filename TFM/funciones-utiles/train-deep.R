# creamos la base del modelo pre-entrenado partiendo de ImageNET
base_model <- application_inception_v3(weights = 'imagenet', include_top = FALSE)

# Añadimos capas adicionales a nuestra red neuronal
predictions <- base_model$output %>%
  layer_global_average_pooling_2d() %>%
  layer_dense(units = 1024, activation = 'relu') %>%
  layer_dense(units = 200, activation = 'softmax')

# creamos un nuevo modelo para entrenar
model <- keras_model(inputs = base_model$input, outputs = predictions)

# Nos aseguramos de entrenar solo nuestras nuevas capas para no destruir el entrenamiento previo.
freeze_weights(base_model)

# compilamos el modelo
model %>% compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy')

# entrenamos el modelo
model %>% fit_generator(...)