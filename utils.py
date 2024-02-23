import torch
from torchvision import datasets, transforms


def test_train_data_loader(test_data, train_data, batch_size=512):
  """
  function to load test and train data
  input: train, test data, batch_size
  """
  kwargs = {
    'batch_size': batch_size, 
    'shuffle': True, 
    'num_workers': 2, 
    }
  # Pin memory only if CUDA is available
  if torch.cuda.is_available():
      kwargs['pin_memory'] = True

  test_loader = torch.utils.data.DataLoader(test_data, **kwargs)
  train_loader = torch.utils.data.DataLoader(train_data, **kwargs)

  return train_loader, test_loader

def get_test_train_data():
  # Train data transformations
  train_transforms = transforms.Compose([
      transforms.RandomApply([transforms.CenterCrop(22), ], p=0.1),
      transforms.Resize((28, 28)),
      transforms.RandomRotation((-15., 15.), fill=0),
      transforms.ToTensor(),
      transforms.Normalize((0.1307,), (0.3081,)),
      ])

  # Test data transformations
  test_transforms = transforms.Compose([
      transforms.ToTensor(),
      transforms.Normalize((0.1307,), (0.3081,))
      ])

  # loading and transforming train data
  train_data = datasets.MNIST('../data', train=True, 
  download=True, transform=train_transforms)

  # loading and transforming test data
  test_data = datasets.MNIST('../data', train=False, 
  download=True, transform=test_transforms)

  return train_data, test_data