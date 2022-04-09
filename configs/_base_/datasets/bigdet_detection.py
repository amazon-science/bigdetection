# BigDetection dataset settings
dataset_type = 'CocoDataset'
data_root = 'data/BigDetection/'
classes = ('accordion', 'air_conditioner', 'airplane', 'alarm_clock', 'alligator', 'alpaca', 'ambulance', 'ant', 'apple', 'armadillo', 'army_tank', 'artichoke',
           'asparagus', 'automatic_washer', 'avocado', 'award', 'awning', 'ax', 'baby_buggy', 'backpack', 'bagel', 'balance_beam', 'ball', 'balloon', 'banana',
           'band_aid', 'banjo', 'baozi', 'barbell', 'barge', 'barrel', 'baseball', 'baseball_bat', 'baseball_glove', 'basket', 'basketball', 'bass_horn',
           'bat_(animal)', 'bathtub', 'bear', 'bed', 'bee', 'beehive', 'beer_bottle', 'bell_pepper', 'belt', 'bench', 'bicycle', 'billboard', 'binder', 'binoculars',
           'bird', 'blackboard', 'blender', 'board_eraser', 'boat', 'book', 'bookcase', 'boot', 'bottle', 'bottle_opener', 'bow-tie', 'bow_(weapon)', 'bowl',
           'bowling_ball', 'box', 'bracelet', 'brassiere', 'bread', 'briefcase', 'broccoli', 'broom', 'building', 'bulldozer', 'bullhorn', 'burrito', 'bus_(vehicle)',
           'butterfly', 'cabbage', 'cabinet', 'cake', 'cake_stand', 'calculator', 'camel', 'camera', 'can', 'can_opener', 'canary', 'candle', 'candy_bar', 'cannon',
           'canoe', 'cantaloup', 'car_(automobile)', 'card', 'cargo_ship', 'carrot', 'cart', 'cassette_deck', 'castle', 'cat', 'cat_furniture', 'caterpillar', 'cd',
           'cello', 'cellular_telephone', 'centipede', 'chair', 'cherry', 'chicken_(animal)', 'chisel', 'chopping_board', 'chopstick', 'christmas_tree', 'cigarette',
           'clarinet', 'cleansing_agent', 'clock', 'clutch_bag', 'coat', 'coat_hanger', 'cocktail', 'coconut', 'coffee_maker', 'coffee_table', 'coin', 'computer_box',
           'computer_keyboard', 'computer_monitor', 'cone', 'converter', 'cooker', 'cookie', 'cooking_utensil', 'cosmetics', 'cow', 'cowboy_hat', 'crab_(animal)',
           'crane', 'crisp_(potato_chip)', 'crow', 'crown', 'crutch', 'cucumber', 'cue', 'cup', 'cupboard', 'curling', 'curtain', 'cymbal', 'dagger', 'dartboard',
           'deer', 'desk', 'dessert', 'diaper', 'dice', 'digital_clock', 'dinosaur', 'dishwasher', 'dispenser', 'dog', 'dog_bed', 'doll', 'dolphin', 'door', 'doorknob',
           'doughnut', 'dragonfly', 'drawer', 'dress', 'drill', 'drum_(musical_instrument)', 'duck', 'duffel_bag', 'dumbbell', 'dumpling', 'durian', 'eagle',
           'earphone', 'earring', 'edible_corn', 'egg', 'egg_roll', 'egg_tart', 'eggbeater', 'eggplant', 'elephant', 'envelope', 'eraser', 'fan', 'faucet', 'fax',
           'ferret', 'ferris_wheel', 'fig_(fruit)', 'file_cabinet', 'fire_engine', 'fire_extinguisher', 'fireplace', 'fireplug', 'fish', 'fishing_rod', 'flag',
           'flashlight', 'flower_arrangement', 'flowerpot', 'flute', 'food_processor', 'football_(American)', 'football_helmet', 'fork', 'fountain', 'fox',
           'french_fries', 'frisbee', 'frog', 'fruit', 'fruit_juice', 'frying_pan', 'fume_hood', 'gameboard', 'garlic', 'gazelle', 'giant_panda', 'giraffe',
           'glass_(drink_container)', 'globe', 'glove', 'goat', 'goggles', 'goldfish', 'golf_ball', 'golf_club', 'golfcart', 'gondola_(boat)', 'goose', 'gorilla',
           'grape', 'grapefruit', 'green_bean', 'green_onion', 'grinder', 'guacamole', 'guitar', 'gun', 'hair_dryer', 'hairbrush', 'hamburger', 'hammer', 'hamster',
           'hand_dryer', 'handbag', 'handcart', 'handle', 'handsaw', 'harbor_seal', 'harmonica', 'harmonium', 'harp', 'hat', 'headset', 'heater', 'hedgehog',
           'helicopter', 'helmet', 'high_heels', 'hippopotamus', 'hockey_stick', 'hog', 'horizontal_bar', 'horse', 'horse_carriage', 'hose', 'hot-air_balloon',
           'hot_dog', 'house', 'humidifier', 'hurdle', 'iPod', 'icecream', 'igniter', 'indoor_rower', 'infant_bed', 'insect', 'iron_(for_clothing)', 'isopod', 'jacket',
           'jaguar', 'jean', 'jellyfish', 'kangaroo', 'kettle', 'key', 'kitchen_table', 'kite', 'kiwi_fruit', 'knife', 'koala', 'ladder', 'ladle', 'ladybug', 'lamp',
           'lantern', 'laptop_computer', 'lavender', 'leather_shoes', 'lemon', 'lettuce', 'license_plate', 'life_buoy', 'life_jacket', 'light_switch', 'lightbulb',
           'lighthouse', 'lily', 'limousine', 'lion', 'lizard', 'lobster', 'lynx', 'mango', 'maple', 'marker', 'mask', 'measuring_cup', 'measuring_stick', 'meatball',
           'melon', 'microphone', 'microwave_oven', 'milk', 'minivan', 'mirror', 'missile', 'mixer_(kitchen_tool)', 'monkey', 'mop', 'motor_scooter', 'motorcycle',
           'mouse_(computer_equipment)', 'muffin', 'mug', 'mule', 'mushroom', 'musical_instrument', 'nail', 'napkin', 'necklace', 'necktie', 'nightstand', 'noodles',
           'notepad', 'nuts', 'okra', 'olive_oil', 'onion', 'orange_(fruit)', 'ostrich', 'otter', 'oven', 'owl', 'oyster', 'paddle', 'paintbrush', 'painting',
           'palm_tree', 'pancake', 'papaya', 'paper_towel', 'parachute', 'parking_meter', 'parrot', 'pasta', 'pastry', 'peach', 'pear', 'pen', 'pencil_box',
           'pencil_sharpener', 'penguin', 'pepper', 'perfume', 'person', 'piano', 'pickup_truck', 'pie', 'pigeon', 'pillow', 'pineapple', 'ping-pong_ball', 'pistol',
           'pizza', 'pizza_cutter', 'plastic_bag', 'plate', 'pliers', 'plum', 'poker_card', 'polar_bear', 'pomegranate', 'pool_table', 'popcorn', 'porch', 'porcupine',
           'poster', 'pot', 'potato', 'potted_plant', 'pretzel', 'printer', 'projector', 'pumpkin', 'punching_bag', 'rabbit', 'raccoon', 'race_car', 'racket',
           'radio_receiver', 'radish', 'rays_and_skates', 'red_panda', 'refrigerator', 'remote_control', 'rhinoceros', 'rice', 'rickshaw', 'ring', 'roller_skate',
           'rose', 'router_(computer_equipment)', 'runner_(carpet)', 'salad', 'saltshaker', 'sandal_(type_of_shoe)', 'sandwich', 'saucer', 'sausage', 'saxophone',
           'scale_(measuring_instrument)', 'scarf', 'scissors', 'scoreboard', 'scorpion', 'screwdriver', 'scrubbing_brush', 'sculpture', 'seahorse', 'seashell',
           'seat_belt', 'segway', 'sewing_machine', 'shaker', 'shampoo', 'shark', 'shaving_cream', 'sheep', 'shirt', 'shoe', 'short_pants', 'shovel', 'shower_head',
           'shrimp', 'sink', 'skateboard', 'ski', 'skirt', 'skullcap', 'skunk', 'slide', 'slipper_(footwear)', 'snail', 'snake', 'sneakers', 'snowboard', 'snowman',
           'snowmobile', 'snowplow', 'soap', 'soccer_ball', 'sock', 'sofa', 'sofa_bed', 'sombrero', 'space_shuttle', 'sparrow', 'spatula', 'speaker_(stero_equipment)',
           'spectacles', 'spice_rack', 'spider', 'spoon', 'sportswear', 'squid_(food)', 'squirrel', 'stapler_(stapling_machine)', 'starfish', 'stationary_bicycle',
           'steak_(food)', 'stethoscope', 'stool', 'stop_sign', 'stove', 'straw_(for_drinking)', 'strawberry', 'street_sign', 'streetlight', 'stretcher',
           'string_cheese', 'submarine', 'suit_(clothing)', 'suitcase', 'sunflower', 'sunglasses', 'sunhat', 'surfboard', 'surveillance', 'sushi', 'swim_cap',
           'swimming_pool', 'swimsuit', 'swing', 'sword', 'syringe', 'table', 'table_tennis_racket', 'tablet_computer', 'taco', 'tape_(sticky_cloth_or_paper)', 'taxi',
           'teapot', 'teddy_bear', 'telephone', 'television_set', 'tennis_ball', 'tennis_racket', 'tent', 'thermos_bottle', 'tiger', 'tissue_paper', 'toaster',
           'toilet', 'toilet_tissue', 'tomato', 'tongs', 'toothbrush', 'towel', 'tower', 'toy', 'traffic_light', 'trailer_truck', 'train_(railroad_vehicle)',
           'training_bench', 'trash_can', 'tray', 'treadmill', 'tree', 'tree_house', 'tricycle', 'tripod', 'trombone', 'trophy_cup', 'trousers', 'truck', 'trumpet',
           'turkey', 'turtle', 'typewriter', 'umbrella', 'unicycle', 'urinal', 'vacuum_cleaner', 'vase', 'vegetables', 'violin', 'volleyball', 'waffle', 'waffle_iron',
           'wall_socket', 'wardrobe', 'watch', 'water_jug', 'water_scooter', 'watermelon', 'whale', 'wheel', 'wheelchair', 'willow', 'wind_chime', 'windmill', 'window',
           'window_blind', 'wine_rack', 'wineglass', 'wolf', 'worm', 'wrench', 'yak', 'zebra', 'zucchini')


img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1333, 800),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=0,
    class_aware_sampling=True,
    sample_weight_path=data_root + 'annotations/cas_weights.json',
    train=dict(
        type=dataset_type,
        ann_file=[data_root + 'annotations/bigdet_obj_train.json',
                  data_root + 'annotations/bigdet_oid_train.json',
                  data_root + 'annotations/bigdet_lvis_train.json'],
        img_prefix=[data_root + 'train/Objects365/',
                    data_root + 'train/OpenImages/',
                    data_root + 'train/LVIS/'],
        classes=classes,
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/bigdet_val.json', 
        img_prefix=data_root + 'val/', 
        classes=classes,
        pipeline=test_pipeline))
evaluation = dict(interval=1, metric='bbox')
