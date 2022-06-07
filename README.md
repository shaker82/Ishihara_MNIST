# Run the notebook

We performed the experiments on Ubuntu with Python3.9.

## Installation of necessary software for ubuntu

If you don't have curl and svn, please install it with the following commands:

```
sudo apt update
sudo apt upgrade
sudo apt install curl
sudo apt-get install subversion
```

## Downloading relevant 3rd party files

To download the necessary 3rd party files, either run the following commands:

```
curl -o ishiharaMC.py https://github.com/icfaust/IshiharaMC/blob/master/ishiharaMC.py
curl -o PngToSvg.py https://raw.githubusercontent.com/gkiril/PNGToSVG/master/PngToSvg.py
svn export https://github.com/joergdietrich/daltonize/trunk/daltonize

```

or download the following files/folders from the repos into the main folder:
* the python file `ishiharaMC.py` from https://raw.githubusercontent.com/gkiril/IshiharaMC/master/ishiharaMC.py 
* the python file `PngToSvg.py` from https://raw.githubusercontent.com/gkiril/PNGToSVG/master/PngToSvg.py
* the folder `daltonize` from: https://github.com/joergdietrich/daltonize/ 

## Installing virtual environment and python dependencies

First, create a clean virtual environment, activate it and uprade your `pip`. To do these steps, run the following commands:

```
python3.9 -m venv venv
. venv/bin/activate
pip install --upgrade pip
```

Next, install the required dependencies with:

```
pip install -r requirements.txt
```

### Generating images

In this section, we explain how to generate the images which is time consuming. If you want to skip this step, please download the images from [here](https://drive.google.com/file/d/10Txr56P3rPVGUpDXU--0snBpaznMbgqu/view), unzip the file and place the unzipped `PFiles` folder in `output_dir`.

To get the MNIST data, produce SVG files and pcikle files, merge them for efficiency and convert them to Ishihara plates, run the following command:

```
python IshiharaCovert.py --data_path Data/MNIST --out_path output_dir
```

To generate plate 1 from the Ishihara's test, run the following command:
```
python IshiharaCreateDS.py --data_path output_dir/PFiles --out_path output_dir/PFiles --plate 1 --manipulation 1 --simulate_color_blindness 1
```

For detailed description of the plates, types of manipulation and simulation of color blindness, see the arguments provided in `IshiharaCreateDS.py` in variables `Manipulation_dic` and `Plates`.

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

## Running the notebook

Before firing up the jupyter notebook, install the jupyter kernel for the virtual environment:

```
ipython kernel install --user --name=venv
```

Then, in your jupyter notebook, choose kernel from the virtual environment `venv` (where all dependencies for this notebook are installed). 

# Ishihara-Like-MNIST
python IshiharaCovert.py --data_path Data\MNIST --out_path Output       

python IshiharaCreateDS.py --data_path Output --out_path Output --plate 1 --manipulation 1 --simulate_color_blindness 1

Download:
https://drive.google.com/file/d/10Txr56P3rPVGUpDXU--0snBpaznMbgqu/view?usp=sharing

https://www.dropbox.com/s/gisaz5tcxqto67n/PFiles.zip?dl=0

https://1drv.ms/u/s!AiTLM7pF2hY5alCp5lJ5Or3tYt8?e=OpJxGr

md5sum: 84261bec1bdc960296130bee61700a53

sha1sum: 9c203453edb4f2f82010f4fe7a097b60020e3e3b

sha256sum: 33d695997d6f0a470fd33d697c183d6f076a5d2a592cd52e8ef5a6873aab1c9d

sha512sum: b385b41c7e2433b0af3b07bf66dd1016920d7ae7e8c9883f77d285713c85a67e585f749dab89fb85094f48a33139ef624bcd4040241c22b51061db61c07125fc
"# Ishihara_MNIST" 
