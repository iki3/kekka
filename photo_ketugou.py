from PIL import Image
def get_concat_h_multi_resize(im_list, resample=Image.BICUBIC):
    min_height = min(im.height for im in im_list)
    im_list_resize = [im.resize((int(im.width * min_height / im.height), min_height),resample=resample)
                      for im in im_list]
    total_width = sum(im.width for im in im_list_resize)
    dst = Image.new('RGB', (total_width, min_height))
    pos_x = 0
    for im in im_list_resize:
        dst.paste(im, (pos_x, 0))
        pos_x += im.width
    return dst

def get_concat_v_multi_resize(im_list, resample=Image.BICUBIC):
    min_width = min(im.width for im in im_list)
    im_list_resize = [im.resize((min_width, int(im.height * min_width / im.width)),resample=resample)
                      for im in im_list]
    total_height = sum(im.height for im in im_list_resize)
    dst = Image.new('RGB', (min_width, total_height))
    pos_y = 0
    for im in im_list_resize:
        dst.paste(im, (0, pos_y))
        pos_y += im.height
    return dst
folder_name='batang.ttf_MCGAN_train'
folder_name='UnBatang.ttf_MCGAN_train'
file_name='UnBatang.ttf'
file_name='umeboshi_.ttf'
# im1 = Image.open('/home/iki/PycharmProjects/MC-GAN_glyph_pretrain_test_katakana_copy_vesion2/MC-GAN/results/'+folder_name+'/test_400+700/images/'+file_name+'_fake_B.png')
# im2 = Image.open('/home/iki/PycharmProjects/MC-GAN_glyph_pretrain_test_katakana_copy_vesion2/MC-GAN/results/'+folder_name+'/test_400+700/images/'+file_name+'_real_A.png')
# im3 = Image.open('/home/iki/PycharmProjects/MC-GAN_glyph_pretrain_test_katakana_copy_vesion2/MC-GAN/results/'+folder_name+'/test_400+700/images/'+file_name+'_real_B.png')
# get_concat_h_multi_resize([im1, im2, im3]).save('/home/iki/PycharmProjects/MC-GAN_glyph_pretrain_test_katakana_copy_vesion2/MC-GAN/results/'+folder_name+'/test_400+700/images/tate.png')
# get_concat_v_multi_resize([im1, im2, im3]).save('/home/iki/PycharmProjects/MC-GAN_glyph_pretrain_test_katakana_copy_vesion2/MC-GAN/results/'+folder_name+'/test_400+700/images/yoko.png')

im1=Image.open('1/'+file_name+'_fake_B.png')
im2=Image.open('1/'+file_name+'_real_A.png')
im3=Image.open('1/'+file_name+'_real_B.png')
get_concat_h_multi_resize([im1, im2, im3]).save('1/tate.png')
get_concat_v_multi_resize([im1, im2, im3]).save('1/yoko.png')