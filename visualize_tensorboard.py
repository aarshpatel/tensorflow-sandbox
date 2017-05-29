import tensorflow as tf


# a = tf.constant(2, name="a")
# b = tf.constant(3, name="b")
# x = tf.add(a, b, name="add")

# # visualize the graph using tensorboard
# with tf.Session() as sess:
# 	writer = tf.summary.FileWriter("./graphs", sess.graph) 
# 	print sess.run(a)
# 	writer.close() # close the writer when you're done using it

# More Constants
a = tf.constant([2, 2], name="a")
b = tf.constant([[0, 1], [2, 3]], name="b")
x = tf.add(a, b, name='add')
y = tf.multiply(a, b, name='mul')

with tf.Session() as sess:
	x, y = sess.run([x, y])
	print x, y

# (almost deterministic outputs) 
# tf.set_random_seed(seed)

# use tensorflow data types

# Only use consant for primitve types. Use variables instead

# create a variable a with scalar value
a = tf.Variable(2, name="scalar")

b = tf.Variable([2, 3], name="vector")
W = tf.Variable(tf.zeros([784, 10]))

# you need to initialize all variables 

init = tf.global_variables_initializer()

