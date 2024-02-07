from data.config import voc, tt100k, coco

accumulated_slice_list = []
slice_list = []
anchor_size_list = []


def get_anchor_nums(feature_map, anchor_box, square_anchor_num=2):
    global accumulated_slice_list
    global slice_list
    global anchor_size_list

    if not accumulated_slice_list:
        before = 0
        for feature, anchor in zip(feature_map, anchor_box):
            
            anchor_size_list.append(len(anchor) * 2 + square_anchor_num)

            slice_list.append(feature * feature * anchor_size_list[-1])
            
            accumulated_slice_list.append(before + slice_list[-1])
            before = accumulated_slice_list[-1]
    return anchor_size_list, accumulated_slice_list


def get_anchor_box_size(idx, feature_map, anchor_box, square_anchor_num=2):
    anchor_size_list, accumulated_slice_list = get_anchor_nums(feature_map, anchor_box, square_anchor_num)
    # print(anchor_size_list, accumulated_slice_list)
    for i, elem in enumerate(accumulated_slice_list):
        if idx <= elem:
            
            n = (idx - (0 if i == 0 else accumulated_slice_list[i - 1])) % anchor_size_list[i]
            return int(n)
            