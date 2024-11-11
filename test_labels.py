def get_label(target_sequence: str) -> list[tuple[int, int, bool]]:
    match target_sequence:
        case "0119":
            return [
                (256, 260, True),
                (504, 520, True),
                (679, 693, True),
                (977, 977, True),
            ]
        case "0152":
            return [
                (48, 61, True),
                (205, 221, True),
                (291, 303, True),
                (384, 398, True),
            ]
        case "0267":
            return [
                (79, 79, True),
                (204, 215, True),
                (345, 345, True),
                (478, 487, True),
            ]
        case "0307":
            return [
                (139, 139, True),
                (343, 345, True),
                (540, 540, True),
                (754, 771, True),
            ]
        case "0507":
            return [
                (93, 93, True),
                (246, 260, True),
                (488, 488, True),
                (667, 671, True),
            ]
        case "0553":
            return [
                (83, 86, True),
                (223, 229, True),
                (369, 377, True),
                (623, 628, True),
            ]
        case "0779":
            return [
                (86, 86, True),
                (224, 227, True),
                (311, 323, True),
                (431, 438, True),
            ]
        case "0783":
            return [
                (77, 83, True),
                (233, 247, True),
                (389, 407, True),
                (595, 595, True),
            ]
        case "0969":
            return [
                (114, 121, True),
                (205, 208, True),
                (320, 321, True),
                (428, 431, True),
            ]
        case "1074":
            return [
                (87, 105, True),
                (402, 406, True),
                (674, 687, True),
                (878, 896, True),
            ]
        case "1245":
            return [
                (69, 83, True),
                (172, 183, True),
                (310, 321, True),
                (425, 432, True),
            ]
        case "1329":
            return [
                (113, 130, True),
                (316, 316, True),
                (476, 492, True),
                (707, 707, True),
            ]
        case "1403":
            return [
                (79, 96, True),
                (212, 227, True),
                (431, 435, True),
                (626, 633, True),
            ]
        case "1543":
            return [
                (60, 64, True),
                (180, 188, True),
                (257, 271, True),
                (352, 353, True),
            ]
        case "1562":
            return [
                (92, 123, True),
                (252, 257, True),
                (562, 562, True),
                (759, 765, True),
            ]
        case "1701":
            return [
                (126, 141, True),
                (264, 281, True),
                (558, 560, True),
                (747, 762, True),
            ]
        case "1777":
            return [
                (81, 93, True),
                (228, 245, True),
                (377, 395, True),
                (530, 550, True),
            ]
        case "1821":
            return [
                (54, 66, True),
                (164, 171, True),
                (260, 260, True),
                (370, 370, True),
            ]
        case "1824":
            return [
                (93, 110, True),
                (274, 280, True),
                (431, 439, True),
                (628, 648, True),
            ]
        case "1854":
            return [
                (65, 67, True),
                (211, 211, True),
                (314, 317, True),
                (423, 437, True),
            ]
        case "1924":
            return [
                (49, 52, True),
                (207, 207, True),
                (346, 359, True),
                (481, 481, True),
            ]
        case "2004":
            return [
                (102, 108, True),
                (235, 238, True),
                (361, 361, True),
                (543, 564, True),
            ]
        case "2058":
            return [
                (38, 52, True),
                (114, 127, True),
                (169, 182, True),
                (227, 232, True),
            ]
        case "2070":
            return [
                (86, 90, True),
                (275, 275, True),
                (471, 475, True),
                (714, 719, True),
            ]
        case "2155":
            return [
                (70, 84, True),
                (203, 218, True),
                (329, 330, True),
                (431, 434, True),
            ]
        case "2186":
            return [
                (142, 158, True),
                (385, 403, True),
                (659, 666, True),
                (945, 959, True),
            ]
        case "2190":
            return [
                (93, 107, True),
                (206, 220, True),
                (376, 377, True),
                (744, 748, True),
            ]
        case "2236":
            return [
                (85, 85, True),
                (183, 183, True),
                (279, 281, True),
                (387, 394, True),
            ]
        case "2303":
            return [
                (154, 168, True),
                (335, 335, True),
                (548, 550, True),
                (744, 745, True),
            ]
        case "2304":
            return [
                (85, 100, True),
                (249, 263, True),
                (463, 463, True),
                (696, 705, True),
            ]
        case "2339":
            return [
                (39, 53, True),
                (141, 149, True),
                (236, 247, True),
                (382, 394, True),
            ]
        case "2429":
            return [
                (101, 120, True),
                (274, 337, True),
                (505, 512, True),
                (771, 771, True),
            ]
        case "2576":
            return [
                (90, 92, True),
                (245, 263, True),
                (454, 470, True),
                (689, 706, True),
            ]
        case "2657":
            return [
                (61, 79, True),
                (261, 262, True),
                (415, 434, True),
                (625, 640, True),
            ]
        case "2679":
            return [
                (105, 121, True),
                (338, 338, True),
                (540, 554, True),
                (776, 776, True),
            ]
        case "2734":
            return [
                (88, 101, True),
                (225, 229, True),
                (382, 393, True),
                (534, 549, True),
            ]
        case "2783":
            return [
                (36, 39, True),
                (192, 197, True),
                (268, 269, True),
                (439, 441, True),
            ]
        case "2845":
            return [
                (83, 98, True),
                (232, 234, True),
                (395, 408, True),
                (551, 551, True),
            ]
        case "2873":
            return [
                (115, 130, True),
                (389, 390, True),
                (647, 663, True),
                (868, 881, True),
            ]
        case "2949":
            return [
                (64, 81, True),
                (281, 286, True),
                (465, 479, True),
                (665, 665, True),
            ]
        case "3076":
            return [
                (102, 102, True),
                (353, 355, True),
                (502, 515, True),
                (734, 734, True),
            ]
        case "3138":
            return [
                (105, 105, True),
                (342, 363, True),
                (527, 546, True),
                (823, 842, True),
            ]
        case "3384":
            return [
                (111, 123, True),
                (277, 277, True),
                (508, 518, True),
                (830, 837, True),
            ]
        case "3676":
            return [
                (127, 141, True),
                (253, 259, True),
                (426, 431, True),
                (612, 628, True),
            ]
        case "3688":
            return [
                (81, 96, True),
                (218, 224, True),
                (396, 396, True),
                (518, 518, True),
            ]
        case "3723":
            return [
                (118, 118, True),
                (287, 302, True),
                (436, 446, True),
                (596, 597, True),
            ]
        case "3748":
            return [
                (117, 117, True),
                (367, 381, True),
                (513, 539, True),
                (789, 789, True),
            ]
        case "3833":
            return [
                (128, 128, True),
                (404, 405, True),
                (600, 600, True),
                (755, 757, True),
            ]
        case "4043":
            return [
                (64, 77, True),
                (205, 214, True),
                (308, 322, True),
                (510, 510, True),
            ]
        case "4061":
            return [
                (105, 121, True),
                (381, 396, True),
                (597, 599, True),
                (774, 793, True),
            ]
        case "4204":
            return [
                (61, 73, True),
                (197, 208, True),
                (299, 307, True),
                (418, 430, True),
            ]
        case "4206":
            return [
                (94, 110, True),
                (280, 297, True),
                (502, 512, True),
                (774, 774, True),
            ]
        case "4253":
            return [
                (133, 147, True),
                (245, 250, True),
                (368, 368, True),
                (558, 559, True),
            ]
        case "4268":
            return [
                (122, 139, True),
                (282, 291, True),
                (485, 485, True),
                (700, 704, True),
            ]
        case "4292":
            return [
                (164, 164, True),
                (280, 280, True),
                (390, 402, True),
                (508, 520, True),
            ]
        case "4409":
            return [
                (110, 128, True),
                (247, 255, True),
                (456, 461, True),
                (658, 658, True),
            ]
        case "4471":
            return [
                (153, 159, True),
                (257, 260, True),
                (372, 378, True),
                (469, 474, True),
            ]
        case "4583":
            return [
                (77, 99, True),
                (282, 300, True),
                (448, 450, True),
                (695, 700, True),
            ]
        case "4789":
            return [
                (72, 89, True),
                (248, 264, True),
                (444, 450, True),
                (639, 643, True),
            ]
        case "4797":
            return [
                (99, 117, True),
                (347, 364, True),
                (625, 626, True),
                (894, 913, True),
            ]
        case "5054":
            return [
                (107, 114, True),
                (186, 188, True),
                (264, 265, True),
                (382, 395, True),
            ]
        case "5281":
            return [
                (103, 103, True),
                (248, 255, True),
                (431, 431, True),
                (633, 650, True),
            ]
        case "5322":
            return [
                (75, 90, True),
                (282, 297, True),
                (463, 479, True),
                (602, 619, True),
            ]
        case "5372":
            return [
                (105, 122, True),
                (292, 307, True),
                (503, 523, True),
                (749, 768, True),
            ]
        case "5381":
            return [
                (80, 93, True),
                (186, 200, True),
                (374, 382, True),
                (557, 574, True),
            ]
        case "5501":
            return [
                (82, 99, True),
                (193, 210, True),
                (346, 363, True),
                (525, 546, True),
            ]
        case "5535":
            return [
                (123, 139, True),
                (331, 348, True),
                (627, 643, True),
                (877, 885, True),
            ]
        case "5571":
            return [
                (74, 77, True),
                (226, 227, True),
                (442, 459, True),
                (632, 649, True),
            ]
        case "5656":
            return [
                (116, 133, True),
                (260, 274, True),
                (399, 416, True),
                (532, 548, True),
            ]
        case "5717":
            return [
                (42, 54, True),
                (219, 224, True),
                (411, 426, True),
                (572, 584, True),
            ]
        case "5823":
            return [
                (64, 66, True),
                (225, 235, True),
                (349, 355, True),
                (468, 470, True),
            ]
        case "5901":
            return [
                (99, 104, True),
                (278, 278, True),
                (522, 523, True),
                (747, 764, True),
            ]
        case "6088":
            return [
                (128, 128, True),
                (350, 367, True),
                (521, 535, True),
                (671, 687, True),
            ]
        case "6228":
            return [
                (102, 102, True),
                (296, 310, True),
                (429, 431, True),
                (676, 679, True),
            ]
        case "6240":
            return [
                (147, 147, True),
                (444, 464, True),
                (852, 870, True),
                (1251, 1264, True),
            ]
        case "6285":
            return [
                (98, 98, True),
                (271, 282, True),
                (477, 483, True),
                (666, 676, True),
            ]
        case "6736":
            return [
                (123, 123, True),
                (376, 391, True),
                (758, 766, True),
                (1005, 1007, True),
            ]
        case "6873":
            return [
                (108, 111, True),
                (279, 288, True),
                (509, 523, True),
                (741, 756, True),
            ]
        case "7076":
            return [
                (102, 121, True),
                (249, 259, True),
                (390, 407, True),
                (623, 623, True),
            ]
        case "7156":
            return [
                (76, 92, True),
                (289, 306, True),
                (474, 492, True),
                (686, 688, True),
            ]
        case "7256":
            return [
                (100, 109, True),
                (340, 352, True),
                (517, 517, True),
                (706, 706, True),
            ]
        case "7262":
            return [
                (83, 100, True),
                (269, 288, True),
                (496, 496, True),
                (650, 668, True),
            ]
        case "7389":
            return [
                (59, 64, True),
                (200, 213, True),
                (433, 440, True),
                (553, 561, True),
            ]
        case "7413":
            return [
                (51, 53, True),
                (168, 178, True),
                (310, 326, True),
                (515, 515, True),
            ]
        case "7530":
            return [
                (88, 102, True),
                (319, 336, True),
                (604, 620, True),
                (840, 845, True),
            ]
        case "7641":
            return [
                (86, 104, True),
                (306, 318, True),
                (551, 567, True),
                (772, 791, True),
            ]
        case "7652":
            return [
                (112, 124, True),
                (305, 305, True),
                (442, 458, True),
                (616, 632, True),
            ]
        case "7712":
            return [
                (96, 121, True),
                (213, 254, True),
                (414, 429, True),
                (587, 606, True),
            ]
        case "9067":
            return [
                (245, 245, True),
                (462, 470, True),
                (719, 727, True),
                (1032, 1046, True),
            ]
        case "9078":
            return [
                (67, 75, True),
                (279, 287, True),
                (408, 423, True),
                (525, 528, True),
            ]
        case "9082":
            return [
                (134, 134, True),
                (285, 289, True),
                (407, 412, True),
                (591, 600, True),
            ]
        case "9125":
            return [
                (123, 123, True),
                (279, 296, True),
                (396, 411, True),
                (540, 542, True),
            ]
        case "9285":
            return [
                (166, 171, True),
                (389, 408, True),
                (674, 688, True),
                (865, 886, True),
            ]
        case "9430":
            return [
                (107, 110, True),
                (354, 368, True),
                (585, 599, True),
                (822, 828, True),
            ]
        case "9613":
            return [
                (129, 131, True),
                (279, 293, True),
                (581, 583, True),
                (914, 918, True),
            ]
        case "9656":
            return [
                (36, 50, True),
                (134, 135, True),
                (242, 273, True),
                (343, 351, True),
            ]
        case "9673":
            return [
                (98, 98, True),
                (310, 310, True),
                (577, 579, True),
                (875, 876, True),
            ]
        case "9730":
            return [
                (103, 104, True),
                (288, 304, True),
                (497, 501, True),
                (745, 754, True),
            ]
        case "9934":
            return [
                (89, 90, True),
                (202, 202, True),
                (441, 457, True),
                (672, 688, True),
            ]
        case "9941":
            return [
                (97, 104, True),
                (254, 263, True),
                (544, 562, True),
                (836, 858, True),
            ]
        case "00386":
            return [
                (73, 75, True),
                (226, 231, True),
                (589, 617, True),
                (883, 908, True),
                (1145, 1174, True),
            ]
        case "02877":
            return [
                (88, 88, True),
                (368, 394, True),
                (620, 625, True),
                (830, 841, True),
                (971, 978, True),
            ]
        case "03023":
            return [
                (64, 94, True),
                (276, 311, True),
                (478, 497, True),
                (633, 686, True),
                (808, 847, True),
            ]
        case "03115":
            return [
                (162, 193, True),
                (388, 427, True),
                (721, 763, True),
                (886, 886, True),
                (1228, 1230, True),
            ]
        case "07562":
            return [
                (78, 79, True),
                (233, 254, True),
                (412, 452, True),
                (574, 581, True),
                (750, 784, True),
            ]
        case "10716":
            return [
                (54, 87, True),
                (268, 270, True),
                (441, 452, True),
                (652, 693, True),
                (924, 931, True),
            ]
        case "10872":
            return [
                (58, 89, True),
                (299, 300, True),
                (429, 457, True),
                (577, 611, True),
                (823, 857, True),
            ]
        case "10908":
            return [
                (79, 97, True),
                (465, 472, True),
                (720, 731, True),
                (1060, 1067, True),
                (1274, 1278, True),
            ]
        case "11036":
            return [
                (106, 141, True),
                (287, 326, True),
                (531, 543, True),
                (793, 832, True),
                (1048, 1050, True),
            ]
        case "11956":
            return [
                (62, 81, True),
                (236, 256, True),
                (712, 723, True),
                (936, 958, True),
                (1104, 1125, True),
            ]
        case "12441":
            return [
                (131, 164, True),
                (273, 309, True),
                (494, 530, True),
                (685, 721, True),
                (953, 989, True),
            ]
        case "13914":
            return [
                (72, 93, True),
                (236, 258, True),
                (397, 401, True),
                (607, 627, True),
                (772, 774, True),
            ]
        case "15260":
            return [
                (59, 92, True),
                (219, 256, True),
                (342, 382, True),
                (515, 546, True),
                (729, 732, True),
            ]
        case "16212":
            return [
                (52, 76, True),
                (349, 357, True),
                (531, 553, True),
                (663, 686, True),
                (814, 837, True),
            ]
        case "16580":
            return [
                (76, 112, True),
                (249, 290, True),
                (407, 438, True),
                (550, 554, True),
                (709, 724, True),
            ]
        case "17907":
            return [
                (59, 98, True),
                (228, 229, True),
                (458, 458, True),
                (621, 624, True),
                (810, 810, True),
            ]
        case "18195":
            return [
                (74, 107, True),
                (346, 346, True),
                (590, 628, True),
                (885, 886, True),
                (1119, 1141, True),
            ]
        case "18581":
            return [
                (62, 148, True),
                (314, 333, True),
                (437, 471, True),
                (587, 593, True),
                (828, 859, True),
            ]
        case "18608":
            return [
                (118, 149, True),
                (375, 393, True),
                (645, 649, True),
                (957, 958, True),
                (1197, 1233, True),
            ]
        case "19626":
            return [
                (127, 156, True),
                (603, 624, True),
                (753, 775, True),
                (1032, 1054, True),
                (1238, 1259, True),
            ]
        case "19650":
            return [
                (59, 84, True),
                (232, 243, True),
                (642, 667, True),
                (794, 818, True),
                (961, 961, True),
            ]
        case "20490":
            return [
                (75, 108, True),
                (341, 341, True),
                (588, 616, True),
                (775, 775, True),
                (960, 962, True),
            ]
        case "20583":
            return [
                (91, 124, True),
                (337, 363, True),
                (558, 591, True),
                (754, 781, True),
                (1013, 1017, True),
            ]
        case "20611":
            return [
                (87, 119, True),
                (290, 290, True),
                (544, 573, True),
                (806, 840, True),
                (940, 980, True),
            ]
        case "21584":
            return [
                (98, 130, True),
                (310, 345, True),
                (500, 514, True),
                (705, 707, True),
                (919, 946, True),
            ]
        case "22222":
            return [
                (71, 72, True),
                (239, 239, True),
                (364, 364, True),
                (503, 664, True),
                (664, 664, True),
            ]
        case "23529":
            return [
                (92, 125, True),
                (255, 296, True),
                (489, 518, True),
                (647, 685, True),
                (898, 899, True),
            ]
        case "24608":
            return [
                (82, 111, True),
                (271, 301, True),
                (406, 437, True),
                (662, 662, True),
                (784, 812, True),
            ]
        case "24832":
            return [
                (62, 95, True),
                (232, 267, True),
                (528, 536, True),
                (895, 939, True),
                (1147, 1190, True),
            ]
        case "26191":
            return [
                (121, 121, True),
                (268, 270, True),
                (492, 532, True),
                (717, 717, True),
                (926, 964, True),
            ]
        case "26211":
            return [
                (82, 113, True),
                (309, 335, True),
                (523, 571, True),
                (821, 854, True),
                (951, 994, True),
            ]
        case "26523":
            return [
                (61, 94, True),
                (198, 244, True),
                (345, 387, True),
                (493, 536, True),
                (659, 701, True),
            ]
        case "27201":
            return [
                (111, 149, True),
                (381, 406, True),
                (640, 677, True),
                (881, 887, True),
                (1170, 1211, True),
            ]
        case "28037":
            return [
                (113, 155, True),
                (282, 303, True),
                (465, 484, True),
                (755, 755, True),
                (1085, 1115, True),
            ]
        case "31143":
            return [
                (125, 146, True),
                (319, 349, True),
                (466, 504, True),
                (681, 713, True),
                (961, 990, True),
            ]
        case "31386":
            return [
                (108, 123, True),
                (367, 406, True),
                (605, 605, True),
                (926, 945, True),
                (1216, 1242, True),
            ]
        case "32472":
            return [
                (55, 89, True),
                (214, 252, True),
                (455, 483, True),
                (612, 632, True),
                (861, 905, True),
            ]
        case "33118":
            return [
                (98, 127, True),
                (267, 292, True),
                (466, 503, True),
                (596, 635, True),
                (861, 879, True),
            ]
        case "33816":
            return [
                (71, 71, True),
                (197, 197, True),
                (644, 646, True),
                (968, 996, True),
                (1478, 1478, True),
            ]
        case "37597":
            return [
                (97, 132, True),
                (317, 353, True),
                (520, 549, True),
                (761, 789, True),
                (937, 945, True),
            ]
        case "38403":
            return [
                (96, 120, True),
                (312, 335, True),
                (551, 584, True),
                (775, 780, True),
                (1121, 1147, True),
            ]
        case "39158":
            return [
                (86, 118, True),
                (269, 270, True),
                (489, 527, True),
                (695, 724, True),
                (861, 864, True),
            ]
        case "39653":
            return [
                (86, 90, True),
                (293, 296, True),
                (446, 450, True),
                (575, 610, True),
                (792, 825, True),
            ]
        case "40314":
            return [
                (57, 91, True),
                (329, 329, True),
                (554, 554, True),
                (752, 790, True),
                (1001, 1025, True),
            ]
        case "41657":
            return [
                (75, 97, True),
                (213, 248, True),
                (424, 453, True),
                (574, 610, True),
                (857, 864, True),
            ]
        case "42146":
            return [
                (71, 102, True),
                (311, 345, True),
                (499, 536, True),
                (690, 745, True),
                (912, 957, True),
            ]
        case "42591":
            return [
                (68, 100, True),
                (274, 303, True),
                (413, 449, True),
                (669, 669, True),
                (955, 984, True),
            ]
        case "42972":
            return [
                (99, 126, True),
                (467, 490, True),
                (852, 855, True),
                (1074, 1084, True),
                (1359, 1388, True),
            ]
        case "45639":
            return [
                (47, 82, True),
                (203, 219, True),
                (368, 371, True),
                (576, 608, True),
                (824, 835, True),
            ]
        case "45675":
            return [
                (65, 96, True),
                (227, 258, True),
                (406, 426, True),
                (697, 699, True),
                (932, 945, True),
            ]
        case "45780":
            return [
                (91, 128, True),
                (251, 287, True),
                (435, 465, True),
                (629, 638, True),
                (826, 826, True),
            ]
        case "46052":
            return [
                (89, 108, True),
                (355, 370, True),
                (671, 678, True),
                (903, 922, True),
                (1140, 1160, True),
            ]
        case "46256":
            return [
                (51, 77, True),
                (342, 358, True),
                (622, 649, True),
                (827, 850, True),
                (1024, 1042, True),
            ]
        case "46357":
            return [
                (53, 75, True),
                (198, 214, True),
                (349, 374, True),
                (545, 569, True),
                (760, 783, True),
            ]
        case "46599":
            return [
                (119, 152, True),
                (366, 386, True),
                (560, 592, True),
                (755, 755, True),
                (928, 928, True),
            ]
        case "48799":
            return [
                (63, 92, True),
                (298, 302, True),
                (486, 496, True),
                (703, 721, True),
                (871, 871, True),
            ]
        case "52644":
            return [
                (57, 72, True),
                (240, 285, True),
                (464, 464, True),
                (735, 763, True),
                (874, 875, True),
            ]
        case "53861":
            return [
                (83, 120, True),
                (271, 275, True),
                (616, 626, True),
                (794, 840, True),
                (1013, 1056, True),
            ]
        case "55274":
            return [
                (28, 64, True),
                (195, 218, True),
                (380, 434, True),
                (657, 684, True),
                (792, 841, True),
            ]
        case "55465":
            return [
                (98, 130, True),
                (229, 268, True),
                (438, 461, True),
                (648, 649, True),
                (854, 859, True),
            ]
        case "55711":
            return [
                (65, 99, True),
                (229, 250, True),
                (449, 459, True),
                (680, 715, True),
                (825, 869, True),
            ]
        case "57457":
            return [
                (98, 127, True),
                (288, 309, True),
                (423, 463, True),
                (599, 636, True),
                (820, 847, True),
            ]
        case "57874":
            return [
                (82, 99, True),
                (364, 379, True),
                (489, 517, True),
                (635, 640, True),
                (802, 824, True),
            ]
        case "59709":
            return [
                (119, 157, True),
                (351, 364, True),
                (575, 578, True),
                (830, 830, True),
                (1139, 1139, True),
            ]
        case "59988":
            return [
                (107, 129, True),
                (350, 373, True),
                (509, 533, True),
                (729, 752, True),
                (879, 904, True),
            ]
        case "60113":
            return [
                (57, 57, True),
                (280, 284, True),
                (569, 598, True),
                (721, 753, True),
                (905, 939, True),
            ]
        case "60222":
            return [
                (83, 89, True),
                (311, 333, True),
                (514, 551, True),
                (628, 679, True),
                (769, 808, True),
            ]
        case "60863":
            return [
                (47, 67, True),
                (339, 341, True),
                (461, 486, True),
                (597, 600, True),
                (759, 785, True),
            ]
        case "60877":
            return [
                (94, 115, True),
                (384, 402, True),
                (575, 601, True),
                (735, 762, True),
                (863, 906, True),
            ]
        case "61417":
            return [
                (49, 61, True),
                (482, 514, True),
                (647, 683, True),
                (829, 835, True),
                (1093, 1096, True),
            ]
        case "62523":
            return [
                (78, 94, True),
                (300, 342, True),
                (469, 488, True),
                (676, 716, True),
                (889, 928, True),
            ]
        case "63047":
            return [
                (125, 125, True),
                (317, 317, True),
                (559, 562, True),
                (808, 820, True),
                (979, 995, True),
            ]
        case "64627":
            return [
                (150, 150, True),
                (338, 361, True),
                (576, 576, True),
                (747, 791, True),
                (1029, 1052, True),
            ]
        case "64656":
            return [
                (232, 241, True),
                (393, 433, True),
                (460, 460, True),
                (608, 631, True),
                (784, 806, True),
            ]
        case "66449":
            return [
                (128, 132, True),
                (232, 241, True),
                (393, 433, True),
                (521, 553, True),
                (754, 781, True),
            ]
        case "69506":
            return [
                (68, 68, True),
                (233, 233, True),
                (439, 459, True),
                (719, 719, True),
                (914, 937, True),
            ]
        case "70198":
            return [
                (75, 94, True),
                (224, 224, True),
                (514, 561, True),
                (805, 805, True),
                (955, 959, True),
            ]
        case "71426":
            return [
                (63, 63, True),
                (256, 297, True),
                (423, 449, True),
                (637, 667, True),
                (896, 923, True),
            ]
        case "72220":
            return [
                (105, 139, True),
                (401, 431, True),
                (524, 565, True),
                (655, 697, True),
                (945, 953, True),
            ]
        case "73061":
            return [
                (68, 84, True),
                (480, 502, True),
                (791, 814, True),
                (1015, 1040, True),
                (1307, 1333, True),
            ]
        case "73297":
            return [
                (71, 101, True),
                (267, 304, True),
                (422, 454, True),
                (700, 723, True),
                (920, 920, True),
            ]
        case "73589":
            return [
                (104, 130, True),
                (358, 385, True),
                (532, 562, True),
                (709, 738, True),
                (925, 949, True),
            ]
        case "74581":
            return [
                (82, 118, True),
                (241, 279, True),
                (420, 461, True),
                (584, 617, True),
                (811, 847, True),
            ]
        case "75439":
            return [
                (35, 35, True),
                (244, 278, True),
                (403, 442, True),
                (657, 696, True),
                (953, 965, True),
            ]
        case "75442":
            return [
                (53, 78, True),
                (277, 311, True),
                (453, 484, True),
                (585, 618, True),
                (915, 949, True),
            ]
        case "76553":
            return [
                (82, 91, True),
                (428, 443, True),
                (610, 624, True),
                (737, 757, True),
                (1110, 1130, True),
            ]
        case "77402":
            return [
                (86, 95, True),
                (213, 217, True),
                (353, 365, True),
                (555, 561, True),
                (756, 791, True),
            ]
        case "77765":
            return [
                (96, 130, True),
                (230, 248, True),
                (339, 364, True),
                (618, 659, True),
                (830, 866, True),
            ]
        case "77777":
            return [
                (77, 77, True),
                (201, 202, True),
                (337, 337, True),
                (474, 474, True),
                (636, 636, True),
            ]
        case "79716":
            return [
                (64, 65, True),
                (225, 247, True),
                (396, 424, True),
                (579, 608, True),
                (848, 877, True),
            ]
        case "91401":
            return [
                (56, 56, True),
                (190, 221, True),
                (341, 381, True),
                (545, 545, True),
                (776, 817, True),
            ]
        case "92637":
            return [
                (55, 63, True),
                (253, 299, True),
                (437, 467, True),
                (586, 626, True),
                (865, 911, True),
            ]
        case "93137":
            return [
                (143, 143, True),
                (379, 410, True),
                (647, 676, True),
                (867, 893, True),
                (1113, 1139, True),
            ]
        case "94137":
            return [
                (177, 184, True),
                (430, 472, True),
                (622, 674, True),
                (881, 919, True),
                (1182, 1225, True),
            ]
        case "94754":
            return [
                (77, 84, True),
                (304, 305, True),
                (462, 462, True),
                (643, 653, True),
                (793, 806, True),
            ]
        case "95901":
            return [
                (107, 109, True),
                (293, 306, True),
                (458, 458, True),
                (644, 644, True),
                (867, 904, True),
            ]
        case "96610":
            return [
                (144, 147, True),
                (378, 389, True),
                (499, 514, True),
                (819, 838, True),
                (1246, 1246, True),
            ]
        case "96847":
            return [
                (60, 60, True),
                (166, 167, True),
                (334, 334, True),
                (659, 670, True),
                (820, 844, True),
            ]
        case "97186":
            return [
                (180, 180, True),
                (382, 399, True),
                (624, 662, True),
                (992, 992, True),
                (1247, 1247, True),
            ]
        case "97394":
            return [
                (97, 121, True),
                (283, 304, True),
                (543, 587, True),
                (807, 824, True),
                (1077, 1120, True),
            ]
        case "7598":
            return [
                (273, 285, True),
                (512, 524, True),
                (715, 723, True),
                (838, 840, True),
            ]
        case "3546":
            return [
                (141, 155, True),
                (277, 290, True),
                (417, 428, True),
                (603, 616, True),
            ]
        case "4358":
            return [
                (245, 261, True),
                (423, 437, True),
                (594, 609, True),
                (821, 830, True),
            ]
        case "3697":
            return [
                (243, 284, True),
                (362, 377, True),
                (471, 482, True),
                (725, 738, True),
            ]
        case "8436":
            return [
                (435, 445, True),
                (564, 754, True),
                (956, 967, True),
                (1119, 1132, True),
            ]
        case "1358":
            return [
                (123, 137, True),
                (231, 245, True),
                (355, 366, True),
                (490, 491, True),
            ]
        case "1156":
            return [
                (190, 203, True),
                (240, 255, True),
                (406, 420, True),
            ]
        case "6654":
            return [
                (184, 197, True),
                (262, 275, True),
                (372, 385, True),
                (593, 606, True),
            ]
        case "1346":
            return [
                (276, 288, True),
                (552, 566, True),
                (768, 778, True),
                (1025, 1039, True),
            ]
        case "0715":
            return [
                (504, 516, True),
                (639, 861, True),
                (1024, 1055, True),
            ]
        case "3361":
            return [
                (248, 259, True),
                (299, 312, True),
                (455, 463, True),
                (585, 599, True),
            ]
        case "8825":
            return [
                (92, 104, True),
                (179, 193, True),
                (294, 302, True),
                (449, 455, True),
            ]
        case "385186":
            return [
                (37, 54, True),
                (504, 519, True),
                (891, 905, True),
                (1299, 1311, True),
                (1730, 1741, True),
                (2126, 2138, True),
            ]
        case "022131":
            return [
                (75, 88, True),
                (326, 338, True),
                (572, 581, True),
                (814, 825, True),
                (1083, 1094, True),
                (1483, 1497, True),
            ]
        case "350697":
            return [
                (50, 65, True),
                (308, 321, True),
                (572, 584, True),
                (959, 972, True),
                (1294, 1305, True),
                (1641, 1653, True),
            ]


    return []