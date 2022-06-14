# Ishihara-like MNIST

This is the repository that provides the code to reproduce the results of the
corresponding paper. The code converts MNIST digit images into Ishihara coloblind test
images. Additionally to the base files, this code includes a Jupyter notebook that shows
how to use the code.

## Installation

Note that we used Python 3.9 for the experiments.

1. Clone this repository;
2. In the folder of the repository (e.g., `ishihara-like-mnist`), initialize the git
   submodules by
   ```bash
   git submodule init
   git submodule update
   ```
3. Install the python requirements via `pip install -r requirements.txt`

## Generating images

In this section, we explain how to generate the images which is time consuming. If you
want to skip this step, please download the images
from [here](https://drive.google.com/file/d/10Txr56P3rPVGUpDXU--0snBpaznMbgqu/view),
unzip the file and place the unzipped `PFiles` folder in `output_dir`.

To get the MNIST data, produce SVG files and pcikle files, merge them for efficiency and
convert them to Ishihara plates, run the following command:

```
python IshiharaCovert.py --data_path Data/MNIST --out_path output_dir
```

To generate plate 1 from the Ishihara's test, run the following command:

```
python IshiharaCreateDS.py --data_path output_dir/PFiles --out_path output_dir/PFiles --plate 1 --manipulation 1 --simulate_color_blindness 1
```

For detailed description of the plates, types of manipulation and simulation of color
blindness, see the arguments provided in `IshiharaCreateDS.py` in
variables `Manipulation_dic` and `Plates`.

* Manipulation options:
    * `No_Manipulation`
    * `upper_half`
    * `right_half`
    * `above_line`
    * `random15`
    * `chess_board`
    * `chess2_board`

* Plates:
    * `Plate_1`
    * `Plate_2`
    * `Plate_3`
    * `Plate_4`
    * `Plate_5`
    * `Plate_6`
    * `Plate_7`
    * `Plate_8`
    * `Plate_9`
    * `Plate_10`
    * `Plate_11`
    * `Plate_12`
    * `Plate_13`
    * `Plate_16`
    * `Plate_17`
    * `Only_Circles`
    * `Only_Dots`
    * `Dots_10_disconnected`
    * `Dots_10_connected`
    * `Random_plates`
    * `Random_colors`

## A sample of different plate coloring

![](All_part_plates.png)

## Ishihara MNIST Data Files

**Circled MNIST:**
```
File: PFiles.tar.gz
URL1: https://1drv.ms/u/s!AiTLM7pF2hY5cP4Fcg9dmXw1fxs?e=TTzIB0
URL2: https://www.dropbox.com/s/ffzi3txg95t6zb1/PFiles.tar.gz?dl=0
Sha256sum: cd26eae1e39ab124f0a489ec3b53f2fef3d74906d31e4a1f082f70c8a4c6aadd
Size: 699MB
Description: This file contains a compressed version of the circled MNIST.

PFiles.
└─ Train_images.
|   | 0.pickle.
|   | 1.pickle.
|   | ...
└─ Test_images.
|   | 0.pickle.
|   | 1.pickle.
|   | ...

Each file Train_images\x.pickle contains the circled versions of all training images of the digit x compressed using the pickle format. The compressed files for the testing images can be found in the folder "Test_images".
Each of these files contains a dictionary that for each MNIST image xxx.jpg contains a key xxx.p for the circular version of that image.
Creation: To re-produce this data, circled MNIST, see the usage of the script IshiharaConvert.py. E.g.,:
python IshiharaConvert.py --data_path Data/MNIST --out_path Output
Usage: This data can be used further to create the colored plates; see the script IshiharaCreateDS.py. E.g., creating the plate "only circles":
python IshiharaCreateDS.py --data_path Output/PFiles --out_path Output --plate 20 --manipulation 1

```



**Only Circles:**
```
File: Only_Circles.tar.gz
URL: https://drive.google.com/file/d/1HCGXeLbfc7_CFLn5AwEdk0SEAOYurnWI
Sha256sum: e889ee771db307cf195e2d7cf7c0541c8ae933f85508e544615e0b0b4e709db8
Size: 1199MB
Description:This file contains images of the only circles plate compressed in two pickle files.

Only_Circles.
└─ Train_images.
|   | Train_images.pickle.
└─ Test_images.
|   | Test_images.pickle.

The file Train_images\Train_images.pickle contains files_dic which is a dictionary of dictionaries, i.e., a dictionary for each digit. For example, for the training file "5244.jpg" (digit 0), the key, "5244.jpg", is invoked as in files_dic['0']["5244.jpg"]. The value is a pytorch tensor of shape torch.Size([3, 112, 112]). The same applies to the testing file  Test_images\Test_images.pickle
Creation: To re-produce this data, only circles, see the script IshiharaCreateDS.py.
python IshiharaCreateDS.py --data_path Output/PFiles --out_path Output --plate 20 --manipulation 1
Usage: This data can be used directly for training and testing using the enclosed tensors. It could also be used to extract the images of the plate; see the script export_import_images.py.
```

**Only Dots:**
```
File: Only_Dots.tar.gz
URL: https://drive.google.com/file/d/1uVqpOyOQF8H1q7_nYC5fMvgqo0CR5wYs
Sha256sum: c46ecc9f75b3c5dadaca4aa043c7a325cc09f18ba78733ece79f79af8e5ee274
Size: 468MB
Description:This file contains images of the only dots plate compressed in two pickle files.

Only_Dots.
└─ Train_images.
|   | Train_images.pickle.
└─ Test_images.
|   | Test_images.pickle.

The file Train_images\Train_images.pickle contains files_dic which is a dictionary of dictionaries, i.e., a dictionary for each digit. For example, for the training file "5244.jpg" (digit 0), the key, "5244.jpg", is invoked as in files_dic['0']["5244.jpg"]. The value is a pytorch tensor of shape torch.Size([3, 112, 112]). The same applies to the testing file  Test_images\Test_images.pickle
Creation: To re-produce this data, only dots, see the script IshiharaCreateDS.py.
python IshiharaCreateDS.py --data_path Output/PFiles --out_path Output --plate 21 --manipulation 1
Usage: This data can be used directly for training and testing using the enclosed tensors. It could also be used to extract the images of the plate; see the script export_import_images.py.
```

**Plate 1:**
```
File: Plate_1.tar.gz
URL: https://drive.google.com/file/d/1UnNgYk8JQQadSrpiqnhqocXJXROzcirt
Sha256sum: 6f2cec0e8e64d3c1fe41ade33cfde3b1185f81abc4f1c39c297eb03c95d89f9a
Size: 2178MB
Description:This file contains images of plate 1 compressed in two pickle files.

Plate_1.
└─ Train_images.
|   | Train_images.pickle.
└─ Test_images.
|   | Test_images.pickle.

The file Train_images\Train_images.pickle contains files_dic which is a dictionary of dictionaries, i.e., a dictionary for each digit. For example, for the training file "5244.jpg" (digit 0), the key, "5244.jpg", is invoked as in files_dic['0']["5244.jpg"]. The value is a pytorch tensor of shape torch.Size([3, 112, 112]). The same applies to the testing file  Test_images\Test_images.pickle
Creation: To re-produce this data, plate 1, see the script IshiharaCreateDS.py.
python IshiharaCreateDS.py --data_path Output/PFiles --out_path Output --plate 1 --manipulation 1
Usage: This data can be used directly for training and testing using the enclosed tensors. It could also be used to extract the images of the plate; see the script export_import_images.py.
```

**Random Colors:**
```
File: Random_colors.tar.gz
URL: https://drive.google.com/file/d/1GuNDKfsW6qNvkM06KHzRNzMMrvpxkhM6
Sha256sum: 98e707fe78a6402da7ca6f1c91412b9eac2b8fb9403e89b80b15fa34e430f6c9
Size: 3101MB
Description:This file contains images of the random colors plate compressed in two pickle files.

Random_colors.
└─ Train_images.
|   | Train_images.pickle.
└─ Test_images.
|   | Test_images.pickle.

The file Train_images\Train_images.pickle contains files_dic which is a dictionary of dictionaries, i.e., a dictionary for each digit. For example, for the training file "5244.jpg" (digit 0), the key, "5244.jpg", is invoked as in files_dic['0']["5244.jpg"]. The value is a pytorch tensor of shape torch.Size([3, 112, 112]). The same applies to the testing file  Test_images\Test_images.pickle
Creation: To re-produce this data, random colors, see the script IshiharaCreateDS.py.
python IshiharaCreateDS.py --data_path Output/PFiles --out_path Output --plate 31 --manipulation 1
Usage: This data can be used directly for training and testing using the enclosed tensors. It could also be used to extract the images of the plate; see the script export_import_images.py.
```


**Plate 1 above line:**
```
File: Plate_1_above_line.tar.gz
URL: https://drive.google.com/file/d/1IdNFILSDXofBHR7-v3YN_TCA_AgzCJm2
Sha256sum: b266827b246a085411304657f16e1961a133d0b3a6820e0e60f87450f60076d7
Size: 2669MB
Description:This file contains images of plate 1 changed with the uncolored manipulation function above_line compressed in two pickle files.

Plate_1_above_line.
└─ Train_images.
|   | Train_images.pickle.
└─ Test_images.
|   | Test_images.pickle.

The file Train_images\Train_images.pickle contains files_dic which is a dictionary of dictionaries, i.e., a dictionary for each digit. For example, for the training file "5244.jpg" (digit 0), the key, "5244.jpg", is invoked as in files_dic['0']["5244.jpg"]. The value is a pytorch tensor of shape torch.Size([3, 112, 112]). The same applies to the testing file  Test_images\Test_images.pickle
Creation: To re-produce this data, plate_1_above_line, see the script IshiharaCreateDS.py.
python IshiharaCreateDS.py --data_path Output/PFiles --out_path Output --plate 1 --manipulation 4
Usage: This data can be used directly for training and testing using the enclosed tensors. It could also be used to extract the images of the plate; see the script export_import_images.py.
```

**Plate 4 chess board:**
```
File: Plate_4_chess_board.tar.gz
URL: https://drive.google.com/file/d/1D86ghvI5XMtnXwiWugPHpq2cp2UUTW9b
Sha256sum: 168c601205b2f5df687b488a03f27894cb0bd5c0ee661c3ec155bad4068fac94
Size: 2929MB
Description:This file contains images of plate 4 changed with the uncolored manipulation function chess_board compressed in two pickle files.

Plate_4_chess_board.
└─ Train_images.
|   | Train_images.pickle.
└─ Test_images.
|   | Test_images.pickle.

The file Train_images\Train_images.pickle contains files_dic which is a dictionary of dictionaries, i.e., a dictionary for each digit. For example, for the training file "5244.jpg" (digit 0), the key, "5244.jpg", is invoked as in files_dic['0']["5244.jpg"]. The value is a pytorch tensor of shape torch.Size([3, 112, 112]). The same applies to the testing file  Test_images\Test_images.pickle
Creation: To re-produce this data, plate_4_chess_board, see the script IshiharaCreateDS.py.
python IshiharaCreateDS.py --data_path Output/PFiles --out_path Output --plate 4 --manipulation 6
Usage: This data can be used directly for training and testing using the enclosed tensors. It could also be used to extract the images of the plate; see the script export_import_images.py.
```

**Plate 8 Sim p:**
```
File: Plate_8_Sim_p.tar.gz
URL: https://drive.google.com/file/d/1A8Xgvye4hdvbBbhX81-LJpwhJEGBCN1c
Sha256sum: a361eac0829262dde6870fab96d74ffd030f7386a8b3b311d6565785edecf3c9
Size: 2700MB
Description:This file contains images ofplate 8 changed with the colored manipulation function simulate_protanopia compressed in two pickle files.

Plate_8_Sim_p.
└─ Train_images.
|   | Train_images.pickle.
└─ Test_images.
|   | Test_images.pickle.

The file Train_images\Train_images.pickle contains files_dic which is a dictionary of dictionaries, i.e., a dictionary for each digit. For example, for the training file "5244.jpg" (digit 0), the key, "5244.jpg", is invoked as in files_dic['0']["5244.jpg"]. The value is a pytorch tensor of shape torch.Size([3, 112, 112]). The same applies to the testing file  Test_images\Test_images.pickle
Creation: To re-produce this data, plate_8_Sim_p, see the script IshiharaCreateDS.py.
python IshiharaCreateSimDal.py --data_path Output/PFiles --input_plate_path Output/Plate_8 --output_plate_path Output --simulate_color_blindness 5
Usage: This data can be used directly for training and testing using the enclosed tensors. It could also be used to extract the images of the plate; see the script export_import_images.py.
```

## Contribution

You are more to welcome to contribute to the code development! In this case, make sure
you have installed pre-commit (`pip install pre-commit`) and that all checks are passed
before committing. Additionally, we use **[black](https://github.com/psf/black)** code
formatting with 88 character limit.
