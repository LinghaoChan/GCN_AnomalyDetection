import scipy.sparse as sp
import scipy.io

def load_data(data_source):
    data = scipy.io.loadmat("data/{}.mat".format(data_source))
    labels = data["gnd"]
    attributes = sp.csr_matrix(data["X"])
    network = sp.lil_matrix(data["A"])

    return network, attributes, labels
data_list = ['BlogCatalog', 'Flickr', 'Amazon', 'Enron', 'Disney']
dataname = data_list[2]
g, att, l = load_data(dataname)
# print(g)
print(att)
print(l)