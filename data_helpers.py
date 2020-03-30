import numpy as np



def load_data_and_labels(positive_data_file, negative_data_file):
    """
    Loads data in and use jieba to split the words 
    """
    # Load data from files
    positive_examples = list(open(positive_data_file, "r", encoding='utf-8').readlines())
    negative_examples = list(open(negative_data_file, "r", encoding='utf-8').readlines())
    x_text = positive_examples + negative_examples
    # Generate labels
    positive_labels = [[0, 1] for s in positive_examples]
    negative_labels = [[1, 0] for s in negative_examples]
    y = np.concatenate([positive_labels, negative_labels], 0)
    
    return [x_text, y]


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]
