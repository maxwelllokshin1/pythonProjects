from torchvision import datasets, transforms

def get_mnist():
    return datasets.MNIST(root="./data", train=True, download=True, transform=transforms.ToTensor())
