# imglabCocoJsonToCreateMLJsonConvertor
it's just simple python app for convert Coco Json from imglab.in annotations to Apple CreateML JSON format



convert this -->
coco_imglab.json

{"images":[{"file_name":"IMG_2106.JPG","height":2533,"width":2472,"id":1},{"file_name":"IMG_1252.JPG","height":2576,"width":1932,"id":2},{"file_name":"IMG_1949.JPG","height":4032,"width":3024,"id":3},{"file_name":"IMG_1988.JPG","height":4032,"width":3024,"id":4}],"type":"instances","annotations":[{"segmentation":[[1529.9999999999977,1219.9999999999982,1879.9999999999973,1219.9999999999982,1879.9999999999973,1539.9999999999977,1529.9999999999977,1539.9999999999977]],"area":111999.99999999953,"iscrowd":0,"image_id":1,"bbox":[1529.9999999999977,1219.9999999999982,349.9999999999995,319.99999999999955],"category_id":1,"id":1,"ignore":0},{"segmentation":[[739.9999999999998,1082.4999999999995,987.4999999999997,1082.4999999999995,987.4999999999997,1307.4999999999995,739.9999999999998,1307.4999999999995]],"area":55687.5,"iscrowd":0,"image_id":2,"bbox":[739.9999999999998,1082.4999999999995,247.49999999999991,224.99999999999991],"category_id":1,"id":1,"ignore":0},{"segmentation":[[449.99999999999983,9.999999999999996,1222.4999999999995,9.999999999999996,1222.4999999999995,429.99999999999983,449.99999999999983,429.99999999999983]],"area":324449.99999999977,"iscrowd":0,"image_id":2,"bbox":[449.99999999999983,9.999999999999996,772.4999999999998,419.99999999999983],"category_id":2,"id":2,"ignore":0},{"segmentation":[[1349.999999999999,1669.9999999999989,1554.9999999999989,1669.9999999999989,1554.9999999999989,1809.9999999999986,1349.999999999999,1809.9999999999986]],"area":28699.999999999534,"iscrowd":0,"image_id":3,"bbox":[1349.999999999999,1669.9999999999989,204.99999999999986,139.9999999999999],"category_id":1,"id":1,"ignore":0},{"segmentation":[[924.9999999999993,964.9999999999993,1309.999999999999,964.9999999999993,1309.999999999999,1279.999999999999,924.9999999999993,1279.999999999999]],"area":121274.99999999988,"iscrowd":0,"image_id":3,"bbox":[924.9999999999993,964.9999999999993,384.9999999999997,314.9999999999998],"category_id":2,"id":2,"ignore":0},{"segmentation":[[1474.9999999999989,849.9999999999994,1854.9999999999986,849.9999999999994,1854.9999999999986,1209.999999999999,1474.9999999999989,1209.999999999999]],"area":136800,"iscrowd":0,"image_id":3,"bbox":[1474.9999999999989,849.9999999999994,379.9999999999997,359.9999999999998],"category_id":2,"id":3,"ignore":0},{"segmentation":[[959.9999999999986,1869.9999999999973,1979.9999999999973,1869.9999999999973,1979.9999999999973,2619.9999999999964,959.9999999999986,2619.9999999999964]],"area":764999.9999999986,"iscrowd":0,"image_id":4,"bbox":[959.9999999999986,1869.9999999999973,1019.9999999999985,749.999999999999],"category_id":1,"id":1,"ignore":0}],"categories":[{"supercategory":"none","id":1,"name":"piglet"},{"supercategory":"none","id":2,"name":"pampushki"}]}

to this -->
annotations.json

[

	{"image":"IMG_2106.JPG",
		"annotations":
		[

			{"label":"piglet","coordinates":{"x":1530,"y":1220,"width":350,"height":320}}
		]
	},
	{"image":"IMG_1252.JPG",
		"annotations":
		[

			{"label":"piglet","coordinates":{"x":740,"y":1082,"width":247,"height":225}},
			{"label":"pampushki","coordinates":{"x":450,"y":10,"width":772,"height":420}}
		]
	},
	{"image":"IMG_1949.JPG",
		"annotations":
		[

			{"label":"piglet","coordinates":{"x":1350,"y":1670,"width":205,"height":140}},
			{"label":"pampushki","coordinates":{"x":925,"y":965,"width":385,"height":315}},
			{"label":"pampushki","coordinates":{"x":1475,"y":850,"width":380,"height":360}}
		]
	},
	{"image":"IMG_1988.JPG",
		"annotations":
		[

			{"label":"piglet","coordinates":{"x":960,"y":1870,"width":1020,"height":750}}
		]
	}
]
