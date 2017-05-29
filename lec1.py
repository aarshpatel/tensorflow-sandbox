import tensorflow as tf

x = tf.constant(2)
y = tf.constant(3)
a = tf.add(x, y)


x = 2
y = 3
op1 = tf.add(x, y)
op2 = tf.multiply(x, y)
useless = tf.multiply(x, op1)
op3 = tf.pow(op2, op1)

with tf.Session() as sess:
    op3, not_useless = sess.run([op3, useless])
    print op3
    print not_useless

# Graphs API

g = tf.Graph()
with g.as_default():
    x = tf.add(3, 5)

sess = tf.Session(graph=g)
with tf.Session() as sess:
    sess.run(x)