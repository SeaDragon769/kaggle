# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:53:21 2018

@author: Administrator
"""
import tensorflow as tf

#%%卷积神经网络

input = tf.Variable(tf.random_normal([1,3,3,5]))
filter = tf.Variable(tf.random_normal([2,2,5,1]))

op = tf.nn.conv2d(input, filter, strides=[1, 1, 1, 1], padding='SAME')

sess=tf.Session()
init_op=tf.initialize_all_variables()
sess.run(init_op)
print(sess.run(op))

sess.close()