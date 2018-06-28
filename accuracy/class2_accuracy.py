import tensorflow as tf
import utils.data_helper

class class2_accuracy:
    def __init__(self):
        print('choose class2_accuracy')
    def def_accuracy(self,inputs, labels):
        labels_m = labels - tf.floor(labels / 2) * 2
        mask = tf.floor(labels / 2)
        # mask = tf.Print(mask, [mask], "mask: ", summarize=32)
        # mask = tf.gather(mask, tf.constant([0]))
        # mask = tf.Print(mask, [mask], "mask1: ", summarize=32)
        # mask = tf.squeeze(mask)
        # idx = tf.where(mask > 0.5)
        # idx = tf.squeeze(idx)
        # labels_m = tf.gather(labels_m, idx, axis=1)
        # inputs = tf.gather(inputs, idx, axis=1)

        inputs=tf.cast(inputs> 0.5, tf.float32)

        #inputs = tf.Print(inputs, [mask], "masks: ", summarize=60)
        #inputs = tf.Print(inputs, [labels_m], "label: ", summarize=60)
        #inputs = tf.Print(inputs, [inputs], "predi: ", summarize=60)

        inputs = inputs * mask
        #inputs = tf.Print(inputs, [(labels_m - inputs) < 0.1], "acc diff: ", summarize=32)
        inputs=tf.cast(tf.abs(labels_m - inputs)<0.1, tf.float32)
        accuracy = tf.reduce_mean(inputs)
        accuracy=accuracy*3-2
        accuracy = tf.Print(accuracy, [accuracy], 'accuracy: ')
        return accuracy