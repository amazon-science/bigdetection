import mmcv


def wider_face_classes():
    return ['face']


def voc_classes():
    return [
        'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat',
        'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person',
        'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor'
    ]


def imagenet_det_classes():
    return [
        'accordion', 'airplane', 'ant', 'antelope', 'apple', 'armadillo',
        'artichoke', 'axe', 'baby_bed', 'backpack', 'bagel', 'balance_beam',
        'banana', 'band_aid', 'banjo', 'baseball', 'basketball', 'bathing_cap',
        'beaker', 'bear', 'bee', 'bell_pepper', 'bench', 'bicycle', 'binder',
        'bird', 'bookshelf', 'bow_tie', 'bow', 'bowl', 'brassiere', 'burrito',
        'bus', 'butterfly', 'camel', 'can_opener', 'car', 'cart', 'cattle',
        'cello', 'centipede', 'chain_saw', 'chair', 'chime', 'cocktail_shaker',
        'coffee_maker', 'computer_keyboard', 'computer_mouse', 'corkscrew',
        'cream', 'croquet_ball', 'crutch', 'cucumber', 'cup_or_mug', 'diaper',
        'digital_clock', 'dishwasher', 'dog', 'domestic_cat', 'dragonfly',
        'drum', 'dumbbell', 'electric_fan', 'elephant', 'face_powder', 'fig',
        'filing_cabinet', 'flower_pot', 'flute', 'fox', 'french_horn', 'frog',
        'frying_pan', 'giant_panda', 'goldfish', 'golf_ball', 'golfcart',
        'guacamole', 'guitar', 'hair_dryer', 'hair_spray', 'hamburger',
        'hammer', 'hamster', 'harmonica', 'harp', 'hat_with_a_wide_brim',
        'head_cabbage', 'helmet', 'hippopotamus', 'horizontal_bar', 'horse',
        'hotdog', 'iPod', 'isopod', 'jellyfish', 'koala_bear', 'ladle',
        'ladybug', 'lamp', 'laptop', 'lemon', 'lion', 'lipstick', 'lizard',
        'lobster', 'maillot', 'maraca', 'microphone', 'microwave', 'milk_can',
        'miniskirt', 'monkey', 'motorcycle', 'mushroom', 'nail', 'neck_brace',
        'oboe', 'orange', 'otter', 'pencil_box', 'pencil_sharpener', 'perfume',
        'person', 'piano', 'pineapple', 'ping-pong_ball', 'pitcher', 'pizza',
        'plastic_bag', 'plate_rack', 'pomegranate', 'popsicle', 'porcupine',
        'power_drill', 'pretzel', 'printer', 'puck', 'punching_bag', 'purse',
        'rabbit', 'racket', 'ray', 'red_panda', 'refrigerator',
        'remote_control', 'rubber_eraser', 'rugby_ball', 'ruler',
        'salt_or_pepper_shaker', 'saxophone', 'scorpion', 'screwdriver',
        'seal', 'sheep', 'ski', 'skunk', 'snail', 'snake', 'snowmobile',
        'snowplow', 'soap_dispenser', 'soccer_ball', 'sofa', 'spatula',
        'squirrel', 'starfish', 'stethoscope', 'stove', 'strainer',
        'strawberry', 'stretcher', 'sunglasses', 'swimming_trunks', 'swine',
        'syringe', 'table', 'tape_player', 'tennis_ball', 'tick', 'tie',
        'tiger', 'toaster', 'traffic_light', 'train', 'trombone', 'trumpet',
        'turtle', 'tv_or_monitor', 'unicycle', 'vacuum', 'violin',
        'volleyball', 'waffle_iron', 'washer', 'water_bottle', 'watercraft',
        'whale', 'wine_bottle', 'zebra'
    ]


def imagenet_vid_classes():
    return [
        'airplane', 'antelope', 'bear', 'bicycle', 'bird', 'bus', 'car',
        'cattle', 'dog', 'domestic_cat', 'elephant', 'fox', 'giant_panda',
        'hamster', 'horse', 'lion', 'lizard', 'monkey', 'motorcycle', 'rabbit',
        'red_panda', 'sheep', 'snake', 'squirrel', 'tiger', 'train', 'turtle',
        'watercraft', 'whale', 'zebra'
    ]


def coco_classes():
    return [
        'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train',
        'truck', 'boat', 'traffic_light', 'fire_hydrant', 'stop_sign',
        'parking_meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep',
        'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella',
        'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard',
        'sports_ball', 'kite', 'baseball_bat', 'baseball_glove', 'skateboard',
        'surfboard', 'tennis_racket', 'bottle', 'wine_glass', 'cup', 'fork',
        'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange',
        'broccoli', 'carrot', 'hot_dog', 'pizza', 'donut', 'cake', 'chair',
        'couch', 'potted_plant', 'bed', 'dining_table', 'toilet', 'tv',
        'laptop', 'mouse', 'remote', 'keyboard', 'cell_phone', 'microwave',
        'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase',
        'scissors', 'teddy_bear', 'hair_drier', 'toothbrush'
    ]


def cityscapes_classes():
    return [
        'person', 'rider', 'car', 'truck', 'bus', 'train', 'motorcycle',
        'bicycle'
    ]


def bigdetection_classes():
    return [
        'accordion', 'air_conditioner', 'airplane', 'alarm_clock', 'alligator', 'alpaca', 'ambulance', 'ant', 'apple', 'armadillo', 'army_tank',
        'artichoke', 'asparagus', 'automatic_washer', 'avocado', 'award', 'awning', 'ax', 'baby_buggy', 'backpack', 'bagel', 'balance_beam', 'ball',
        'balloon', 'banana', 'band_aid', 'banjo', 'baozi', 'barbell', 'barge', 'barrel', 'baseball', 'baseball_bat', 'baseball_glove', 'basket',
        'basketball', 'bass_horn', 'bat_(animal)', 'bathtub', 'bear', 'bed', 'bee', 'beehive', 'beer_bottle', 'bell_pepper', 'belt', 'bench', 'bicycle',
        'billboard', 'binder', 'binoculars', 'bird', 'blackboard', 'blender', 'board_eraser', 'boat', 'book', 'bookcase', 'boot', 'bottle', 'bottle_opener',
        'bow-tie', 'bow_(weapon)', 'bowl', 'bowling_ball', 'box', 'bracelet', 'brassiere', 'bread', 'briefcase', 'broccoli', 'broom', 'building',
        'bulldozer', 'bullhorn', 'burrito', 'bus_(vehicle)', 'butterfly', 'cabbage', 'cabinet', 'cake', 'cake_stand', 'calculator', 'camel', 'camera',
        'can', 'can_opener', 'canary', 'candle', 'candy_bar', 'cannon', 'canoe', 'cantaloup', 'car_(automobile)', 'card', 'cargo_ship', 'carrot', 'cart',
        'cassette_deck', 'castle', 'cat', 'cat_furniture', 'caterpillar', 'cd', 'cello', 'cellular_telephone', 'centipede', 'chair', 'cherry',
        'chicken_(animal)', 'chisel', 'chopping_board', 'chopstick', 'christmas_tree', 'cigarette', 'clarinet', 'cleansing_agent', 'clock', 'clutch_bag',
        'coat', 'coat_hanger', 'cocktail', 'coconut', 'coffee_maker', 'coffee_table', 'coin', 'computer_box', 'computer_keyboard', 'computer_monitor',
        'cone', 'converter', 'cooker', 'cookie', 'cooking_utensil', 'cosmetics', 'cow', 'cowboy_hat', 'crab_(animal)', 'crane', 'crisp_(potato_chip)',
        'crow', 'crown', 'crutch', 'cucumber', 'cue', 'cup', 'cupboard', 'curling', 'curtain', 'cymbal', 'dagger', 'dartboard', 'deer', 'desk', 'dessert',
        'diaper', 'dice', 'digital_clock', 'dinosaur', 'dishwasher', 'dispenser', 'dog', 'dog_bed', 'doll', 'dolphin', 'door', 'doorknob', 'doughnut',
        'dragonfly', 'drawer', 'dress', 'drill', 'drum_(musical_instrument)', 'duck', 'duffel_bag', 'dumbbell', 'dumpling', 'durian', 'eagle', 'earphone',
        'earring', 'edible_corn', 'egg', 'egg_roll', 'egg_tart', 'eggbeater', 'eggplant', 'elephant', 'envelope', 'eraser', 'fan', 'faucet', 'fax',
        'ferret', 'ferris_wheel', 'fig_(fruit)', 'file_cabinet', 'fire_engine', 'fire_extinguisher', 'fireplace', 'fireplug', 'fish', 'fishing_rod', 'flag',
        'flashlight', 'flower_arrangement', 'flowerpot', 'flute', 'food_processor', 'football_(American)', 'football_helmet', 'fork', 'fountain', 'fox',
        'french_fries', 'frisbee', 'frog', 'fruit', 'fruit_juice', 'frying_pan', 'fume_hood', 'gameboard', 'garlic', 'gazelle', 'giant_panda', 'giraffe',
        'glass_(drink_container)', 'globe', 'glove', 'goat', 'goggles', 'goldfish', 'golf_ball', 'golf_club', 'golfcart', 'gondola_(boat)', 'goose',
        'gorilla', 'grape', 'grapefruit', 'green_bean', 'green_onion', 'grinder', 'guacamole', 'guitar', 'gun', 'hair_dryer', 'hairbrush', 'hamburger',
        'hammer', 'hamster', 'hand_dryer', 'handbag', 'handcart', 'handle', 'handsaw', 'harbor_seal', 'harmonica', 'harmonium', 'harp', 'hat', 'headset',
        'heater', 'hedgehog', 'helicopter', 'helmet', 'high_heels', 'hippopotamus', 'hockey_stick', 'hog', 'horizontal_bar', 'horse', 'horse_carriage',
        'hose', 'hot-air_balloon', 'hot_dog', 'house', 'humidifier', 'hurdle', 'iPod', 'icecream', 'igniter', 'indoor_rower', 'infant_bed', 'insect',
        'iron_(for_clothing)', 'isopod', 'jacket', 'jaguar', 'jean', 'jellyfish', 'kangaroo', 'kettle', 'key', 'kitchen_table', 'kite', 'kiwi_fruit',
        'knife', 'koala', 'ladder', 'ladle', 'ladybug', 'lamp', 'lantern', 'laptop_computer', 'lavender', 'leather_shoes', 'lemon', 'lettuce',
        'license_plate', 'life_buoy', 'life_jacket', 'light_switch', 'lightbulb', 'lighthouse', 'lily', 'limousine', 'lion', 'lizard', 'lobster', 'lynx',
        'mango', 'maple', 'marker', 'mask', 'measuring_cup', 'measuring_stick', 'meatball', 'melon', 'microphone', 'microwave_oven', 'milk', 'minivan',
        'mirror', 'missile', 'mixer_(kitchen_tool)', 'monkey', 'mop', 'motor_scooter', 'motorcycle', 'mouse_(computer_equipment)', 'muffin', 'mug', 'mule',
        'mushroom', 'musical_instrument', 'nail', 'napkin', 'necklace', 'necktie', 'nightstand', 'noodles', 'notepad', 'nuts', 'okra', 'olive_oil', 'onion',
        'orange_(fruit)', 'ostrich', 'otter', 'oven', 'owl', 'oyster', 'paddle', 'paintbrush', 'painting', 'palm_tree', 'pancake', 'papaya', 'paper_towel',
        'parachute', 'parking_meter', 'parrot', 'pasta', 'pastry', 'peach', 'pear', 'pen', 'pencil_box', 'pencil_sharpener', 'penguin', 'pepper', 'perfume',
        'person', 'piano', 'pickup_truck', 'pie', 'pigeon', 'pillow', 'pineapple', 'ping-pong_ball', 'pistol', 'pizza', 'pizza_cutter', 'plastic_bag',
        'plate', 'pliers', 'plum', 'poker_card', 'polar_bear', 'pomegranate', 'pool_table', 'popcorn', 'porch', 'porcupine', 'poster', 'pot', 'potato',
        'potted_plant', 'pretzel', 'printer', 'projector', 'pumpkin', 'punching_bag', 'rabbit', 'raccoon', 'race_car', 'racket', 'radio_receiver', 'radish',
        'rays_and_skates', 'red_panda', 'refrigerator', 'remote_control', 'rhinoceros', 'rice', 'rickshaw', 'ring', 'roller_skate', 'rose',
        'router_(computer_equipment)', 'runner_(carpet)', 'salad', 'saltshaker', 'sandal_(type_of_shoe)', 'sandwich', 'saucer', 'sausage', 'saxophone',
        'scale_(measuring_instrument)', 'scarf', 'scissors', 'scoreboard', 'scorpion', 'screwdriver', 'scrubbing_brush', 'sculpture', 'seahorse',
        'seashell', 'seat_belt', 'segway', 'sewing_machine', 'shaker', 'shampoo', 'shark', 'shaving_cream', 'sheep', 'shirt', 'shoe', 'short_pants',
        'shovel', 'shower_head', 'shrimp', 'sink', 'skateboard', 'ski', 'skirt', 'skullcap', 'skunk', 'slide', 'slipper_(footwear)', 'snail', 'snake',
        'sneakers', 'snowboard', 'snowman', 'snowmobile', 'snowplow', 'soap', 'soccer_ball', 'sock', 'sofa', 'sofa_bed', 'sombrero', 'space_shuttle',
        'sparrow', 'spatula', 'speaker_(stero_equipment)', 'spectacles', 'spice_rack', 'spider', 'spoon', 'sportswear', 'squid_(food)', 'squirrel',
        'stapler_(stapling_machine)', 'starfish', 'stationary_bicycle', 'steak_(food)', 'stethoscope', 'stool', 'stop_sign', 'stove',
        'straw_(for_drinking)', 'strawberry', 'street_sign', 'streetlight', 'stretcher', 'string_cheese', 'submarine', 'suit_(clothing)', 'suitcase',
        'sunflower', 'sunglasses', 'sunhat', 'surfboard', 'surveillance', 'sushi', 'swim_cap', 'swimming_pool', 'swimsuit', 'swing', 'sword', 'syringe',
        'table', 'table_tennis_racket', 'tablet_computer', 'taco', 'tape_(sticky_cloth_or_paper)', 'taxi', 'teapot', 'teddy_bear', 'telephone',
        'television_set', 'tennis_ball', 'tennis_racket', 'tent', 'thermos_bottle', 'tiger', 'tissue_paper', 'toaster', 'toilet', 'toilet_tissue', 'tomato',
        'tongs', 'toothbrush', 'towel', 'tower', 'toy', 'traffic_light', 'trailer_truck', 'train_(railroad_vehicle)', 'training_bench', 'trash_can', 'tray',
        'treadmill', 'tree', 'tree_house', 'tricycle', 'tripod', 'trombone', 'trophy_cup', 'trousers', 'truck', 'trumpet', 'turkey', 'turtle', 'typewriter',
        'umbrella', 'unicycle', 'urinal', 'vacuum_cleaner', 'vase', 'vegetables', 'violin', 'volleyball', 'waffle', 'waffle_iron', 'wall_socket',
        'wardrobe', 'watch', 'water_jug', 'water_scooter', 'watermelon', 'whale', 'wheel', 'wheelchair', 'willow', 'wind_chime', 'windmill', 'window',
        'window_blind', 'wine_rack', 'wineglass', 'wolf', 'worm', 'wrench', 'yak', 'zebra', 'zucchini',
    ]



dataset_aliases = {
    'voc': ['voc', 'pascal_voc', 'voc07', 'voc12'],
    'imagenet_det': ['det', 'imagenet_det', 'ilsvrc_det'],
    'imagenet_vid': ['vid', 'imagenet_vid', 'ilsvrc_vid'],
    'coco': ['coco', 'mscoco', 'ms_coco'],
    'wider_face': ['WIDERFaceDataset', 'wider_face', 'WIDERFace'],
    'cityscapes': ['cityscapes'],
    'bigdetection': ['bigdetection', 'big_detection', 'BigDetection']
}


def get_classes(dataset):
    """Get class names of a dataset."""
    alias2name = {}
    for name, aliases in dataset_aliases.items():
        for alias in aliases:
            alias2name[alias] = name

    if mmcv.is_str(dataset):
        if dataset in alias2name:
            labels = eval(alias2name[dataset] + '_classes()')
        else:
            raise ValueError(f'Unrecognized dataset: {dataset}')
    else:
        raise TypeError(f'dataset must a str, but got {type(dataset)}')
    return labels
