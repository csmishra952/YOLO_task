
import torch
from PIL import Image
from torchvision import transforms
from facenet_pytorch import InceptionResnetV1

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def get_facenet_embeddings(img_path):
    resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)
    img = Image.open(img_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((160, 160)),
        transforms.ToTensor()
    ])
    img_tensor = transform(img).unsqueeze(0).to(device)
    embedding = resnet(img_tensor).detach().cpu().numpy()
    return embedding
