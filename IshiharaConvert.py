#  Python package `ishihara-like-mnist`
#
#  file: IshiharaCovert.py
#
#  Authors: Ammar Shaker  (Ammar.Shaker@neclab.eu)
#
#  NEC Laboratories Europe GmbH, Copyright (c) 2022, All rights reserved.
#  THIS HEADER MAY NOT BE EXTRACTED OR MODIFIED IN ANY WAY.
#
#  --- PROPRIETARY INFORMATION ---
#
#  SOFTWARE LICENSE Agreement
#  ACADEMIC OR NON-PROFIT ORGANIZATION NONCOMMERCIAL RESEARCH USE ONLY
#  BY USING OR DOWNLOADING THE SOFTWARE, YOU ARE AGREEING TO THE TERMS OF THIS LICENSE
#  AGREEMENT.  IF YOU DO NOT AGREE WITH THESE TERMS, YOU MAY NOT USE OR DOWNLOAD THE
#  SOFTWARE.
#
#  This is a license agreement ("Agreement") between your academic institution or
#  non-profit organization or self (called "Licensee" or "You" in this Agreement) and
#  NEC Laboratories Europe GmbH (called "Licensor" in this Agreement).  All rights not
#  specifically granted to you in this Agreement are reserved for Licensor.
#  RESERVATION OF OWNERSHIP AND GRANT OF LICENSE: Licensor retains exclusive ownership
#  of any copy of the Software (as defined below) licensed under this Agreement and
#  hereby grants to Licensee a personal, non-exclusive, non-transferable license to use
#  the Software for noncommercial research purposes, without the right to sublicense,
#  pursuant to the terms and conditions of this Agreement. NO EXPRESS OR IMPLIED
#  LICENSES TO ANY OF LICENSOR’S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. As used in
#  this Agreement, the term "Software" means (i) the actual copy of all or any portion
#  of code for program routines made accessible to Licensee by Licensor pursuant to
#  this Agreement, inclusive of backups, updates, and/or merged copies permitted
#  hereunder or subsequently supplied by Licensor,  including all or any file
#  structures, programming instructions, user interfaces and screen formats and
#  sequences as well as any and all documentation and instructions related to it,
#  and (ii) all or any derivatives and/or modifications created or made by You to any
#  of the items specified in (i).
#  CONFIDENTIALITY/PUBLICATIONS: Licensee acknowledges that the Software is proprietary
#  to Licensor, and as such, Licensee agrees to receive all such materials and to use
#  the Software only in accordance with the terms of this Agreement.  Licensee agrees
#  to use reasonable effort to protect the Software from unauthorized use,
#  reproduction, distribution, or publication. All publication materials mentioning
#  features or use of this software must explicitly include an acknowledgement the
#  software was developed by NEC Laboratories Europe GmbH.
#  COPYRIGHT: The Software is owned by Licensor.
#  PERMITTED USES:  The Software may be used for your own noncommercial internal
#  research purposes. You understand and agree that Licensor is not obligated to
#  implement any suggestions and/or feedback you might provide regarding the Software,
#  but to the extent Licensor does so, you are not entitled to any compensation related
#  thereto.
#  DERIVATIVES: You may create derivatives of or make modifications to the Software,
#  however, You agree that all and any such derivatives and modifications will be
#  owned by Licensor and become a part of the Software licensed to You under this
#  Agreement.  You may only use such derivatives and modifications for your own
#  noncommercial internal research purposes, and you may not otherwise use, distribute
#  or copy such derivatives and modifications in violation of this Agreement.
#  BACKUPS:  If Licensee is an organization, it may make that number of copies of the
#  Software necessary for internal noncommercial use at a single site within its
#  organization provided that all information appearing in or on the original labels,
#  including the copyright and trademark notices are copied onto the labels of the
#  copies.
#  USES NOT PERMITTED:  You may not distribute, copy or use the Software except as
#  explicitly permitted herein. Licensee has not been granted any trademark license as
#  part of this Agreement. Neither the name of NEC Laboratories Europe GmbH nor the
#  names of its contributors may be used to endorse or promote products derived from
#  this Software without specific prior written permission.
#  You may not sell, rent, lease, sublicense, lend, time-share or transfer, in whole or
#  in part, or provide third parties access to prior or present versions (or any parts
#  thereof) of the Software.
#  ASSIGNMENT: You may not assign this Agreement or your rights hereunder without the
#  prior written consent of Licensor. Any attempted assignment without such consent
#  shall be null and void.
#  TERM: The term of the license granted by this Agreement is from Licensee's
#  acceptance of this Agreement by downloading the Software or by using the Software
#  until terminated as provided below.
#  The Agreement automatically terminates without notice if you fail to comply with any
#  provision of this Agreement.  Licensee may terminate this Agreement by ceasing using
#  the Software.  Upon any termination of this Agreement, Licensee will delete any and
#  all copies of the Software. You agree that all provisions which operate to protect
#  the proprietary rights of Licensor shall remain in force should breach occur and
#  that the obligation of confidentiality described in this Agreement is binding in
#  perpetuity and, as such, survives the term of the Agreement.
#  FEE: Provided Licensee abides completely by the terms and conditions of this
#  Agreement, there is no fee due to Licensor for Licensee's use of the Software in
#  accordance with this Agreement.
#  DISCLAIMER OF WARRANTIES:  THE SOFTWARE IS PROVIDED "AS-IS" WITHOUT WARRANTY OF ANY
#  KIND INCLUDING ANY WARRANTIES OF PERFORMANCE OR MERCHANTABILITY OR FITNESS FOR A
#  PARTICULAR USE OR PURPOSE OR OF NON-INFRINGEMENT.  LICENSEE BEARS ALL RISK RELATING
#  TO QUALITY AND PERFORMANCE OF THE SOFTWARE AND RELATED MATERIALS.
#  SUPPORT AND MAINTENANCE: No Software support or training by the Licensor is provided
#  as part of this Agreement.
#  EXCLUSIVE REMEDY AND LIMITATION OF LIABILITY: To the maximum extent permitted under
#  applicable law, Licensor shall not be liable for direct, indirect, special,
#  incidental, or consequential damages or lost profits related to Licensee's use of
#  and/or inability to use the Software, even if Licensor is advised of the possibility
#  of such damage.
#  EXPORT REGULATION: Licensee agrees to comply with any and all applicable export
#  control laws, regulations, and/or other laws related to embargoes and sanction
#  programs administered by law.
#  SEVERABILITY: If any provision(s) of this Agreement shall be held to be invalid,
#  illegal, or unenforceable by a court or other tribunal of competent jurisdiction,
#  the validity, legality and enforceability of the remaining provisions shall not in
#  any way be affected or impaired thereby.
#  NO IMPLIED WAIVERS: No failure or delay by Licensor in enforcing any right or remedy
#  under this Agreement shall be construed as a waiver of any future or other exercise
#  of such right or remedy by Licensor.
#  GOVERNING LAW: This Agreement shall be construed and enforced in accordance with the
#  laws of Germany without reference to conflict of laws principles.  You consent to the
#  personal jurisdiction of the courts of this country and waive their rights to venue
#  outside of Germany.
#  ENTIRE AGREEMENT AND AMENDMENTS: This Agreement constitutes the sole and entire
#  agreement between Licensee and Licensor as to the matter set forth herein and
#  supersedes any previous agreements, understandings, and arrangements between
#  the parties relating hereto.
#      THIS HEADER MAY NOT BE EXTRACTED OR MODIFIED IN ANY WAY.


r"""
   This Script can be used to transform MNIST into circled MNIST.
   Examples:
            Creating circled MNIST:
            python IshiharaConvert.py --data_path "Data\MNIST" --out_path Output

"""

import argparse
import os
import pickle
from os import listdir
from os.path import exists, isdir, isfile, join
from typing import Any, List, Tuple

import numpy as np
import PIL.ImageOps
from PIL import Image

import IshiharaSimulate.plates as plates
import IshiharaSimulate.utils as utils
from IshiharaMC import ishiharaMC
from PNGToSVG import pngtosvg


def check_SVG_exists(fname: str, SVGpath: str) -> Tuple[bool, str, str]:
    """This function checks if an SVG file exists and constructs different file
    names."""
    # pdb.set_trace()
    fname_sp = fname.split(os.sep)
    fname, nr, folder = fname_sp[-1], fname_sp[-2], fname_sp[-3]

    fnameextension = fname.split(".")
    svg_file = join(SVGpath, folder, nr, fnameextension[0] + ".svg")
    pickle_file = join(SVGpath, folder, nr, fnameextension[0] + ".p")

    return exists(svg_file), svg_file, pickle_file


def create_SVG(jpg_file: str, svg_file: str) -> None:
    """This function creates an SVG file after transforming an image to bilevel."""
    # pdb.set_trace()
    image = Image.open(jpg_file)
    image = PIL.ImageOps.invert(image)
    image = image.convert("1").convert("RGBA")
    svg_image = pngtosvg.rgba_image_to_svg_contiguous(image)
    with open(svg_file, "w") as text_file:
        text_file.write(svg_image)


def save_pkl(pickle_file: str, output: np.ndarray, idx_final: np.ndarray) -> None:
    """This function dumps a list of circles and their indicators into a pickle file."""
    data = {"output": output, "idx_final": idx_final}
    with open(pickle_file, "wb") as file:
        # dump information to that file
        pickle.dump(data, file)


def load_pkl(pickle_file: str) -> Tuple[np.ndarray, np.ndarray]:
    """This function reads a pickle file and returns a list of circles and indicators.
    Each circle has an indicator of whether a circle is in the target digit or not.
    """
    with open(pickle_file, "rb") as file:
        data = pickle.load(file)
    return data["output"], data["idx_final"]


def get_black_paths(svg_file: str) -> Tuple[List[np.ndarray], List[List[np.ndarray]]]:
    """This function reads an SVG file and returns only paths with a mean RGB smaller
    than 50 (Black)."""
    path_strings, path_style = utils.get_d_style(svg_file)
    paths: Any = []
    black_index = []
    for p, s in zip(path_strings, path_style):
        strip = utils.clean_strip(p)
        paths += [strip]
        if utils.get_mean_RGB(s) < 50:
            black_index += [len(paths) - 1]

    # Normalizing the locations using the bounding box
    paths = utils.normaize_paths(paths)
    # Choosing only black paths
    paths = [paths[i] for i in black_index]
    # paths_org keeps the path hierarchy
    paths_org = paths
    # paths contains all paths unnested
    paths = [x1 for x in paths_org for x1 in x]

    return paths, paths_org


def get_shapes_and_indices(
    paths: List[np.ndarray], paths_org: List[List[np.ndarray]]
) -> Tuple[np.ndarray, np.ndarray]:
    """This function performs the simulation and returns a list of circles and indicators.
    paths contain all paths as a single list. paths_org is a list of lists of paths.
    """
    output = np.array(
        ishiharaMC.createPlate(paths, num=[4000, 2 * 4000, 4 * 4000, 8 * 4000])
    )
    # Computing the indices for the target shape

    idx = [[ishiharaMC.circinPoly(x1, output) for x1 in x] for x in paths_org]
    idx_new = []
    for i, arr in enumerate(idx):
        if len(arr) == 1:
            idx_new += [arr[0]]
        else:
            outer = utils.get_outer_path(paths_org[i])

            temp = np.array([True] * arr[0].shape[0])
            for x in arr[:outer] + arr[outer + 1 :]:
                temp_or = np.logical_or(arr[outer], x)
                temp_and = np.logical_and(arr[outer], x)
                temp = np.logical_and(
                    temp, np.logical_and(temp_or, np.logical_not(temp_and))
                )
            idx_new += [temp]

    idx_final = idx_new[0]
    for x in idx_new[1:]:
        idx_final = np.logical_or(idx_final, x)
    return output, idx_final


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_path", help="Where to find the data.", type=str, default="datasets"
    )
    parser.add_argument(
        "--out_path", help="Where to save the data.", type=str, default="Output"
    )

    args = parser.parse_args()

    mypath = args.data_path
    outpath = args.out_path
    plates.create_folder_tree(outpath, "SVG")
    SVGpath = join(outpath, "SVG")

    onlyfolders = [join(mypath, f) for f in listdir(mypath) if isdir(join(mypath, f))]
    onlyfolders = [
        join(F1, f) for F1 in onlyfolders for f in listdir(F1) if isdir(join(F1, f))
    ]
    onlyfiles = [
        join(F1, f)
        for F1 in onlyfolders
        for f in listdir(F1)
        if isfile(join(F1, f)) and ".jpg" in f
    ]

    # Converting every image into an SVG file and a pcikle file containing the results
    # of MC
    for file in onlyfiles:
        file_exists, svg_file, pickle_file = check_SVG_exists(file, SVGpath)
        print(file_exists, svg_file)
        if not file_exists:
            create_SVG(file, svg_file)

            print(svg_file)
            paths, paths_org = get_black_paths(svg_file)
            output, idx_final = get_shapes_and_indices(paths, paths_org)
            save_pkl(pickle_file, output, idx_final)

    # Merging the pickle files
    plates.create_folder_tree(outpath, "PFiles", first_level_only=True)
    onlyfolders = [
        join(SVGpath, f) for f in listdir(SVGpath) if isdir(join(SVGpath, f))
    ]
    print(onlyfolders)
    onlyfolders = [
        join(F1, f) for F1 in onlyfolders for f in listdir(F1) if isdir(join(F1, f))
    ]
    for folder in onlyfolders:
        onlyfiles = [
            join(folder, f)
            for f in listdir(folder)
            if isfile(join(folder, f)) and ".p" in f
        ]
        nr, parentFolder = folder.split(os.sep)[-1], folder.split(os.sep)[-2]
        result_dic = {}
        for file in onlyfiles:
            fname = file.split(os.sep)[-1]
            output, idx_final = load_pkl(file)
            result_dic[fname] = [output, idx_final]

        pickle_file = join(outpath, "PFiles", parentFolder, nr + ".pickle")
        with open(pickle_file, "wb") as file:
            # dump information to that file
            pickle.dump(result_dic, file)
