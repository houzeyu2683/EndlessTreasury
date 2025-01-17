import diffusers.models.unets.unet_2d_blocks
import torch

layer_1 = diffusers.models.unets.unet_2d_blocks.DownBlock2D(
    in_channels=64,  # 輸入圖像通道數
    out_channels=128,  # 下采樣後的輸出通道數
    temb_channels=16,
    num_layers=1
)
x = torch.randn(1, 64, 32, 32)
t = torch.randn(1, 16)
out_1, skip_1 = layer_1(x, t)
out_1.shape
skip_1[0].shape
skip_1[1].shape

skip_a = (torch.randn(1,64, 32, 32), torch.randn(1,64, 16,16))

layer_2 = diffusers.models.unets.unet_2d_blocks.UpBlock2D(
    in_channels=128,
    prev_output_channel=64,
    out_channels=32,
    temb_channels=16
)
out_2 = layer_2(out_1, skip_a, t)
out_2.shape


x_down, skip_features = layer(x, t)

layer = diffusers.models.unets.unet_2d_blocks.UpBlock2D(
    in_channels=256,
    # prev_output_channel=256,
    out_channels=512,
    temb_channels=128
)
x_out = layer(x_down, skip_features, t)
print(x_out.shape)
# print(x_down.shape)
# print(skip_features[0].shape)
# print(skip_features[1].shape)

# print('done')