# dataset settings
dataset_type = 'CocoDataset'
data_root = '/content/drive/MyDrive/ELG4960_Out/2/'
img_norm_cfg = dict(
    mean=[127.0], std=[128.0], to_rgb=False)
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
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        ann_file=data_root + 'train/annotations.json',
        img_prefix=data_root + 'train/',
        pipeline=train_pipeline,
        classes = ('defect',)),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'valid/annotations.json',
        img_prefix=data_root + 'valid/',
        pipeline=test_pipeline,
        classes = ('defect',)),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'test/annotations.json',
        img_prefix=data_root + 'test/',
        pipeline=test_pipeline,
        classes = ('defect',)))
evaluation = dict(interval=10, metric='mAP')
