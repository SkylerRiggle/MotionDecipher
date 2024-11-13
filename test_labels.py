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
        case "022131":
            return [
                (50, 68, True),
                (232, 257, True),
                (388, 414, True),
                (592, 618, True),
                (826, 847, True),
                (1097, 1123, True),
            ]
        case "024741":
            return [
                (498, 508, True),
                (694, 719, True),
                (923, 940, True),
                (1134, 1134, True),
                (1329, 1339, True),
                (1579, 1608, True),
            ]
        case "024750":
            return [
                (99, 104, True),
                (301, 319, True),
                (509, 530, True),
                (700, 707, True),
                (882, 903, True),
                (1067, 1069, True),
            ]
        case "031111":
            return [
                (185, 198, True),
                (444, 467, True),
                (751, 777, True),
                (1028, 1053, True),
                (1194, 1208, True),
                (1358, 1370, True),
            ]
        case "033856":
            return [
                (157, 172, True),
                (338, 356, True),
                (503, 522, True),
                (723, 732, True),
                (917, 933, True),
                (1157, 1166, True),
            ]
        case "037036":
            return [
                (93, 104, True),
                (286, 297, True),
                (478, 492, True),
                (704, 710, True),
                (926, 939, True),
                (1099, 1099, True),
            ]
        case "059034":
            return [
                (89, 98, True),
                (196, 211, True),
                (312, 318, True),
                (462, 468, True),
                (621, 641, True),
                (796, 816, True),
            ]
        case "063079":
            return [
                (163, 163, True),
                (399, 412, True),
                (641, 664, True),
                (895, 901, True),
                (1088, 1111, True),
                (1342, 1349, True),
            ]
        case "082559":
            return [
                (80, 82, True),
                (187, 192, True),
                (359, 387, True),
                (499, 523, True),
                (599, 622, True),
                (815, 817, True),
            ]
        case "094691":
            return [
                (80, 80, True),
                (302, 310, True),
                (563, 579, True),
                (750, 750, True),
                (935, 942, True),
                (1231, 1251, True),
            ]
        case "106116":
            return [
                (61, 80, True),
                (271, 280, True),
                (435, 446, True),
                (615, 639, True),
                (711, 732, True),
                (913, 924, True),
            ]
        case "108933":
            return [
                (43, 53, True),
                (169, 178, True),
                (305, 311, True),
                (440, 441, True),
                (578, 594, True),
                (697, 711, True),
            ]
        case "124128":
            return [
                (72, 97, True),
                (256, 284, True),
                (490, 513, True),
                (714, 738, True),
                (957, 983, True),
                (1202, 1206, True),
            ]
        case "128676":
            return [
                (120, 140, True),
                (256, 276, True),
                (410, 413, True),
                (627, 630, True),
                (785, 785, True),
                (955, 955, True),
            ]
        case "136623":
            return [
                (106, 131, True),
                (291, 313, True),
                (461, 461, True),
                (619, 631, True),
                (821, 843, True),
                (1050, 1074, True),
            ]
        case "138778":
            return [
                (84, 108, True),
                (234, 247, True),
                (382, 397, True),
                (508, 524, True),
                (621, 641, True),
                (782, 790, True),
            ]
        case "140824":
            return [
                (178, 198, True),
                (377, 395, True),
                (624, 832, True),
                (827, 1088, True),
                (1065, 1298, True),
                (1276, 1298, True),
            ]
        case "143994":
            return [
                (129, 159, True),
                (329, 349, True),
                (542, 566, True),
                (791, 803, True),
                (968, 979, True),
                (1204, 1232, True),
            ]
        case "149624":
            return [
                (72, 97, True),
                (228, 248, True),
                (428, 436, True),
                (567, 570, True),
                (732, 755, True),
                (897, 919, True),
            ]
        case "151282":
            return [
                (128, 157, True),
                (322, 339, True),
                (503, 526, True),
                (712, 727, True),
                (983, 999, True),
                (1240, 1251, True),
            ]
        case "152770":
            return [
                (127, 150, True),
                (284, 305, True),
                (471, 495, True),
                (763, 783, True),
                (912, 918, True),
                (1125, 1128, True),
            ]
        case "154385":
            return [
                (33, 103, True),
                (189, 208, True),
                (323, 349, True),
                (637, 660, True),
                (848, 872, True),
                (984, 1013, True),
            ]
        case "155253":
            return [
                (109, 128, True),
                (257, 260, True),
                (416, 426, True),
                (545, 564, True),
                (676, 684, True),
                (795, 808, True),
            ]
        case "172366":
            return [
                (121, 148, True),
                (313, 331, True),
                (543, 565, True),
                (927, 944, True),
                (1145, 1145, True),
                (1271, 1271, True),
            ]
        case "189870":
            return [
                (130, 151, True),
                (327, 347, True),
                (517, 517, True),
                (708, 729, True),
                (897, 918, True),
                (1100, 1121, True),
            ]
        case "219530":
            return [
                (93, 111, True),
                (307, 329, True),
                (569, 572, True),
                (787, 804, True),
                (1066, 1084, True),
                (1313, 1313, True),
            ]
        case "225228":
            return [
                (48, 68, True),
                (184, 209, True),
                (319, 329, True),
                (484, 505, True),
                (581, 602, True),
                (739, 744, True),
            ]
        case "234422":
            return [
                (94, 117, True),
                (243, 266, True),
                (499, 523, True),
                (662, 683, True),
                (849, 874, True),
                (1053, 1076, True),
            ]
        case "240287":
            return [
                (85, 108, True),
                (230, 253, True),
                (433, 433, True),
                (596, 621, True),
                (818, 819, True),
                (993, 997, True),
            ]
        case "241961":
            return [
                (93, 120, True),
                (314, 341, True),
                (487, 514, True),
                (790, 813, True),
                (943, 962, True),
                (1190, 1219, True),
            ]
        case "260422":
            return [
                (164, 181, True),
                (432, 435, True),
                (658, 883, True),
                (864, 1097, True),
                (1075, 1307, True),
                (1281, 1307, True),
            ]
        case "261119":
            return [
                (92, 118, True),
                (301, 301, True),
                (570, 596, True),
                (707, 733, True),
                (819, 846, True),
                (1163, 1163, True),
            ]
        case "287687":
            return [
                (85, 105, True),
                (270, 270, True),
                (387, 401, True),
                (540, 540, True),
                (684, 697, True),
                (810, 830, True),
            ]
        case "289737":
            return [
                (152, 173, True),
                (378, 386, True),
                (526, 547, True),
                (749, 771, True),
                (963, 984, True),
                (1228, 1247, True),
            ]
        case "298392":
            return [
                (125, 154, True),
                (356, 358, True),
                (520, 523, True),
                (785, 788, True),
                (1043, 1048, True),
                (1275, 1299, True),
            ]
        case "336396":
            return [
                (109, 124, True),
                (241, 245, True),
                (439, 445, True),
                (607, 819, True),
                (819, 990, True),
                (986, 990, True),
            ]
        case "338910":
            return [
                (157, 172, True),
                (325, 341, True),
                (565, 571, True),
                (803, 810, True),
                (1032, 1054, True),
                (1274, 1274, True),
            ]
        case "340153":
            return [
                (153, 171, True),
                (353, 377, True),
                (569, 569, True),
                (784, 808, True),
                (989, 990, True),
                (1293, 1299, True),
            ]
        case "350697":
            return [
                (106, 120, True),
                (231, 239, True),
                (403, 410, True),
                (639, 642, True),
                (762, 772, True),
                (910, 924, True),
            ]
        case "366078":
            return [
                (65, 70, True),
                (211, 224, True),
                (324, 329, True),
                (536, 536, True),
                (708, 724, True),
                (848, 858, True),
            ]
        case "373782":
            return [
                (164, 170, True),
                (501, 519, True),
                (685, 698, True),
                (925, 939, True),
                (1119, 1125, True),
                (1308, 1336, True),
            ]
        case "385186":
            return [
                (136, 156, True),
                (399, 404, True),
                (554, 576, True),
                (846, 868, True),
                (1128, 1142, True),
                (1356, 1364, True),
            ]
        case "399354":
            return [
                (141, 142, True),
                (302, 302, True),
                (410, 410, True),
                (578, 578, True),
                (755, 760, True),
                (896, 904, True),
            ]
        case "399958":
            return [
                (134, 141, True),
                (326, 326, True),
                (524, 524, True),
                (681, 681, True),
                (852, 871, True),
                (1165, 1168, True),
            ]
        case "411333":
            return [
                (64, 75, True),
                (204, 230, True),
                (324, 352, True),
                (548, 574, True),
                (654, 678, True),
                (762, 792, True),
            ]
        case "455829":
            return [
                (171, 191, True),
                (337, 349, True),
                (495, 505, True),
                (789, 790, True),
                (1033, 1053, True),
                (1337, 1337, True),
            ]
        case "459191":
            return [
                (102, 123, True),
                (323, 345, True),
                (611, 611, True),
                (821, 844, True),
                (1052, 1052, True),
                (1292, 1320, True),
            ]
        case "460359":
            return [
                (170, 193, True),
                (335, 351, True),
                (518, 523, True),
                (780, 804, True),
                (1006, 1029, True),
                (1220, 1235, True),
            ]
        case "464281":
            return [
                (126, 147, True),
                (317, 531, True),
                (512, 752, True),
                (729, 956, True),
                (955, 1233, True),
                (1205, 1233, True),
            ]
        case "464801":
            return [
                (158, 177, True),
                (371, 374, True),
                (556, 575, True),
                (734, 734, True),
                (896, 896, True),
                (1176, 1201, True),
            ]
        case "476478":
            return [
                (121, 142, True),
                (313, 335, True),
                (516, 528, True),
                (730, 753, True),
                (893, 897, True),
                (1110, 1110, True),
            ]
        case "488681":
            return [
                (80, 99, True),
                (225, 245, True),
                (365, 368, True),
                (574, 574, True),
                (742, 745, True),
                (908, 1099, True),
                (992, 1099, True),
            ]
        case "498534":
            return [
                (49, 69, True),
                (248, 256, True),
                (358, 361, True),
                (480, 495, True),
                (609, 626, True),
                (766, 785, True),
            ]
        case "502617":
            return [
                (68, 69, True),
                (197, 206, True),
                (334, 356, True),
                (586, 589, True),
                (777, 803, True),
                (951, 956, True),
            ]
        case "513636":
            return [
                (100, 121, True),
                (268, 289, True),
                (425, 449, True),
                (657, 675, True),
                (835, 854, True),
                (1045, 1062, True),
            ]
        case "543359":
            return [
                (83, 102, True),
                (216, 238, True),
                (416, 438, True),
                (563, 582, True),
                (729, 756, True),
                (984, 990, True),
            ]
        case "551594":
            return [
                (191, 193, True),
                (342, 347, True),
                (605, 635, True),
                (843, 860, True),
                (1100, 1100, True),
                (1364, 1388, True),
            ]
        case "561129":
            return [
                (90, 117, True),
                (265, 288, True),
                (552, 577, True),
                (712, 740, True),
                (893, 924, True),
                (1110, 1113, True),
            ]
        case "570517":
            return [
                (129, 144, True),
                (347, 366, True),
                (595, 598, True),
                (824, 835, True),
                (1045, 1068, True),
                (1308, 1324, True),
            ]
        case "571448":
            return [
                (131, 134, True),
                (331, 351, True),
                (498, 526, True),
                (573, 704, True),
                (682, 861, True),
                (843, 1049, True),
                (1042, 1049, True),
            ]
        case "591930":
            return [
                (154, 170, True),
                (455, 455, True),
                (724, 750, True),
                (1000, 1000, True),
                (1261, 1283, True),
                (1488, 1488, True),
            ]
        case "597432":
            return [
                (101, 104, True),
                (233, 240, True),
                (347, 353, True),
                (438, 453, True),
                (554, 561, True),
                (658, 679, True),
            ]
        case "600017":
            return [
                (157, 163, True),
                (407, 424, True),
                (590, 590, True),
                (755, 1061, True),
                (1035, 1286, True),
                (1263, 1286, True),
            ]
        case "600202":
            return [
                (116, 120, True),
                (290, 307, True),
                (485, 499, True),
                (701, 724, True),
                (940, 954, True),
                (1140, 1163, True),
            ]
        case "625813":
            return [
                (153, 387, True),
                (362, 578, True),
                (558, 812, True),
                (802, 1021, True),
                (996, 1294, True),
                (1274, 1294, True),
            ]
        case "628208":
            return [
                (108, 123, True),
                (277, 300, True),
                (616, 627, True),
                (807, 830, True),
                (986, 1005, True),
                (1162, 1178, True),
            ]
        case "635924":
            return [
                (131, 131, True),
                (311, 317, True),
                (496, 512, True),
                (692, 692, True),
                (936, 958, True),
                (1153, 1171, True),
            ]
        case "658388":
            return [
                (105, 115, True),
                (231, 246, True),
                (394, 395, True),
                (607, 618, True),
                (810, 822, True),
                (927, 942, True),
            ]
        case "671621":
            return [
                (86, 87, True),
                (279, 294, True),
                (441, 467, True),
                (715, 718, True),
                (910, 939, True),
                (1119, 1147, True),
            ]
        case "672187":
            return [
                (160, 178, True),
                (353, 363, True),
                (580, 609, True),
                (750, 773, True),
                (994, 1000, True),
                (1150, 1173, True),
            ]
        case "672295":
            return [
                (101, 101, True),
                (257, 263, True),
                (422, 447, True),
                (563, 589, True),
                (756, 756, True),
                (922, 935, True),
            ]
        case "680028":
            return [
                (116, 116, True),
                (305, 312, True),
                (491, 491, True),
                (650, 651, True),
                (848, 875, True),
                (1031, 1053, True),
            ]
        case "691750":
            return [
                (82, 86, True),
                (236, 242, True),
                (430, 450, True),
                (585, 604, True),
                (738, 753, True),
                (887, 888, True),
            ]
        case "694067":
            return [
                (47, 54, True),
                (179, 186, True),
                (308, 327, True),
                (500, 508, True),
                (636, 653, True),
                (837, 859, True),
            ]
        case "701510":
            return [
                (191, 191, True),
                (407, 407, True),
                (606, 631, True),
                (1076, 1080, True),
                (1253, 1273, True),
                (1517, 1517, True),
            ]
        case "708889":
            return [
                (111, 121, True),
                (280, 457, True),
                (450, 604, True),
                (590, 731, True),
                (729, 1043, True),
                (1043, 1043, True),
            ]
        case "727631":
            return [
                (113, 121, True),
                (345, 369, True),
                (628, 628, True),
                (832, 850, True),
                (1121, 1144, True),
                (1334, 1358, True),
            ]
        case "739662":
            return [
                (97, 106, True),
                (505, 509, True),
                (720, 729, True),
                (857, 864, True),
                (1023, 1026, True),
                (1305, 1325, True),
            ]
        case "743789":
            return [
                (90, 95, True),
                (235, 255, True),
                (462, 490, True),
                (728, 732, True),
                (884, 884, True),
                (1089, 1089, True),
            ]
        case "760695":
            return [
                (81, 108, True),
                (315, 329, True),
                (503, 504, True),
                (725, 725, True),
                (889, 1054, True),
                (1042, 1054, True),
            ]
        case "761576":
            return [
                (77, 102, True),
                (305, 326, True),
                (474, 499, True),
                (608, 628, True),
                (785, 800, True),
                (959, 969, True),
            ]
        case "767134":
            return [
                (157, 175, True),
                (384, 401, True),
                (617, 638, True),
                (828, 851, True),
                (1017, 1041, True),
                (1231, 1253, True),
            ]
        case "783302":
            return [
                (135, 143, True),
                (348, 362, True),
                (526, 545, True),
                (739, 756, True),
                (979, 979, True),
                (1240, 1260, True),
            ]
        case "790517":
            return [
                (98, 114, True),
                (356, 360, True),
                (587, 592, True),
                (785, 803, True),
                (1010, 1037, True),
                (1221, 1240, True),
            ]
        case "791689":
            return [
                (92, 93, True),
                (234, 239, True),
                (426, 450, True),
                (677, 683, True),
                (883, 891, True),
                (1073, 1074, True),
            ]
        case "791692":
            return [
                (120, 126, True),
                (320, 320, True),
                (539, 562, True),
                (742, 748, True),
                (956, 1200, True),
                (1180, 1200, True),
            ]
        case "793673":
            return [
                (155, 176, True),
                (330, 363, True),
                (498, 526, True),
                (699, 721, True),
                (882, 903, True),
                (1113, 1151, True),
            ]
        case "902410":
            return [
                (58, 58, True),
                (257, 264, True),
                (465, 487, True),
                (661, 682, True),
                (781, 800, True),
                (1002, 1017, True),
            ]
        case "904313":
            return [
                (117, 117, True),
                (318, 318, True),
                (532, 539, True),
                (769, 789, True),
                (967, 991, True),
                (1201, 1217, True),
            ]
        case "927958":
            return [
                (65, 74, True),
                (196, 213, True),
                (354, 364, True),
                (524, 527, True),
                (636, 648, True),
                (761, 766, True),
            ]
        case "936146":
            return [
                (140, 146, True),
                (292, 310, True),
                (461, 468, True),
                (593, 613, True),
                (779, 801, True),
                (959, 960, True),
            ]
        case "946313":
            return [
                (294, 298, True),
                (464, 489, True),
                (650, 671, True),
                (874, 882, True),
                (1029, 1057, True),
                (1267, 1291, True),
            ]
        case "955780":
            return [
                (73, 82, True),
                (220, 228, True),
                (314, 326, True),
                (710, 722, True),
                (833, 845, True),
                (970, 970, True),
            ]
        case "972764":
            return [
                (131, 134, True),
                (263, 281, True),
                (473, 496, True),
                (715, 720, True),
                (977, 980, True),
                (1235, 1258, True),
            ]
        case "977026":
            return [
                (88, 96, True),
                (266, 275, True),
                (437, 454, True),
                (737, 737, True),
                (937, 960, True),
                (1208, 1208, True),
            ]
        case "980805":
            return [
                (91, 96, True),
                (331, 331, True),
                (533, 542, True),
                (767, 776, True),
                (931, 939, True),
                (1143, 1167, True),
            ]
        case "989085":
            return [
                (121, 132, True),
                (330, 349, True),
                (515, 524, True),
                (773, 773, True),
                (977, 997, True),
                (1181, 1204, True),
            ]
        case "996267":
            return [
                (74, 82, True),
                (167, 174, True),
                (296, 300, True),
                (435, 453, True),
                (578, 580, True),
                (798, 813, True),
            ]
        case "997256":
            return [
                (107, 107, True),
                (306, 306, True),
                (550, 571, True),
                (820, 824, True),
                (1042, 1058, True),
                (1276, 1280, True),
            ]
        case "998766":
            return [
                (122, 122, True),
                (266, 266, True),
                (438, 442, True),
                (645, 664, True),
                (878, 882, True),
                (1060, 1062, True),
            ]
        case "0011557":
            return [
                (222, 222, True),
                (404, 404, True),
                (667, 669, True),
                (835, 848, True),
                (1184, 1184, True),
                (1361, 1361, True),
                (1649, 1650, True),
            ]
        case "0059923":
            return [
                (134, 134, True),
                (317, 317, True),
                (680, 694, True),
                (986, 986, True),
                (1184, 1184, True),
                (1516, 1546, True),
                (1834, 1863, True),
            ]
        case "0139798":
            return [
                (197, 197, True),
                (436, 465, True),
                (701, 724, True),
                (1014, 1014, True),
                (1284, 1286, True),
                (1590, 1590, True),
                (1918, 1920, True),
            ]
        case "0226319":
            return [
                (134, 134, True),
                (375, 404, True),
                (532, 564, True),
                (857, 860, True),
                (1058, 1092, True),
                (1355, 1384, True),
                (1628, 1630, True),
            ]
        case "0236782":
            return [
                (107, 314, True),
                (285, 522, True),
                (495, 704, True),
                (704, 963, True),
                (948, 1222, True),
                (1215, 1515, True),
                (1483, 1515, True),
            ]
        case "0342763":
            return [
                (110, 111, True),
                (415, 434, True),
                (652, 672, True),
                (867, 898, True),
                (1113, 1136, True),
                (1346, 1353, True),
                (1578, 1604, True),
            ]
        case "0349053":
            return [
                (131, 132, True),
                (456, 467, True),
                (695, 708, True),
                (1070, 1070, True),
                (1373, 1373, True),
                (1673, 1689, True),
                (1953, 1972, True),
            ]
        case "0369652":
            return [
                (179, 179, True),
                (483, 502, True),
                (736, 743, True),
                (1031, 1031, True),
                (1277, 1283, True),
                (1545, 1562, True),
                (1815, 1840, True),
            ]
        case "0433818":
            return [
                (114, 119, True),
                (330, 345, True),
                (553, 581, True),
                (723, 723, True),
                (981, 994, True),
                (1203, 1237, True),
                (1439, 1451, True),
            ]
        case "0545574":
            return [
                (213, 213, True),
                (447, 470, True),
                (673, 681, True),
                (893, 909, True),
                (1101, 1125, True),
                (1492, 1504, True),
                (1754, 1754, True),
            ]
        case "0549294":
            return [
                (305, 305, True),
                (570, 596, True),
                (815, 824, True),
                (1166, 1166, True),
                (1523, 1545, True),
                (1865, 1865, True),
                (2297, 2315, True),
            ]
        case "0921859":
            return [
                (192, 213, True),
                (504, 506, True),
                (753, 760, True),
                (959, 960, True),
                (1185, 1201, True),
                (1405, 1433, True),
                (1670, 1673, True),
            ]
        case "0976015":
            return [
                (132, 160, True),
                (358, 358, True),
                (614, 631, True),
                (857, 857, True),
                (1092, 1122, True),
                (1356, 1385, True),
                (1619, 1654, True),
            ]
        case "0989791":
            return [
                (190, 190, True),
                (406, 415, True),
                (654, 667, True),
                (905, 905, True),
                (1160, 1173, True),
                (1464, 1470, True),
                (1766, 1789, True),
            ]
        case "1022049":
            return [
                (149, 169, True),
                (482, 482, True),
                (731, 731, True),
                (1001, 1001, True),
                (1358, 1358, True),
                (1811, 1813, True),
                (2300, 2300, True),
            ]
        case "1042011":
            return [
                (207, 228, True),
                (583, 583, True),
                (880, 891, True),
                (1207, 1229, True),
                (1604, 1604, True),
                (2011, 2037, True),
                (2270, 2293, True),
            ]
        case "1100316":
            return [
                (195, 218, True),
                (520, 542, True),
                (908, 908, True),
                (1211, 1211, True),
                (1779, 1790, True),
                (2144, 2167, True),
                (2534, 2534, True),
            ]
        case "1220291":
            return [
                (224, 246, True),
                (443, 464, True),
                (654, 673, True),
                (1004, 1004, True),
                (1393, 1413, True),
                (1844, 1844, True),
                (2202, 2223, True),
            ]
        case "1224113":
            return [
                (198, 222, True),
                (459, 478, True),
                (656, 676, True),
                (998, 1000, True),
                (1507, 1533, True),
                (1716, 1740, True),
                (2128, 2144, True),
            ]
        case "1303398":
            return [
                (241, 261, True),
                (565, 582, True),
                (890, 890, True),
                (1262, 1280, True),
                (1488, 1506, True),
                (1844, 1844, True),
                (2145, 2146, True),
            ]
        case "1320392":
            return [
                (265, 285, True),
                (540, 554, True),
                (909, 930, True),
                (1280, 1280, True),
                (1649, 1660, True),
                (2039, 2039, True),
                (2446, 2469, True),
            ]
        case "1394366":
            return [
                (316, 363, True),
                (738, 754, True),
                (1124, 1124, True),
                (1483, 1497, True),
                (1884, 1902, True),
                (2289, 2290, True),
                (2559, 2559, True),
            ]
        case "1430526":
            return [
                (180, 205, True),
                (492, 513, True),
                (761, 783, True),
                (1067, 1067, True),
                (1424, 1442, True),
                (1742, 1775, True),
                (2069, 2082, True),
            ]
        case "1441762":
            return [
                (174, 196, True),
                (458, 476, True),
                (731, 745, True),
                (1038, 1062, True),
                (1370, 1371, True),
                (1712, 1712, True),
                (2094, 2116, True),
            ]
        case "1523792":
            return [
                (186, 224, True),
                (476, 494, True),
                (872, 889, True),
                (1191, 1204, True),
                (1610, 1610, True),
                (1937, 1937, True),
                (2323, 2346, True),
            ]
        case "1536705":
            return [
                (166, 187, True),
                (414, 431, True),
                (766, 785, True),
                (1164, 1167, True),
                (1526, 1528, True),
                (1941, 1944, True),
                (2256, 2275, True),
            ]
        case "1739783":
            return [
                (257, 277, True),
                (644, 648, True),
                (966, 986, True),
                (1400, 1404, True),
                (1754, 1755, True),
                (2105, 2105, True),
                (2398, 2417, True),
            ]
        case "1773652":
            return [
                (218, 224, True),
                (569, 569, True),
                (815, 815, True),
                (1214, 1214, True),
                (1583, 1583, True),
                (1928, 1928, True),
                (2423, 2423, True),
            ]
        case "2034822":
            return [
                (281, 293, True),
                (602, 604, True),
                (992, 992, True),
                (1342, 1344, True),
                (1731, 1731, True),
                (2092, 2109, True),
                (2369, 2386, True),
            ]
        case "2058229":
            return [
                (218, 231, True),
                (581, 581, True),
                (857, 859, True),
                (1166, 1168, True),
                (1503, 1512, True),
                (1842, 1852, True),
                (2318, 2318, True),
            ]
        case "2237232":
            return [
                (95, 97, True),
                (231, 231, True),
                (401, 673, True),
                (670, 843, True),
                (843, 1058, True),
                (1058, 1288, True),
                (1262, 1288, True),
            ]
        case "2250270":
            return [
                (120, 124, True),
                (249, 277, True),
                (472, 473, True),
                (689, 689, True),
                (876, 1144, True),
                (1144, 1373, True),
                (1370, 1373, True),
            ]
        case "2274740":
            return [
                (107, 109, True),
                (222, 224, True),
                (486, 488, True),
                (648, 648, True),
                (800, 800, True),
                (975, 977, True),
                (1274, 1274, True),
            ]
        case "2276152":
            return [
                (231, 247, True),
                (528, 546, True),
                (962, 970, True),
                (1447, 1458, True),
                (1931, 1931, True),
                (2362, 2362, True),
                (2755, 2772, True),
            ]
        case "2380123":
            return [
                (107, 107, True),
                (315, 315, True),
                (527, 527, True),
                (719, 719, True),
                (903, 905, True),
                (1115, 1115, True),
                (1142, 1143, True),
            ]
        case "2409469":
            return [
                (200, 205, True),
                (658, 660, True),
                (1040, 1040, True),
                (1385, 1385, True),
                (1818, 1821, True),
                (2213, 2214, True),
                (2567, 2570, True),
            ]
        case "2693278":
            return [
                (193, 199, True),
                (542, 542, True),
                (899, 899, True),
                (1180, 1180, True),
                (1580, 1596, True),
                (2126, 2126, True),
                (2522, 2522, True),
            ]
        case "2786382":
            return [
                (384, 399, True),
                (804, 805, True),
                (1183, 1183, True),
                (1631, 1634, True),
                (2009, 2010, True),
                (2489, 2489, True),
                (2951, 2951, True),
            ]
        case "2849452":
            return [
                (174, 192, True),
                (512, 512, True),
                (825, 828, True),
                (1205, 1205, True),
                (1619, 1620, True),
                (2083, 2093, True),
                (2538, 2554, True),
            ]
        case "2922857":
            return [
                (264, 282, True),
                (617, 623, True),
                (1106, 1124, True),
                (1491, 1510, True),
                (1937, 1942, True),
                (2515, 2529, True),
                (2955, 2956, True),
            ]
        case "3023575":
            return [
                (82, 98, True),
                (272, 272, True),
                (449, 461, True),
                (670, 689, True),
                (913, 913, True),
                (1208, 1211, True),
                (1424, 1425, True),
            ]
        case "3101803":
            return [
                (112, 131, True),
                (346, 366, True),
                (614, 614, True),
                (925, 944, True),
                (1316, 1319, True),
                (1580, 1580, True),
                (1863, 1884, True),
            ]
        case "3162409":
            return [
                (94, 94, True),
                (290, 337, True),
                (485, 485, True),
                (687, 706, True),
                (872, 875, True),
                (1133, 1133, True),
                (1349, 1350, True),
            ]
        case "3162445":
            return [
                (104, 118, True),
                (329, 347, True),
                (578, 578, True),
                (808, 827, True),
                (1013, 1014, True),
                (1193, 1197, True),
                (1454, 1465, True),
            ]
        case "3182384":
            return [
                (115, 129, True),
                (273, 293, True),
                (469, 476, True),
                (641, 659, True),
                (809, 826, True),
                (1032, 1035, True),
                (1334, 1338, True),
            ]
        case "3353798":
            return [
                (178, 196, True),
                (369, 382, True),
                (525, 528, True),
                (758, 777, True),
                (968, 969, True),
                (1194, 1196, True),
                (1402, 1404, True),
            ]
        case "3359319":
            return [
                (117, 119, True),
                (349, 367, True),
                (568, 580, True),
                (872, 877, True),
                (1154, 1166, True),
                (1481, 1499, True),
                (1811, 1814, True),
            ]
        case "3400260":
            return [
                (164, 184, True),
                (412, 422, True),
                (608, 608, True),
                (822, 827, True),
                (1074, 1095, True),
                (1305, 1321, True),
                (1570, 1572, True),
            ]
        case "3444750":
            return [
                (172, 186, True),
                (337, 355, True),
                (514, 531, True),
                (704, 710, True),
                (985, 986, True),
                (1254, 1270, True),
                (1595, 1595, True),
            ]
        case "3453422":
            return [
                (173, 183, True),
                (439, 441, True),
                (683, 701, True),
                (989, 1008, True),
                (1191, 1196, True),
                (1418, 1443, True),
                (1641, 1661, True),
            ]
        case "3498597":
            return [
                (155, 161, True),
                (374, 374, True),
                (653, 654, True),
                (896, 900, True),
                (1115, 1131, True),
                (1364, 1364, True),
                (1636, 1641, True),
            ]
        case "3501030":
            return [
                (147, 168, True),
                (534, 543, True),
                (866, 867, True),
                (1131, 1203, True),
                (1511, 1511, True),
                (1847, 1867, True),
                (2312, 2316, True),
            ]
        case "3694284":
            return [
                (146, 153, True),
                (379, 379, True),
                (629, 629, True),
                (855, 861, True),
                (1081, 1112, True),
                (1374, 1375, True),
                (1678, 1680, True),
            ]
        case "3698730":
            return [
                (165, 180, True),
                (411, 422, True),
                (672, 675, True),
                (903, 905, True),
                (1074, 1076, True),
                (1389, 1410, True),
                (1631, 1632, True),
            ]
        case "3734528":
            return [
                (152, 152, True),
                (404, 404, True),
                (626, 634, True),
                (830, 832, True),
                (1026, 1028, True),
                (1240, 1260, True),
                (1542, 1546, True),
            ]
        case "3923467":
            return [
                (214, 227, True),
                (471, 476, True),
                (717, 731, True),
                (942, 963, True),
                (1172, 1172, True),
                (1343, 1356, True),
                (1583, 1583, True),
            ]
        case "3998929":
            return [
                (167, 167, True),
                (447, 447, True),
                (693, 696, True),
                (1006, 1017, True),
                (1303, 1303, True),
                (1577, 1595, True),
                (1860, 1860, True),
            ]
        case "4092529":
            return [
                (82, 104, True),
                (269, 269, True),
                (464, 464, True),
                (639, 664, True),
                (794, 794, True),
                (920, 944, True),
                (1199, 1199, True),
            ]
        case "4277121":
            return [
                (159, 169, True),
                (346, 365, True),
                (547, 549, True),
                (659, 660, True),
                (820, 842, True),
                (940, 963, True),
                (1090, 1115, True),
            ]
        case "4287409":
            return [
                (91, 107, True),
                (239, 257, True),
                (387, 390, True),
                (531, 535, True),
                (663, 680, True),
                (794, 998, True),
                (998, 998, True),
            ]
        case "4492560":
            return [
                (41, 61, True),
                (140, 160, True),
                (306, 484, True),
                (465, 591, True),
                (581, 690, True),
                (690, 829, True),
                (829, 829, True),
            ]
        case "4791482":
            return [
                (37, 58, True),
                (191, 198, True),
                (352, 352, True),
                (553, 574, True),
                (695, 700, True),
                (827, 827, True),
                (979, 999, True),
            ]
        case "4802447":
            return [
                (46, 70, True),
                (221, 225, True),
                (389, 389, True),
                (570, 594, True),
                (763, 781, True),
                (933, 944, True),
                (1127, 1142, True),
            ]
        case "4954796":
            return [
                (82, 103, True),
                (275, 275, True),
                (425, 450, True),
                (608, 628, True),
                (764, 782, True),
                (938, 939, True),
                (1102, 1119, True),
            ]
        case "4972640":
            return [
                (140, 160, True),
                (376, 377, True),
                (597, 613, True),
                (890, 908, True),
                (1083, 1083, True),
                (1271, 1274, True),
                (1498, 1498, True),
            ]
        case "4985010":
            return [
                (145, 163, True),
                (382, 384, True),
                (601, 602, True),
                (783, 784, True),
                (997, 997, True),
                (1244, 1244, True),
                (1472, 1478, True),
            ]
        case "5011877":
            return [
                (115, 130, True),
                (348, 349, True),
                (584, 605, True),
                (735, 736, True),
                (998, 998, True),
                (1154, 1155, True),
                (1303, 1303, True),
            ]
        case "5078016":
            return [
                (160, 173, True),
                (488, 488, True),
                (787, 788, True),
                (1040, 1057, True),
                (1319, 1319, True),
                (1553, 1571, True),
                (1840, 1844, True),
            ]
        case "5176472":
            return [
                (80, 94, True),
                (325, 341, True),
                (496, 501, True),
                (848, 1067, True),
                (1064, 1280, True),
                (1280, 1506, True),
                (1479, 1506, True),
            ]
        case "5333169":
            return [
                (160, 175, True),
                (651, 653, True),
                (843, 859, True),
                (1059, 1077, True),
                (1353, 1374, True),
                (1703, 1705, True),
                (2048, 2048, True),
            ]
        case "5586158":
            return [
                (101, 105, True),
                (221, 225, True),
                (389, 390, True),
                (584, 584, True),
                (767, 987, True),
                (973, 1193, True),
                (1193, 1193, True),
            ]
        case "5634681":
            return [
                (254, 254, True),
                (660, 660, True),
                (972, 988, True),
                (1308, 1316, True),
                (1679, 1682, True),
                (2038, 2041, True),
                (2417, 2435, True),
            ]
        case "5928616":
            return [
                (217, 231, True),
                (506, 508, True),
                (846, 865, True),
                (1160, 1162, True),
                (1424, 1424, True),
                (1750, 1772, True),
                (2144, 2145, True),
            ]
        case "5940973":
            return [
                (189, 204, True),
                (452, 452, True),
                (707, 707, True),
                (959, 959, True),
                (1301, 1306, True),
                (1548, 1551, True),
                (1894, 1912, True),
            ]
        case "5964768":
            return [
                (160, 169, True),
                (361, 594, True),
                (593, 852, True),
                (852, 1052, True),
                (1040, 1268, True),
                (1268, 1467, True),
                (1464, 1467, True),
            ]
        case "6070127":
            return [
                (100, 105, True),
                (348, 355, True),
                (554, 554, True),
                (749, 751, True),
                (1005, 1026, True),
                (1251, 1272, True),
                (1565, 1565, True),
            ]
        case "6164168":
            return [
                (125, 126, True),
                (287, 306, True),
                (470, 470, True),
                (668, 670, True),
                (849, 854, True),
                (1025, 1029, True),
                (1289, 1289, True),
            ]
        case "6236652":
            return [
                (118, 119, True),
                (297, 300, True),
                (515, 515, True),
                (719, 720, True),
                (869, 871, True),
                (1108, 1121, True),
                (1337, 1357, True),
            ]
        case "6344229":
            return [
                (135, 138, True),
                (354, 372, True),
                (587, 589, True),
                (760, 760, True),
                (1013, 1031, True),
                (1225, 1244, True),
                (1523, 1523, True),
            ]
        case "6410925":
            return [
                (138, 141, True),
                (371, 377, True),
                (592, 625, True),
                (842, 842, True),
                (1106, 1106, True),
                (1368, 1389, True),
                (1643, 1657, True),
            ]
        case "6782460":
            return [
                (197, 198, True),
                (425, 428, True),
                (629, 630, True),
                (887, 906, True),
                (1136, 1136, True),
                (1396, 1397, True),
                (1690, 1690, True),
            ]
        case "6785052":
            return [
                (158, 158, True),
                (417, 418, True),
                (682, 694, True),
                (940, 962, True),
                (1196, 1423, True),
                (1404, 1686, True),
                (1624, 1686, True),
            ]
        case "6867993":
            return [
                (191, 191, True),
                (444, 446, True),
                (682, 958, True),
                (958, 1219, True),
                (1215, 1468, True),
                (1463, 1712, True),
                (1710, 1712, True),
            ]
        case "6898459":
            return [
                (149, 150, True),
                (373, 377, True),
                (632, 632, True),
                (866, 870, True),
                (1138, 1138, True),
                (1409, 1426, True),
                (1709, 1709, True),
            ]
        case "6979222":
            return [
                (170, 170, True),
                (401, 401, True),
                (648, 649, True),
                (902, 902, True),
                (1200, 1216, True),
                (1346, 1374, True),
                (1495, 1524, True),
            ]
        case "7025864":
            return [
                (144, 148, True),
                (362, 583, True),
                (562, 769, True),
                (747, 972, True),
                (970, 1217, True),
                (1217, 1439, True),
                (1439, 1439, True),
            ]
        case "7207217":
            return [
                (208, 210, True),
                (461, 485, True),
                (725, 728, True),
                (952, 952, True),
                (1176, 1202, True),
                (1379, 1379, True),
                (1660, 1660, True),
            ]
        case "7426907":
            return [
                (178, 180, True),
                (385, 402, True),
                (602, 621, True),
                (852, 854, True),
                (1139, 1139, True),
                (1457, 1457, True),
                (1758, 1763, True),
            ]
        case "7525684":
            return [
                (170, 170, True),
                (384, 402, True),
                (586, 604, True),
                (803, 820, True),
                (1067, 1310, True),
                (1308, 1560, True),
                (1560, 1560, True),
            ]
        case "7577844":
            return [
                (196, 213, True),
                (467, 487, True),
                (735, 896, True),
                (894, 1132, True),
                (1129, 1361, True),
                (1361, 1549, True),
                (1549, 1549, True),
            ]
        case "7711828":
            return [
                (166, 182, True),
                (317, 317, True),
                (540, 561, True),
                (693, 698, True),
                (930, 930, True),
                (1146, 1170, True),
                (1428, 1430, True),
            ]
        case "7772558":
            return [
                (194, 194, True),
                (368, 525, True),
                (524, 757, True),
                (740, 939, True),
                (920, 1111, True),
                (1089, 1358, True),
                (1358, 1358, True),
            ]
        case "7861768":
            return [
                (134, 134, True),
                (290, 311, True),
                (545, 553, True),
                (811, 817, True),
                (1059, 1061, True),
                (1331, 1333, True),
                (1629, 1634, True),
            ]
        case "7948306":
            return [
                (95, 110, True),
                (320, 322, True),
                (587, 587, True),
                (787, 789, True),
                (1062, 1080, True),
                (1325, 1325, True),
                (1582, 1588, True),
            ]
        case "7989121":
            return [
                (168, 183, True),
                (541, 541, True),
                (740, 754, True),
                (1026, 1026, True),
                (1292, 1308, True),
                (1525, 1543, True),
                (1748, 1753, True),
            ]
        case "9074169":
            return [
                (170, 172, True),
                (377, 380, True),
                (543, 549, True),
                (698, 699, True),
                (897, 919, True),
                (1408, 1410, True),
                (1706, 1708, True),
            ]
        case "9298124":
            return [
                (164, 166, True),
                (371, 391, True),
                (624, 624, True),
                (820, 822, True),
                (1026, 1066, True),
                (1241, 1260, True),
                (1595, 1615, True),
            ]
        case "9454007":
            return [
                (197, 430, True),
                (417, 618, True),
                (606, 816, True),
                (803, 1086, True),
                (1083, 1280, True),
                (1280, 1571, True),
                (1568, 1571, True),
            ]
        case "9471550":
            return [
                (167, 167, True),
                (465, 469, True),
                (744, 744, True),
                (965, 990, True),
                (1198, 1200, True),
                (1395, 1415, True),
                (1683, 1686, True),
            ]
        case "9895929":
            return [
                (281, 284, True),
                (477, 478, True),
                (689, 691, True),
                (962, 962, True),
                (1205, 1207, True),
                (1484, 1489, True),
                (1802, 1802, True),
            ]

    return []