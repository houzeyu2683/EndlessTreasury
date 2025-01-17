import diffusers
import torch

model = diffusers.UNet2DModel()
x, t = torch.randn(1, 3, 64, 64), 943
y  = model(x, t)
z = y.sample
z.shape



# from diffusers import StableCascadeUNet

# model = StableCascadeUNet()

# y[0].shape
# o = y[1]
# y
# len(y)


# model = diffusers.UNet2DModel(
#     sample_size=28,           # the target image resolution
#     in_channels=3,            # the number of input channels, 3 for RGB images
#     out_channels=3,           # the number of output channels
#     layers_per_block=2,       # how many ResNet layers to use per UNet block
#     block_out_channels=(32, 64, 64), # Roughly matching our basic unet example
#     down_block_types=( 
#         "DownBlock2D",        # a regular ResNet downsampling block
#         "AttnDownBlock2D",    # a ResNet downsampling block with spatial self-attention
#         "AttnDownBlock2D",
#     ), 
#     up_block_types=(
#         "AttnUpBlock2D", 
#         "AttnUpBlock2D",      # a ResNet upsampling block with spatial self-attention
#         "UpBlock2D",          # a regular ResNet upsampling block
#       ),
# )
# print(model)

