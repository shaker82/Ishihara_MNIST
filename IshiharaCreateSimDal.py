"""
   Written by Ammar Shaker <ammar.shaker@neclab.eu>. Copyright 2022
   Based on original code by Oliver Siemoneit. Copyright 2007
   And the original code by Joerg Dietrich. Copyright 2015-2020
   This code is licensed under the GNU GPL version 2.

   This Script can be used to transform images of the input plate using one of six
   colored plate manipulators. It offers a simulation and daltonization function for
   each of deuteranopia, protanopia, and tritanopia.
   Examples:
            Simulating deuteranopia on Plate 1:
            ```
            python IshiharaCreateSimDal.py --data_path PFiles --input_plate_path \
                Plate_1_new --output_plate_path Temp --simulate_color_blindness 1
            ```
            Daltonization for protanopia on Plate 1:
            ```
            python IshiharaCreateSimDal.py --data_path PFiles --input_plate_path \
                Plate_1_new --output_plate_path Temp --simulate_color_blindness 5
            ```
"""

import argparse
import os
import pickle
from os import listdir
from os.path import exists
from pathlib import Path
from typing import List

import numpy as np
from daltonize import daltonize
from PIL import Image


def create_sim_colorblind_plates(
    files: List[str],
    Input_plate: str,
    Output_plate: str,
    suffix: str,
    color_blindness: str,
    gamma: float,
) -> None:
    """This function simulate clolorblindness on the images in the input plate using
    the daltonize library."""
    for f in files:
        number = f.split(os.sep)[-1].split(".")[0]
        with open(f, "rb") as file:
            data = pickle.load(file)
            for i, key in enumerate(data.keys()):
                jpg_file = str(
                    Path(Input_plate) / suffix / number / (key.split(".")[0] + ".jpg")
                )
                new_jpg_file = str(
                    Path(Output_plate) / suffix / number / (key.split(".")[0] + ".jpg")
                )
                # print(jpg_file, new_jpg_file)
                if not exists(jpg_file):
                    print("File ", jpg_file, " not found!")
                    continue
                orig_img = np.asarray(
                    Image.open(jpg_file).convert("RGB"), dtype=np.float16
                )
                orig_img = daltonize.gamma_correction(orig_img, gamma)

                simul_rgb = daltonize.simulate(orig_img, color_blindness)
                simul_img = daltonize.array_to_img(simul_rgb, gamma)
                simul_img.save(new_jpg_file)


def create_daltonize_colorblind_plates(
    files: List[str],
    Input_plate: str,
    Output_plate: str,
    suffix: str,
    color_blindness: str,
    gamma: float,
) -> None:
    """This function daltonize the images in the input plate using the daltonize
    library."""
    for f in files:
        number = f.split(os.sep)[-1].split(".")[0]
        with open(f, "rb") as file:
            data = pickle.load(file)
            for i, key in enumerate(data.keys()):
                jpg_file = str(
                    Path(Input_plate) / suffix / number / (key.split(".")[0] + ".jpg")
                )
                new_jpg_file = str(
                    Path(Output_plate) / suffix / number / (key.split(".")[0] + ".jpg")
                )
                # print(jpg_file, new_jpg_file)
                if not exists(jpg_file):
                    print("File ", jpg_file, " not found!")
                    continue
                orig_img = np.asarray(
                    Image.open(jpg_file).convert("RGB"), dtype=np.float16
                )
                orig_img = daltonize.gamma_correction(orig_img, gamma)

                dalton_rgb = daltonize.daltonize(orig_img, color_blindness)
                dalton_img = daltonize.array_to_img(dalton_rgb, gamma)
                dalton_img.save(new_jpg_file)


def create_sim_colorblind_file(
    jpg_file: str,
    outpath: str,
    new_plate: str,
    color_blindness: str,
    gamma: float,
    saveFile: bool = False,
):
    """This function simulates colorblindness for a single image file. No need for
    circled_MNIST. This function is used only in the tutorial."""

    new_jpg_file = str(
        Path(outpath) / (new_plate + jpg_file.split(os.sep)[-1].split(".")[0] + ".jpg")
    )
    # print(jpg_file,new_jpg_file)

    orig_img = np.asarray(Image.open(jpg_file).convert("RGB"), dtype=np.float16)
    orig_img = daltonize.gamma_correction(orig_img, gamma)

    simul_rgb = daltonize.simulate(orig_img, color_blindness)
    simul_img = daltonize.array_to_img(simul_rgb, gamma)
    if saveFile:
        simul_img.save(new_jpg_file)
    return simul_img


def create_daltonize_colorblind_file(
    jpg_file: str,
    outpath: str,
    new_plate: str,
    color_blindness: str,
    gamma: float,
    save_file: bool = False,
):
    """This function daltonizes a single image file. No need for circled_MNIST. This
    function is used only in the tutorial."""

    new_jpg_file = str(
        Path(outpath) / (new_plate + jpg_file.split(os.sep)[-1].split(".")[0] + ".jpg")
    )

    print(jpg_file, new_jpg_file)

    orig_img = np.asarray(Image.open(jpg_file).convert("RGB"), dtype=np.float16)
    orig_img = daltonize.gamma_correction(orig_img, gamma)

    dalton_rgb = daltonize.daltonize(orig_img, color_blindness)
    dalton_img = daltonize.array_to_img(dalton_rgb, gamma)
    if save_file:
        dalton_img.save(new_jpg_file)
    return dalton_img


def create_folder_tree(path: str, name: str):
    """This function creates the necessary folder structure needed for a new plate."""
    (Path(path) / name / "Test_images").mkdir(parents=True, exist_ok=True)
    (Path(path) / name / "Train_images").mkdir(parents=True, exist_ok=True)
    for i in range(10):
        (Path(path) / name / "Test_images" / str(i)).mkdir(parents=True, exist_ok=True)
        (Path(path) / name / "Train_images" / str(i)).mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--data_path",
        help=(
            "Path and name of the plate to be color-manipulated. E.g., "
            "Plate_1_above_line"
        ),
        type=str,
        default="./datasets",
    )

    parser.add_argument(
        "--input_plate_path", default="data/", help="path where data is located"
    )

    parser.add_argument(
        "--output_plate_path",
        help="Where to save the data.",
        type=str,
        default="./datasets",
    )

    parser.add_argument(
        "--simulate_color_blindness",
        help=(
            "type of color blindness (deuteranopia, "
            "protanopia, tritanopia), default is simulate d "
            " {1: simulate d, 2: simulate p, 3: simulate t, "
            "4: daltonize d, 5: daltonize p, 6: daltonize t}"
        ),
        type=int,
        default=1,
    )
    parser.add_argument(
        "--gamma",
        help=(
            "value of gamma correction to be applied before transformation. "
            "The default applies the standard sRGB correction with an exponent of 2.4"
            "Use 1 for no gamma correction."
        ),
        type=float,
        default=2.4,
    )

    args = parser.parse_args()

    circled_MNIST = args.data_path
    input_plate_path = args.input_plate_path
    output_plate_path = args.output_plate_path
    plate_name = input_plate_path.split(os.sep)[-1]
    color_blindness = args.simulate_color_blindness
    gamma = args.gamma

    test_path = str(Path(circled_MNIST) / "Test_images")
    test_files = [
        str(Path(test_path) / f) for f in listdir(test_path) if ".pickle" in f
    ]

    train_path = str(Path(circled_MNIST) / "Train_images")
    train_files = [
        str(Path(train_path) / f) for f in listdir(train_path) if ".pickle" in f
    ]

    if color_blindness < 1 or color_blindness > 6:
        raise NameError("No such a colored manipulation option!")

    # Running the creation

    types = {
        1: "Sim_d",
        2: "Sim_p",
        3: "Sim_t",
        4: "Dal_d",
        5: "Dal_p",
        6: "Dal_t",
    }
    color_blindness = types[args.simulate_color_blindness]

    create_folder_tree(output_plate_path, plate_name + "_" + color_blindness)
    if args.simulate_color_blindness < 5:
        create_sim_colorblind_plates(
            test_files,
            input_plate_path,
            str(Path(output_plate_path) / (plate_name + "_" + color_blindness)),
            "Test_images",
            str(color_blindness[-1]),
            gamma,
        )
        create_sim_colorblind_plates(
            train_files,
            input_plate_path,
            str(Path(output_plate_path) / (plate_name + "_" + color_blindness)),
            "Train_images",
            str(color_blindness[-1]),
            gamma,
        )
    else:
        create_daltonize_colorblind_plates(
            test_files,
            input_plate_path,
            str(Path(output_plate_path) / (plate_name + "_" + color_blindness)),
            "Test_images",
            str(color_blindness[-1]),
            gamma,
        )
        create_daltonize_colorblind_plates(
            train_files,
            input_plate_path,
            str(Path(output_plate_path) / (plate_name + "_" + color_blindness)),
            "Train_images",
            str(color_blindness[-1]),
            gamma,
        )
