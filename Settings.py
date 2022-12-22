import math

#define a resolução da tela
Resolution = largura , altura = 1366 , 768
half_widht = largura //2
half_height = altura //2

#define o fps padrão
FPS = 60

#define o player

player_pos = 1.5, 5 #mini_map
player_angle = 0
player_speed = 0.001
player_rot_speed = 0.002
player_size_scale = 80

mouse_sensisitivity = 0.00015
mouse_max_rel = 40
mouse_border_left = 100
mouse_border_right = largura - mouse_border_left

floor_color = (57,49,90,255)

fov = math.pi /3
half_fov = fov / 2
num_rays = largura // 2
half_num_rays = num_rays // 2
delta_angle = fov / num_rays
max_depth = 20

screen_dist = half_widht /math.tan(half_fov)
scale = largura // num_rays

texture_size = 256
half_texture_size = texture_size // 2