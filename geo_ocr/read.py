import os
from predict_all import *


def read(image_path, nolog=False):

    if not os.path.isfile(image_path):
        print("Files does not exists")
        return

    image_arrays = fragmenter.do_fragmentation(image_path, nolog=nolog)
    result = ''
    full_score = 0
    full_count = 0

    for n in image_arrays:
        img_arr = n["arr"]
        meta_data = n["meta"]
        img_arr = img_arr.flatten()
        [char, score] = recognize_image(img_arr)
        full_score += score
        full_count += 1
        if not nolog:
            print meta_data, char.encode('utf8'), score
        meta_data['char'] = char
        meta_data['score'] = score
    if not nolog:
        print 'Avg score: %d' % (full_score * 100 / full_count)

    # ----- for testing --------
    # use export_word as a module
    export_words.test([n["meta"] for n in image_arrays])


if __name__ == '__main__':
    args = init_arguments()
    read(args.image, args.nolog)
