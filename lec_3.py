"""
Improving our linear regression model using huber loss

Huber Loss
----------
    - Robust to outliers 
    - Intuition: if the difference between the predicted value and the real
    value is small, square it. If it's large take its 
    absolute difference
"""

import tensorflow as tf

def huber_loss(labels, predictions, delta=1.0):
    """ Implementation of huber loss """

    residual = tf.abs(predictions - labels)
    condition = tf.less(residual, delta)
    small_res = .5 * tf.square(residual)
    large_res = delta * residual - 0.5 * tf.square(delta)
    return tf.select(condition, small_res, large_res)

