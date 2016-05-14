#inspired by http://people.idsia.ch/~juergen/icann2009bayer.pdf

import tensorflow as tf
import hyperchamber as hc

hc.set("learning_rate",
        [0.01])
hc.set("batch_size",
        [128])
hc.set('rnn_size',
        [4])

TRAIN_STEPS=100
TESTS = TRAIN_STEPS/10

def rnn(x, scope='rnn'):
    with tf.variable_scope(scope):
        memory=hc.get('rnn_size')
        cell = rnn_cell.BasicLSTMCell(memory)
        x, state = rnn.rnn(cell, [x], dtype=tf.boolean)
        #w = tf.get_variable('w', [hc.get('rnn_size'),4])
        #b = tf.get_variable('b', [4])
        #x = tf.nn.xw_plus_b(x, w, b)
        x=tf.sign(x)
        return x, state

# Each step of the graph we have:
# x is [BATCH_SIZE, 4] where the data is an one hot binary vector of the form:
# [start_token end_token a b]
#
# y is [BATCH_SIZE, 4] is a binary vector of the chance each character is correct
#
def create_graph(x, y):
    output, state = rnn(x)
    return tf.sum(tf.reduce_mean(output*tf.log(y))))

def parallel_run(sess, train_step, costs):
    return [sess.run(train_step, cost) for cost in costs]
def run():
    rand = np.random_uniform()#TODO as int
    x_input = []
    y_input = []
    console.log("Training each RNN")
    for configs in hc.configs(1):
        # sess = tf.session
        # TODO: Create subgraphs on config
        graph_costs=[]
        for config in configs:
            _, graph_cost = create_graph(x, y)
            graph_costs.push(graph_cost)
        for i in range(TRAIN_STEPS):
            _, costs = parallel_run(sess, train_step, graph_costs)
            hc.cost(configs, costs)

   for config in hc.best_configs(3):
        print(config)

def encode(chars):
    def vectorize(c):
        if(c=="S"):
            return [1,0,0,0]
        if(c=="T"):
            return [0,1,0,0]
        if(c=="a"):
            return [0,0,1,0]
        if(c=="b"):
            return [0,0,0,1]
    return [vectorize(c) for c in chars]


def get_an_bn(n):
    return encode("a"*n+"b"*n)
def get_an_bn_an(n):
    return encode("a"*n+"b"*n+"a"*n)

# returns a vector of a**nb**n grammars given a set of one-hot vectors x, denoting the next element in a generated sequence
# Each value is returned as an array of possible next inputs.
# for example:
# get_an_bn_grammar(ST) # T
# get_an_bn_grammar(SabT) # T/a-b-T
# get_an_bn_grammar(SaaabbbT) # T/a-a/b-a/b-b-b-b-T
#
# where S and T designate start and end symbols
def get_an_bn_grammar(x):
    return ""

# same as above but with extra 'a's
def get_an_bn_an_grammar(x):
    return ""
